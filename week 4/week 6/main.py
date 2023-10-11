import numpy as np
import matplotlib.pyplot as plt
data = np.genfromtxt("mjlo-15_0.txt", delimiter=',')
timestamp = data[:, 0]
temperature = data[:, 8]  
humidity = data[:, 6]    
pm25 = data[:, 2]         
pm10 = data[:, 3]         
voltage = data[:, 1]  

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 10))

ax1.plot(timestamp, temperature, label='Temperatuur (°C)', color='blue')
ax1.plot(timestamp, humidity, label='Vochtigheidsgraad (%)', color='red')
ax1.set_xlabel('Tijd')
ax1.set_ylabel('Temperatuur / Vochtigheidsgraad')
ax1.legend()

ax2.plot(timestamp, pm25, label='PM2.5', color='green')
ax2.plot(timestamp, pm10, label='PM10', color='purple')
ax2.set_xlabel('Tijd')
ax2.set_ylabel('PM2.5 / PM10')
ax2.legend()

ax3.plot(timestamp, voltage, label='Voltage (V)', color='yellow')
ax3.set_xlabel('Tijd')
ax3.set_ylabel('Voltage')
ax3.legend()

plt.show()
