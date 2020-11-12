########################################################
# Description: the main process to control the evaluations 
# Author: Jamie Zhu <jimzhu@GitHub>
# License: MIT
# Last updated: 2016/05/04
########################################################

import numpy as np
import time
from commons.utils import logger # import from ../../commons
from commons import evallib # import from ../../commons
from wsdream import NIMF
from scipy import stats
import multiprocessing


#======================================================#
# Function to evalute the approach at all settings
#======================================================#
def execute(matrix, para):
    # loop over each density and each round
    if para['parallelMode']: # run on multiple processes
        pool = multiprocessing.Pool()
        for den in para['density']: 
            for roundId in xrange(para['rounds']):
                pool.apply_async(executeOneSetting, (matrix, den, roundId, para))
        pool.close()
        pool.join()
    else: # run on single processes
        for den in para['density']:
            for roundId in xrange(para['rounds']):
                executeOneSetting(matrix, den, roundId, para)
    # summarize the dumped results
    evallib.summarizeResult(para)


#======================================================#
# Function to run the prediction approach at one setting
#======================================================#
def executeOneSetting(matrix, density, roundId, para):
    logger.info('density=%.2f, %2d-round starts.'%(density, roundId + 1))
    
    # remove data matrix    
    (trainMatrix, testMatrix) = evallib.removeEntries(matrix, density, roundId) 

    # QoS prediction
    startTime = time.clock() # to record the running time for one round             
    predictedMatrix = NIMF.predict(trainMatrix, para) 
    runningTime = float(time.clock() - startTime)

    # evaluate the estimation error  
    evalResult = evallib.evaluate(testMatrix, predictedMatrix, para)
    result = (evalResult, runningTime)

    # dump the result at each density
    outFile = '%s%s_%s_result_%.2f_round%02d.tmp'%(para['outPath'], para['dataName'], 
        para['dataType'], density, roundId + 1)
    evallib.dumpresult(outFile, result)
    
    logger.info('density=%.2f, %2d-round done.'%(density, roundId + 1))
    logger.info('----------------------------------------------')

