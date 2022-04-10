'''
Author: Zach LeClaire
Date: 2/25/2022
Description: Module For running LVQ 
'''

import numpy as np
import math

class LVQ:
    

    #fields:
    prototypes: np.ndarray

    '''
    Module for analyzing data using a self organizing map.
    -----------------------------
    Parameters: 
    PROTO_COUNT: number of prototypes (eg k = 9)
        note: should be an odd number
    lattice_map: Hashmap that maps the index in the prototype matrix to its ccoresponding coordinate in the lattice (1,n)
        n: number of vectors
    T_MAX: max number of itterations
    distance: distance metric used
    sample_fun: function used to get data samples - emulating stream in 
    alpha0: initial learning rate
    gamma0: initial coupling constant
    '''
    def train(X1, X2, PROTO_COUNT, T_MAX, distance, sample_func, alpha0, gamma0):

        #get center of data
        avg = np.zeros((1,X[0].shape[0]))
        total = 0
        #take sum of all vectors
        for x in X:
            avg += x
            total += 1
        #compute average
        avg = avg * 1/total
        LVQ.prototypes = np.tile(avg, (PROTO_COUNT, 1) ) + (0.5*np.ones((PROTO_COUNT, X[0].shape[0])) - np.random.rand(PROTO_COUNT, X[0].shape[0]))

        beta = math.log(10)/T_MAX
        #Loop through t:
        t = 0
        while t < T_MAX:
            sample = LVQ.sample_func(X,t)
            bmu_index, bmu = LVQ.getBMU(LVQ.prototypes, sample, distance)
            alpha = LVQ.getLearningRate(t, alpha0, beta)

            #update the best matching prototype vector
            index = 0
            LVQ.prototypes[bmu_index] = bmu + alpha*(sample - bmu)
            t += 1
        #we are done!

    @staticmethod
    def sample_func(X,t):
        index = t%X.shape[1]
        return X[t]
    
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
    def getLearningRate(t, alpha0, beta):
        return alpha0 * math.exp(-t*beta)

    @staticmethod
    def euclidian_distance(x1,x2):
        return abs(np.linalg.norm(x1-x2))