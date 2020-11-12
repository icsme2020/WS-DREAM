########################################################
# dataloader.py
# Author: Jamie Zhu <jimzhu@GitHub>
# Created: 2014/2/6
# Last updated: 2015/8/29
########################################################

import numpy as np 
from commons.utils import logger
import os

#======================================================#
# Function to load the dataset
#======================================================#
def load(para):
    if para['dataName'] == 'dataset#1':
        datafile = para['dataPath'] + para['dataName'] + '/' + para['dataType'] + 'Matrix.txt'
        logger.info('Loading data: %s'%os.path.abspath(datafile))
        dataMatrix = np.loadtxt(datafile)
        logger.info('Data size: %d users * %d services'\
            %(dataMatrix.shape[0], dataMatrix.shape[1]))
    elif para['dataName'] == 'dataset#2':
        datafile = para['dataPath'] + para['dataName'] + '/' + para['dataType'] + 'data.txt'
        logger.info('Loading data: %s'%os.path.abspath(datafile))
        dataMatrix = -1 * np.ones((142, 4500, 64))
        fid = open(datafile, 'r')
        for line in fid:
            data = line.split(' ')
            rt = float(data[3])
            if rt > 0:
                dataMatrix[int(data[0]), int(data[1]), int(data[2])] = rt
        fid.close()
        logger.info('Data size: %d users * %d services * %d timeslices'\
            %(dataMatrix.shape[0], dataMatrix.shape[1], dataMatrix.shape[2]))      
        dataMatrix = preprocess(dataMatrix, para)
    logger.info('Loading data done.')
    logger.info('----------------------------------------------') 
    return dataMatrix


#======================================================#
# Function to preprocess the dataset which
# deletes the invalid values
#======================================================#
def preprocess(matrix, para):
    if para['dataType'] == 'rt':
        matrix = np.where(matrix == 0, -1, matrix)
        matrix = np.where(matrix >= 19.9, -1, matrix)
    elif para['dataType'] == 'tp':
        matrix = np.where(matrix == 0, -1, matrix)
    return matrix


#======================================================#
# Function to load the service provider and country information
#======================================================#
def loadServInfo(para):
    wsLocFile = para['dataPath'] + para['dataName'] + '/' + 'wslist.txt'
    data = np.genfromtxt(wsLocFile, dtype=np.str, comments='$', 
        delimiter='\t', skip_header=2)
    wsProvider = data[:, 2]
    wsCountry = data[:, 4]
    providerSet = set(wsProvider)
    countrySet = set(wsCountry)
    providerDict = {}
    countryDict = {}
    cnt = 0
    for provider in providerSet:
        providerDict[provider] = cnt
        cnt += 1
    cnt = 0
    for country in countrySet:
        countryDict[country] = cnt
        cnt += 1
        
    wsInfoList = np.zeros((data.shape[0], 2))
    for i in xrange(data.shape[0]):
        wsInfoList[i, :] = [providerDict[wsProvider[i]], countryDict[wsCountry[i]]]
    return wsInfoList

