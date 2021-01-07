# Debug C++ in Visual Studio Code

https://code.visualstudio.com/docs/cpp/cpp-debug

## 

有必要说的是，使用gcc时，如果要加入debug信息，需要加上`-g`选项

## 条件断点

条件断点使您仅在条件的值为true时才可以中断特定代码行的执行。要设置条件断点，请右键单击现有断点，然后选择**编辑断点**。这将打开一个小窥视窗口，您可以在其中输入必须评估为true的条件，以便在调试过程中命中断点。

## 函数断点

函数断点使您可以在函数的开头而不是在特定的代码行上中断执行。要设置功能断点，请在“**运行”**视图上的**“****断点”**部分内单击鼠标右键，然后选择“**添加功能断点”**并输入要在其上中断执行的功能的名称。

Function breakpoints enable you to break execution at the beginning of a function instead of on a particular line of code. To set a function breakpoint, on the **Run** view right-click inside the **Breakpoints** section, then choose **Add Function Breakpoint** and enter the name of the function on which you want to break execution.

## 表达式求值

VS Code supports expression evaluation in several contexts:

- You can type an expression into the **Watch** section of the **Run** view and it will be evaluated each time a breakpoint is hit.
- You can type an expression into the **Debug Console** and it will be evaluated only once.
- You can evaluate any expression that appears in your code while you're stopped at a breakpoint.

Expressions in the **Watch** section take effect in the application being debugged; an expression that modifies the value of a variable will modify that variable for the duration of the program.

VS Code在以下情况下支持表达式评估：

- 您可以在**“运行”**视图的**“****监视”**部分中键入一个表达式，每次遇到断点时都会对其求值。
- 您可以在**Debug Console中**键入一个表达式，并且该表达式只会被评估一次。
- 在断点处停止时，您可以评估代码中出现的任何表达式。

“**监视”**部分中的表达式在正在调试的应用程序中生效；修改变量值的表达式将在程序运行期间修改该变量。



## 内存转储调试

(*看起来暂时用不上*)

VS Code的C / C ++扩展还具有调试内存转储的功能。要调试内存转储，请打开`launch.json`文件，然后将`coreDumpPath`（对于GDB或LLDB）或`dumpPath`（对于Visual Studio Windows Debugger）属性添加到**C ++ Launch**配置中，将其值设置为包含内存转储路径的字符串。这甚至适用于在x64机器上调试的x86程序。



## Additional symbols

(*看起来暂时用不上*)

If there are additional directories where the debugger can find symbol files (for example, `.pdb` files for the Visual Studio Windows Debugger), they can be specified by adding the `additionalSOLibSearchPath` (for GDB or LLDB) or `symbolSearchPath` (for the Visual Studio Windows Debugger).

For example:

```
    "additionalSOLibSearchPath": "/path/to/symbols;/another/path/to/symbols"
```

or

```
    "symbolSearchPath": "C:\\path\\to\\symbols;C:\\another\\path\\to\\symbols"
```



## 定位源文件

如果源文件不在编译位置，则可以更改源文件的位置。这是通过在本`sourceFileMap`节中添加的简单替换对完成的。将使用此列表中的第一个匹配项。

(*应该是基于匹配替换，在列表中找到第一个匹配的符号*)

The source file location can be changed if the source files are not located in the compilation location. This is done by simple replacement pairs added in the `sourceFileMap` section. The first match in this list will be used.

For example:

```json
"sourceFileMap": {
    "/build/gcc-4.8-fNUjSI/gcc-4.8-4.8.4/build/i686-linux-gnu/libstdc++-v3/include/i686-linux-gnu": "/usr/include/i686-linux-gnu/c++/4.8",
    "/build/gcc-4.8-fNUjSI/gcc-4.8-4.8.4/build/i686-linux-gnu/libstdc++-v3/include": "/usr/include/c++/4.8"
}
```



## GDB, LLDB, and LLDB-MI Commands (GDB/LLDB)

(*看来还是不用的好*)

