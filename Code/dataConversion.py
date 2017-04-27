#!/usr/bin/env python
"""Converts data into meaningful python json object representation to work with
   files.
"""
__author__ = "Deval Shah"
__email__ = "devalshah1619@gmail.com"

from dataIO import readData
from dataIO import dumpData

#########################################################################################################
"""Extracting filenames of all files in candidate profile data"""

import glob
filenames =  glob.glob("C:\\Users\\Deval\\Desktop\\AOBD FINAL EXAM\\Candidate Profile Data\\*.txt")
data = readData(filenames)

#########################################################################################################
"""Store Candidate Profile Data in json format(for each file a seperate dict) and
   dumping entire json in .data file
"""
dataPath = "C:\\Users\\Deval\\Desktop\\AOBD FINAL EXAM\\Python Readable Data\\candidate_profile_json.data"
dumpData(dataPath,data)

##########################################################################################################
