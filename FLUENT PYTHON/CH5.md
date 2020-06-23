

# 概述

Python中函数是一等对象。包含的特点有：

- 在运行时创建
- 能赋值给变量或数据结构中的元素
- 能作为参数传给函数
- 能作为函数的返回结果

**函数对象本身是function类的实例。**

# 高阶函数

把函数作为参数或者把函数作为结果返回的函数被称为高阶函数。书中这部分很多内容本人都已经了解了，于是不赘述。

<u>书中介绍了两个好用的函数</u>：

all 和 any 也是内置的归约函数。
`all(iterable)`
如果 iterable 的每个元素都是真值，返回 True；all([]) 返回 True。
`any(iterable)`
只要 iterable 中有元素是真值，就返回 True；any([]) 返回 False。

# 匿名函数

作者不是很建议使用lambda函数，因为会降低可读性，性能上几乎没有提升。这里的内容用到了直接搜索就好。

# 可调用对象

调用运算符：`()`

能否调用取决于`__call__`

可调用对象：

- 用户定义的函数
- 内置函数
- 内置方法
- 方法
- 类
- 类的实例
- 生成器函数

**判断对象能否调用：**`callable()`

# 用户定义的可调用类型

**探知属性：**`dir()`

一个可能有用的属性：`__dict__`

函数使用 `__dict__`属性存储赋予它的用户属性。这个方法使动态赋予属性成为了可能。

```python
def upper_case_name(obj):
    return ("%s %s" % (obj.first_name, obj.last_name)).upper()
upper_case_name.short_description = 'Customer name'
```

以下这些方法是函数对象特有的：

`['__annotations__', '__call__', '__closure__', '__code__', '__defaults__', '__get__', '__globals__', '__kwdefaults__', '__name__', '__qualname__']`

![image-20200623144240288](E:%5CMDNotes%5CFLUENT%20PYTHON%5Cimage-20200623144240288.png)![image-20200623144306853](E:%5CMDNotes%5CFLUENT%20PYTHON%5Cimage-20200623144306853.png)

知道这些方法的存在就行，可以用的时候再来看。

# 从定位参数到仅限关键字参数

```python
def tag(name, *content, cls=None, **attrs):
```

在这个定义中，要注意的地个地方：

- 第一个定位参数被给到name，剩余的都会被content吸收掉，cls只能通过关键字访问

- 在函数内部，被content吸收掉的变量都存在元组变量content中。

- 多余的关键字参数都回传给`attrs`中。

- 在这个例子中，如果传入content为key的键值对，也会被吸收到`attrs`中。

- 以关键字传`name`时，这一键值对可以放在后面，不影响正常工作。

- 可以用字典加\*\*的方式传参，字典中的键值写作字符串就好。

  ```python
  >>> my_tag = {'name': 'img', 'title': 'Sunset Boulevard','src': 'sunset.jpg', 'cls': 'framed'}
  >>> tag(**my_tag)
  ```

# 获取关于参数的信息

函数对象有个` __defaults__ `属性，它的值是一个元组，里面保存着定位参数和关键字参数的默认值。仅限关键字参数的默认值在` __kwdefaults__ `属性中。然而，参数的名称在`__code__ `属性中，它的值是一个 code 对象引用，自身也有很多属性。

示例函数：

```python
def clip(text, max_len=80):
    """在max_len前面或后面的第一个空格处截断文本
    """
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len) 
        if space_after >= 0: 
            end = space_after 
    if end is None: # 没找到空格
        end = len(text) 
    return text[:end].rstrip()
```
比较朴素的查看参数方式如下

```python
>>> from clip import clip 
>>> clip.__defaults__ 
(80,) 
>>> clip.__code__ # doctest: +ELLIPSIS 
<code object clip at 0x...> 
>>> clip.__code__.co_varnames 
('text', 'max_len', 'end', 'space_before', 'space_after') 
>>> clip.__code__.co_argcount 
2
```
使用 inspect 模块是获取参数信息更好的方式

```python
>>> from clip import clip 
>>> from inspect import signature 
>>> sig = signature(clip) 
>>> sig # doctest: +ELLIPSIS 
<inspect.Signature object at 0x...> 
>>> str(sig) 
'(text, max_len=80)' 
>>> for name, param in sig.parameters.items(): 
... print(param.kind, ':', name, '=', param.default) 
... 
POSITIONAL_OR_KEYWORD : text = <class 'inspect._empty'> 
POSITIONAL_OR_KEYWORD : max_len = 80
```

inspect.signature 函数返回一个 inspect.Signature 对象，它有一个 parameters属性，这是一个有序映射，把参数名和 inspect.Parameter 对象对应起来。

各个 Parameter 属性也有自己的属性，例如 name、default 和 kind（包括下一节表示注释的annotation属性 ）。

`inspect._empty `值表示没有默认值。kind属性的值有五种：

- POSITIONAL_OR_KEYWORD

  可以通过定位参数和关键字参数传入的形参（多数 Python 函数的参数属于此类）。

- VAR_POSITIONAL

  定位参数元组。

- VAR_KEYWORD

  关键字参数字典。

- KEYWORD_ONLY

  仅限关键字参数（Python 3 新增）。

- POSITIONAL_ONLY

  仅限定位参数；目前，Python 声明函数的句法不支持，但是有些使用 C 语言实现且不接受关键字参数的函数（如 divmod）支持。

**书中还介绍了`inspect.Signature`对象的`bind`方法，不过作为非框架开发者，暂时看起来感觉没什么用**




# 函数注释

P3支持新的注释方式：

添加的注解可以是任何类型，其中最常用的类型是类（如 str 或 int）和字符串（如'int > 0'）。

```python
def clip(text:str, max_len:'int > 0'=80) -> str:
```

这种方法不会做额外的工作，只是会把注解存放在`__annotations__ `中，

```python
>>> from clip_annot import clip
>>> clip.__annotations__
{'text': <class 'str'>, 'max_len': 'int > 0', 'return': <class 'str'>}
```



提取注解可以使用`inspect.signature()`

![image-20200623155138978](E:%5CMDNotes%5CFLUENT%20PYTHON%5Cimage-20200623155138978.png) 
这个示例展示了如何提取注释，用的时候再看。




**<u>发现</u>**了一个有趣的针对字符串的函数`ljust()`，看起来可以调节字符串长度。

# 支持函数式编程的包

Python中的`operator `和`functools `等包使函数式编程变得方便。

`functools.reduce`使用函数和一个可迭代对象（我猜）做参数，返回运算结果和迭代器下一元素的结果。

示例：

```                             python
from functools import reduce
def fact(n):
    return reduce(lambda a, b: a*b, range(1, n+1))
```

**`operator `模块为多个算术运算符提供了对应的函数，从而避免使用`lambda`表达式**

```                             python
from functools import reduce
from operator import mul
def fact(n):
    return reduce(mul, range(1, n+1))
```
















