# 🧠 Developing H2PC for Bayesian Network Structure Learning: A Comparative Study

**Author**: Lorenzo Venturi  
**Program**: Master’s Degree in Artificial Intelligence, University of Bologna  
**Course**: Fundamentals of AI Module 3, focus on probabilistic reasoning and Bayesian Networks
📅 **Date**: April 1, 2025  
📧 **Contact**: lorenzo.venturi14@studio.unibo.it 

---

## 📄 Abstract

This project presents the Python implementation and evaluation of the **H2PC algorithm**, a hybrid approach for structure learning in **Bayesian Networks (BNs)**. It is compared against the well-known **Max-Min Hill-Climbing (MMHC)** algorithm. Tests are conducted using real benchmark datasets with varying complexity. Results highlight H2PC's superior accuracy and scalability, unexpectedly also in minimizing false positives and maintaining performance with limited data, unlike the original paper ( https://www.sciencedirect.com/science/article/abs/pii/S0957417414002553 )main problem of being really slow, the algorithm seems to be faster than Pgmpy's implementatio of MMHC and obtain lower false positive edges.

---

## 📌 Goals

- ✅ Implement the H2PC algorithm in Python using the **PyAgrum** library.
- 🔍 Compare H2PC to **MMHC** across datasets of increasing complexity.
- 📊 Evaluate using key metrics: SHD, Precision, Recall, False Positive Edge Ratio, BIC Score, and Execution Time.
- 🎯 Visualize the learned Bayesian Networks and their differences from the true Network.

---

## 🛠️ Libraries

- [PyAgrum](https://pyagrum.readthedocs.io/) – For BN learning and independence testing
  (the idea of using pyagrum comes partially from this other implementation https://github.com/bastienchassagnol/algo_H2PC)
- [PGMPY](https://pgmpy.org/) – For visualization and comparison with MMHC
- [Graphviz](https://graphviz.org/) – For DAG visualizations

---

## 🧪 Methodology

The project follows a three-step structure:

1. **Implementation**:
   - Build the **HPC** subroutines: DE PCS, DE SPS, and FDR-IAPC.
   - Complete the H2PC algorithm by combining constraint-based and score-based strategies.

2. **Testing**:
   - Use three datasets from the [bnlearn repository](https://www.bnlearn.com/bnrepository/): Asia, Sachs, and Alarm.
   - Compare H2PC vs MMHC at different dataset sizes.

3. **Evaluation**:
   - Key metrics: **False Positive Edge Ratio**, **Precision**, **Recall**, **SHD**, **BIC**, and **Execution Time**.
   - Analysis includes both the undirected skeleton and the full DAG.

---

## 📈 Results Summary

- **Asia Dataset**: H2PC consistently achieved lower SHD and better precision/recall.
- **Sachs Dataset**: H2PC significantly outperformed MMHC in all metrics, especially with smaller data.
- **Alarm Dataset**: MMHC was infeasible due to high complexity; H2PC succeeded with strong structural accuracy.

> 🔬 Overall, this implementation of **H2PC shows robustness, scalability**, **low false positive edges rates** and fast computation unlike in the original paper.

---

## 📂 Dataset Details

| Dataset | Nodes | Arcs |
|---------|-------|------|
| Asia    | 8     | 8    |
| Sachs   | 11    | 17   |
| Alarm   | 37    | 46   |

All datasets are publicly available at: [https://www.bnlearn.com/bnrepository](https://www.bnlearn.com/bnrepository)

---

## 🧾 Key Concepts

- **Markov Blanket**: A set of variables that renders a target node conditionally independent from all others.
- **HPC Algorithm**: Builds a skeleton using DE PCS, DE SPS, and FDR-IAPC.
- **Tabu Hill-Climbing**: Used for orienting edges post skeleton discovery.

---

## 📌 References

- Gasse, Aussem, and Elghazel. *A hybrid algorithm for Bayesian network structure learning*, 2014.  
- Peña, J.M. *Learning Gaussian graphical models with FDR control*, 2008.  
- Tsamardinos, Brown, and Aliferis. *The Max-Min Hill-Climbing Algorithm*, 2006.

---

## ✅ Conclusion

> “H2PC proved to be a **reliable and scalable** method for structure learning in Bayesian Networks, unlike in the orginal paper, especially effective in **limiting false positives** and much faster than MMHC pgmpy's implementation.”
