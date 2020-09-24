import os
import hashlib
# L1 = ['D:\\PAPER', 'D:\\BOOK2']
# L2 = 'D:\ODrive\OneDrive - The Hong Kong Polytechnic University\\'


L1 = ['E:\\MDNotes\\U_code\\', 'E:\\MDNotes\\Z_analysis_src\\']
L2 = 'E:\\MDNotes\\tt\\'

# def pl(L, L_new):
#     L_split = [os.path.split(x) for x in L]
#     if not L_new.endswith('\\') :
#         if not L_new.endswith('/') :
#             L_new = L_new+'\\'
#     L_p = [L_new+x[1] for x in L_split]
#     return L_p


def get_all_filenames(Dir) : 
    filenames = os.walk(Dir)
    D_Dir_files = {}
    files = []
    for i in filenames:
        # print(i)
        # print('==================')
        if len(i[1]) == 0 :
            files.extend([i[0]+'\\'+x for x in i[2]])
            D_Dir_files[i[0]] = i[2]
    return files


 
def get_file_md5(filename):
    md5 = hashlib.md5()
    f = open(filename,'rb')
    while True:
        b = f.read(8096)
        if not b:
          break
    md5.update(b)
    f.close()
    return md5.hexdigest()

def cpfiles(Dir,path) :
    files = get_all_filenames(Dir)
    Lx_files = [x.replace(Dir, path) for x in files]
    for file in files :
        Des_file = file.replace(Dir, path)

        # Des_file exists and is same to the origin one
        if os.path.exists(Des_file) :
            if get_file_md5(file) == get_file_md5(Des_file) :
                continue
        os.system('copy '+file+' '+Des_file)


#os.path.getmtime(file) 
for i in L1 :
    cpfiles(i, L2)
    
    


