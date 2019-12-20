#!/usr/bin/env python2

"""Converts the input file into a matrix and smooths the input using low pass filter"""

__author__ = "Vipin Jose"
__version__ = "1.0.1"
__maintainer__ = "Vipin Jose"
__email__ = "vipinjose90@gmail.com"

#inmport modules
import numpy as np
import pandas as pd
import csv
from subprocess import call
import os

def readandsmooth(infile):
    try:
        os.remove('smoothed-mice.csv')
    except OSError:
        pass

    #Call RScript that smoothens the input
    cutoff = 0.002
    cutoff = str(cutoff)
    path = 'Rscript discretesmooth.R ' + infile + ' ' + cutoff
    call([path], shell=True)
    points = []
    with open("smoothed-mice.csv", 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            points.append(float(row[0]))
    y = points
    t = np.linspace(1, len(y), len(y))
    V = pd.DataFrame([t,y]).transpose()
    V.plot()
    V = V.as_matrix()
    return(V)
