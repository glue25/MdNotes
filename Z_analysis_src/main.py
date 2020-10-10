
from utilities import find_str_from_file,find_str_from_files
from utilities import get_all_filenames, get_filtered_filenames
from utilities import Dirs



L_ads = get_all_filenames(Dirs['ddisasm'])
Lt = get_filtered_filenames(L_ads, str_not_in='.git')
# for x in L_gtirb+L_souffle+L_dd : 
#     for filename in file_L :
#         if filename in x :
#             Lt.append(x)
# for i in Lt :
#     print(i)
# print(len(Lt))
# Lt = [x for x in Lt if (x.endswith('.cmake')or(x.endswith('.txt')))]
Lr = find_str_from_files('/home/zhou/DGit/libehp-master/build/include', Lt, show_row=False, useRE=True)
for i in Lr :
    print(i)
print(len(Lr))


