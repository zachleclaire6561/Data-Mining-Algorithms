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
    '''

    @staticmethod
    def k_mediods(cluster_count, D, tau):
        if(cluster_count < 1 or tau < 0 or not clustering.is_normal_arr(D)):
            print("Invalid Inputs")

        #initialization:
        #number of vectors
        MAX_THRESH = 10
        n = D.shape[0]
        m = D.shape[1]

        tigtness_current = 0
        tightness_last = 0
        delta_Q = float("inf")
        time = 0
        Identity = np.random.randint(cluster_count, size=n) # each index has value \in {1...k}
        Identity_center = np.random.choice(n, cluster_count, replace=False)  # each index maps to index of means in Indetity
        
        #q_array = np.zeros(1,int(n))
        while(abs(delta_Q) > tau and time < MAX_THRESH):
            #first, we update the cluster centers
            for k in range(0, cluster_count):
                #select indices in cluster k
                indices_k = []
                for i in range(0, n):
                    if(Identity[i] == cluster_count):
                        indices_k.append(i)
                k_count = len(indices_k)
                if(k_count > 0):
                    # center of the data
                    center_dist = float("inf")
                    center_index = 0
                    #calculate total distances
                    for i in range(0,k_count):
                        total_dist = 0
                        for j in range(0,k_count):
                            total_dist += D[indices_k[i],indices_k[j]]
                        if(total_dist < center_dist):
                            center_index = i
                            center_dist = total_dist
                    #print(k, indices_k)
                    #print(f"Indices: {len(indices_k)} Identity_center: {Identity_center.shape} k: {k} center: {center_index}")
                    Identity_center[k] = indices_k[center_index]
            #print(Identity_center)


            #second, assign each vector into a clustering
            for i in range(0, n):
                min = float("inf")
                min_index = -1
                for j in range(0, cluster_count):
                    dist = D[i, Identity_center[j]]
                    print(j, dist)
                    if dist < min:
                        min = dist
                        min_index = j
                print(min_index)
                Identity[i] = min_index
            print(Identity)
            
            #update tightness
            tigtness_current = 0
            for i in range(1, n):
                tigtness_current += D[i, Identity_center[Identity[i]]]**2
            delta_Q = tigtness_current - tightness_last
            tightness_last = tigtness_current
            #update time step
            time += 1
            print(time, delta_Q)
        
        return Identity

    @staticmethod
    def k_mediods_wrapper(k, X, tau, distance):
        #find distance matrix
        D = np.zeros((X.shape[0], X.shape[0]))
        for i in range(0, X.shape[0]):
            for j in range(0, X.shape[0]):
                # itterate through each combination of vectors to construct matrix
                D[i,j] = distance(X[i], X[j])
        #np.savetxt("dist.csv", D, delimiter=",")
        return clustering.k_mediods(k, D, tau)
    
    @staticmethod
    def k_means(k, X, tau):
        print("MeMe")


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