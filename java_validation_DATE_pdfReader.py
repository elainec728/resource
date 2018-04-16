# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 22:30:53 2017

@author: wc57661
"""
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np
import csv
import os
from scipy.integrate import simps

cwd=os.getcwd()
def bandwidth(std, n):
     return 1.06*std*np.exp(-0.2*np.log(n))
def date_to_index(y,m,d):
    return(y-1)*365+(m-1)*30+d-1
def getLSDPHL(bandwidth):
    return np.log(bandwidth)+0.5*np.log(2*np.pi)
def test(raw_data):
    std=np.std(raw_data)
    bw=bandwidth(std,len(raw_data))
    print('std: ',std)
    print('bandwitdth: ',bw)
    print('getLSDPHL: ',getLSDPHL(bw))

#input
histo_size=102
#input_file_name='DATE_INDEX.csv'
#output_file_name='output_date.csv'
#output_histo_file_name='output_date_histo.csv'
#input_file_name='bd_try.csv'
input_file_name='0811data.csv'
output_file_name='output.csv'
output_histo_file_name='output_histo.csv'
minmin=-203950.72	

#date_to_index(1985,7,26) 
maxmax=14503482.27	

#date_to_index(1985,7,26)
#%%
#import
raw_data=[]
with open(input_file_name, mode='r') as csvfile:#, newline=''
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in reader:
        for ele in row:
            raw_data.append(float(ele))
raw_data_size=len(raw_data)
raw_data=np.asarray(raw_data)
#np.atleast_2d(raw_data)
#null_record=list(raw_data).count(0)

#statistics
#min_raw_data=min(raw_data)
#max_raw_data=max(raw_data)
from scipy.stats import mode
mode(raw_data)
min_raw_data=minmin
max_raw_data=maxmax
#sum_raw_data=sum(raw_data)
mean_raw_data=np.mean(raw_data)
std=np.std(raw_data)
band_width=bandwidth(std, raw_data_size)

#%%
#KDF
#date
step=(max_raw_data-min_raw_data)/(histo_size-1)
histo=np.linspace(min_raw_data,max_raw_data+step,histo_size+1)
kd=stats.gaussian_kde(raw_data)
#kd.set_bandwidth(bw_method='scott')
#y1=kd.evaluate(histo)
#kd.set_bandwidth(bw_method='silverman')
#y2=kd.evaluate(histo)
#kd.set_bandwidth(bw_method=kd.factor / 3.)
#y3=kd.evaluate(histo)
#kd.set_bandwidth(band_width)
#y4=kd.evaluate(histo)
y_kd=kd.evaluate(histo)
print('kd integration: ',simps(y_kd,histo))


#check
print('data_size: ',raw_data_size)
print('histo_size: ',len(histo))
print('min: ',min_raw_data)
print('max: ',max_raw_data)
print('mean: ',mean_raw_data)
print('standard deviation: ',std)
print('bandwidth: ',band_width)
print('step: ', step)

#%%
#loop as java
def normPDF(value, band_width, histo):
    return np.exp(-0.5*(histo-value)**2/band_width**2-np.log(band_width)-0.5*np.log(2*np.pi))
y=np.zeros(len(histo))
for value in raw_data:
    for i in range(len(histo)):
        y[i]+=normPDF(value,band_width,histo[i])
y_temp=y/raw_data_size
#validate
print('java integration: ',simps(y_temp,histo))

#plot
#plt.plot(histo, y1, label='Scott (default)')
#plt.plot(histo, y2, label='Silverman')
#plt.plot(histo, y3, label='Const (1/3 * Silverman)')
#plt.plot(histo, y4, label='1.06')
#plt.subplot(221)
hist, bin=np.histogram(raw_data,bins=500)
plt.figure(figsize=(12,6))
#plt.hist(raw_data,bins=70)
#plt.subplot(222)
#plt.plot(histo,y_temp*5*10**7)
plt.plot(histo,y_temp)
list(zip(histo,y_temp))

#output
#with open(output_file_name, mode='w') as csvfile:
#    writer = csv.writer(csvfile,delimiter='\n')
#    writer.writerow(y_temp)
#with open(output_histo_file_name, mode='w') as csvfile:
#    writer = csv.writer(csvfile,delimiter='\n')
#    writer.writerow(histo)
#with open('try.csv', mode='w') as csvfile:
#    writer = csv.writer(csvfile,delimiter='\n')
#    writer.writerow([h,y for h in histo for y in y_temp])
#%%%
raw_data_1=np.ones(50)
histo_size_1=20
min_raw_data_1=-1
max_raw_data_1=2
#mean_raw_data=np.mean(raw_data_1)
std_1=np.std(raw_data_1)
#band_width_1=bandwidth(std,len(raw_data_1))
band_width_1=0.07
test(raw_data_1)
step_1=(max_raw_data_1-min_raw_data_1)/(histo_size_1-1)
histo_1=np.linspace(min_raw_data_1,max_raw_data_1+step_1,histo_size_1+1)
y_1=np.zeros(len(histo_1))
for value in raw_data_1:
    for i in range(len(histo_1)):
        y_1[i]+=normPDF(value,band_width_1,histo_1[i])
y_temp1=y_1/len(raw_data_1)
plt.plot(histo_1,y_temp1)
#%%%
count_list=np.linspace(1,10001,11).tolist()
std_list=np.linspace(1,1001,11).tolist()
#def apply_bw(std,count):
#    bw_set={}
#    bw=[]
#    for i in range(len(std)):
#        bw=[bandwidth(std[i],n) for n in count]
#        bw_set[std[i]]=bw
#    return bw_set
#def index_of(v,list):
#    step=list[1]-list[0]
#    i=int((v-list[0])/step)
#    return i
#def for_plot(count_list,std_list,para,i):
#    bw_set=apply_bw(std_list,count_list)
#    y=[]
#    if para=='std':#modify std, fixed n
##        i=index_of(v,count_list)
#        keys=bw_set.keys()
#        for key in keys:
#            y.append(bw_set[key][i])
#    elif para=='count':#modify n, fixed std
##        y=bw_set[index_of(v,std_list)]
#        y=bw_set[i]
#    return y

def apply_bw2(std,count):
    bw=[]
    if len([count])==1:
        bw=[bandwidth(s,count) for s in std]
    elif len([std])==1:
        bw=[bandwidth(std,c) for c in count]
    return bw
def bw_plot(std,count,para,index):
    fig = plt.figure()
    n=1
    if para=='std':
        for i in index:
            ax=fig.add_subplot(len(index),1,n)
            y=apply_bw2(std,count[i])
            ax.plot(std,y)
            n+=1
    elif para=='count':
        for i in index:
            ax=fig.add_subplot(len(index),1,n)
            y=apply_bw2(std[i],count)
            ax.plot(std,y)
            n+=1
bw_plot(std_list,count_list,'std',[1,4,9])            
            
    
#bw_set=apply_bw(std_list,count_list)
#bw_change_std=for_plot(count_list,std_list,'std',i)
#bw_change_n=for_plot(count_list,std_list,'count',i)

    
#plt.scatter(count,bw)
#bw_std=[bandwidth(std,)]