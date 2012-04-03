#!/usr/local/bin/python2.7
# encoding: utf-8     

import numpy as NP
from scipy import stats as ST     

n = int(1e5)
NP.random.seed(456934)
xn = NP.random.randn(n)
gkde = ST.gaussian_kde(xn)
x = NP.linspace(-2, 2, 500)
kde_pdf = gkde.evaluate(x)
d = NP.column_stack((x, kde_pdf)).tolist()           

#------------ bimodal -------------#
alpha = .6
mlo, mhi = (-3, 3)
xn = NP.concatenate( [mlo + NP.random.randn(alpha * n),
        mhi + NP.random.randn((1 - alpha) * n)] )
