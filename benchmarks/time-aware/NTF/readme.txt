----------------------------------------------------------------------------
README file 
Author: Jamie Zhu <jimzhu@GitHub>
Last updated: 2016/5/3
----------------------------------------------------------------------------

This directory implements a time-aware QoS prediction approach, Non-negative 
Tensor Factorization (NTF), which has been proposed in the existing work 
[Zhang et al., WWW'14].

----------------------------------------------------------------------------
Contents of this directory
----------------------------------------------------------------------------

NTF/
  - readme.txt       - descriptions of this directory 
  - run_rt.py        - script file for running on response-time QoS data
  - run_tp.py        - script file for running on throughput QoS data
  - evaluator.py     - the main process to control the evaluations 
  - __init__.py      - a file to append necessary system paths
  - result/                     - directory for storing evaluation results
    - dataset#2_rt_result.txt   - evaluation results on response-time QoS data
    - dataset#2_tp_result.txt   - evaluation results on throughput QoS data

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

- Wancai Zhang, Hailong Sun, Xudong Liu and Xiaohui Guo, "Temporal QoS-Aware 
  Web Service Recommendation via Non-negative Tensor Factorization," in Proc.
  of the 23rd International World Wide Web Conference (WWW), 2014, pp.585-596.

IF YOU USE THIS PACKAGE IN PUBLISHED RESEARCH, PLEASE CITE THE ABOVE PAPERS. 
THANKS!

----------------------------------------------------------------------------
License
----------------------------------------------------------------------------

The MIT License (MIT)
Copyright (c) 2016, WS-DREAM, CUHK



