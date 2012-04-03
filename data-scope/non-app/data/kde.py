#!/usr/local/bin/python2.7
# encoding: utf-8

import numpy as NP
from scipy import stats as ST

n = int(1e3)
NP.random.seed(456934)
xn = NP.random.randn(n)
gkde = ST.gaussian_kde(xn)
x = NP.linspace(-7, 7, 101)
kde_pdf = gkde.evaluate(x)
d = NP.column_stack((x, kde_pdf)).tolist()

# bimodal:
n = int(1e5)
NP.random.seed(291803)
alpha = .6
mlo, mhi = (-3, 3)      # position of the 2 peaks
x = NP.linspace(-7, 7, 1000)
xn = NP.concatenate( [mlo + NP.random.randn(alpha * n),
    	mhi + NP.random.randn((1-alpha) * n)] )       	
gkde = ST.gaussian_kde(xn)
kde_pdf = alpha * ST.norm.pdf(x, loc=mlo) + (1-alpha) * ST.norm.pdf(x, loc=mhi)
d = NP.column_stack((x, kde_pdf)).tolist()

