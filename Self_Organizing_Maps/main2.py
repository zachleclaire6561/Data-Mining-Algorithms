'''
Code for testing SOM
'''
from SOM import SOM

#imported libraries
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import numpy as np
import scipy.io
from itertools import cycle
import matplotlib.pyplot as plt

#get matlab data as nested dictionary
mat = scipy.io.loadmat('HandWrittenDigits.mat')

#extract data from dictionaries
X = mat['X'].transpose()
I = mat['I'].transpose()

# choose set of digits to test:
X_Choosen = []
set = [2,3,5]
for i in range(0, I.shape[0]):
    if I[i] in set:
        X_Choosen.append(X[i])

#sample function for SOM - cycle if we exceed the number of datapoints
myit = cycle(X_Choosen)

def getSample():
    return next(myit)

#intialization of parameters:
PROTO_COUNT = 100 # the number of prototype vectors
protodim = (PROTO_COUNT, X_Choosen[0].shape[0])
T_MAX = 500*PROTO_COUNT

#generate randomized prototype vectors
print(protodim)

#get center of data
avg = np.zeros((1,X_Choosen[0].shape[0]))
total = 0
#take sum of all vectors
for x in X_Choosen:
    avg += x
    total += 1
#compute average
avg = avg * 1/total
