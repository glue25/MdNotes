1.  

   **Main.cpp**

   第一个定义了些数据类型，看起来更偏向于服务gtirb

   ```c++
       registerAuxDataTypes();  // Registration.cpp
       registerDatalogLoaders();  // Registration.cpp
   ```

   第二个函数`registerDatalogLoaders`里调用gtirb-decoder/DatalogProgram.h里的`DatalogProgram::registerLoader`函数，这个函数为`DatalogProgram`类里`static`的`loaders`（一个**静态的**返回private的map变量的函数，这个map存的是二进制类型与对应loader的映射,但是调用起来会返回一个loader（定义在gtirb-decoder里的CompositeLoader.h）虽然map的value是个句柄，但是会在gtirb-decoder里的`DatalogProgram::load`进行载入（毕竟一个被分析文件只会出现一种对应格式））因为`loaders`函数和里面的变量都是`static`，应该是全类共用这个变量

2.  

   **Main.cpp**

   接收参数

3. 载入数据，初始化了`DatalogProgram`对象.

   ```c++
   auto GTIRB = GtirbBuilder::read(filename);
   // Add `ddisasmVersion' aux data table.
   GTIRB->IR->addAuxData<gtirb::schema::DdisasmVersion>(DDISASM_FULL_VERSION_STRING);
   // Decode and load GTIRB Module into the SouffleProgram context.
   gtirb::Module &Module = *(GTIRB->IR->modules().begin());
   std::optional<DatalogProgram> Souffle = DatalogProgram::load(Module);
   ```

   最后这个load会返回`Loader.load(Module);`

   load的代码如下

   ```c++
   std::optional<DatalogProgram> DatalogProgram::load(const gtirb::Module &Module)
   {
       auto Target = std::make_tuple(Module.getFileFormat(), Module.getISA());
       auto Loader = loaders().at(Target)();
       return Loader.load(Module);
   }
   ```

   而`Loader`来自于下面函数的返回值

   ```c++
   CompositeLoader ElfArm64Loader()
   {
       CompositeLoader Loader("souffle_disasm_arm64");
       Loader.add(ModuleLoader);
       Loader.add(SectionLoader);
       Loader.add<Arm64Loader>();
       Loader.add<DataLoader>(DataLoader::Pointer::QWORD);
       Loader.add(ElfSymbolLoader);
       Loader.add(ElfExceptionLoader);
       return Loader;
   }
   ```

   也就是说`Souffle`接收的值是`CompositeLoader.load(Module)`

   ```c++
   using Loader = std::function<void(const gtirb::Module&, DatalogProgram&)>;
   std::vector<Loader> Loaders;
   std::string Name;
   
   std::optional<DatalogProgram> load(const gtirb::Module& Module)
   {
       if(auto SouffleProgram = std::shared_ptr<souffle::SouffleProgram>(souffle::ProgramFactory::newInstance(Name)))
       {
           DatalogProgram Program{SouffleProgram};  // 初始化DatalogProgram对象
           return operator()(Module, Program);
       }
       return std::nullopt;
   }
   
   std::optional<DatalogProgram> operator()(const gtirb::Module& Module, DatalogProgram& Program)
   {
       for(auto& Loader : Loaders)
       {
           Loader(Module, Program);
       }
       return Program;
   }
   ```

   也就是说`Souffle`接收的值是定义在`CompositeLoader.load(Module)`中的`Program`。`Program`这个变量在`load`被定义,是一个gtirb-decoder/DatalogProgram.h里的`DatalogProgram`对象。返回的`Program`经过了`operator()(Module, Program)`处理，`operator()`这个函数里会调用

   ```c++
   for(auto& Loader : Loaders)
       {
           Loader(Module, Program);
       }
       return Program;
   ```

   其中`Loaders`是一个函数的`Vector`，里面是函数，`Loaders`在`gtirb-decoder/target`中的两个文件被定义。

   ```c++
   CompositeLoader ElfArm64Loader()
   {
       CompositeLoader Loader("souffle_disasm_arm64");
       Loader.add(ModuleLoader);
       Loader.add(SectionLoader);
       Loader.add<Arm64Loader>();
       Loader.add<DataLoader>(DataLoader::Pointer::QWORD);
       Loader.add(ElfSymbolLoader);
       Loader.add(ElfExceptionLoader);
       return Loader;
   }
   ```

   也就是说这里的几个被`add`的函数都会把`Program`处理一遍

   `ModuleLoader`定义在gtirb-decoder/core/ModuleLoader.h里。与`Program`相关的操作是几个`Program.insert`

   ```c++
       void insert(const std::string& Name, const T& Data)
       {
           if(auto* Relation = Program->getRelation(Name))
           {
               for(const auto Element : Data)
               {
                   souffle::tuple Row(Relation);
                   Row << Element;
                   Relation->insert(Row);
               }
           }
       }
   ```

   其中`Program`是`souffle::SouffleProgram`指针，`Program->getRelation(Name)`返回的是`The pointer of the target relation`。细节没太看懂，但总之是向名字对应的变量中存数据

   `SectionLoader`定义在gtirb-decoder/core/SectionLoader.h里。与`Program`相关的操作是个`Program.insert`

   `Loader.add<Arm64Loader>();`重载了`()`，被调用的应该是里面的insert函数，但是没有发现被调用的迹象

   `ElfSymbolLoader`定义在gtirb-decoder/format/ElfLoader.cpp里。与`Program`相关的操作也是`Program.insert`

   `ElfExceptionLoader`模式不一样，但还是insert那一套

   `DataLoader`重载了`()`，核心还是`insert`

4. 去掉多余信息（？）

   ```c++
   // Remove initial entry point.
   if(gtirb::CodeBlock *Block = Module.getEntryPoint())
   {
       Block->getByteInterval()->removeBlock(Block);
   }
   Module.setEntryPoint(nullptr);
   // Remove placeholder relocation data.
   Module.removeAuxData<gtirb::schema::Relocations>();
   ```

   这里不是太明白为什么这么做，不过这个应该是和Datalog无关的，也无助于反编译，为了不作弊？看看

   如果不去掉，会写什么信息进去？？？？？**总之这个我看不懂**

   而且`load`在前面，已经与`souffle`无关了

5.  

   没太看明白这个是干什么的

   ```c++
   Souffle->insert("option", createDisasmOptions(vm));
   ```

6.  

   `Souffle->writeFacts(dir);`

   是可选的，用作debug的

7.  

   `Souffle->run();`运行分析，这里实际调用的是`souffle`对象的`run()`

8.  

   `disassembleModule(*GTIRB->Context, Module, Souffle->get(), vm.count("self-diagnose") != 0);`

   函数里面大部分是通过`gtirb::Module.addAuxData`实现的，信息都进入了`GTIRB`。

9. 

