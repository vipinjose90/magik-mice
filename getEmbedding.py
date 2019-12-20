import numpy as np
from scipy import sparse

def getEmbedding(datain, maxtau, windowsize, gap=1):
    print ("MaxTau = {0} " .format(maxtau))
    print ("Window Size = {0} " .format(windowsize))
    print ("Gap = {0} " .format(gap))
    print("")
    out=[]
    for tau in range(gap, maxtau+1):
        lagged = np.roll(datain, -tau, axis=0)[:-tau]
        lagged = lagged[0:windowsize]
        out.append(lagged.tolist())    
    out = np.array(out, dtype=float).transpose()
    return(out)
