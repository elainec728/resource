    # -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 03:44:19 2017

@author: wc57661
"""

from scipy import stats
import matplotlib.pyplot as plt
import numpy as np
import csv
import os
from scipy.integrate import simps
from sklearn.cluster import MeanShift, estimate_bandwidth


cwd=os.getcwd()

def bandwidth(std, n):
     return 1.06*std*np.exp(-0.2*np.log(n))

#input
histo_size=500
input_file_name='gc20Value.csv'
output_file_name='output.csv'
minmin=-251591
maxmax=3449797

#import
raw_data=[]
with open(input_file_name, mode='r') as csvfile:#, newline=''
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in reader:
        for ele in row:
            raw_data.append(float(ele))
raw_data_size=len(raw_data)
raw_data=np.asarray(raw_data)

#statistics
#min_raw_data=min(raw_data)
#max_raw_data=max(raw_data)
min_raw_data=minmin
max_raw_data=maxmax
sum_raw_data=sum(raw_data)
mean_raw_data=np.mean(raw_data)
std=np.std(raw_data)
band_width=bandwidth(std, raw_data_size)


#KDF
step=(max_raw_data-min_raw_data)/histo_size
histo=np.linspace(min_raw_data-step,max_raw_data+step,histo_size+2)
kd=stats.gaussian_kde(raw_data)
kd.set_bandwidth(bw_method='scott')
y1=kd.evaluate(histo)
kd.set_bandwidth(bw_method='silverman')
y2=kd.evaluate(histo)
kd.set_bandwidth(bw_method=kd.factor / 3.)
y3=kd.evaluate(histo)
kd.set_bandwidth(band_width)
y4=kd.evaluate(histo)

#legend()

#check
raw_data_size
min_raw_data
max_raw_data
sum_raw_data
mean_raw_data

#loop
def normPDF(value, band_width, histo):
    return np.exp(-0.5*(histo-value)**2/band_width**2-np.log(band_width)-0.5*np.log(2*np.pi))
y=np.zeros(len(histo))
for value in raw_data:
    for i in range(len(histo)):
        y[i]+=normPDF(value,band_width,histo[i])
y_temp=y/raw_data_size
#validate
simps(y_temp,histo)

#plot
#plt.plot(histo,kernel_pdf,'.')
#fig, ax = plt.subplots()
#plt.plot(raw_data, np.ones(len(raw_data) / (4. * raw_data.size), 'bo', label='Data points (rescaled)')
#plt.plot(histo[:100], y1[:100], label='Scott (default)')
#plt.plot(histo[:100], y2[:100], label='Silverman')
#plt.plot(histo[:100], y3[:100]*10000, label='Const (1/3 * Silverman)')
#plt.plot(histo[:100], y4[:100]*10000, label='1.06')
plt.plot(histo, y1, label='Scott (default)')
plt.plot(histo, y2, label='Silverman')
plt.plot(histo, y3, label='Const (1/3 * Silverman)')
plt.plot(histo, y4, label='1.06')
plt.subplot(221)
hist, bin=np.histogram(raw_data,bins=1000)
plt.hist(raw_data,bins=1000)
plt.subplot(222)
plt.plot(histo,y_temp*8*10**8)

#output
with open(output_file_name, mode='w') as csvfile:
    writer = csv.writer(csvfile,delimiter='\n')
    writer.writerow(y_temp)
#%%
#try mean shift
#temp=raw_data.reshape(-1,1)
#bandwidth = estimate_bandwidth(temp, quantile=0.3, n_samples=500, n_jobs=10)
#test
temp_test=[1, 1.5, 1.8, 1.9, 2, 2.1, 2.2, 2.5,2.9,3.5]
temp_test=list(np.random.randn(20)*5)
temp_test.extend(list(np.random.randn(10)*2+7))
temp_test=[3.7060308181360826 , 3.8197131758372076 , 4.756093498656137 , 8.333923671803312 , 1.313119789661918 , 4.843912489321799 , 7.270751560799569 , 6.112748157287726 , 4.168420154758035 , 3.2870249641846963 , 2.339240087512506 , 2.8670560430626395 , 2.0427909214796633 , 5.250439271715555 , 9.232217456539741 , 5.073692283537233 , 6.263921808400215 , 1.4060563609368335 , 5.237245244363368 , 1.2142048982302889 , 9.38473198380946 , 3.4642828414787523 , 4.545225917635264 , 5.321949456872623 , 2.9072423727905976 , 7.480982170052065 , 3.9644269835057666 , 3.0412658786216626 , 1.6747446585613877 , 7.177977028842131 , 5.747274773491968 , 5.221460908153082 , 7.522632311880712 , 5.593295938324192 , 8.183270784757392 , 4.225558319361752 , 6.7870430299555125 , 5.800205916885345 , 5.510794086292181 , 6.072258645682237 , 4.310503142725205 , 3.1381802729650623 , 3.1312197358595215 , 1.249267097141074 , 2.655054534803524 , 7.3842952027420745 , 3.0706969977516385 , 7.53714065376767 , 9.335883838052744 , 3.560157187459638]
temp=np.asarray(temp_test).reshape(-1,1)
bandwidth = estimate_bandwidth(temp, quantile=0.3)

ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
ms.fit(temp)
labels = ms.labels_
cluster_centers = ms.cluster_centers_

labels_unique = np.unique(labels)
n_clusters_ = len(labels_unique)
print("bandwidth:", bandwidth)
print("number of estimated clusters :", n_clusters_)
print("estimated clusters centers:\n", cluster_centers)


#cluster graph
from itertools import cycle

plt.figure(1)
np.random.normal()
cluster_count=[]
colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
for k, col in zip(range(n_clusters_), colors):
    my_members = labels == k
    cluster_count.append(sum(my_members))
    cluster_center = cluster_centers[k]
    plt.plot(temp[my_members, 0], np.random.randn(len(temp[my_members, 0])), col + '.')
    plt.plot(cluster_center[0], 0, 'o', markerfacecolor=col,
             markeredgecolor='k', markersize=14)
zip(range(n_clusters_),cluster_count)
plt.title('Estimated number of clusters: %d' % n_clusters_)
plt.show()