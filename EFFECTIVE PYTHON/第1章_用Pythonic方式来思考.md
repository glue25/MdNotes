# 摘要



#章节内容包括1..2..3..

1. 确认自己所用的Python版本
2. 

# 主要内容

## 第1条：确认自己所用的Python版本

使用`python --version`查看当前使用的Python版本。

## 第2条：遵循PEP8风格指南

使用官方推荐的编程风格https://www.python.org/dev/peps/pep-0008/

<u>Pylint ( [http://www.pylint.org/]( http://www.pylint.org/))是一款流行的Python源码静态分析工具。它可以自动检查受测代码是否符合PEP 8风格指南，而且还能找出Python程序里的多种常见错误。</u>

一些原来没注意到的规范：

- <u>每行最多79个字符，注释&字符串72个字符。</u>

- 跨行代码的符号写在一行最前面。

- <u>文件中的那些import语句应该按顺序划分成三个部分，分别表示标准库模块、第三方模块以及自用模块。在每一部分之中，各import语句应该按模块的字母顺序来排列。</u>

- 关于模块级dunders(\_\_XXX\_\_),一般的顺序为：注释字符串，\_\_future\_\_，模块级dunders，import。

  ```python
  """This is the example module.
  
  This module does stuff.
  """
  
  from __future__ import barry_as_FLUFL
  
  __all__ = ['a', 'b', 'c']
  __version__ = '0.1'
  __author__ = 'Cardinal Biggles'
  
  import os
  import sys
  ```

- 标点（,;:...）前不空，最多后面空一格。切片操作里的:前后都空。

- 使用->时前后不空，

- 如果没有参数批注，默认参数里的=前后不空（有参数批注则前后空格）。

  ```python
  # Correct:
  def munge(sep: AnyStr = None): ...
  def munge(input: AnyStr, sep: AnyStr = None, limit=1000): ...
  ```

- 不建议同一行上多个语句

- 单个元素的尾逗号最好括起来，多个元素时的尾逗号最好换行。

  ```python
  # Correct:
  FILES = [
      'setup.cfg',
      'tox.ini',
      ]
  initialize(FILES,
             error=True,
             )
  ```

- 多行注释中，除了最后一句外，在每段的结尾句后加两个空格。

- <u>`from XXX import *`不会引入以下划线开头的对象</u>。

- <u>借助上一条，可以通过下划线来使全局变量仅在模块内使用</u>。

- <u>模块应该用\_\_all\_\_来标记公用的方法</u>。

- 使用`''.startswith() and ''.endswith() `而不是`foo[:3] == 'bar'`来判断。

- 对象类型比较应始终使用isinstance()而不是直接比较类型。

- `try...finally`结构里不建议在`finally`里return，这样会错过`finally`中的异常。

## 第3条：了解bytes、str与unicode的区别

把编解码放在最外围去做，程序核心部分使用str(python2中的unicode)

在Python 3里面,如果通过内置的open函数获取了文件句柄，那么请注意，该句柄默认会采用UTF-8编码格式来操作文件。

而在Python 2中， 文件操作的默认编码格式则是二进制形式。

在P3中，用w参数向文件写随机数字是不行的了，需要wb参数。

## 第4条：用辅助函数来取代复杂的表达式

虽然很多操作可以使用布尔运算符简化，但是为了可读性，可以设立辅助函数，避免复杂表达式。

## 第5条：了解切割序列的办法

list切片操作作为赋值的右值时，操作后产生全新的list，改变这个list不影响原list。<u>例如`b = a[:]`表示复制，下面语句不会报错：</u>

`assert b == a and b is not a`。

list[-0:]是生成原列表的copy，但我觉得这么做可读性差，不用为好。**如果想要复制可以直接`b = a[:]`**。

list切片操作作为赋值的左值时，可以直接更改list，左值中对应的部分会直接被修改，赋值操作可以是不等长的。

## 第6条：在单次切片操作内，不要同时指定start、end和stride

**生成反转序列可以使用`y = x[::-1]`**。

不建议这么做的原因也是出于可读性的考虑，分成两条，一条划定范围一条步进比较好。

## 第7条：用列表推导来取代map和filter

已经在做了，略。

## 第8条：不要使用含有两个以上表达式的列表推导

还是出于可读性的考虑。

## 第9条：用生成器表达式来改写数据量较大的列表推导

节约内存。不过生成器内有状态，不能重复使用。

## 第10条：尽量用enumerate取代range

```python
for i, flavor in enumerate(flavor_list):
    print('%d: %s' % (i + 1， flavor))
=====================================
1: vanilla
2: chocolate
3: pecan
4: strawberry
```

enumerate第二个参数支持从索引不为1的地方开始遍历，但如果支持步长这些操作就好了（<u>**关于这一点说不定未来可以向官方提议**</u>）。

## 第11条：用zip函数同吋遍历两个迭代器

```python
for name, count in zip(names, letters):
    if count > max_letters:
        longest_name = name
        max_letters = count
```

但是zip方法中如果一个迭代器到了尽头，会提前停止。

## 第12条：不要在for和while循环后面写else块

由于此处`else`的特殊语义，容易造成误会。

## 第13条：合理利用try/except/else/finally结构中的每个代码块

1. `finally`

   如果既要将异常向上传播，又要在异常发生时执行清理工作，那就可以使用`try/finally`结构。这种结构有一项常见的用途，就是确保程序能够可靠地关闭文件句柄(<u>还有另外一种写法，参见本书第43条</u>)。

   我理解的finally是使try和except后面接上同一段代码，但是和直接写在异常处理外相比，还是有点差别的。如果是不上报异常仅是处理的情况，try和except中被运行的代码包括<u>try中出错前的代码，异常处理中的代码，finally部分代码，写在外面的后续处理代码</u>。如果处理后上报异常，处理的代码有<u>try中出错前的代码，异常处理中的代码，finally部分代码</u>。可见把必要的后续处理写在finally是明智的，**主要针对的是发生异常后必要的后续代码**。当然没有异常时也会执行

2. `else`

   如果没有异常，就执行else，增加了可读性。可以把没有异常时要执行的语句放在这里。

3. `else`的顺序先于`finally`

















