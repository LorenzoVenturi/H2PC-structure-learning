# H2PC-structure-learning
H2PC bayesian network structure learning implementation on Python with PyAgrum and Pgmpy tests.

This mini-project aims to implement and test the H2PC algorithm, a method for structure learning in the context of Bayesian Network. The algorithm is compared to the state-of-the-art Max-Min-Hill-Climbing.
The implementation is done with Python and the PyAgrum library.
The visual representation of the networks and tests are generated with PGMPY and Graphviz libraries. The results show that H2PC is able to build a more accurate Bayesian Network structure compared to the rival; in particular this implementation shows an extremely low false-positive edge ratio and good performance even with a small fraction of the dataset available, the time complexity shows (not accordingly to the original paper) a faster H2PC performances than MMHC.
