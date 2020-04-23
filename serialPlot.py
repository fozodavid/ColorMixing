import re
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import constants as c

def plotting():
    fig = plt.figure()
    ax1 = fig.add_subplot(1,1,1)
    def animate(i):
        data = open(c.FILE_NAME, 'r').read()
        lines = data.split('\n')
        rs = []
        gs = []
        bs = []

        for line in lines:
            if re.match('^\d+, \d+, \d+$', line):
                array = line.split(', ')
                rs.append(int(array[0]))
                gs.append(int(array[1]))
                bs.append(int(array[2]))

        ax1.clear()
        ax1.plot(rs, color='r')
        ax1.plot(gs, color='g')
        ax1.plot(bs, color='b')

        plt.ylabel('Levels')
        plt.title('Light Level Measurements')

    plt.title('RGB Readings')

    ani = animation.FuncAnimation(fig, animate, frames=100, interval=200)
    plt.show()
