########################################################
# Description: throughput prediction  
# Implemented approach: Biased Matrix Factorization
# Author: Jamie Zhu <jimzhu@GitHub>
# License: MIT
# Last updated: 2016/05/04
########################################################

import __init__
import os, sys, time
import numpy as np
from commons.utils import logger 
from commons import utils
from commons import dataloader
import evaluator


import __init__
import os, sys, time
import numpy as np
from commons.utils import logger 
from commons import utils
from commons import dataloader
import evaluator
 
# parameter config area
para = {'dataPath': '../../../data/',
		'dataName': 'dataset#1',
		'dataType': 'tp', # set the dataType as 'rt' or 'tp'
		'outPath': 'result/',
		'metrics': ['MAE', 'NMAE', 'RMSE', 'MRE', 'NPRE'], # delete where appropriate
		'density': np.arange(0.05, 0.31, 0.05), # matrix density
		'rounds': 20, # how many runs are performed at each matrix density
		'dimension': 10, # dimenisionality of the latent factors
		'etaInit': 0.001, # inital learning rate. We use line search
						 # to find the best eta at each iteration
		'lambda': 500, # regularization parameter
		'maxIter': 300, # the max iterations
		'saveTimeInfo': False, # whether to keep track of the running time
		'saveLog': True, # whether to save log into file
		'debugMode': False, # whether to record the debug info
        'parallelMode': True # whether to leverage multiprocessing for speedup
		}


startTime = time.time() # start timing
utils.setConfig(para) # set configuration
logger.info('==============================================')
logger.info('BiasedMF: Biased Matrix Factorization')

# load the dataset
dataMatrix = dataloader.load(para)

# evaluate QoS prediction algorithm
evaluator.execute(dataMatrix, para)

logger.info('All done. Elaspsed time: ' + utils.formatElapsedTime(time.time() - startTime)) # end timing
logger.info('==============================================')

