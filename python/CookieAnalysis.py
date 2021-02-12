#! /usr/bin/env python

# imports of external packages to use in our code
import sys
import math
import numpy as np
import matplotlib.pyplot as plt

# import our Random class from python/Random.py file
sys.path.append(".")
from MySort import MySort

# main function for our CookieAnalysis Python code
if __name__ == "__main__":
   
    haveInput = False

    for i in range(1,len(sys.argv)):
        if sys.argv[i] == '-h' or sys.argv[i] == '--help':
            continue

        InputFile = sys.argv[i]
        haveInput = True
    
    if '-h' in sys.argv or '--help' in sys.argv or not haveInput:
        print ("Usage: %s [options] [input file]" % sys.argv[0])
        print ("  options:")
        print ("   --help(-h)          print options")
        print
        sys.exit(1)
    
    Nmeas = 1
    times = []
    times_avg = []

    need_rate = True
    
    with open(InputFile) as ifile:
        for line in ifile:
            if need_rate:
                need_rate = False
                rate = float(line)
                continue
            
            lineVals = line.split()
            Nmeas = len(lineVals)
            t_avg = 0
            for v in lineVals:
                t_avg += float(v)
                times.append(float(v))

            t_avg /= Nmeas
            times_avg.append(t_avg)

    Sorter = MySort()

    times = Sorter.DefaultSort(times)
    times_avg = Sorter.DefaultSort(times_avg)
    # try some other methods! see how long they take
    # times_avg = Sorter.BubbleSort(times_avg)
    # times_avg = Sorter.InsertionSort(times_avg)
    # times_avg = Sorter.QuickSort(times_avg)

    # create histogram of our data
    n, bins, patches = plt.hist(times, 100, density=True, facecolor='b', alpha=0.5)

    # plot formating options
    plt.xlabel('Time')
    plt.ylabel('Probability density')
    plt.title('Time_Plot')
    plt.grid(True)
    
    plt.savefig('time.png')

    plt.show()

    plt.clf()

    n2, bins2, patches2 = plt.hist(times_avg, 100, density=True, facecolor='b', alpha=0.5)
    plt.axvline(times_avg[len(times_avg)//2], color='r', linewidth=1, label='50 percentile')
    plt.axvline(times_avg[4*len(times_avg)//25], color='r', linestyle='--', linewidth=1 , label = '1 σ interval')
    plt.axvline(times_avg[21*len(times_avg)//25], color='r', linestyle='--', linewidth=1)
    plt.axvline(times_avg[5*len(times_avg)//200], color='r', linestyle=':', linewidth=1, label = '2 σ interval')
    plt.axvline(times_avg[195*len(times_avg)//200], color='r', linestyle=':', linewidth=1)


    # plot formating options
    plt.xlabel('Average Time')
    plt.ylabel('Probability density')
    plt.title('Time_average_Plot')
    plt.legend()

    
    plt.savefig('time_average.png')


    plt.show()
