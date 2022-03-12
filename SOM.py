'''
Author: Zach LeClaire
Date: 2/25/2022
Description: Module For Analyzing Data using a SOM 
'''

import numpy as np
import math

class SOM:
    
    '''
    Module for analyzing data using a self organizing map.
    -----------------------------
    Parameters: 
    proto_dim: dimensions of the prototypes (n,m)
        n: number of prototypes vectors / lattice coordinates
        : number of categories/vector entries
    lattice_map: Hashmap that maps the index in the prototype matrix to its ccoresponding coordinate in the lattice (1,n)
        n: number of vectors
    T_MAX: max number of itterations
    distance: distance metrix used
    sample_fun: function used to get data samples - emulating stream in 
    alpha0: initial learning rate
    alpha1: lower bound for learning rate
    gamma0: initial coupling constant
    gamma1: lower bound on coupling constant
    caller: function to analyze/print data itteration by itteration. 
        caller(bmu, alpha, gamma, prototypes)
        default: does nothing
    '''
    @staticmethod
    def getSOM(prototypes, lattice_map, T_MAX, distance, sample_func, alpha0, alpha1, gamma0, gamma1):
        
        #Loop through t:
        t = 0
        while t < T_MAX:
            sample = sample_func()
            bmu_index, bmu = SOM.getBMU(prototypes, sample, distance)
            alpha = SOM.getLearningRate(t, T_MAX, alpha0, alpha1)
            gamma = SOM.getCouplingConstat(t, T_MAX, gamma0, gamma1)

            #update all prototype vectors
            index = 0
            for proto in prototypes:
                #caller(bmu)
                dist = SOM.lattice_distance(bmu_index, index, lattice_map)
                neigborhood_value = math.exp(-1/(2*gamma**2)*dist**2)
                proto = proto + alpha*neigborhood_value*(sample - proto)
                index += 1

            # bring-bring. Who's there? 
            #caller(bmu, alpha, gamma, prototypes)
            t += 1
        return prototypes
    
    @staticmethod
    def getBMU(prototypes, sample, distance):
        #init variables
        best_dist = float("inf")
        best_vec = 0

        #check every prototype vector
        index = 0
        for proto in prototypes:
            #check if distance between sample and prototype < current lowest
            new_dist = distance(sample,proto)
            if  new_dist < best_dist:
                best_dist = new_dist
                best_vec = proto
            index += 1
        
        return index, best_vec

    @staticmethod
    def getLearningRate(t, T_MAX, alpha0, alpha1):
        return max(alpha0 * (1-t/T_MAX), alpha1)

    @staticmethod
    def getCouplingConstat(t, T_MAX, gamma0, gamma1):
        return max(gamma0*(1-t/T_MAX), gamma1)

    @staticmethod
    def euclidian_distance(x1,x2):
        return abs(np.linalg.norm(x1-x2))

    @staticmethod
    def lattice_distance(i1,i2,lattice_map):
        dist = SOM.euclidian_distance(lattice_map(i1),lattice_map(i2))
        return dist