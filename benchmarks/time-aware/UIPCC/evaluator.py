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
from wsdream import UIPCC
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
    evallib.summarizeResult(para, tensor.shape[2], tag='UPCC_')
    evallib.summarizeResult(para, tensor.shape[2], tag='IPCC_')
    evallib.summarizeResult(para, tensor.shape[2], tag='UIPCC_')


#======================================================#
# Function to run the prediction approach at one setting
#======================================================#
def executeOneSetting(matrix, density, roundId, sliceId, para):
    (numUser, numService) = matrix.shape

    # remove data entries to generate trainMatrix and testMatrix  
    seedID = roundId + sliceId * 100
    (trainMatrix, testMatrix) = evallib.removeEntries(matrix, density, seedID)
    (testVecX, testVecY) = np.where(testMatrix)     
    testVec = testMatrix[testVecX, testVecY]

    # invocation to UPCC
    startTime = time.clock() 
    predictedMatrix1 = UIPCC.UPCC(trainMatrix, para)
    runningTime1 = float(time.clock() - startTime)

    # evaluate the prediction error  
    predVec = predictedMatrix1[testVecX, testVecY]
    evalResult = evallib.errMetric(testVec, predVec, para['metrics'])
    result = (evalResult, runningTime1)

    # dump the result at each density
    tag = 'UPCC_'
    outFile = '%s%s%s_%s_result_%02d_%.2f_round%02d.tmp'%(para['outPath'], 
        tag, para['dataName'], para['dataType'], sliceId + 1, density, roundId + 1)
    evallib.dumpresult(outFile, result)
    logger.info('UPCC done.')

    # invocation to IPCC
    startTime = time.clock() 
    predictedMatrix2 = UIPCC.IPCC(trainMatrix, para)
    runningTime2 = float(time.clock() - startTime)

    # evaluate the prediction error  
    predVec = predictedMatrix2[testVecX, testVecY]
    evalResult = evallib.errMetric(testVec, predVec, para['metrics'])
    result = (evalResult, runningTime2)

    # dump the result at each density
    tag = 'IPCC_'
    outFile = '%s%s%s_%s_result_%02d_%.2f_round%02d.tmp'%(para['outPath'], 
        tag, para['dataName'], para['dataType'], sliceId + 1, density, roundId + 1)
    evallib.dumpresult(outFile, result)
    logger.info('IPCC done.')

    # invocation to UIPCC
    startTime = time.clock() 
    predictedMatrix = UIPCC.UIPCC(trainMatrix, predictedMatrix1, predictedMatrix2, para)
    runningTime = float(time.clock() - startTime) + runningTime1 + runningTime2

    # evaluate the prediction error  
    predVec = predictedMatrix[testVecX, testVecY]
    evalResult = evallib.errMetric(testVec, predVec, para['metrics'])
    result = (evalResult, runningTime)

    # dump the result at each density
    tag = 'UIPCC_'
    outFile = '%s%s%s_%s_result_%02d_%.2f_round%02d.tmp'%(para['outPath'], 
        tag, para['dataName'], para['dataType'], sliceId + 1, density, roundId + 1)
    evallib.dumpresult(outFile, result)
    logger.info('UIPCC done.')

    logger.info('density=%.2f, sliceId=%02d, %2d-round done.'\
        %(density, sliceId + 1, roundId + 1))

