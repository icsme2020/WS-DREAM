##WS-DREAM

WS-DREAM is a package of open source-code and datasets to benchmark QoS-driven services research, especially on Web service recommendation.

With both datasets and source code publicly released, WS-DREAM repository would allow ease of reproducing the existing approaches, and potentially inspires more research efforts in this area. Specifically, for future research on QoS prediction of Web services, you do not need to write your own program from scratch. The WS-DREAM framework can be easily extended to new implementations. This is exactly the goal of maintaining this repository.


## Publications About WS-DREAM

1. Zibin Zheng, Yilei Zhang, Michael R. Lyu, "[Investigating QoS of Real-World Web Services](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=6357180)," *IEEE Trans. Services Computing (TSC)*, 2014.

1. Jieming Zhu, Pinjia He, Zibin Zheng, Michael R. Lyu, "[Towards Online, Accurate, and Scalable QoS Prediction for Runtime Service Adaptation](http://jiemingzhu.github.io/pub/jmzhu_icdcs2014.pdf)," in *Proc. of IEEE International Conference on Distributed Computing Systems (ICDCS)*, 2014.

1. Zibin Zheng, Michael R. Lyu, "[Collaborative Reliability Prediction of Service-Oriented Systems](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=6062071)," in *Proc. of ACM/IEEE International Conference on Software Engineering (ICSE)*, 2010. [**ACM SIGSOFT Distinguished Paper Award**]

1. Zibin Zheng, Yilei Zhang, Michael R. Lyu, "[Distributed QoS Evaluation for Real-World Web Services](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=5552800)," in *Proc. of IEEE International Conference on Web Services (ICWS)*, 2010. [**Best Student Paper Award**]

1. Zibin Zheng, Hao Ma, Michael R. Lyu, Irwin King, "[WSRec: A Collaborative Filtering based Web Service Recommender System](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=5175854)," in *Proc. of IEEE International Conference on Web Services (ICWS)*, 2009.

1. Zibin Zheng, Michael R. Lyu, "[WS-DREAM: A distributed Reliability Assessment Mechanism for Web Services](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=4630108)," in *Proc. of IEEE/IFIP International Conference on Dependable Systems and Networks (DSN)*, 2008.

