import multiprocessing
import time
import serialRead
import serialPlot

if __name__ == '__main__':
    p1 = multiprocessing.Process(name='p1', target=serialRead.reading)
    p2 = multiprocessing.Process(name='p2', target=serialPlot.plotting)
    p1.start()
    p2.start()
