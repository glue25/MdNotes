配置c/cpp与vscode插件的使用要领

## C/C++ for Visual Studio Code

https://code.visualstudio.com/docs/languages/cpp

这个链接里更多是总览性的，没啥具体知识，可以找到一些链接

## Using C++ on Linux in VS Code

https://code.visualstudio.com/docs/cpp/config-linux

As you go through the tutorial, you will create three files in a `.vscode` folder in the workspace:

- `tasks.json` (compiler build settings)（尝试构建的时候会生成）
- `launch.json` (debugger settings)
- `c_cpp_properties.json` (compiler path and IntelliSense settings)

### `tasks.json`

完成tasks.josin定义的build任务快捷键的是`Ctrl+Shift+B`

关于修改tasks.json，主要的改动还是输入和输出

Modifying tasks.json：You can modify your `tasks.json` to build multiple C++ files by using an argument like `"${workspaceFolder}/*.cpp"` instead of `${file}`. You can also modify the output filename by replacing `"${fileDirname}/${fileBasenameNoExtension}"` with a hard-coded filename (for example 'helloworld.out').

### `launch.json`

这个文件配置调试（F5），可以通过the main menu, choose **Run** > **Add Configuration...** and then choose **C++ (GDB/LLDB)**打开`launch.json`

默认情况下插件不会加入断点，配置文件中的"stopAtEntry"也会是false，我认为改成true会比较实用

F5可以进入调试，进入后

- 继续调试：F5
- 单步跳过：F10，不会跳进子函数内部
- 单步调试：F11 会跳进子函数的内部，甚至可以跳进看标准库的代码
- 单步跳过：Shift+F11 回到自己的代码(不是后退，而是继续执行)

一开始对printf语句执行F10时出现报错Error: 无法解析不存在的文件"/build/glibc-S7xCS9/glibc-2.27/csu/libc-start.c，有博客https://blog.csdn.net/weixin_39758398/article/details/101912759是针对这一问题的。

监视变量可以通过键入变量名称的方式实现

### `c_cpp_properties.json`



可以通过`Ctrl+Shift+P`然后输入`C/C++:Edit configurations`来修改

`"includePath"`是要重点关照的，解决缺头文件的问题



## Debug配置

https://code.visualstudio.com/docs/cpp/cpp-debug

支持条件断点和函数断点，都在Run那里

支持多线程调试（暂时用不到，暂略）

### 其他符号位置

`"symbolSearchPath"`



### 找到源文件

`"sourceFileMap"`

这是通过在本`sourceFileMap`节中添加的简单替换对完成的。将使用此列表中的第一个匹配项。

例如：

```
"sourceFileMap": {
    "/build/gcc-4.8-fNUjSI/gcc-4.8-4.8.4/build/i686-linux-gnu/libstdc++-v3/include/i686-linux-gnu": "/usr/include/i686-linux-gnu/c++/4.8",
    "/build/gcc-4.8-fNUjSI/gcc-4.8-4.8.4/build/i686-linux-gnu/libstdc++-v3/include": "/usr/include/c++/4.8"
}
```



### 意外报错

Linux：

- 您可能会看到一条错误消息：

  ```
  ptrace: Operation not permitted
  ```

  。这是由于GDB需要提升的权限才能附加到进程。可以使用以下解决方案解决此问题：

  1. 在使用*attach to process时*，需要提供密码才能开始调试会话。

  2. 要暂时禁用此错误，请使用以下命令：

     `echo 0 | sudo tee /proc/sys/kernel/yama/ptrace_scope`

  3. 要永久删除此错误，添加一个名为`10-ptrace.conf`来`/etc/sysctl.d/`，并添加以下`kernel.yama.ptrace_scope = 0`。



## 更深入的调试相关内容

https://code.visualstudio.com/docs/editor/debugging

https://code.visualstudio.com/docs/cpp/launch-json-reference



c_cpp_properties.json

https://code.visualstudio.com/docs/cpp/customize-default-settings-cpp









## 编辑C++

https://code.visualstudio.com/docs/cpp/cpp-ide

### 自动格式化

“设置**文档格式”**（Ctrl + Shift + I）或仅使用“**格式选择”**（Ctrl + K Ctrl + F）来**格式化**当前文件。

【还有自动定时的格式化，但我觉得不实用，网站上有】

### 快速看定义

Ctrl+Shift+F10

### 搜索符号

您可以在当前文件或工作区中搜索符号，以更快地浏览代码。

要在<u>当前文件</u>中搜索符号，请按Ctrl + Shift + O，然后输入要查找的符号的名称。将会出现一个潜在匹配的列表。在您输入时会被过滤。从匹配列表中选择以导航到其位置。

要在<u>当前工作空间</u>中搜索符号，请按Ctrl + T

您也可以通过“**命令面板”**访问这些命令来搜索符号。使用**快速打开**（Ctrl + P），然后输入“ @”命令搜索当前文件，或输入“＃”命令搜索当前工作空间。Ctrl + Shift + O和Ctrl + T只是“ @”和“＃”命令的快捷方式，因此所有操作均相同。

### 转到定义

F12