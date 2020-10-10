from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import subprocess

def job():
    subprocess.call('git pull')
    subprocess.call('git add --all')
    subprocess.call('git commit -m "daily update"')
    subprocess.call('git push MDNotes master')
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

