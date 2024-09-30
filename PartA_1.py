# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 15:53:24 2024

@author: inger
"""
#Part A, 1.

from math import sqrt 

def std_loops():
#Define sum_a and sum_b
    sum_a = 0
    sum_b = 0

#Define the list from the task
    num_lst = [1, 2, 3, 4, 5]

#Find the lenght of the list, so that i have a variable in the for-loop
    N = 0
    
    for i in num_lst:
        
        N = N + 1
    

#Part 1
    for i in range(1, N + 1):
        xi = num_lst[i - 1]
        sum_a = sum_a + xi
        
    mx = 1 / N  * sum_a    #For mx = the mean


#Part 2
    for i in range(1, N + 1):
        b = (num_lst[i - 1])**2
        sum_b = sum_b + b

    S = 1/N * sum_b    #For S = the mean of squares

#Part 3 and 4
    o = sqrt(S - mx ** 2)     #For o = the standard deviation

    print(round(o, 4))
    
std_loops()