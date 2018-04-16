# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 02:12:00 2017

@author: wc57661
"""

import numpy as np
import matplotlib.pyplot as plt
from itertools import cycle
#from mpl_toolkits.mplot3d import Axes3D
#from sklearn.base import BaseEstimator, ClusterMixin
#from sklearn.neighbors import NearestNeighbors
from sklearn.cluster import MeanShift, estimate_bandwidth

#1 D input// java validation
org=np.array([8.716539012678787 , 3.021229416797309 , 5.853854357941585 , 2.2676789929758536 , 5.041662672103989 , 8.10802982282901 , 3.5149402292247114 , 7.703738991136596 , 1.13273376231085 , 3.10323948159803 , 9.73865342245891 , 8.79585875229411 , 6.742328025776208 , 8.101719005268814 , 4.312382098008126 , 4.733431094338297 , 9.61698062372377 , 4.096949153066291 , 2.6445669133457694 , 7.275832043575164 , 5.524340378472239 , 7.787434415515486 , 5.760664705907873 , 6.43641976028767 , 8.043484105456443 , 8.19875741143481 , 5.021576709089063 , 7.529503789302713 , 7.678842076068609 , 3.7347261140560915 , 6.365716891058644 , 6.7196025790100675 , 1.5662008212657417 , 4.111863630988441 , 5.662031667504406 , 6.256242336706739 , 8.153503259490416 , 4.128566516047884 , 8.453663546443403 , 7.7777568409033115 , 9.759674335889445 , 1.3735744942665642 , 3.9705884082661 , 1.4239804829951157 , 2.8414593721058528 , 9.78797121246863 , 3.7944318069548544 , 2.0104318295758574 , 7.131270269517667 , 3.4607450963436497       ])
X=org.reshape(-1,1)
rand=np.random.uniform(-0.2,0.2,len(X))
rand=rand.reshape(-1,1)
#X=np.array(list(zip(org,rand[0])))

bandwidth = estimate_bandwidth(X, quantile=0.3)
ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
ms.fit(X)
labels = ms.labels_
cluster_centers = ms.cluster_centers_

labels_unique = np.unique(labels)
n_clusters_ = len(labels_unique)
print("Mean Shift :")
print("bandwidth:", bandwidth)
print("#estimated clusters :", n_clusters_)
print("estimated clusters centers:\n", cluster_centers)

#plot
colors = cycle('grcmykb')
cluster_count=[]
#fig=plt.figure(1,figsize=(12, 12))
fig, ax = plt.subplots(figsize=(12,5))
for k, col in zip(range(n_clusters_), colors):
    my_members = labels == k
    cluster_count.append(sum(my_members))
    cluster_center = cluster_centers[k]
    cluster_min=min(X[my_members, 0])
    cluster_max=max(X[my_members, 0])
    ax.scatter(X[my_members, 0], rand[my_members, 0], color=col,marker='.',alpha=0.8)
    ax.scatter(cluster_center[0], 0, color=col, marker='D')
    ax.plot([cluster_min,cluster_min],[-0.2,0.2], color=col,alpha=0.5)
    ax.plot([cluster_max,cluster_max],[-0.2,0.2], color=col,alpha=0.5)
