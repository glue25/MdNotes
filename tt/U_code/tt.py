import os
import hashlib
# L1 = ['D:\\PAPER', 'D:\\BOOK2']
# L2 = 'D:\ODrive\OneDrive - The Hong Kong Polytechnic University\\'


L1 = ['E:\\MDNotes\\U_code', 'E:\\MDNotes\\Z_analysis_src']
# L1 = ['E:\\MDNotes\\Z_analysis_src']
L2 = 'E:\\MDNotes\\tt\\'

def pl(L, L_new):
    L_split = [os.path.split(x) for x in L]
    if not L_new.endswith('\\') :
        if not L_new.endswith('/') :
            L_new = L_new+'\\'
    L_p = [L_new+x[1] for x in L_split]
    return L_p


def get_all_filenames(Dir, mkDir=None) : 
    filenames = os.walk(Dir)
    files = []
    for i in filenames:
        if mkDir is None :
            pass
        else :
            if not os.path.exists(i[0].replace(Dir, mkDir)) :
                os.mkdir(i[0].replace(Dir, mkDir))
            # print('i',i)
            # Dir2 = [i[0]+'\\'+x for x in i[1]]
            # print('Dir2',Dir2)
            # Dir2 = [x.replace(Dir, mkDir) for x in Dir2]
            # print('Dir2',Dir2)
            # for s_dir in Dir2:
            #     if not os.path.exists(s_dir) :
            #         print('fdkfnjd')
            #         os.mkdir(s_dir)#.replace('\\','/'))

        files.extend([i[0]+'\\'+x for x in i[2]])
    print('=======================================================')
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
    

    files = get_all_filenames(Dir,path)
    # for i in files :
    #     print(i)
    # make dir
    

    print('===========================================')
    Lx_files = [x.replace(Dir, path) for x in files]
    for file in files :
        Des_file = file.replace(Dir, path)

        # Des_file exists and is same to the origin one
        if os.path.exists(Des_file) :
            if get_file_md5(file) == get_file_md5(Des_file) :
                continue
        # if not os.path.exists(os.path.split(Des_file)[0]):
        #     os.mkdir(os.path.split(Des_file)[0])
        os.system('copy '+file+' '+Des_file)


#os.path.getmtime(file) 
L_td=pl(L1,L2)
print(L_td)
for i,t in zip(L1,L_td) :
    cpfiles(i, t)
    
    
# files=os.walk(L1[1])
# for i in files :
#     print(i)

