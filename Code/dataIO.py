#!/usr/bin/env python
"""Functions for reading and dumping data files
"""
__author__ = "Deval Shah"
__email__ = "devalshah1619@gmail.com"

#########################################################################################################

def dumpData(dataPath,data):
    """Dumps data file in specified dataPath"""
    import pickle
    with open(dataPath,'wb') as f:
        pickle.dump(data,f)

#########################################################################################################

def readData(filenames,data={}):
    """Loading json directory and storing in python dictionary"""
    import json
    for i in range(len(filenames)):
        with open(filenames[i]) as data_file:
            data[i] = json.load(data_file)
    return data

#########################################################################################################
