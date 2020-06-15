import numpy as p
import pandas as pd
from scipy.stats import poisson as pos

x = p.array([0,1,2,3,4])
y = p.array([122,60,15,2,9,1])
x2 = []
for i in range(len(x)):
    xy = x[i]*y[i]
    x2.append(xy)
    x4 = p.sum(x2)
    y4 = p.sum(y)
total_xy = x4
total_y = y4
mu = total_xy/total_y   

poisson_dis = [] 
for i in range(len(x)):
    poss = pos.pmf(i,mu)
    poisson_dis.append(poss)
 
print("Poisson distribution :",poisson_dis) 
