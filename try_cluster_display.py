# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 05:08:13 2017

@author: wc57661
"""

import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import MeanShift, estimate_bandwidth
from itertools import cycle
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans


def view_3_fig(fig):    
    fig1=fig.add_subplot(221)
    fig1.set_xlabel('y');fig1.set_ylabel('x')
    fig2=fig.add_subplot(222)
    fig2.set_xlabel('z');fig2.set_ylabel('x')
    fig3=fig.add_subplot(223)
    fig3.set_xlabel('y');fig3.set_ylabel('z')
    return fig1, fig2, fig3
def mean_shift(bandwidth,temp,colors,fig):
    ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
    ms.fit(temp)
    labels = ms.labels_
    cluster_centers = ms.cluster_centers_

    labels_unique = np.unique(labels)
    n_clusters_ = len(labels_unique)
    print("bandwidth:", bandwidth)
    print("#estimated clusters :", n_clusters_)
    print("estimated clusters centers:\n", cluster_centers)

    if temp.shape[1]==2:
        cluster_count=[]
        for k, col in zip(range(n_clusters_), colors):
            my_members = labels == k
            cluster_count.append(sum(my_members))
            cluster_center = cluster_centers[k]
            fig.scatter(temp[my_members, 0], temp[my_members, 1], color=col,marker='.',alpha=0.2)
            fig.scatter(cluster_center[0], cluster_center[1], color=col, marker='D')
        cluster_info = zip(range(n_clusters_),cluster_centers,cluster_count)
        return list(cluster_info),labels
    elif temp.shape[1]==3:
        ax = fig.add_subplot(111, projection='3d')
        cluster_count=[]
        for k, col in zip(range(n_clusters_), colors):
            my_members = labels == k
            cluster_count.append(sum(my_members))
            cluster_center = cluster_centers[k]
            ax.scatter(temp[my_members, 0],temp[my_members, 1],temp[my_members, 2], c=col , marker='.')
            ax.scatter(cluster_center[0], cluster_center[1], cluster_center[2], c=col, marker= 'D')
        ax.set_xlabel('X Label');ax.set_ylabel('Y Label');ax.set_zlabel('Z Label')

        plt.show()
        cluster_info = zip(range(n_clusters_),cluster_centers,cluster_count)
        return list(cluster_info),labels

def build_coordinate(x,y,z=0):
    if z==0:
        coor=list(zip(x,y))
        temp=np.asarray(coor).reshape(len(x),2)
    else:
        coor=list(zip(x,y,z))
        temp=np.asarray(coor).reshape(len(x),3)
    return temp
#=================================================================================================================
#create coordinates
rand1x=5*np.random.randn(1,100)+15;rand1y=8*np.random.randn(1,100)+65;rand1z=10*np.random.randn(1,100)+20
rand2x=7*np.random.randn(1,100)+40;rand2y=8*np.random.randn(1,100)+5;rand2z=15*np.random.randn(1,100)+60
rand3x=7*np.random.randn(1,100)+5;rand3y=8*np.random.randn(1,100)+30;rand3z=8*np.random.randn(1,100)+5
rand_x=[];rand_y=[];rand_z=[]
rand_x=list(rand1x[0])
rand_x.extend(list(rand2x[0]));rand_x.extend(list(rand3x[0]))
rand_y=list(rand1y[0])
rand_y.extend(list(rand2y[0]));rand_y.extend(list(rand3y[0]))
rand_z=list(rand1z[0])
rand_z.extend(list(rand2z[0]));rand_z.extend(list(rand3z[0]))
point_size=len(rand_x)
colors = cycle('grcmykb')
#original data plot
#2d scatter
i=1
fig=plt.figure(i,figsize=(12, 12))
fig.suptitle('3view scatter')
i+=1
fig1=fig.add_subplot(221)
fig1.set_xlabel('y');fig1.set_ylabel('x')
plt.scatter(rand_y,rand_x)

fig2=fig.add_subplot(222)
fig2.set_xlabel('z');fig2.set_ylabel('x')
plt.scatter(rand_z,rand_x)

fig3=fig.add_subplot(223)
fig3.set_xlabel('y');fig3.set_ylabel('z')
plt.scatter(rand_y,rand_z)

#3d scatter
fig=plt.figure(i,figsize=(12, 12))
fig.suptitle('3d scatter')
i+=1

ax = fig.add_subplot(111, projection='3d')
ax.scatter(rand_x,rand_y,rand_z, c='r', marker='.')
ax.set_xlabel('X Label');ax.set_ylabel('Y Label');ax.set_zlabel('Z Label')
plt.show()
#===============================================================================================
#2d mean shift 
tempyx=build_coordinate(rand_y,rand_x);tempzx=build_coordinate(rand_z,rand_x);tempyz=build_coordinate(rand_y,rand_z)
bandwidth_yx = estimate_bandwidth(tempyx, quantile=0.3, n_jobs=10)
bandwidth_zx = estimate_bandwidth(tempzx, quantile=0.3, n_jobs=10)
bandwidth_yz = estimate_bandwidth(tempyz, quantile=0.3, n_jobs=10)
#2d cluster
fig=plt.figure(i,figsize=(12, 12))
fig1,fig2,fig3=view_3_fig(fig)
fig.suptitle('2d cluster 3view')
i+=1
cluster_info_yx,labels_yx=mean_shift(bandwidth_yx,tempyx,colors,fig1)
cluster_info_zx,labels_zx=mean_shift(bandwidth_zx,tempzx,colors,fig2)
cluster_info_yz,labels_yz=mean_shift(bandwidth_yz,tempyz,colors,fig3)
#============================================================================================================
#3d mean shift 
temp=build_coordinate(rand_x,rand_y,rand_z)
bandwidth = estimate_bandwidth(temp, quantile=0.3, n_samples=500, n_jobs=10)
#3d cluster
fig=plt.figure(i,figsize=(12, 12))
fig.suptitle('3d cluster')
i+=1
cluster_info,labels=mean_shift(bandwidth,temp,colors,fig)
##3d 3view
#fig=plt.figure(i,figsize=(12, 12))
#fig1,fig2,fig3=view_3_fig(fig)
#fig.suptitle('3d cluster 3view')
#i+=1
#rrand_x=np.asarray(rand_x).reshape(-1,1)
#rrand_y=np.asarray(rand_y).reshape(-1,1)
#rrand_z=np.asarray(rand_z).reshape(-1,1)
#for k, col in zip(range(len(cluster_info)), colors):
#    my_members = labels == k
#    cluster_center = cluster_info[k][1]
#    fig1.scatter(rrand_y[my_members],rrand_x[my_members],color=col,marker='.',alpha=0.2)
#    fig1.scatter(cluster_center[1],cluster_center[0], color=col, marker='D')
#    fig2.scatter(rrand_z[my_members],rrand_x[my_members],color=col,marker='.',alpha=0.2)
#    fig2.scatter(cluster_center[2],cluster_center[0], color=col, marker='D')
#    fig3.scatter(rrand_y[my_members],rrand_z[my_members],color=col,marker='.',alpha=0.2)
#    fig3.scatter(cluster_center[1],cluster_center[2], color=col, marker='D')

#labels
def unique_rows(data):
    uniq = np.unique(data.view(data.dtype.descr * data.shape[1]))
    return uniq.view(data.dtype).reshape(-1, data.shape[1])
labels_array=list(zip(labels_yx,labels_zx,labels_yz,labels))
a=np.asarray(labels_array).reshape(len(labels_array),4)
unique_combinations=unique_rows(a)
unique_combination_count=[]
for i in range(len(unique_combinations)):
    members=[]
    for j in range(len(a)):
        members.append(list(a[j])==list(unique_combinations[i]))
    unique_combination_count.append(sum(members))
np.set_printoptions(threshold=50)
contingency=list(zip(unique_combinations.tolist(),unique_combination_count))
    
#================================================================================================================
#Kmeans
km_n_clusters=3
km = KMeans(n_clusters=km_n_clusters, random_state=0).fit(temp)
labels=km.labels_
n_clusters_=len(km.cluster_centers_)
cluster_centers=km.cluster_centers_
fig=plt.figure(i,figsize=(12, 12))
fig.suptitle('3d cluster mean shift')
i+=1
ax = fig.add_subplot(111, projection='3d')
cluster_count=[]
for k, col in zip(range(n_clusters_), colors):
    my_members = labels == k
    cluster_count.append(sum(my_members))
    cluster_center = cluster_centers[k]
    ax.scatter(temp[my_members, 0],temp[my_members, 1],temp[my_members, 2], c=col , marker='.')
    ax.scatter(cluster_center[0], cluster_center[1], cluster_center[2], c=col, marker= 'D')
ax.set_xlabel('X Label');ax.set_ylabel('Y Label');ax.set_zlabel('Z Label')
plt.show()