'''
Author: Zach LeClaire
Date: 2/7/2022
Description: Module For Clustering Data. 
'''
import numpy as np
import math

class LDA:
    
    '''
    LDA Wrapper
    -----------------------------
    Parameters: 
    Data matrix 
    Desc: D Shape: (MXN)
    Annontation matrix L Shape: (1 X N)

    '''
    @staticmethod
    def LDA_Wrapper(D, L):
        #initialize parameters
        n = D.shape[1]
        m = D.shape[0]
        # stores separate matrix for each cluster
        numCats = LDA.getMax(L)
        X_W = [None] * LDA.getMax(L)
        # for each j,
        for j in range (0, numCats):
            bool_arr = np.where(L == j)
            X_W[j] = D.where(bool_arr)
            
        #center each matrix: 
        for j in range (0, numCats):
            avg = np.zeros((1,X_W[j].shape[1]))
            total = 0
            #take sum of all vectors
            for x in X_W[j]:
                avg += x
                total += 1
            #compute average
            avg = avg * 1/total
            X_W[j] = X_W[j] - np.tile(avg, (X_W[j].shape[0], 1) )
        
        X_W_temp = None
        for x in X_W:
            if X_W_temp == None:
                X_W_temp = x
            X_W_temp

        X_W = np.concatenate(X_W)


        centering_matrix = np.identity() - 1/n*np.ones((n,n))
        
        # create 

        return 1


        @staticmethod
        def getMax(I):
            max = -1
            for i in I:
                if i > max: 
                    max = i
            return max