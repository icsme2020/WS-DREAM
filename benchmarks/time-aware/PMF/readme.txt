----------------------------------------------------------------------------
README file 
Author: Jamie Zhu <jimzhu@GitHub>
Last updated: 2016/5/3
----------------------------------------------------------------------------

This directory implements a QoS prediction approach, probabilistic matrix 
factorization (PMF), which has been published in the existing work [Zheng et 
al., TSC'13].

----------------------------------------------------------------------------
Contents of this directory
----------------------------------------------------------------------------

PMF/
  - readme.txt       - descriptions of this directory 
  - run_rt.py        - script file for running on response-time QoS data
  - run_tp.py        - script file for running on throughput QoS data
  - evaluator.py     - the main process to control the evaluations 
  - __init__.py      - a file to append necessary system paths
  - result/
    - dataset#2_rt_result.txt  - evaluation results on response-time QoS data
    - dataset#2_tp_result.txt  - evaluation results on throughput QoS data

Note that the experimental results are provided with the metrics (MAE, NMAE, 
RMSE, MRE, NPRE). Each experiment is run for 20 times and the average result 
(including std value) is reported. 

----------------------------------------------------------------------------
Reference and citation
----------------------------------------------------------------------------

Please refer to the following papers for the detailed descriptions of the 
implemented algorithms:

- WS-DREAM: A Package of Open Source-Code and Datasets to Benchmark QoS 
  Prediction Approaches of Web Services. Available at: https://github.com/wsdream.

- Zibin Zheng, Hao Ma, M.R. Lyu, and Irwin King, "Collaborative Web Service 
  QoS Prediction via Neighbourhood Integrated Matrix Factorization," IEEE 
  Transactions on Service Computing (TSC), vol. 6, no. 3, 2013, pp. 289-299. 
 
- R. Salakhutdinov and A. Mnih, "Probabilistic Matrix Factorization," in Proc. 
  of Advances in Neural Information Processing Systems (NIPS'07), pp. 1257-1264, 
  2007.

IF YOU USE THIS PACKAGE IN PUBLISHED RESEARCH, PLEASE CITE THE ABOVE PAPERS. 
THANKS!

----------------------------------------------------------------------------
License
----------------------------------------------------------------------------

The MIT License (MIT)
Copyright (c) 2016, WS-DREAM, CUHK

