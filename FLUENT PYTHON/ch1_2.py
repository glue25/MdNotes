
from math import hypot #求模
'''
__repr__:h获得一个对象的字符串表示形式，否则在打印实例时会是<Vector object at 地址>
__str__:只有在str()函数中才用到
若无__str__，解释器会用__repr__替代

__rmul__待补充
P10自定义布尔值
P11 表
'''
class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __repr__(self):
        return 'Vector(%r,%r)'%(self.x,self.y)
    def __abs__(self):
        return hypot(self.x,self.y)
    def __bool__(self):
        return bool(abs(self))
    def __add__(self, other):
        x=self.x+other.x
        y=self.y+other.y
        return Vector(x,y)
    def __mul__(self, other):
        return Vector(self.x*other.x,self.y*other.y)
