# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 09:17:23 2017

@author: wc57661
"""
#import sys
#sys.path.append('C:\\Users\wc57661\workspace_python\cluster_compare')
import numpy as np
import matplotlib.pyplot as plt
#from cluster_method.cluster_plot import cluster_plot
from sklearn.cluster import MeanShift, estimate_bandwidth



def prepare_random_data(size,mean,std):
    part_size=int(size/len(mean))
    remaining=size
    data=[]
    for i in range(len(mean)):
        if i != len(mean)-1:
            part=std[i]*np.random.randn(1,part_size)+mean[i]
            data+=list(part[0])
            remaining-=part_size
        else:
            part=std[i]*np.random.randn(1,remaining)+mean[i]
            data+=list(part[0])
    return data


#data preparation
mean=[50,120,200,300]
std=[10,10,10,10]
size=400
data=prepare_random_data(size,mean,std)
X=np.asarray(data).reshape(-1,1)

i=1
fig=plt.figure(i,figsize=(12, 5))
fig.suptitle('Scatter')
fig.add_subplot(111)
plt.scatter(data,np.zeros_like(data))

def mean_shift(X,quantile):
    bandwidth = estimate_bandwidth(X, quantile=quantile)
    ms = MeanShift(bandwidth=bandwidth)
    ms.fit(X)
    labels = ms.labels_
    n_clusters_ = len(np.unique(labels))
    cluster_count=[]
    for i in range(n_clusters_):
        my_members = labels == i
        cluster_count.append(sum(my_members))
    print("Mean Shift :")
    print("bandwidth:", bandwidth)
    print("#estimated clusters :", n_clusters_)
    print("estimated clusters centers:\n", ms.cluster_centers_)
    print("clusters counts :", cluster_count)
    print("sum of clustered counts :", sum(cluster_count))
    return ms, cluster_count
ms,cluster_count=mean_shift(X,0.2)
centers=ms.cluster_centers_
labels=ms.labels_

def cluster_mean(X,labels):
    mean=[]
    n=np.unique(labels)
    for i in n:
        members=labels==i
        mean.append(list(sum((X[members]))/len(X[members])))
    return mean
c_mean=cluster_mean(X,labels)
point=75
point=[[point]]
point_label=ms.predict(point)




