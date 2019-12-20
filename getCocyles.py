from subprocess import call
import webbrowser
import os
import glob
import heapq

def getCocyles(data, max_distance, skeleton=2):
    # remove old files
    try:
        os.remove('points-1.val')
    except OSError:
        pass
    try:
        filelist=glob.glob('*.ccl')
        for file in filelist:
            os.remove(file)
    except OSError:
        pass
    try:
        os.remove('points-0.val')
    except OSError:
        pass
    try:
        os.remove('points-0.pdf')
    except OSError:
        pass
    try:
        os.remove('points-0.ccl')
    except OSError:
        pass
    try:
        os.remove('points.vrt')
    except OSError:
        pass
    try:
        os.remove('points.dgm')
    except OSError:
        pass
    try:
        os.remove('points.bdry')
    except OSError:
        pass
    
    # Run persistence cohomology from Dionysus
    data_file = str(data) 
    max_distance = str(max_distance)
    skeleton = str(skeleton)
    path = './rips-pairwise-cohomology ' + data_file + ' -m '+ max_distance +' -s ' + skeleton + ' -b points.bdry -c points -v points.vrt -d points.dgm'
    call([path], shell=True)
    print("Built Rips")
