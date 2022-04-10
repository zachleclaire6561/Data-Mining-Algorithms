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
mat = scipy.io.loadmat('HandwrittenDigits.mat')

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
(gamma0,gamma1) = (1,0.5)

#create Lattice map for prototype vectors
lattice_map = []
nx = 10
ny = 10
xl = np.linspace(1,10,nx)
yl = np.linspace(1,10,ny)
xv, yv = np.meshgrid(xl, yl)

for i in range(0,10):
    for j in range(0,10):
        x = xv[i][j]
        y = yv[i][j]
        lattice_map.append(np.array([x,y]))

'''
def updateFunc(bmu, alpha, gamma, prototypes):
    print(f"bmu: {bmu} alpha: {alpha}, gamma: {gamma}, prototypes: {prototypes}")
'''

prototypes = SOM.getSOM(prototypes, lattice_map, T_MAX, distance, getSample, alpha0, alpha1, gamma0, gamma1)


#get best matching samples from X_choosen to match prototype
V = []
for proto in prototypes: 
    best_x,index = SOM.getBMU(X_Choosen, proto, SOM.euclidian_distance)
    V.append(best_x)

print(prototypes.shape)

#print(V)
n = 10
m = 10
fig, axs = plt.subplots(n, m)
for i in range(n):
  for j in range(m):
    axs[i,j].imshow(np.reshape(V[n*i+j], (16,16)), interpolation='nearest')

#plt.imshow(np.reshape(V[0], (16,16)), interpolation='nearest')
plt.show()