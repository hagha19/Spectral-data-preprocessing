
from pysptools import spectro as sp
import numpy as np
from scipy.signal import savgol_filter

def preprocessing_methods(sample , method):
    if method==0: #AB
        out = np.log10(1/sample)
    elif method==1:#CR
        out = np.zeros(np.shape(sample))
        for k in range(out.shape[0]):
            out[k,:] = sp.SpectrumConvexHullQuotient(list(sample[k,:]), list(range(out.shape[1]))).get_continuum_removed_spectrum()
    elif method==2:#RFD
        out = savgol_filter(sample , 3,polyorder=1 , deriv=1)
    elif method==3:#RSD
        out = savgol_filter(sample , 5,polyorder=3 , deriv=2)
    elif method==4:#AFD
        out = np.log10(1/sample)
        out = savgol_filter(out , 3,polyorder=1 , deriv=1)
    elif method==5:#ASD
        out = np.log10(1/sample)
        out = savgol_filter(out , 5,polyorder=3 , deriv=2)
    elif method==6:
        out = sample
    return out