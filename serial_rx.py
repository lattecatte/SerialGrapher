import serial
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.dates import DateFormatter
from matplotlib.figure import Figure
from datetime import datetime

ser = serial.Serial('COM29', 9600) # change string 'COM29' to match receiving port
ser.close()
ser.open()

time_format = '%Y/%m/%d %H:%M:%S'

fig = plt.figure(figsize=(7,4))
ax = fig.add_subplot(1, 2, 1)
ax1 = fig.add_subplot(1, 2, 2)
xs = []; ys = []
xs1 = []; ys1 = []

def animate(mag_time, xs, ys, xs1, ys1):
    sentence = ser.readline().decode('Ascii')

    if sentence.startswith('$MAG'):
        sentence_chopped = sentence.split(',')

        mag_sqrt = np.sqrt(float(sentence_chopped[3])**2 + float(sentence_chopped[4])**2 + float(sentence_chopped[5])**2)
        mag_time_raw = sentence_chopped[1] + ' ' + sentence_chopped[2]
        mag_time = datetime.strptime(mag_time_raw, time_format)

        xs.append(mag_time); ys.append(mag_sqrt)
        xs1.append(mag_time); ys1.append(mag_sqrt)
        xs1 = xs1[-15:]; ys1 = ys1[-15:] # replace 15 with your desired time interval (in seconds) for the graph on the right 

        mag_sqrt_max = max(ys)
        mag_sqrt_min = min((v for v in ys if v!=0), default=1000000)
        mag_sqrt_mean = sum(ys) / len(ys)
        
        ax.clear()
        ax.plot(xs, ys)
        ax.text(0.15, 0.35, 'MAX:' + str(round(mag_sqrt_max)), horizontalalignment='right', verticalalignment='center', transform=ax.transAxes)
        ax.text(0.15, 0.25, 'MIN:' + str(round(mag_sqrt_min)), horizontalalignment='right', verticalalignment='center', transform=ax.transAxes)
        ax.text(0.15, 0.15, 'AVG:' + str(round(mag_sqrt_mean)), horizontalalignment='right', verticalalignment='center', transform=ax.transAxes)
        ax.text(0.15, 0.05, 'NOW:' + str(round(ys1[-1])), horizontalalignment='right', verticalalignment='center', transform=ax.transAxes)
        ax.set_title('Cumulative Data', fontsize=18)
        ax.set_xlabel('Time', fontsize=16, labelpad=15)
        ax.set_ylabel('sqrt(MAGx^2 + MAGy^2 + MAGz^2)', fontsize=16, labelpad=30)
        ax.tick_params(axis='x', labelrotation=90)
        ax.yaxis.get_major_locator().set_params(integer=True)
        # ax.set_ylim([0,None]) # uncomment this line to make 0 always visible on the y-axis
        ax1.clear()
        ax1.plot(xs1, ys1)
        ax1.set_title('15s Interval Data', fontsize=18)
        ax1.set_xlabel('Time', fontsize=16, labelpad=15)
        ax1.tick_params(axis='x', labelrotation=90)
        ax1.yaxis.get_major_locator().set_params(integer=True)

        plt.subplots_adjust(left=0.1, bottom=0.2)
        plt.ticklabel_format(style='plain', useOffset=False, axis='y')
        
        print('MAG Line:', len(ys), '(', mag_time_raw, ',', round(mag_sqrt, 2), ')')
        # print(sentence_chopped) # print entire line
        
ani = animation.FuncAnimation(fig, animate, fargs=(xs,ys,xs1,ys1), interval=1)
fig.suptitle('MAG Data from Virtual Serial Port', fontsize=20)
plt.tight_layout()
plt.show()