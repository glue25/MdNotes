from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import subprocess
L1 = ['D:\\PAPER', 'D:\\BOOK2']
L2 = 'D:\ODrive\OneDrive - The Hong Kong Polytechnic University\\'
def job():
    #git add -A
    subprocess.call('git add -A')
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

