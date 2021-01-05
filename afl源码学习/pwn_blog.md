为了实现插装，afl重写了汇编器（as），afl是个

# afl-gcc.c源码分析

https://ch4r1l3.github.io/2019/03/05/AFL%E6%BA%90%E7%A0%81%E5%88%86%E6%9E%901%E2%80%94%E2%80%94afl-gcc-c%E6%BA%90%E7%A0%81%E5%88%86%E6%9E%90/



main函数，关键的部分是下面这三行

```
find_as(argv[0]);
edit_params(argc, argv);
execvp(cc_params[0], (char**)cc_params);
```

find_as就是寻找as（汇编器，将汇编变为二进制）

edit_params主要是进行配置，博主提到<u>*AFL可以使用sanitizer去更有效的查找memory access bugs*</u>

execvp的功能是执行elf，应该是真正执行gcc

博主提到打印execvp中参数

```
gcc note.c -o www -B /home/test/afl-2.52b -g -O3 -funroll-loops -D__AFL_COMPILER=1 -DFUZZING_BUILD_MODE_UNSAFE_FOR_PRODUCTION=1
```

其中 -B

```
-B <directory>           Add <directory> to the compiler's search paths
```

大概就是汇编器的目录

后面那些东西我不了解，**回头再看**

# afl-as.c源码分析

*<u>博主提到了ASAN（Address Sanitizer ）https://www.jianshu.com/p/3a2df9b7c353 https://github.com/google/sanitizers/wiki/AddressSanitizer检测内存错误的工具，速度快，已集成到gcc </u>*

edit_params这个函数功能和名字差不多

前面都是配置，后面的add_instrumentation函数是重点

插入的部分代码(开头插入,fprintf是插入)

```c
  if (input_file) {
    inf = fopen(input_file, "r");
    if (!inf) PFATAL("Unable to read '%s'", input_file);
  } else inf = stdin;
  outfd = open(modified_file, O_WRONLY | O_EXCL | O_CREAT, 0600);
  if (outfd < 0) PFATAL("Unable to write to '%s'", modified_file);
  outf = fdopen(outfd, "w");
  if (!outf) PFATAL("fdopen() failed");  

  while (fgets(line, MAX_LINE, inf)) {
    /* In some cases, we want to defer writing the instrumentation trampoline
       until after all the labels, macros, comments, etc. If we're in this
       mode, and if the line starts with a tab followed by a character, dump
       the trampoline now. */
    if (!pass_thru && !skip_intel && !skip_app && !skip_csect && instr_ok &&
        instrument_next && line[0] == '\t' && isalpha(line[1])) {
      fprintf(outf, use_64bit ? trampoline_fmt_64 : trampoline_fmt_32,
              R(MAP_SIZE));
      instrument_next = 0;
      ins_lines++;
    }
    /* Output the actual line, call it a day in pass-thru mode. */
    fputs(line, outf);
```

有一些有趣的地方，trampoline_fmt_64是在.h定义的，看起来是判断64/32的，但是看完定义就不太懂了

pass_thru是配置参数函数中修改的，当被处理对象是.s时为1（不插入）

skip_intel在后面的大循环中被更改，如果是intel格式就为1，好像是要排除手写，按理来说不会被意外触发，意外触发会让整个文件都无法插装

skip_app Detect and skip ad-hoc \_\_asm\_\_ blocks

skip_csect防止64 32掺杂

instr_ok出代码段被置1



下面这篇博客解答了模板是什么，插入时到底发生了什么

https://blog.csdn.net/weixin_43961839/article/details/108630078