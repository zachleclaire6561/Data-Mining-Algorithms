'''
Author: Zach LeClaire
Date: 2/7/2022
Description: Module For Clustering Data. 
'''
import numpy as np
import math

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
    def k_mediods_general(k, D, tau, distance):
        if(k < 1 or tau < 0 or not clustering.is_normal_arr(D)):
            print("Invalid Inputs")

        #initialization:
        #number of vectors
        MAX_THRESH = 1000
        n = D.shape[0]
        m = D.shape[1]
        k=10
        tigtness_current = float("inf")
        tightness_last = 0
        time = 0
        Identity = np.zeros((1,n)) # each index has value \in {1...k}
        Identity_center = np.random.choice(n, k, replace=False)  # each index maps to index of means in Indetity
        
        #q_array = np.zeros(1,int(n))
        while(tigtness_current - tightness_last > tau or time > MAX_THRESH):
            #first, we update the charertistic vectors
            for k in range(1, k):
                #select indices in cluster k
                indices_k = np.where(np.any(Identity == k, axis=1))
                
                #tuples are a curse and a blessing
                k_count = indices_k[0].shape[0]
                center_dist = float("inf")
                center_index = -1
                #calculate distances
                for i in range(1,k_count):
                    total_dist = 0
                    for j in range(1,k_count):
                        total_dist += distance(D[indices_k[i]], D[indices_k[j]])
                    if(total_dist < center_dist):
                        center_index = i
                print(indices_k, center_index)
                Identity_center[k] = indices_k[center_index]

            #second, assign each vector into a clustering
            for i in range(1, n):
                min = float("inf")
                min_index = 0
                for j in range(1,k):
                    dist = distance(D[i], D[Identity_center[j]])
                    if(dist < min):
                        min_index = j
                Identity[i] = min_index

            #update tightness
            tigtness_last = tigtness_current
            tigtness_current = 0

            for i in range(1, n):
                tigtness_current += distance(D[i], D[Identity_center[Identity[i]]])**2
            
            #update time step
            time += 1
        
        return Identity

    @staticmethod
    def k_mediods(k, D, tau):
        clustering.k_mediods_general(k, D, tau, clustering.euclidian_distance)
    
    @staticmethod
    def k_means(k, D, tau):
        clustering.k_mediods_general(k, D, tau, clustering.euclidian_distance)


    @staticmethod
    def is_normal_arr(a): # a is input array to be tested
        return a.dtype is not np.dtype('object')

    @staticmethod
    def euclidian_distance(x1,x2):
        return np.linalg.norm(x1-x2)

    #non-convergent algorithms anyone?
    @staticmethod
    def random_distance(x1,x2):
        return math.random()