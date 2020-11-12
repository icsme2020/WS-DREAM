----------------------------------------------------------------------------
README file 
Author: Jamie Zhu <jimzhu@GitHub>
Last updated: 2016/5/5
----------------------------------------------------------------------------

This package implements a recent QoS prediction approach, Latent Factor and 
Latent Neighbor Model (LN-LFM), proposed in the existing work [Yu et al., 
SCC'14].

----------------------------------------------------------------------------
Contents of this directory
----------------------------------------------------------------------------

LN_LFM/
  - readme.txt       - descriptions of this directory 
  - run_rt.py        - script file for running on response-time QoS data
  - run_tp.py        - script file for running on throughput QoS data
  - evaluator.py     - the main process to control the evaluations 
  - __init__.py      - a file to append necessary system paths
  - result/          - results on WS-DREAM dataset#1
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

- Dongjin Yu, Yu Liu, Yueshen Xu, and Yuyu Yin, "Personalized QoS Prediction 
  for Web Services Using Latent Factor Models," in Proc. of IEEE International 
  Conference on Services Computing (SCC), 2014, pp. 107-114. 

IF YOU USE THIS PACKAGE IN PUBLISHED RESEARCH, PLEASE CITE THE ABOVE PAPERS. 
THANKS!

----------------------------------------------------------------------------
License
----------------------------------------------------------------------------

The MIT License (MIT)
Copyright (c) 2016, WS-DREAM, CUHK
