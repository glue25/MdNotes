

https://blog.csdn.net/weixin_43961839/article/details/108630078

对afl-as的解析很到位，写入的不只是那一个随机数，还有处理堆栈的汇编代码，以及调用*\_\_afl_maybe_log*的代码。main_payload大约是200行左右的汇编代码，包含申请共享内存，记录覆盖率等逻辑功能。



该hashmap并非记录的每个插桩点的触发次数，而是将上一个插桩点ID与当前插桩点ID的异或值作为key，也就是该map记录的是路径的边而不是点，也就是每次跳转路径的触发次数，然后再通过该map来确定每次fuzz是否触发了新的路径。

真正记录的是插装点与上一个插装点的异或值



add_instrumentation：插桩函数，在文件对应的地点插入上文分析中的trampoline和main_payload，插桩点类型如下：

```c
/*
^main:      - function entry point (always instrumented)
^.L0:       - GCC branch label
^.LBB0_0:   - clang branch label (but only in clang mode)
^\tjnz foo  - conditional branche
*/
```