from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import subprocess
import os
import shutil
def delete_pycache():
    dir_ = os.getcwd()
    target = '__pycache__'
    for dirs in os.walk(dir_) :
        for dir__ in dirs[1] :
            dirname = os.path.join(dirs[0], dir__)
            if target in dirname :
                print(dirname)
                shutil.rmtree(dirname)
def job():
    #git add -A
    #subprocess.call('git add --all')
    # subprocess.call('git commit -m "daily update"')
    # subprocess.call('git push MDNotes master')
    os.system('git pull')
    delete_pycache()
    os.system("git add --all")
    os.system('git commit -m "daily update"')
    os.system("git push")
    s = ''.join((datetime.now().strftime("%Y-%m-%d %H:%M:%S"),'--Updated!'))
    print(s)

# BlockingScheduler
scheduler = BlockingScheduler()
scheduler.add_job(job, 'interval', hours=6)#, hours=2

print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), end = '--')
print('Begin!!!')
job()
scheduler.start()

print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), end = '--')
print('End')