##Related Links
- A list of papers that use or cite WS-DREAM: [http://wsdream.github.io/bibliography](https://github.com/wsdream/wsdream-docs/blob/master/biblist.rst)

- WS-DREAM open-source code: [http://wsdream.github.io/code](https://github.com/wsdream/WS-DREAM)

- WS-DREAM open datasets: [http://wsdream.github.io/dataset](https://github.com/wsdream/wsdream-dataset)

##Code Archive

####Baseline approaches
- UMEAN: [benchmarks/baseline/UMEAN]
- IMEAN: [benchmarks/baseline/UMEAN]

####Neighbourhood-based approaches
- [UIPCC](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=5674010 "Zheng et al., TSC'2011"): [[benchmarks/neighbourhood-based/UIPCC](https://github.com/wsdream/WS-DREAM/tree/76b35a6a21c5d209a1897c4719a5e32a3e79c782/UIPCC)]
- [ADF](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=6301755 "Wu et al., TSMC'2013"): [[benchmarks/neighbourhood-based/ADF](https://github.com/wsdream/WS-DREAM/tree/76b35a6a21c5d209a1897c4719a5e32a3e79c782/ADF)]
- [NRCF](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=6338940&tag=1 "Sun et al., TSC'2013"): [[benchmarks/neighbourhood-based/NRCF](https://github.com/wsdream/WS-DREAM/tree/76b35a6a21c5d209a1897c4719a5e32a3e79c782/NRCF)]

####Model-based approaches
- [PMF](http://dl.acm.org/citation.cfm?id=2430548 "Zheng et al., TOSEM'2013") \(a.k.a. Regularized SVD): [[benchmarks/model-based/PMF](https://github.com/wsdream/WS-DREAM/tree/master/benchmarks/model-based/PMF)]
- [NMF](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=6076756 "Zhang et al., SRDS'2011"): [[benchmarks/model-based/NMF](https://github.com/wsdream/WS-DREAM/tree/master/benchmarks/model-based/NMF)]
- [BiasedMF](http://ieeexplore.ieee.org/xpl/articleDetails.jsp?arnumber=6930523 "Yu et al., SCC'2014"): [[benchmarks/model-based/BiasedMF](https://github.com/wsdream/WS-DREAM/tree/master/benchmarks/model-based/BiasedMF)]
- [LN-LFM](http://ieeexplore.ieee.org/xpl/articleDetails.jsp?arnumber=6930523 "Yu et al., SCC'2014"): [[benchmarks/model-based/LN_LFM](https://github.com/wsdream/WS-DREAM/tree/master/benchmarks/model-based/LN_LFM)]

####Hybrid approaches  
- [CloudPred](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=6076756 "Zhang et al., SRDS'2011"): [[benchmarks/hybrid/CloudPred](https://github.com/wsdream/WS-DREAM/tree/76b35a6a21c5d209a1897c4719a5e32a3e79c782/CloudPred)]
- [EMF](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=6274140 "Lo et al., SCC'2012"): [[benchmarks/hybrid/EMF](https://github.com/wsdream/WS-DREAM/tree/master/benchmarks/hybrid/EMF)]
- [NIMF](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=6122009 "Zheng et al., TSC'2013"): [[benchmarks/hybrid/NIMF](https://github.com/wsdream/WS-DREAM/tree/master/benchmarks/hybrid/NIMF)]

####Location-aware approaches
- [RegionKNN](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=5552807 "Chen et al., ICWS'2010"): [[benchmarks/location-aware/RegionKNN](https://github.com/wsdream/WS-DREAM/tree/76b35a6a21c5d209a1897c4719a5e32a3e79c782/Location-aware/RegionKNN)]
- [LACF](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=6257808 "Tang et al., ICWS'2012"): [[benchmarks/location-aware/LACF](https://github.com/wsdream/WS-DREAM/tree/76b35a6a21c5d209a1897c4719a5e32a3e79c782/Location-aware/LACF)]
- [LBR](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=6257841 "Lo et al., ICWS'2012"): [[benchmarks/location-aware/LBR](https://github.com/wsdream/WS-DREAM/tree/76b35a6a21c5d209a1897c4719a5e32a3e79c782/Location-aware/LBR)]
- [HMF](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=6928911 "He et al., ICWS'2014"): [[benchmarks/location-aware/HMF](https://github.com/wsdream/WS-DREAM/tree/76b35a6a21c5d209a1897c4719a5e32a3e79c782/Location-aware/HMF)]
- [LoRec](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=6684151 "Chen et al., TPDS'2014"): [[benchmarks/location-aware/LoRec](https://github.com/wsdream/WS-DREAM/tree/76b35a6a21c5d209a1897c4719a5e32a3e79c782/Location-aware/LoRec)]

####Time-aware approaches
- Average: [[benchmarks/time-aware/Baseline](https://github.com/wsdream/WS-DREAM/tree/master/benchmarks/time-aware/Baseline)]
- [UIPCC](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=5674010 "Zheng et al., TSC'2011"): [[benchmarks/time-aware/UIPCC](https://github.com/wsdream/WS-DREAM/tree/master/benchmarks/time-aware/UIPCC)]
- [PMF](http://dl.acm.org/citation.cfm?id=2430548 "Zheng et al., TOSEM'2013"): [[benchmarks/time-aware/PMF](https://github.com/wsdream/WS-DREAM/tree/master/benchmarks/time-aware/PMF)]
- [TF](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=6132969&tag=1 "Zhang et al., ISSRE'2011"): [[benchmarks/time-aware/TF](https://github.com/wsdream/WS-DREAM/tree/76b35a6a21c5d209a1897c4719a5e32a3e79c782/Time-aware/TF)] 
- [WSPred](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=6132969&tag=1 "Zhang et al., ISSRE'2011"): [[benchmarks/time-aware/WSPred](https://github.com/wsdream/WS-DREAM/tree/76b35a6a21c5d209a1897c4719a5e32a3e79c782/Time-aware/WSPred)]  
- [CLUS](http://ieeexplore.ieee.org/xpl/articleDetails.jsp?arnumber=6874541 "Silic et al., FSE'2013"): [[benchmarks/time-aware/CLUS](https://github.com/wsdream/WS-DREAM/tree/76b35a6a21c5d209a1897c4719a5e32a3e79c782/Time-aware/CLUS)]
- [NTF](http://dl.acm.org/citation.cfm?id=2568001 "Zhang et al., WWW'2014"): [[benchmarks/time-aware/NTF](https://github.com/wsdream/WS-DREAM/tree/76b35a6a21c5d209a1897c4719a5e32a3e79c782/Time-aware/NTF)]
- [TD-WSRec](http://ieeexplore.ieee.org/xpl/articleDetails.jsp?arnumber=6928878 "Hu et al., ICWS'14"): [benchmarks/time-aware/TD_WSRec] 
  
####Online prediction approaches
- [AMF](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=6888908&tag=1 "Zhu et al., ICDCS'2014"): [[benchmarks/online/AMF](https://github.com/wsdream/AMF)] 
- [OPred](http://ieeexplore.ieee.org/xpl/articleDetails.jsp?arnumber=6720144 "Zhang et al., TSMC'2014"): [benchmarks/online/OPred]

####Ranking-based approaches
- [GreedyRank](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=5623393 "Zheng et al., SRDS'2010"): [[benchmarks/ranking-based/GreedyRank](https://github.com/wsdream/WS-DREAM/tree/76b35a6a21c5d209a1897c4719a5e32a3e79c782/Ranking-based/GreedyRank)]  
- [CloudRank](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=6320550 "Zheng et al., TPDS'2013"): [[benchmarks/ranking-based/CloudRank](https://github.com/wsdream/WS-DREAM/tree/76b35a6a21c5d209a1897c4719a5e32a3e79c782/Ranking-based/CloudRank)] 


##Dependencies
- Python 2.7 (https://www.python.org)
- Cython 0.20.1 (http://cython.org)
- numpy 1.8.1 (http://www.scipy.org)
- scipy 0.13.3 (http://www.scipy.org)
- AMF (https://github.com/wsdream/AMF)
- PPCF (https://github.com/wsdream/PPCF)

##Usage

The algorithms in WS-DREAM are mostly implemented in C++ and further wrapped up as a python package for common use.

1. Install `wsdream` package
    
  Download the repo at: https://github.com/wsdream/WS-DREAM/tarball/master,
  
  then install the package `python setup.py install --user`. 

2. Change directory `cd` to `"benchmarks/"`, and configure the parameters in benchmark scripts
  
  For example, in `run_rt.py`, you can config the `'parallelMode': True` if you are running a multi-core machine. You can also set `'rounds': 1` for testing, which can make the execution finish soon.

3. Read `"readme.txt"` for each appraoch, and execute the provided benchmark scripts 
    
	```
    $ python run_rt.py
    $ python run_tp.py 
    ```
4. Check the evaluation results in `"result/"` directory. Note that the repository has maintained the results evaluated on [WS-DREAM datasets](https://github.com/wsdream/dataset), which are ready for immediate use.


## Citation
IF YOU USE THIS PACKAGE IN ANY PUBLISHED RESEARCH, PLEASE KINDLY CITE THE FOLLOWING PAPER:
- WS-DREAM: A Package of Open Source-Code and Datasets to Benchmark QoS Prediction Approaches of Web Services. Available at: https://github.com/wsdream.


## Contributors
Great thanks to WS-DREAM contributors:
- [Jieming Zhu](http://jiemingzhu.github.io/), Postdoc Fellow, The Chinese University of Hong Kong, Hong Kong (Coordinator)
- [Zibin Zheng](http://www.zibinzheng.com/), Associate Professor, Sun Yat-sen University, China (for UIPCC)
- Pinjia He, PhD Student, The Chinese University of Hong Kong, Hong Kong (for HMF)
- [Yuwen Xiong](https://github.com/Orpine), Visiting Student from Zhejiang University, China (for TF, NTF, WSPred, OPred, BiasedMF, SVD++)
- Yifei Lu, Visiting Student from Zhejiang University, China (for ADF, T-WSRec)


##Feedback
For bugs and feedback, please post to [our issue page](https://github.com/wsdream/WS-DREAM/issues). For any other enquires, please drop an email to our team (wsdream.maillist@gmail.com).

##License
[The MIT License (MIT)](./LICENSE)

Copyright &copy; 2016, [WS-DREAM](https://wsdream.github.io), CUHK