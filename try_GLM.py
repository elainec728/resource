# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 23:34:41 2017

@author: wc57661
"""

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
import csv
import re



#import
input_file_name='try_csv.csv'
raw_data=[]
with open(input_file_name, mode='r') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in reader:
        raw_data.append(row)
col1=[]
col2=[]
col3=[]
col4=[]
col5=[]
for row in raw_data:
    a=re.split(',',row[0])
    col1.append(int(a[0]))
    col2.append(int(a[1]))
    col3.append(float(a[2]))
    col4.append(float(a[3]))
    col5.append(int(a[4]))
#coordinate=list(zip(col1,col2))
#coll1=[]
#coll2=[]
#coll5=[]
#for i in range(len(coordinate)):
#    coordinate[i]=list(coordinate[i])
#    coll1[i]=list(col1[i])
#    coll2[i]=list(col2[i])
#    coll5[i]=list(col5[i])

#split data
#x_train_set=coordinate[:100]
#x_test_set=coordinate[-100:]
x_train_set=np.asarray(col1[:100]).reshape(-1,1)
x_test_set=np.asarray(col1[-100:]).reshape(-1,1)
y_train_set=col5[:100]
y_test_set=col5[-100:]

#model
regr = linear_model.LinearRegression()
regr.fit(x_train_set,y_train_set)

#output
print('Coefficients: \n', regr.coef_)
# The mean squared error
print("Mean squared error: %.2f"
      % np.mean((regr.predict(x_test_set) - y_test_set) ** 2))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % regr.score(x_test_set, y_test_set))

#plot
# Plot outputs
plt.scatter(x_test_set, y_test_set,  color='black')
plt.plot(x_test_set, regr.predict(x_test_set), color='blue',
         linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()



##input
#diabetes = datasets.load_diabetes()
## Use only one feature
#diabetes_X = diabetes.data[:, np.newaxis, 2]
## Split the data into training/testing sets
#diabetes_X_train = diabetes_X[:-20]
#diabetes_X_test = diabetes_X[-20:]
## Split the targets into training/testing sets
#diabetes_y_train = diabetes.target[:-20]
#diabetes_y_test = diabetes.target[-20:]
#
## Create linear regression object
#regr = linear_model.LinearRegression()
#
## Train the model using the training sets
#regr.fit(diabetes_X_train, diabetes_y_train)
#
## The coefficients
#print('Coefficients: \n', regr.coef_)
## The mean squared error
#print("Mean squared error: %.2f"
#      % np.mean((regr.predict(diabetes_X_test) - diabetes_y_test) ** 2))
## Explained variance score: 1 is perfect prediction
#print('Variance score: %.2f' % regr.score(diabetes_X_test, diabetes_y_test))
#
## Plot outputs
#plt.scatter(diabetes_X_test, diabetes_y_test,  color='black')
#plt.plot(diabetes_X_test, regr.predict(diabetes_X_test), color='blue',
#         linewidth=3)
#
#plt.xticks(())
#plt.yticks(())
#
#plt.show()