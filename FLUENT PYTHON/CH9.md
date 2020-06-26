

# 对象表示形式

这里介绍了获取对象的字符串表示形式的标准方式。

- repr():以便于开发者理解的方式返回对象的字符串表示方式。对用于`__repr__`方法。
- str():以便于用户理解的方式返回对象的字符串表示方式。对用于`__str__`方法。

此外，相关的方法还有`__bytes__`,`__format__`。

bytes 函数会调用` __bytes__` 方法，生成实例的二进制表示形式。

**repr()和eval()为逆方法**



书上的例程有一个地方很有意思：

```python
class Vector2d:
    typecode = 'd' 
    def __init__(self, x, y):
        self.x = float(x) 
        self.y = float(y)
    def __iter__(self):
        return (i for i in (self.x, self.y)) 
    def __repr__(self):
        class_name = type(self).__name__
    return '{}({!r}, {!r})'.format(class_name, *self) 
    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + 
        bytes(array(self.typecode, self)))
```

第二行暂时不细究。

第十行的`*self`很有意思，可以这么做是因为类实现了`__iter__`。

`__bytes__`实现中，为了生成字节序列，我们把 typecode 转换成字节序列，然后………迭代 Vector2d 实例，得到一个数组，再把数组转换成字节序列。



# classmethod与staticmethod

备选构造方法会用到classmethod装饰器。

下面为一个从字节码构造函数的方法：

![image-20200626090026857](E:%5CMDNotes%5CFLUENT%20PYTHON%5CCH9.assets%5Cimage-20200626090026857.png) 

classmethod的用法是定义操作**类**，而不是操作**实例**的方法。









