# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 09:29:43 2017

@author: wc57661
"""

def bhattacharyya(h1, h2):
    def normalize(h):
        return h/np.sum(h)
    return np.sqrt(1-np.sum(np.sqrt(np.multiply(normalize(h1),normalize(h2)))))