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
l = ['a','b','c']
print('|'.join(['']+l+['']))

