****************************************************************************
** README file 
** Author: Jamie Zhu <jimzhu@GitHub>
** Last updated: 2016/5/3
****************************************************************************

This directory maintains the core implementation of each algorithm using C++,
as well as the corresponding Python wrapper using Cython. 

****************************************************************************
Approaches Implemented
****************************************************************************

Baseline approaches
*******************
* UMEAN
* IMEAN
* Average

Neighbourhood-based approaches
******************************
* UPCC [Zheng et al., ICWS'09]
* IPCC [Zheng et al., ICWS'09]
* UIPCC [Zheng et al., TSC'11]
* ADF [Wu et al., TSMC'13]
* NRCF [Sun et al., TSC'13]

Model-based approaches
**********************
* PMF [Zheng et al., TSC'13]
* NMF [Zhang et al., SRDS'11]
* Biased-MF [Yu et al., SCC'14]
* LN-LFM [Yu et al., SCC'14]

Hybrid approaches
****************-
* CloudPred [Zhang et al., SRDS'11]
* NIMF [Zheng et al., TSC'13]
* EMF [Lo et al., SCC'12]

Location-aware approaches
*************************
* RegionKNN [Chen et al., ICWS'10]
* LACF [Tang et al., ICWS'12]
* LBR [Lo et al., ICWS'12]
* HMF [He et al., ICWS'14]
* LoRec [Chen et al., TPDS'14]

Time-aware approaches
*********************
* TF [Zhang et al., ISSRE'11]
* WSPred [Zhang et al., ISSRE'11]
* CLUS [Silic et al., FSE'13, TSC'15]
* NTF [Zhang et al., WWW'14]

Online approaches
*****************
* AMF [Zhu et al., ICDCS'14]

Ranking-based approaches
************************
* GreedyRank [Zheng et al., SRDS'10]
* CloudRank [Zheng et al., SRDS'10, TPDS'13]

****************************************************************************
Reference and citation
****************************************************************************

Please refer to the following papers for the detailed descriptions of the 
implemented algorithms:

- WS-DREAM: A Package of Open Source-Code and Datasets to Benchmark QoS 
  Prediction Approaches of Web Services. Available at: https://github.com/wsdream.

IF YOU USE THIS PACKAGE IN PUBLISHED RESEARCH, PLEASE CITE THE ABOVE PAPERS. 
THANKS!

****************************************************************************
License
****************************************************************************

The MIT License (MIT)
Copyright (c) 2016, WS-DREAM, CUHK

