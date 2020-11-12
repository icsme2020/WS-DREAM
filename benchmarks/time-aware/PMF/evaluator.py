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
from wsdream import PMF
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
                for sliceId in xrange(tensor.shape[2]):
                    matrix = tensor[:, :, sliceId]
                    pool.apply_async(executeOneSetting, (matrix, den, roundId, sliceId, para))
        pool.close()
        pool.join()
    else: # run on single processes
        for den in para['density']:
            for roundId in xrange(para['rounds']):
                for sliceId in xrange(tensor.shape[2]):
                    matrix = tensor[:, :, sliceId]
                    executeOneSetting(matrix, den, roundId, sliceId, para)
    # summarize the dumped results
    evallib.summarizeResult(para, tensor.shape[2])


#======================================================#
# Function to run the prediction approach at one setting
#======================================================#
def executeOneSetting(matrix, density, roundId, sliceId, para):
    (numUser, numService) = matrix.shape
    dim = para['dimension']

    # remove data entries to generate trainMatrix and testMatrix  
    seedID = roundId + sliceId * 100
    (trainMatrix, testMatrix) = evallib.removeEntries(matrix, density, seedID)
    (testVecX, testVecY) = np.where(testMatrix)     
    testVec = testMatrix[testVecX, testVecY]

    # invocation to the prediction function
    startTime = time.clock() 
    predictedMatrix = PMF.predict(trainMatrix, para)
    runningTime = float(time.clock() - startTime)

    # evaluate the prediction error  
    predVec = predictedMatrix[testVecX, testVecY]
    evalResult = evallib.errMetric(testVec, predVec, para['metrics'])
    result = (evalResult, runningTime)

    # dump the result at each density
    outFile = '%s%s_%s_result_%02d_%.2f_round%02d.tmp'%(para['outPath'], 
        para['dataName'], para['dataType'], sliceId + 1, density, roundId + 1)
    evallib.dumpresult(outFile, result)  
    logger.info('density=%.2f, sliceId=%02d, %2d-round done.'\
        %(density, sliceId + 1, roundId + 1))





