# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 08:08:53 2022

@author: Sammy
"""

import numpy

N,M=map(int,input().split())
my_array=numpy.array([input().split() for i in range(N)],int)
my_sum=numpy.sum(my_array,axis=0)
my_prod=numpy.prod(my_sum,axis=0)
print(my_prod)