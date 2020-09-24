import re
import os
Dirs = {
    'Dir' : 'D:\\ddisasm\\src',
    'gtirb' : 'D:\\gtirb',
    'souffle' : 'D:\\souffle'
}
Dir = Dirs['Dir']
Dir_gtirb = 'D:\\gtirb'
Dir_souffle = 'D:\\souffle'

def get_all_filenames(Dir) : 
    filenames = os.walk(Dir)
    D_Dir_files = {}
    files = []
    for i in filenames:
        if len(i[1]) != 0 :
            files.extend([i[0]+'\\'+x for x in i[2]])
            D_Dir_files[i[0]] = i[2]
    # with open('D_Dir_files.txt', 'w', encoding='utf8') as f :
    #     f.write(repr(D_Dir_files))
    return files
#                                                                             ;
def find_str_from_file(s, filename, show_row=False, useRE=True):
    # print('===',show_row,useRE)
    pattern = re.compile(s)
    with open(filename, 'r', encoding = 'utf8') as f:
        lines = f.readlines()
        Length = len(lines)
        Locations = []
        if show_row :
            # print(show_row)
            # print(2)
            # identify line and row
            for i, line in enumerate(lines) : 
                pos=0
                while True :
                    match = pattern.search(line, pos)
                    if not match :
                        break
                    s = match.start()
                    e = match.end()
                    pos = e
                    Locations.append((i, (s, e)))
        elif useRE :
            # use re but don't identify row
            for i, line in enumerate(lines) : 
                if pattern.search(line):
                    Locations.append(i)
        else : 
            # print(1)
            # don't use re and don't identify row
            for i, line in enumerate(lines) : 
                if s in line : 
                    Locations.append(i)
        return Locations


#                                                                             ;
def find_str_from_files(s, filenames=None,**file_search_para) :
    '''
    surch a str in filenames

    s : str to search
    filenames : files to be research. If this para is None, filenames are 
    files in Dir
    file_search_para : parameters for find_str_from_file
    '''
    if filenames is None :
        filenames = []
        with open('D_Dir_files.txt', 'r', encoding = 'utf8') as f : 
            D_Dir_files = eval(f.read())
            for folder in D_Dir_files.keys() : 
                sub_files = [folder+'\\'+x for x in D_Dir_files[folder]]
                filenames.extend(sub_files)
    else :
        pass

    Locations = []

    # Search in the file
    # if file_search_para is None :
    #     file_search_para = {}
    # print(file_search_para)
    for file in filenames : 
        Result = find_str_from_file(s, file, **file_search_para)
        Locations.extend([(file, x) for x in Result])
    return Locations



#                                                                             ;

def find_str_from_folders(s, folders=None, D_Dir_files=None, 
    **file_search_para) :
    '''
    surch a str in folders

    s                : str to search
    folders          : folders to be research. If this para is None, find the 
                       s in all the paths
    D_Dir_files      : the Dictionary saves the information about Dirs and 
                       files. If this para is None, use the Dictionary saved 
                       in D_Dir_files.txt
    file_search_para : parameters for find_str_from_file
    '''
    if D_Dir_files is None :
        with open('D_Dir_files.txt', 'r', encoding = 'utf8') as f : 
            D_Dir_files = eval(f.read())
    if folders is None :
        folders = D_Dir_files.keys()
    files = []
    for folder in folders : 
        sub_files = [x if (('\\' in x) or ('/' in x)) else folder+'\\'+x \
            for x in D_Dir_files[folder]]
        files.extend(sub_files)
    # print(len(files))
    Locations = []

    # Search in the file
    # if file_search_para is None :
    #     file_search_para = {}
    
    for file in files : 
        Result = find_str_from_file(s, file, **file_search_para)
        Locations.extend([(file, x) for x in Result])
    return Locations
