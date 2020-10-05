import os
from utilities import *
#LIEF_ROOT
ts = 'castone'
for i in os.walk('/') :
    for j in i[2] :
        file = i[0]+'/'+j
        if True:#'LIEF' in i[0] :
            if 'LIEF' in i[0] :

                print(file)
                
        # if ts in file :
        #     print(file)