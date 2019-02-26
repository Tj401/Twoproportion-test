# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 16:21:55 2019

@author: kdandebo
"""

import pandas as pd

#import matplotlib.pyplot as plt
import numpy as np
from statsmodels.stats.proportion import proportions_ztest

TwoProp = pd.ExcelFile('C:/Users/kdandebo/Desktop/Models/DS training/Yogesh data sets/JohnyTalkers(unstacked).xlsx')
TwoProp = TwoProp.parse("Sheet1")
print(TwoProp.columns)
#Prop = np.array([[58,152], [480,740]])
print(proportions_ztest(np.array([58,152]),np.array([480,740]),alternative='two-sided'))
#as p-value lessthan 0.05 . alternative hypothesis, works as proportions are not equal

print(proportions_ztest(np.array([58,152]),np.array([480,740]),alternative='larger'))