----------------------------------------------------------------------------
README file 
Author: Jamie Zhu <jimzhu@GitHub>
Last updated: 2016/5/3
----------------------------------------------------------------------------

This directory implements popular neighbourhood-based QoS prediction approaches, 
including UPCC, IPCC, UIPCC (a.k.a. WSRec). 

----------------------------------------------------------------------------
Contents of this directory
----------------------------------------------------------------------------

UIPCC/
  - readme.txt       - descriptions of this directory 
  - run_rt.py        - script file for running on response-time QoS data
  - run_tp.py        - script file for running on throughput QoS data
  - evaluator.py     - the main process to control the evaluations 
  - __init__.py      - a file to append necessary system paths
  - result/
    - UPCC_dataset#2_rt_result.txt   - evaluation results on response-time data
    - UPCC_dataset#2_tp_result.txt   - evaluation results on throughput data	
    - IPCC_dataset#2_rt_result.txt   - evaluation results on response-time data
    - IPCC_dataset#2_tp_result.txt   - evaluation results on throughput data  
    - UIPCC_dataset#2_rt_result.txt  - evaluation results on response-time data
    - UIPCC_dataset#2_tp_result.txt  - evaluation results on throughput data 

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

- Zibin Zheng, Hao Ma, Michael R. Lyu, and Irwin King, "QoS-Aware Web Service 
  Recommendation by Collaborative Filtering", IEEE Transactions on Service 
  Computing, vol.4, no.2, pp.140-152, 2011.

IF YOU USE THIS PACKAGE IN PUBLISHED RESEARCH, PLEASE CITE THE ABOVE PAPERS. 
THANKS!

----------------------------------------------------------------------------
License
----------------------------------------------------------------------------

The MIT License (MIT)
Copyright (c) 2016, WS-DREAM, CUHK

