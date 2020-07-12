# 2020.7.12

今天成功运行了URL检测的代码，

经验：

1. 分析APP时，要导入一个带dependence的包，soot不需要格外引入。
2. 代码出问题可能是APP版本的问题，验证代码发现API中报错，可以换APP试试，先验证代码是可能运行的。今天的问题是不能解析出Via.apk，而其他两个都可以解析，而出错的代码在soot的API `Scene.v().loadNecessaryClasses()`中，**以后要探索能否有解决办法，现在暂时不用**。
3. 

发现：

1. `Options.v().set_XXX`语句一般对应了命令行中的XXX Option，可以通过查命令行的文档快速了解命令目的。
2. `Options.XXX`是命令行中Option的可选参数，是常量，可以通过这种方式调用。
3. `Scene.v()`与`PackManager.v()`目的待确定。==\*==
4. 窥到了JAVA中正则表达式的写法。
5. `soot.SootClass`与`soot.SootMethod`中应该有很多处理类与方法的API。
6. `soot.ValueBox`提供的大概是代码块相关的API？



==\*==应该整理常用命令行的写法。





























