'''
Author: Zach LeClaire
Date: 2/27/2022
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
        m: number of samples/vectors
        n: number of categories/vector entries
    T_MAX: max number of itterations
    distance: distance metrix used
    sample_fun: function used to get data samples
    alpha0: initial learning rate
    alpha1: lower bound for learning rate
    gamma0: initial coupling constant
    gamma1: lower bound on coupling constant
    '''
    @staticmethod
    def getSOM(proto_dim, T_MAX, distance, sample_func, alpha0, alpha1, gamma0, gamma1):
        #generate randomized prototype vectors
        prototypes = np.random(proto_dim)
        
        #Loop
        t = 0 
        while t < T_MAX:
            sample = sample_func()
            bmu = SOM.getBMU(prototypes, sample, distance)
            alpha = SOM.getLearningRate(t, T_MAX, alpha0, alpha1)
            gamma = SOM.getCouplingConstat(t, T_MAX, gamma0, gamma1)

            #update all prototype vectors
            for proto in prototypes:
                dist = distance(sample, proto)
                neigborhood_value = math.exp(-1/(2*gamma**2)*dist**2)
                proto = proto + alpha*neigborhood_value*(sample - proto)
            t += 1
        return prototypes
    
    @staticmethod
    def getBMU(prototypes, sample, distance):
        #init variables
        best_dist = float("inf")
        best_vec = 0

        #check every prototype vector
        for proto in prototypes:
            #check if distance between sample and prototype < current lowest
            new_dist = distance(sample,proto)
            if  new_dist < best_dist:
                best_dist = new_dist
                best_vec = proto
        return best_vec

    @staticmethod
    def getLearningRate(t, T_MAX, alpha0, alpha1):
        return math.max(alpha0 * (1-t/T_MAX), alpha1)

    @staticmethod
    def getCouplingConstat(t, T_MAX, gamma0, gamma1):
        return math.max(gamma0*(1-t/T_MAX), gamma1)

    @staticmethod
    def euclidian_distance(x1,x2):
        return abs(np.linalg.norm(x1-x2))