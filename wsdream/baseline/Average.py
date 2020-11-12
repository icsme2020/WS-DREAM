########################################################
# Average.py: Baseline approach to time-aware QoS prediction
# Author: Jamie Zhu <jimzhu@GitHub>
# Created: 2016/4/26
# Last updated: 2016/4/26
########################################################

import numpy as np


#======================================================#
# Function to perform the prediction algorithm
#======================================================#
def predict(removedTensor, para):
    # average QoS of each service
    numService = removedTensor.shape[1]
    predTensor = np.zeros(removedTensor.shape)
    for i in xrange(numService):
        removedMatrix = removedTensor[:, i, :]
        sMean = np.sum(removedMatrix) / (np.sum(removedMatrix > 0) + np.spacing(1))
        predTensor[:, i, :] = sMean
        
    return predTensor


