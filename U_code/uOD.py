from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import hashlib
import shutil
import os
import subprocess
L1 = [] #'D:\\PAPER', 'D:\\BOOK2', 'C:\\Users\\65132\\Documents\\WeChat Files\\wxid_4ri4cmu08nhl22\\FileStorage\\File\\2020-10']
L1.append('D:\\PAPER')
L1.append('D:\\BOOK2')
L1.append('C:\\Users\\65132\\Documents\\WeChat Files\\wxid_4ri4cmu08nhl22\\FileStorage\\File\\2020-10')
L1.append('C:\\Users\\65132\\Documents\\WeChat Files\\wxid_4ri4cmu08nhl22\\FileStorage\\File\\2020-11')
L1.append('C:\\Users\\65132\\Documents\\WeChat Files\\wxid_4ri4cmu08nhl22\\FileStorage\\File\\2020-12')
L1.append('D:\\BOOK')

L2 = 'D:\ODrive\OneDrive - The Hong Kong Polytechnic University\\'

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

        files.extend([i[0]+'\\'+x for x in i[2]])
    return files
 
def get_file_md5(filename):
    md5 = hashlib.md5()

    f = open(filename,'rb')
    b = f.read(20000)
    f.close()

    return b

def cpfiles(Dir,path, f) :
    files = get_all_filenames(Dir,path)

    Lx_files = [x.replace(Dir, path) for x in files]
    
    for file in files :
        Des_file = file.replace(Dir, path)

        if os.path.exists(Des_file) :
            if get_file_md5(file) == get_file_md5(Des_file) :
                f.write(''.join((file,',',' tg','\n')))
                # print('tg')
                continue
            else :
                # 
                if os.path.getmtime(Des_file)>os.path.getmtime(file) :
                    f.write(''.join((file,',',' on','\n')))
                    continue

        shutil.copy(file, Des_file)
        f.write(''.join((file,',',' new copy','\n')))
    


def job():
    
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), end = '--')
    print('Start synchronizing ')
    L_td=pl(L1,L2)
    for d in L_td :
        print(d)
    f = open('log.txt', 'w', encoding='utf8')
    for i,t in zip(L1,L_td) :
        cpfiles(i, t, f)
    f.close()
    print('Synchronize over')
    

# BlockingScheduler
scheduler = BlockingScheduler()
scheduler.add_job(job, 'interval', hours=6)#, hours=2

print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), end = '--')
print('Begin!!!')
job()
scheduler.start()

# print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), end = '--')
# print('End')

