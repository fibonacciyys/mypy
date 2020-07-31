# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 00:42:17 2018

@author: YY
"""

import numpy as np
#import pandas as pd

sx = '''
0.37	0.64	0.52	0.510 
0.54	0.43	0.28	0.417 
0.8	0.53	0.6	0.643 
1	1.17	1.19	1.120 
1.03	1.27	1.2	1.167 
0.84	0.8	0.73	0.790 

'''

zd_data = np.array(list(map(lambda x : x.split('\t'),sx.strip().split('\n'))))




zd_data = zd_data.transpose()