For the `C++ (GDB/LLDB)` debugging environment, you can execute GDB, LLDB and LLDB-MI commands directly through the debug console with the `-exec` command, but be careful, executing commands directly in the debug console is untested and might crash VS Code in some cases.



## Natvis框架

这个可以配置更个性化的调试视图

暂略



## 已知问题

### 符号和代码导航

对所有平台：

- Because the extension doesn't parse function bodies, **Peek Definition** and **Go to Definition** don't work for symbols defined inside the body of a function.（字面意思知道，但还是不明白这是什么意思）

### Debugging

这个BUG我认为用第二种方法解决会好一些

Linux:

- You may see an error saying: `ptrace: Operation not permitted`. This is due to GDB needing elevated permissions in order to attach to a process. This can be solved using the solutions below:

  1. When using *attach to process*, you need to provide your password before the debugging session can begin.

  2. To disable this error temporarily, use the following command:

     `echo 0 | sudo tee /proc/sys/kernel/yama/ptrace_scope`

  3. To remove the error permanently, add a file called `10-ptrace.conf` to `/etc/sysctl.d/` and add the following `kernel.yama.ptrace_scope = 0`.



# Configuring C/C++ debugging

https://code.visualstudio.com/docs/cpp/launch-json-reference

The `launch.json` file is used to configure the debugger in Visual Studio Code.

其中的`program`是可执行文件的路径，是必需的。

## 配置调试行为

### program

可执行文件的路径，是必需的

### symbolSearchPath

Tells the Visual Studio Windows Debugger what paths to search for symbol (.pdb) files. Separate multiple paths with a semicolon. For example: `"C:\\Symbols;C:\\SymbolDir2"`.（<u>Linux也需要吗？？？</u>）

### requireExactSource

An optional flag that tells the Visual Studio Windows Debugger to require current source code to match the pdb.（<u>Linux也需要吗？？？</u>）



### additionalSOLibSearchPath

Tells GDB or LLDB what paths to search for .so files. Separate multiple paths with a semicolon. For example: `"/Users/user/dir1;/Users/user/dir2"`.（<u>这个应该需要费心配一下，不过应该可以从C/C++配置文件复制</u>）



### externalConsole

Used only when launching the debuggee. For `attach`, this parameter does not change the debuggee's behavior.(*<u>attach是什么</u>*)

- **Windows**: When set to true, it will spawn an external console. When set to false, it will use VS Code's integratedTerminal.
- **Linux**: When set to true, it will notify VS Code to spawn an external console. When set to false, it will use VS Code's integratedTerminal.（<u>看来一般是false</u>）
- **macOS**: When set to true, it will spawn an external console through `lldb-mi`. When set to false, the output can be seen in VS Code's debugConsole. Due to limitations within `lldb-mi`, integratedTerminal support is not available.



### logging

Optional flags to determine what types of messages should be logged to the Debug Console.

- **exceptions**: Optional flag to determine whether exception messages should be logged to the Debug Console. Defaults to true.
- **moduleLoad**: Optional flag to determine whether module load events should be logged to the Debug Console. Defaults to true.
- **programOutput**: Optional flag to determine whether program output should be logged to the Debug Console. Defaults to true.
- **engineLogging**: Optional flag to determine whether diagnostic engine logs should be logged to the Debug Console. Defaults to false.
- **trace**: Optional flag to determine whether diagnostic adapter command tracing should be logged to the Debug Console. Defaults to false.
- **traceResponse**: Optional flag to determine whether diagnostic adapter command and response tracing should be logged to the Debug Console. Defaults to false.

### visualizerFile

