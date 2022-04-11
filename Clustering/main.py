#Run code from here:
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import numpy as np
import scipy.io
from clustering import clustering
mat = scipy.io.loadmat('CongressionalVoteData.mat')
X = mat['X'].transpose()
I = mat['I'].transpose()

k=2

#process by removing reps with zero-votes
no_show = []
for i in range(0,X.shape[0]):
    if(np.all(X[i] == 0)):
        no_show.append(i)
j = 0
while j < len(no_show):
    # we need to make an adjustment each time by j because the array shifts by j
    X = np.delete(X, no_show[j]-j, 0)
    j+=1
print(no_show)


np.savetxt("X.csv", I, delimiter=",")
I_n = clustering.k_mediods_wrapper(k, X, -0.001, clustering.voting_distance)
print(I_n)
print(np.sum(I_n))

np.savetxt("I.csv", I, delimiter=",")
np.savetxt("I_n.csv", I_n, delimiter=",")
'''

fig, ax = plt.subplots()
ax.scatter(X[:-1], X[1:], np.where(I<0, I))

ax.set_xlabel(r'$\Delta_1$', fontsize=15)
ax.set_ylabel(r'$\Delta_2$', fontsize=15)
ax.set_title('Volume and percent change')

ax.grid(True)
fig.tight_layout()

plt.show()

'''