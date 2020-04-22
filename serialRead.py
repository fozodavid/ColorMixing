import serial
import re
import matplotlib.pyplot as plt
import matplotlib.animation as animation

ser = serial.Serial('/dev/ttyACM0', 9600)

plt.show()
newValues = [0,0,0]

while True:
    data = ser.readline().decode("utf-8")
    values = re.findall('\d+', data)
    if (len(values) == 3):
        newValues = values

    plt.clf()
    plt.bar([1], newValues[0], color='r')
    plt.bar([2], newValues[1], color='g')
    plt.bar([3], newValues[2], color='b')

