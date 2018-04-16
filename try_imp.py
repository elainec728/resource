# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 17:42:25 2017

@author: wc57661
"""
#%%
import imp

(f,pathname,desc)=imp.find_module('cluster_method',path=['C:\\Users\wc57661\workspace_python\cluster_compare'])
test = imp.load_module('cluster_method', f, pathname, desc)
#import test
test

#%%
def import_non_local(name, path,custom_name=None):
    import imp
#    custom_name = custom_name or name
    f, pathname, desc = imp.find_module(name, path)
    module = imp.load_module(name, f, pathname, desc)
#    f.close()

    return module
path='C:\\Users\\wc57661\\workspace_python\\cluster_compare'
package_name='cluster_method'
test=import_non_local(package_name,[path])
#test
## Import non-local module, use a custom name to differentiate it from local
## This name is only used internally for identifying the module. We decide
## the name in the local scope by assigning it to the variable calendar.
#calendar = import_non_local('calendar','std_calendar')
#
## import local module normally, as calendar_local
#import calendar as calendar_local
#
#print calendar.Calendar
#print calendar_local
