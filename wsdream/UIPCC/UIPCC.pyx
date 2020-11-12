#########################################################
# UIPCC.pyx: a python wrapper
# Author: Jamie Zhu <jimzhu@GitHub>
# Created: 2014/2/6
# Last updated: 2016/4/27
#########################################################

import numpy as np
cimport numpy as np # import C-API


#########################################################
# Make declarations on functions from cpp file
#
cdef extern from "c_UIPCC.h":
    void c_UPCC(double *removedData, double *uMean, int numUser, 
    	int numService, int topK, double *predData)
#########################################################


#########################################################
# Function to perform UPCC
# return the predicted matrix
#
def UPCC(removedMatrix, para):
    cdef int numUser = removedMatrix.shape[0]
    cdef int numService = removedMatrix.shape[1]
    cdef int topK = para['topK']
    cdef np.ndarray[double, ndim=2, mode='c'] predMatrix = \
        np.zeros((numUser, numService), dtype=np.float64)
    uMean = np.sum(removedMatrix, axis=1) / (np.sum(removedMatrix > 0, axis=1)
            + np.spacing(1)) # avoid divide-by-zero
    c_UPCC(<double *> (<np.ndarray[double, ndim=2, mode='c']> removedMatrix).data, 
    	<double *> (<np.ndarray[double, ndim=1, mode='c']> uMean).data, 
    	numUser, 
    	numService,
    	topK, 
    	<double *> predMatrix.data)
    return predMatrix
#########################################################


#########################################################
# Function to perform IPCC
# return the predicted matrix
#
def IPCC(removedMatrix, para):
    # use copy() to make sure the transpose makes effect in memory
    predMatrix = UPCC(removedMatrix.T.copy(), para)
    predMatrix = predMatrix.T
    return predMatrix
#########################################################


#########################################################
# Function to perform UIPCC
# return the predicted matrix
#
def UIPCC(removedMatrix, predMatrixUPCC, predMatrixIPCC, para)  :
    lmd = para['lambda']
    predMatrix = lmd * predMatrixUPCC + (1 - lmd) * predMatrixIPCC
    return predMatrix
#########################################################


