import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

columns = ['CPU_Usage_%', 'RAM_Usage_%']

#setting runt time limit
start_time = datetime.strptime("09:45:00", "%H:%M:%S")
end_time = datetime.strptime("09:47:30", "%H:%M:%S")

#30 sec tick
time_ticks = [start_time + timedelta(seconds=30 * i) for i in range(int((end_time - start_time).seconds / 30) + 1)]

# Load data
df = pd.read_csv('system_monitor.csv', usecols= columns)

#plot
df.plot()

# Set x-axis limits
#plt.xlim([start_time, end_time]) # adding this creates the parameters I want but doest show the data

# Format y-axis as percentage
plt.ylim(0, 90)

# Rotate x-ticks
plt.title('Pc Performance')
plt.xlabel('Run Time')
plt.ylabel('Percentage %')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()