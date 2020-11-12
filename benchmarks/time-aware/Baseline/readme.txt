****************************************************************************
* README file 
* Author: Jamie Zhu <jimzhu@GitHub>
* Last updated: 2016/05/3      
****************************************************************************

This directory maintains the testing code used to benchmark a baseline QoS
prediction approach.

****************************************************************************
Contents of this directory
****************************************************************************

Baseline/
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

****************************************************************************
Reference and citation
****************************************************************************

Please refer to the following paper for the detailed description of the 
implemented algorithm:

- WS-DREAM: A Package of Open Source-Code and Datasets to Benchmark QoS 
  Prediction Approaches of Web Services. Available at: https://github.com/wsdream.

- Jieming Zhu, Pinjia He, Zibin Zheng, and Michael R. Lyu, "Online QoS 
  Prediction for Runtime Service Adaptation via Adaptive Matrix Factorization," 
  in submission. 

IF YOU USE THIS PACKAGE IN PUBLISHED RESEARCH, PLEASE CITE THE ABOVE PAPER. 
THANKS!

****************************************************************************
License
****************************************************************************

The MIT License (MIT)
Copyright (c) 2016, WS-DREAM, CUHK


