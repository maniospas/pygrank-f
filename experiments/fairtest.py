import pygrankf as pgf
import tensorflow as tf


with tf.device('cpu'):
    for coefficients in [pgf.PageRank(0.85), pgf.PageRank(0.9), pgf.HeatKernels(1), pgf.HeatKernels(3)]:
        algorithms = pgf.experiments("experiments/algorithms/fairsym.yaml", coefficients=coefficients)
        pgf.benchmark("experiments/fairness/diffusion.yaml", algorithms,
                      update=True, delim="&", endl="\\\\\n", total=True)

