from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import shutil
import os
path_project = '/home/zhou/ddisasm_m/test_ddisasm/ddisasm'
path_target = '/home/zhou/ddisasm_m/test_ddisasm/cmakelists'

def pl(L, L_new):
    L_split = [os.path.split(x) for x in L]
    if not L_new.endswith('/') :
        L_new = L_new+'/'
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

        files.extend([i[0]+'/'+x for x in i[2]])
    return files

def rm_empty_folder(path_target) :
    paths = []
    file_paths = []
    useful_paths = []
    
    # path_target = '/home/zhou/ddisasm_m/test_ddisasm/cmakelists'
    for i in os.walk(path_target) :
        paths.append(i[0])
        if i[2] :
            file_paths.append(i[0])
    
    paths = [x.replace(path_target,'') for x in paths]
    file_paths = [x.replace(path_target,'') for x in file_paths]


    for path in paths :
        for file_path in file_paths :
            if path in file_path :
                useful_paths.append(path)
    useful_paths = [path_target+x for x in useful_paths]
    paths = [path_target+x for x in paths]
    for path in paths :
        if path not in useful_paths :
            try:
                shutil.rmtree(path)
            except :
                pass
            


'''


'''
def cpfiles(Dir,path) :
    files = get_all_filenames(Dir,path)

    Lx_files = [x.replace(Dir, path) for x in files]
    
    for file in files :
        Des_file = file.replace(Dir, path)
        if 'CMakeLists' not in Des_file :
            continue
        shutil.copy(file, Des_file)
    rm_empty_folder(path_target)
    


cpfiles(path_project,path_target)
    
