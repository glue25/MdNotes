# """
# 先不考虑命令行传参的事情，先按照手动设计参数进行设计
# """

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

class A:
    L = []
    l=None

a = A()
print(a.L is A.L) # 可变对象，实例属性和类属性一致
print(a.l is A.l) # 不可变对象，实例属性和类属性一致
a.l=30
print(a.l is A.l) # 修改不可变对象后，实例属性和类属性不一致
a.L.append('123')
print(a.L is A.L) # 修改可变对象后，实例属性和类属性一致

a.ll=3
print(a.ll)       # 为不存在的实例属性赋值，会新建实例属性
print('='*10)

b = A()
print(b.L is a.L) #两个实例共享可变对象属性
print(b.l == a.l)
print(b.l is A.l) #没修改的情况下，没有建新对象
