# %%
#Here: function to handle optimal splits:

import numpy as np
import scipy.io
from Tree import BinaryTree, Node

#get matlab data as nested dictionary
image = scipy.io.loadmat('MysteryImage.mat')

#extract compressed matrix from dictionaries

#columns: y-axis; rows: x-axis; vals: [r,g,b]
Y = image['cols']
X = image['rows']
V = image['vals']

# number of pixels
n = np.shape(X)[0]

# %%
#split s means we check all y-values to see if they're above or below the line
'''
split cost functions
Desc: finds cost of a split
parameters: 
s: split value
c1: mean color left/below split [r,g,b]
c2: mean color right/above split [r,g,b]
'''
def hor_split_cost(s, c1, c2):
    cost = 0
    for i in range (0,n):
        if(Y[i] <= s):
            cost += np.linalg.norm(V[i]-c1)**2
        else:
            cost += np.linalg.norm(V[i]-c2)**2
    return cost

def vert_split_cost(s,c1,c2):
    cost = 0
    for i in range (0,n):
        if(X[i] <= s):
            cost += np.linalg.norm(V[i]-c1)**2
        else:
            cost += np.linalg.norm(V[i]-c2)**2
    return cost


def optimal_split_vert(points_in_range):
    s = points_in_range[0]
    opt_c1 = np.zeros((1,3))
    opt_c2 = np.zeros((1,3))
    min_cost = float('inf')

    for i in points_in_range:
        #left mean
        c1 = np.zeros((1,3))
        #right mean
        c2 = np.zeros((1,3))
        #Horzontal split:
        count_1 = 0
        for j in points_in_range:
            if(Y[j] <= Y[i]):
                c1 += V[j]
                count_1 += 1
            else:
                c2 += V[j]
        #average
        if(count_1 > 0):
            c1 = 1/count_1 * c1
        if(len(points_in_range) - count_1 > 0):
            c2 = 1/(len(points_in_range) - count_1) * c2
        #left mean
        c1 = np.zeros((1,3))
        #right mean
        c2 = np.zeros((1,3))

        vert_cost = hor_split_cost(i,c1,c2)
        # if option lower cost, set to new optimal split value & save info about split
        if(vert_cost < min_cost):
            s = i
            min_cost = vert_cost
            opt_c1 = c1
            opt_c2 = c2

        #END For Loop
    #return information about split
    return s, opt_c1, opt_c2, min_cost



def optimal_split_hor(points_in_range):
    s = points_in_range[0]
    opt_c1 = np.zeros((1,3))
    opt_c2 = np.zeros((1,3))
    min_cost = float('inf')

    for i in points_in_range:
        #left mean
        c1 = np.zeros((1,3))
        #right mean
        c2 = np.zeros((1,3))
        #Horzontal split:
        count_1 = 0
        for j in points_in_range:
            if(X[j] <= X[i]):
                c1 += V[j]
                count_1 += 1
            else:
                c2 += V[j]
        #average
        if(count_1 > 0):
            c1 = 1/count_1 * c1
        if(len(points_in_range) - count_1 > 0):
            c2 = 1/(len(points_in_range) - count_1) * c2
        #left mean
        c1 = np.zeros((1,3))
        #right mean
        c2 = np.zeros((1,3))

        hor_cost = hor_split_cost(i,c1,c2)
        # if option lower cost, set to new optimal split value & save info about split
        if(hor_cost < min_cost):
            s = i
            min_cost = hor_cost
            opt_c1 = c1
            opt_c2 = c2

        #END For Loop
    #return information about split
    return s, opt_c1, opt_c2, min_cost
# %%
'''
Regression function
Desc: does tree regression on the image data
parameters: 
MAX_ITTER: maximum number of itterations
X_interval: [a,b] lower and upper boundaries of interval
Y_interval: [a,b] lower and upper boundaries of interval  

Return Values: 
False: Failure

'''

MAX_ITTER = 3
itter = 0
def regression(X_interval, Y_interval, parent_list):
    #assemble list of pts
    points_in_range = parent_list
    for i in range(0,n):
        if(not (X[i] in range(X_interval[0], X_interval[1]) and Y[i] in range(Y_interval[0], Y_interval[1]))):
            np.delete(points_in_range, i)
    print("points found")
    #if(len(points_in_range) < 0):
    #    return False
    # Direction: True = horizontal; False = vertical

    #setting up tree structure:
    s_hor,c1_hor,c2_hor,min_cost_hor = optimal_split_hor(points_in_range)
    s_vert,c1_vert,c2_vert,min_cost_vert = optimal_split_vert(points_in_range)
    node = None
    if(min_cost_hor <= min_cost_vert):
        node = Node(s_hor, True, c1_hor, c2_hor)
    else:
        node = Node(s_vert, False, c1_vert, c2_vert)
    global itter
    itter +=1
    print(f'itteration: {itter}')

    #check if terminal node:
    if(itter < MAX_ITTER):        
        if(node.direction):
            #Horizontal split:
            #We need to do the thing
            node.left = regression(X_interval, [Y_interval[0], Y[node.split]], points_in_range)
            node.right = regression(X_interval, [Y[node.split], Y_interval[1]], points_in_range)
        else:
            #Vertical Split:
            node.left = regression([Y_interval[0], Y[node.split]], Y_interval, points_in_range)
            node.right = regression([Y[node.split],Y_interval[1]], Y_interval, points_in_range)
    else: 
        node.left = None
        node.right = None
    #return node
    return node

# %%
'''
print('starting to run regression:')
root = regression([0, 1456],[0, 2592],np.arange(n))
tree = BinaryTree(root)
'''


Y = [0.25, 0.1, 0.8]
X = [0.25,0.8,0.6]
V = [[0.1,0.5,0.2],[0.4,0.1,0.3],[0.9,0.2,0.0]]
n = 3

X_interval = [0,1]
Y_interval = [0,1]

root = regression(X_interval, Y_interval, np.arange(n))
tree = BinaryTree(root)
tree.print_tree()