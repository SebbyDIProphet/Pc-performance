import csv
import psutil
import time
from datetime import datetime

startTime = time.time()
#csv file name
filename = "system_monitor.csv"

#write the csv header if file don't exist
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Timestamp', 'CPU_Usage_%', 'RAM_Usage_%', 'Uptime_seconds'])


#Funtion to get Uptime
def get_uptime():
    boot_time = psutil.boot_time()
    current_time = time.time()
    uptime = current_time - boot_time
    return int(uptime)


#monitor loop
try:

    while True:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cpu_usage = psutil.cpu_percent(interval=1)
        ram_usage = psutil.virtual_memory().percent
        uptime = get_uptime()

        #write to csv
        with open(filename, mode = 'a', newline = '') as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, cpu_usage, ram_usage, uptime])

        print(f"[{timestamp} CPU: {cpu_usage}% | RAM: {ram_usage}% | Uptime: {uptime}s")

        #intervals between each run
        time.sleep(3)


except KeyboardInterrupt:
    print("Monitoring stopped by user.")