`.natvis` file to be used when debugging. See [Create custom views of native objects](https://docs.microsoft.com/visualstudio/debugger/create-custom-views-of-native-objects) for information on how to create Natvis files.（<u>与.native/自定义视图相关，暂时应该用不上</u>）

### showDisplayString

When a `visualizerFile` is specified, `showDisplayString` will enable the display string. Turning on this option can cause slower performance during debugging.（<u>看起来与上一条有关，不用上一条就不用管这个吧</u>）



### 例子

```json
{
  "name": "C++ Launch (Windows)",
  "type": "cppvsdbg",
  "request": "launch",
  "program": "C:\\app1\\Debug\\app1.exe",
  "symbolSearchPath": "C:\\Symbols;C:\\SymbolDir2",
  "externalConsole": true,
  "logging": {
    "moduleLoad": false,
    "trace": true
  },
  "visualizerFile": "${workspaceFolder}/my.natvis",
  "showDisplayString": true
}
```

## 配置目标应用程序

### args

JSON array of command-line arguments to pass to the program when it is launched. Example `["arg1", "arg2"]`. <u>If you are escaping characters, you will need to double escape them. For example, `["{\\\"arg1\\\": true}"]` will send `{"arg1": true}` to your application.</u>

### cwd

Sets the working directory of the application launched by the debugger.

### environment

Environment variables to add to the environment for the program. Example: `[ { "name": "squid", "value": "clam" } ]`.（**<u>看不懂</u>**）

### 例子

```json
{
  "name": "C++ Launch",
  "type": "cppdbg",
  "request": "launch",
  "program": "${workspaceFolder}/a.out",
  "args": ["arg1", "arg2"],
  "environment": [{ "name": "squid", "value": "clam" }],
  "cwd": "${workspaceFolder}"
}
```



## 自定义GDB或LLDB

### MIMode

指示VS Code将连接到的调试器。必须设置为`gdb`或`lldb`。这是在每个操作系统的基础上预先配置的，可以根据需要进行更改。

### miDebuggerPath

调试器的路径（例如gdb）。仅指定可执行文件时，它将在操作系统的PATH变量中搜索调试器（Linux和Windows上为GDB，OS X上为LLDB）。

### miDebuggerArgs

传递给调试器的其他参数（例如gdb）。

### stopAtEntry 

如果设置为true，则调试器应在目标的入口点停止（在附加时忽略）。默认值为`false`。

### setupCommands 

要设置GDB或LLDB，要执行的JSON命令数组。范例：`"setupCommands": [ { "text": "target-run", "description": "run target", "ignoreFailures": false }]`。

### customLaunchSetupCommands

如果提供的话，它将用一些其他命令替换用于启动目标的默认命令。例如，这可以是“ -target-attach”以便附加到目标进程。空的命令列表将启动命令替换为空，这在将调试器作为命令行选项提供给调试器时很有用。范例：`"customLaunchSetupCommands": [ { "text": "target-run", "description": "run target", "ignoreFailures": false }]`。

### launchCompleteCommand 

调试器完全设置后要执行的命令，以使目标进程运行。允许的值为“ exec-run”，“ exec-continue”，“ None”。默认值为“ exec-run”。

**例：**

```
{
  "name": "C++ Launch",
  "type": "cppdbg",
  "request": "launch",
  "program": "${workspaceFolder}/a.out",
  "stopAtEntry": false,
  "customLaunchSetupCommands": [
    { "text": "target-run", "description": "run target", "ignoreFailures": false }
  ],
  "launchCompleteCommand": "exec-run",
  "linux": {
    "MIMode": "gdb",
    "miDebuggerPath": "/usr/bin/gdb"
  },
  "osx": {
    "MIMode": "lldb"
  },
  "windows": {
    "MIMode": "gdb",
    "miDebuggerPath": "C:\\MinGw\\bin\\gdb.exe"
  }
}
```

### symbolLoadInfo

- **loadAll**：如果为true，则将加载所有库的符号，否则将不加载solib符号。由ExceptionList修改。默认值为true。
- **exceptionList**：以分号分隔的文件名列表（允许使用通配符）`;`。修改LoadAll的行为。如果LoadAll为true，则不要为与列表中任何名称匹配的库加载符号。否则，仅为匹配的库加载符号。例：`"foo.so;bar.so"`



其余主题包括

调试转储文件、远程调试或本地服务器调试调试、附加属性、环境变量定义文件。暂略











