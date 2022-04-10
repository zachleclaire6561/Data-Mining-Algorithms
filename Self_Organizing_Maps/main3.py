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

#prototype matrix = average + rand-offset centered at zero in R^n
prototypes = np.tile(avg, (PROTO_COUNT, 1) ) + (0.5*np.ones((protodim[0], protodim[1])) - np.random.rand(protodim[0], protodim[1]))

distance = SOM.euclidian_distance
(alpha0,alpha1) = (0.9,0.01)
(gamma0,gamma1) = (PROTO_COUNT/3,0.5)

'''
def updateFunc(bmu, alpha, gamma, prototypes):
    print(f"bmu: {bmu} alpha: {alpha}, gamma: {gamma}, prototypes: {prototypes}")
'''

prototypes = SOM.getSOM(protodim, T_MAX, distance, getSample, alpha0, alpha1, gamma0, gamma1)

#get best matching samples from X_choosen to match prototype
V = []
for proto in prototypes: 
    best_x = SOM.getBMU(X_Choosen, proto, SOM.euclidian_distance)
    V.append(best_x)
print(V)
plt.imshow(np.reshape(V[0], (1,1)), interpolation='nearest')
plt.show()