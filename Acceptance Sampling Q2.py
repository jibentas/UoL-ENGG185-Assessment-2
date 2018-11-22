import numpy as np
from numpy.random import *

bad = randint(70)+2

test_array=np.zeros(150) # initialises a zero array of size 150
test_array[:bad]=1 # sets values in the array as non-conforming, the amount is set by the variable 'bad' (in this case, 39)
result_list=[] # initialises an empty list
for i in range(10000): # 10000 iterations, as requested
    shuffle(test_array) # creates a pseudo-random array after each iteration
    if sum(test_array[:20])>2: # TRUE (i.e. fail) if there are more than two non-conforming units in the pseudo-random twenty selected units
        result_list.append(1)
    else:
        result_list.append(0)
print(sum(result_list)/len(result_list)) # calculates and outputs the probability of rejecting the lot by comparing the passes to fails

#print(1-sum(result_list)/len(result_list))