from colorama import Fore, Style, init
import humanize
import pyfiglet
import psutil
import time
from datetime import datetime

init(autoreset=True)
#title


def get_uptime():
    boot_time = datetime.fromtimestamp(psutil.boot_time())
    uptime_duration = datetime.now() - boot_time
    return humanize.naturaldelta(uptime_duration)

#dashboard loop
try:
    while True:

        title = pyfiglet.figlet_format('My Performance')
        print(Fore.YELLOW + title)
        print(Fore.LIGHTBLACK_EX + f"System Uptime: {get_uptime()}")


        cpu = psutil.cpu_percent(interval=1)
        print(Fore.WHITE +'CPU Usage:' + str(cpu)+'%')

        ram = psutil.virtual_memory().percent
        print(Fore.WHITE + 'RAM Usage:' + str(ram)+'%' )

        print(Fore.GREEN + "-" * 45)
        time.sleep(2)

except KeyboardInterrupt:
    print(Fore.RED + "\nMonitoring stopped by user.")







