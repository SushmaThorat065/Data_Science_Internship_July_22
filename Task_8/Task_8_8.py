# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 21:04:27 2022

@author: Sushma Thorat
"""

N = int(input())
X = list(map(float,input().strip().split()))
Y = list(map(float,input().strip().split()))

x = sum(X) / N
y = sum(Y) / N

stdv_x = (sum([(i - x)**2 for i in X]) / N)**0.5
stdv_y = (sum([(i - y)**2 for i in Y]) / N)**0.5


covariance = sum([(X[i] - x) * (Y[i] - y) for i in range(N)])

correlation_coefficient = covariance / (N * stdv_x * stdv_y)

print(round(correlation_coefficient,3))