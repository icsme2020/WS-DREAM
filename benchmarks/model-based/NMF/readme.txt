----------------------------------------------------------------------------
README file 
Author: Jamie Zhu <jimzhu@GitHub>
Last updated: 2016/5/3
----------------------------------------------------------------------------

This directory implements a QoS prediction approach, non-negative matrix 
factorization (NMF), which has been employed as a baseline approach 
for comparison in the existing work [Zhang et al., SRDS'11].

----------------------------------------------------------------------------
Contents of this directory
----------------------------------------------------------------------------

NMF/
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

- Yilei Zhang, Zibin Zheng, and Michael R. Lyu, "Exploring Latent Features 
  for Memory-Based QoS Prediction in Cloud Computing," in Proc. of the 30th 
  IEEE Symposium on Reliable Distributed Systems (SRDS'11), 2011, pp. 1-10.  
 
- Daniel D. Lee, H. Sebastian Seung, "Algorithms for Non-negative Matrix 
  Factorization," in Proc. Advances in Neural Information Processing Systems 
  (NIPS'00), 2000, pp. 556-562.

IF YOU USE THIS PACKAGE IN PUBLISHED RESEARCH, PLEASE CITE THE ABOVE PAPERS. 
THANKS!

----------------------------------------------------------------------------
License
----------------------------------------------------------------------------

The MIT License (MIT)
Copyright (c) 2016, WS-DREAM, CUHK

