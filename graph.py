import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import re
from scipy import interpolate

GLOBAL_AVG_TEMP_CSV = 'data/avg_temp.txt'



#avg_temp = pd.read_csv(GLOBAL_AVG_TEMP_CSV) #load CSV file
#avg_temp = avg_tem.drop([0,1,2]) #drop first 3 rows


year = []
temperature = []
count = 0


with open(GLOBAL_AVG_TEMP_CSV,'r') as f:
	for line in f:
	 	if count > 4:
	 		values = line.strip().split()
	 		year.append(values[0])
	 		temperature.append(float(values[2]))
	 	count += 1


#Interpolate Values
N = len(year)
	 	 
x = np.arange(0,N,1)
y = temperature
f = interpolate.interp1d(x, y, fill_value = "extrapolate")

extrapoltaed_temp = [f(N+i+1) for i in range(60)]
temperature += extrapoltaed_temp


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# Major ticks every 20, minor ticks every 5
major_ticks = np.arange(-0.5, 4, 0.5)
minor_ticks = np.arange(0, 200, 20)


ax.set_xticks(minor_ticks, minor=True)
ax.set_yticks(major_ticks)
#ax.set_yticks(minor_ticks, minor=True)
ax.grid(which='both')

ax.plot(temperature)
ax.plot(np.arange(N,N+60,1),extrapoltaed_temp,marker='.')


plt.show()
