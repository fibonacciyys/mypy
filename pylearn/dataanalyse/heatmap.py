# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 12:55:00 2019

@author: ReoNa
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



sns.set()
np.random.seed(0)
uniform_data = np.random.rand(5,6)
heatmap = sns.heatmap(uniform_data,annot=True, square=False)
bottom, top = heatmap.get_ylim()
heatmap.set_ylim(bottom + 0.5, top - 0.5)
plt.show()

#data = [[0.5,0.2],[0.1,0.9]]
#ax = sns.heatmap(data)
#plt.matshow(data)

#def trim(strr):
#    li = []
#    for i in strr:
#        if i not in li:
#            li.append(i)
#    return li
#
#print(trim('google'))
#
#''.join(['google'[index] for index in sorted(['google'.index(i) for i in set('google')])])
