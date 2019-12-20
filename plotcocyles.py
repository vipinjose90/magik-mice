import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from subprocess import call
import webbrowser
import os
import heapq
from getEmbedding import getEmbedding
from getCocyles import getCocyles
from sys import argv


def plotcocyles(cofile):
   # mapping for circular value parameterization
    callcmd = 'python cocycle.py points.bdry points-' + cofile  + '.ccl points.vrt'
    q = call([callcmd], shell=True)
    if q==0:
        print("Circular Value Parameterization successful")
    else:
        print("Circular Value Parameterization not successful. Continuing ...")
       
    # Generating the output in the form of a PDF
    vis_path = 'python plotpca.py points-' + cofile + '.val ' + 'data.txt' 
    q = call([vis_path], shell=True)
    if q==0:
        print("Plotting sucessful!")

if __name__ == '__main__':
    # Smoothens the input and converts to a matrix for further processing
    plotcocyles(argv[1])   
