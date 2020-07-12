# """
# 先不考虑命令行传参的事情，先按照手动设计参数进行设计
# """
import os
# from Pysrc.utilities import setOutputFileName, RawFile2Triad, MDFile2Triad
# from Pysrc.parameters import Phase

# InputFileName = 'RawWords\\Jimple生词.txt'

# OutputFileName = setOutputFileName(InputFileName)
# InputPhase = 'R'
# OutputPhase = 'Rn'

# # Check parameters
# assert Phase.IsLegalInputPhase(InputPhase)
# assert Phase.IsLegalOutputPhase(OutputPhase)
# #To be continued ...

# #分单文件多文件情况处理，True对应单文件，条件慢慢补
# if True :
#     # 将文件内容转化成三元组
#     if Phase.IsLegalRawInputPhase(InputFileName) :
#         FileTriad = RawFile2Triad(InputFileName)
#     else :
#         FileTriad = MDFile2Triad(InputFileName)
# else :
#     pass


# s = '      x   t f       '
# print(s.strip())
# import re
# print(re.sub('[ ,]','','a b , sd '))   # abcwrt22666
# class B:
#     def __init__(self,l):
#         super().__init__()
#         self.l = l
#         self.n=0
#     def __next__(self) :
#         if self.n<self.l :
#             self.n += 1
#             return self.n
#         else :
#             self.n = 0
#             raise StopIteration()
#     def __iter__(self):
#         return 0
# class A:
#     def __iter__(self):
#         return B(10)

# a=A()
# print(a)
# for i in a :
#     print(i)
# from operator import itemgetter, indexOf
# __Importance = ['*','=','']
# # print(__Importance(indexOf('=')))
# class Grade(object):
#     def __init__(self) :
#         self._values = {}
#     def __get__(self, instance, instance_type) :
#         print('#'*15)
#         print('in __get__')
#         print('#'*15)
#         if instance is None: return self
#         return self#self._values.get(instance, 0)
#     def __set__(self, instance, value) :
#         print('#'*15)
#         print('in __set__')
#         print('#'*15)
#         if not (0 <= value <= 100):
#             raise ValueError('Grade must be between 0 and 100')
#         self._values[instance] = value

# def R():
#     for i in range(10) :
#         yield i
# s = 'assdgh'
# r = range(10)
# for i,j in zip(s, r) :
#     print(i,'-',j)
os.makedirs('ttt')


