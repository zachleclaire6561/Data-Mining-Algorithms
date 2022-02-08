'''
Author: Zach LeClaire
Date: 2/7/2022
Description: Module For Clustering Data. 
'''
import numpy as np

class clustering:
    
    '''
    K_means clustering algorithm
    -----------------------------
    Parameters: 
    k: number of clusters
    tau: tolerance for Clustering (don't set too low)
    D: Data matrix as numpy array. Assume shape: (n, m)
    n = number of vectors
    m = number of elements in vectors
    '''

    @staticmethod
    def k_means(k, D, tau):
        if(k < 1 or tau < 0 or not clustering.is_normal_arr(D)):
            print("Invalid Inputs")

        #initialization:
        #number of vectors
        MAX_THRESH = 100
        n = D.shape[1]
        m = D.shape[2]
        tigtness_current = float("inf")
        tightness_last = 0
        time = 0
        Identity = np.zeros((1,n))
        
        #initial random assignments of charactertic vectors:
        # use numpy.random.choice to do this

        q_array = np.zerros(1,n)
        while(tigtness_current - tightness_last > tau or time > MAX_THRESH):
            #first, we update the charertistic vectors

            #second, assign each vector into a clustering

            #update tightness
            tigtness_last = tigtness_current
            tigtness_current = 0
            # for group in group_set:
                # for vector in group
                    # update in-group tightness

            time += 1

    @staticmethod
    def k_mediods(k, D, tau):
        print("")

    @staticmethod
    def is_normal_arr(a): # a is input array to be tested
        return a.dtype is not np.dtype('object')