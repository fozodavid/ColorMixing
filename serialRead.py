import os
import time
import serial
import re
from collections import deque
import constants as c

def reading():
    ser = serial.Serial('/dev/ttyACM0', 9600)
    if (os.path.isfile(c.FILE_NAME)):
        os.remove(c.FILE_NAME)

    os.mknod(c.FILE_NAME)

    while True:
        contents = []
        totalLength = 0
        
        with open(c.FILE_NAME, "r") as file:
            contents = deque(file.read().split('\n'))
            totalLength = len(contents)

        if (totalLength > c.MAX_LENGTH):
            contents.popleft()
            with open(c.FILE_NAME, "w") as file:
                file.write('\n'.join(list(contents)))

        try:
            data = ser.readline().decode("utf-8")
            values = re.findall('\d+', data)
#            print(values)
                
            with open(c.FILE_NAME, "a") as file:
                if len(values) == 3 and type(values[2]) != '':
                    file.write("{0}, {1}, {2}\n".format(values[0], values[1], values[2]))
#                    print("data written")
        except UnicodeDecodeError:
            print("unicode decode Error")

        time.sleep(0.005)
