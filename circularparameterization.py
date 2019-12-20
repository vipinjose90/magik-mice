import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from subprocess import call
import webbrowser
import os
import heapq
from getEmbedding import getEmbedding
from getCocyles import getCocyles


def findParameterization(datain, gap, maxdist, startval):
    j = maxdist
    i = startval
    q = 1
    stop = 1
    while stop==1:
        maxtau = i
        print("")
        print("Embedding Length = {0}".format(i))
        print("******************************")
        q=1
        while q!=0:
            windowsize = datain.shape[0]-maxtau
            print("")
            print("")
            print("")
            print("Cutoff Parameter = {0}".format(j))
            print("...........................")
            print("")
            X = getEmbedding(datain[:,1], maxtau, windowsize, gap)
            X.astype('float64', order='C')
            np.savetxt('data.txt', X, fmt = '%f')
            getCocyles('./data.txt', j)
            # mapping for circular value parameterization
            q = call(['python cocycle.py points.bdry points-0.ccl points.vrt'], shell=True)
            call(['python cocycle.py points.bdry points-1.ccl points.vrt'], shell=True)
            if q==0:
                print("Circular Value Parameterization successful")
            else:
                print("Circular Value Parameterization not successful. Continuing ...")
                j = j + 1
            
            if q==0:
                stop=0
            elif j > maxdist:
                q=0
                j = maxdist
        i = i+1
        
    # Generating the output in the form of a PDF
    vis_path = 'python plotpca.py points-0.val ' + 'data.txt' + ' scatter.py points-0.val points-1.val'
    q = call([vis_path], shell=True)
    if q==0:
        print("Plotting sucessful!")
        vis_path = 'Rscript plotpersdiag.R'
        call([vis_path], shell=True)
    
    # print working embedding length and cutoff parameter
    print("")
    print("First possible embedding length = {0}".format(i-1))
    print("")
    print("MaxTau = {0}".format(maxtau))
    print("")
    print("Cutoff parameter used = {0}".format(j))
    # open pdf
    webbrowser.open_new(r'file:/Users/vipinjose/VJWorkSpace/Computational Topology/Magik-Mice/points-0.pdf')
    webbrowser.open_new(r'file:/Users/vipinjose/VJWorkSpace/Computational Topology/Magik-Mice/persdiag.pdf')
    return(i-1,maxtau,j)
