########################################################
# evaluator.py
# Author: Jamie Zhu <jimzhu@GitHub>
# Created: 2014/2/6
# Last updated: 2015/8/30
########################################################

import numpy as np
import time
from commons.utils import logger # import from ../../commons
from lib import evallib # import from ../lib
from wsdream.baseline import Average
from scipy import stats
import multiprocessing


#======================================================#
# Function to evalute the approach at all settings
#======================================================#
def execute(tensor, para):
    # loop over each density and each round
    if para['parallelMode']: # run on multiple processes
        pool = multiprocessing.Pool()
        for den in para['density']: 
            for roundId in xrange(para['rounds']):
                pool.apply_async(executeOneSetting, (tensor, den, roundId, para))
        pool.close()
        pool.join()
    else: # run on single processes
        for den in para['density']:
            for roundId in xrange(para['rounds']):
                executeOneSetting(tensor, den, roundId, para)
    # summarize the dumped results
    evallib.summarizeResult(para, tensor.shape[2])


#======================================================#
# Function to run the prediction approach at one setting
#======================================================#
def executeOneSetting(tensor, density, roundId, para):
    logger.info('density=%.2f, %2d-round starts.'%(density, roundId + 1))
    (numUser, numService, numTime) = tensor.shape

    # remove the entries of data to generate trainTensor and testTensor
    (trainTensor, testTensor) = evallib.removeTensor(tensor, density, roundId, para) 

    # invocation to the prediction function
    startTime = time.clock() # to record the running time for one round             
    predictedTensor = Average.predict(trainTensor, para) 
    runningTime = float(time.clock() - startTime) / numTime

    # evaluate the prediction error 
    for sliceId in xrange(numTime):
        testMatrix = testTensor[:, :, sliceId]
        predictedMatrix = predictedTensor[:, :, sliceId]
        (testVecX, testVecY) = np.where(testMatrix)
        testVec = testMatrix[testVecX, testVecY]
        predVec = predictedMatrix[testVecX, testVecY]
        evalResult = evallib.errMetric(testVec, predVec, para['metrics'])        
        result = (evalResult, runningTime)

        # dump the result at each density
        outFile = '%s%s_%s_result_%02d_%.2f_round%02d.tmp'%(para['outPath'], 
            para['dataName'], para['dataType'], sliceId + 1, density, roundId + 1)
        evallib.dumpresult(outFile, result)
        
    logger.info('density=%.2f, %2d-round done.'%(density, roundId + 1))
    logger.info('----------------------------------------------')








