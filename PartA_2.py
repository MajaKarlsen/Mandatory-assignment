# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 15:14:23 2024

@author: inger
"""

#Part A, 2.
from math import sqrt

def std_builtin():
    
    num_lst = [1, 2, 3, 4, 5]

    N = len(num_lst)

    mx = 1 / N * sum(num_lst)

    S = (1 / N) * sum(x**2 for x in num_lst)

    o = sqrt(S - mx**2)

    print(round(o, 4))

std_builtin()

