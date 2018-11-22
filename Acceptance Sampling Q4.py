import numpy as np
import matplotlib.pyplot as plt
from numpy.random import *

def reject(bad):
    plt.figure(0) # initialises a figure
    while bad < 150:
        test_array=np.zeros(150) # initialises a zero array of size 150
        test_array[:bad]=1 # sets values in the array as non-conforming, the amount is set by the variable 'bad' (in this case, 39)
        result_list=[] # initialises an empty list
        for i in range(10000): # 10000 iterations, as requested
            shuffle(test_array) # creates a pseudo-random array after each iteration
            if sum(test_array[:20])>2: # TRUE (i.e. fail) if there are more than two non-conforming units in the pseudo-random twenty selected units
                result_list.append(1)
            else:
                result_list.append(0)
        result=sum(result_list)/len(result_list) # calculates the probability of rejecting the lot by comparing the passes to fails
        l_array.append(result)
        bad+=1 # increments the value of 'bad'
        plt.plot(l_array) # plots the current value of 'result'
    plt.xlabel='''Value of Variable 'bad' ''' # labels the x axis
    plt.ylabel='Probability of Rejection' # labels the y axis
    plt.show() # outputs the graph

reject(0) # starts the 'reject' function with a bad value of 0