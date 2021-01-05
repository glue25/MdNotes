1. Main.cpp里处理参数的部分

2.  gritb-decoder/DatalogProgram里DatalogProgram类的`DatalogProgram::loaders()`挺有意思

   ```c++
   std::map<DatalogProgram::Target, DatalogProgram::Factory> &DatalogProgram::loaders()
   {
       static std::map<Target, Factory> Loaders;
       return Loaders;
   }
   ```

   函数里面是一个`static`的定义变量语句和`return`被定义变量（的引用）的语句。对类有用的是里面的那个变量，但是外面用到这个变量时都是用`loaders()`返回的这个变量的引用。

   好像这样更安全（？）

3. 用`using`重新定义数据类型

   ```c++
   using Target = std::tuple<gtirb::FileFormat, gtirb::ISA>;
   using Factory = std::function<CompositeLoader()>;
   ```

   

4. `std::optional`

   返回`std::nullopt`或一个实现了`->`与`*`（这两种指针操作符）的对象。

5. `{}`初始化

   https://www.cnblogs.com/zyk1113/p/13452493.html

   

6.  

   `std::function`表示可调用对象

7.  

   `std::shared_pt`智能指针

   只要将 `new` 运算符返回的指针 `p` 交给一个 `shared_ptr` 对象“托管”，就不必担心在哪里写`delete p`语句——实际上根本不需要编写这条语句，托管 `p` 的 `shared_ptr` 对象在消亡时会自动执行`delete p`。而且，该 `shared_ptr` 对象能像指针 `p` —样使用，即假设托管 `p` 的 `shared_ptr` 对象叫作 `ptr`，那么 `*ptr` 就是 `p` 指向的对象。

8.  

   `std::forward`通常是用于完美转发的，它会将输入的参数原封不动地传递到下一个函数中，这个“原封不动”指的是，如果输入的参数是左值，那么传递给下一个函数的参数的也是左值；如果输入的参数是右值，那么传递给下一个函数的参数的也是右值。

9.  

   `template<typename T, typename... Args>`变参模板

10. 

