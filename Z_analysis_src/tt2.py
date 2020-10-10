import os
from utilities import *
#LIEF_ROOT
ts = 'castone'
for i in os.walk('/home/zhou/ddisasm_m/test_ddisasm/ddisasm') :
    # if '/home/zhou/DGit/souffle-1.7.1' in i[0] :
    #     continue
    for j in i[2] :

        file = i[0]+'/'+j
        if 'CMakeLists' in file:
            print(file)
        # if ts in file :
        #     print(file)
print('='*80)

for i in os.walk('/home/zhou/ddisasm_m/test_ddisasm/cmakelists') :
    # if '/home/zhou/DGit/souffle-1.7.1' in i[0] :
    #     continue
    for j in i[2] :

        file = i[0]+'/'+j
        # if 'CMakeLists' in file:
        print(file)
