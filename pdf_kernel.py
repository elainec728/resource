# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from scipy import stats
from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np
import random
from sklearn.neighbors.kde import KernelDensity

random.seed()
a=[]
n=10000
for i in range(n):
    a.append(random.gammavariate(3,5))
    #a.append(random.gauss(0,1))

n1=15
n2=100

plt.figure(1) 
#histogram 
plt.subplot(221)
hist1, bin1=np.histogram(a,bins=n1)
plt.hist(a,bins=n1)
plt.subplot(222)
#line graph with left boarder and count
plt.plot(bin1[:-1],hist1)

plt.figure(2) 
#histogram 
plt.subplot(221)
hist2, bin2=np.histogram(a,bins=n2)
plt.hist(a,bins=n2)
plt.subplot(222)
#line graph with left boarder and count
x1=bin1[:-1]
x2=bin2[:-1]
plt.plot(x2,hist2)

plt.figure(3) 
#PDF  
y=norm.pdf(a)
plt.plot(a,norm.pdf(a),'.')

plt.figure(4) 
plt.subplot(221)
#kernel function with left boarder from histo
kd=stats.gaussian_kde(a)
plt.plot(x1,kd.evaluate(x1))
#compare discrete
y1=kd.evaluate(x1)
plt.plot(x1,y1,'.')

plt.subplot(222)
plt.plot(x2,kd.evaluate(x2))
#compare discrete
y2=kd.evaluate(x2)
plt.plot(x2,y2,'.')

#kernel function with set intervel
plt.figure(5) 
interval1=np.linspace(min(a),max(a),n1)
interval2=np.linspace(min(a),max(a),n2)

plt.subplot(221)
plt.plot(interval1,kd.evaluate(interval1))
plt.subplot(222)
plt.plot(interval2,kd.evaluate(interval2))