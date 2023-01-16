import numpy as np
import matplotlib.pyplot as plt

def derivation(func, A, B, n):
    x=[];y=[];yfunc=[]
    h=(B-A)/n
    for i in np.linspace(A,B,n):
        diffkvot=(func(i+h)-func(i))/h
        x.append(i)
        y.append(diffkvot)
        yfunc.append(func(i))
    return(x,y,yfunc)

