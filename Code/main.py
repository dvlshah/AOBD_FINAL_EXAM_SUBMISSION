#!/usr/bin/env python
"""
"""
__author__ = "Deval Shah"
__email__ = "devalshah1619@gmail.com"

from dataPreprocessing import no_of_candidates
from dataPreprocessing import filenames
from dataPreprocessing import dataPath
from dataPreprocessing import dataPath2
from dataPreprocessing import fdata
from dataDisplay import dataDisplay
import pickle

data_json = pickle.load(open(dataPath, 'rb'))
data = pickle.load(open(dataPath2,"rb"))
_,candidates = no_of_candidates(filenames,data_json)
currentJobStatusData,skillData,qualificationData = fdata(data,candidates)

#Displaying all candidates(set candidate id to -1) for file having file index = 0
#dataDisplay(candidates,currentJobStatusData,skillData,qualificationData,fileIndex=0,candidateID=-1)

#Displaying candidate with candidate id = 4(set candidate id to 4) for file having file index = 0
dataDisplay(candidates,currentJobStatusData,skillData,qualificationData,fileIndex=0,candidateID=4)


fileIndex = 0
candidateID = 4

userProfile = [candidates[fileIndex][candidateID],
               currentJobStatusData[fileIndex][candidateID],
               skillData[fileIndex][candidateID],
               qualificationData[fileIndex][candidateID]]

#Printing entire user profile with candidate having candidateID = 4 and 
#file index = 0(1st file in folder)
print(userProfile)
