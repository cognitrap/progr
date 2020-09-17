#Modulen med funktionerna
#modulen heter hyper.py

import numpy as np

def cas(a):
    return((np.exp(a)+np.exp(-a))/2.)

def san(a):
    return((np.exp(a)-np.exp(-a))/2.)
