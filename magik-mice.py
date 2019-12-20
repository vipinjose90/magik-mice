#!/usr/bin/env python2

"""This module calculates the cohomology parameterization for the input - end-to-end. This includes smoothing the data and finding the best window embedding"""

__author__ = "Vipin Jose"
__version__ = "1.0.1"
__maintainer__ = "Vipin Jose"
__email__ = "vipinjose90@gmail.com"

#inmport modules
import numpy as np
import pandas as pd
from circularparameterization import findParameterization
from sys import argv
from readandsmooth import readandsmooth

if __name__ == '__main__':
	# Smoothens the input and converts to a matrix for further processing
	V = readandsmooth(argv[1])

	# Finds the appropriate embedding and circular parameterization
	findParameterization(V, 1, 2, 150)
