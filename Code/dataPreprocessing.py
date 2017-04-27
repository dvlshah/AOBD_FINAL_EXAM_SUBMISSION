#!/usr/bin/env python
"""Preprocesses the data provided in given text files in candidate profile data
   and forms clean version of data representation keeping only the attributes
   required by application.
"""
__author__ = "Deval Shah"
__email__ = "devalshah1619@gmail.com"

##########################################################################################################
import glob
import pickle
from dataIO import dumpData

#Change dataPath,dataPath2 and filenames parameter if you run in any other machine
dataPath = "C:\\Users\\Deval\\Desktop\\AOBD FINAL EXAM\\Python Readable Data\\candidate_profile_json.data"
dataPath2 = "C:\\Users\\Deval\\Desktop\\AOBD FINAL EXAM\\Python Readable Data\\processed.data"
filenames =  glob.glob("C:\\Users\\Deval\\Desktop\\AOBD FINAL EXAM\\Candidate Profile Data\\*.txt")

##########################################################################################################
def no_of_candidates(filenames,data_json,total_candidates=[]):
    """Description - Filter function for making a list of number of candidates to keep track of
                     dictionary indexes of each candidate of each file stored in json format
       Args :
            param1 (list) : filenames --> Names of all files in candidate profile data folder stored in list
            param2 (json) : data_json --> Json representation of data.
            param3 (default empty list) : candidates --> To store each candidate-id per file

       Returns :
            2d dictionary , 2d list
    """
    CandidateID_Data = attributeData(data_json,'CandidateID')
    for j in range(len(filenames)):
        current_idx =  [int(CandidateID_Data[j][i]) for i in CandidateID_Data[j]]
        total_candidates.append(current_idx)
    return CandidateID_Data , total_candidates

##########################################################################################################
def attributeData(data_json,attribute_name,temp1={},temp2={}):
    """Description - Filter function for selecting a particular attribute for entire data.
                     Returns filtered data with that attribute only for whole data
       Args :
            param1 (json) : data_json --> Json representation of data.
            param2 (str) : attribute_name -->String for name of  attribute by which we want to filter our data
            param3 (default empty dictionary) : temp1 --> Dictionary for storing attribute filtered data dictionary of each candidate
            param4 (default empty dictionary): temp2  --> Dictionary for storing attribute dictionary for each file

       Returns :
            2d dictionary
    """
    for i in range(len(filenames)):
        temp1 = {}
        for j in range(len(data_json[i])):
            if attribute_name == 'Skills':
                temp1[j] = data_json[i][j][attribute_name].encode('utf-8').decode('ascii','ignore')
            elif attribute_name == 'Company':
                temp1[j] = data_json[i][j]['Work-Experience'][attribute_name].encode('utf-8').decode('ascii','ignore')
            elif attribute_name == 'Job Title':
                temp1[j] = data_json[i][j]['Work-Experience'][attribute_name].encode('utf-8').decode('ascii','ignore')
            elif attribute_name == 'Job-Duration':
                temp1[j] = data_json[i][j]['Work-Experience'][attribute_name].encode('utf-8').decode('ascii','ignore')
            elif attribute_name == 'Location':
                temp1[j] = data_json[i][j]['Location'].encode('utf-8').decode('ascii','ignore')
            elif attribute_name == 'Qualification':
                temp1[j] = data_json[i][j]['Education'][attribute_name].encode('utf-8').decode('ascii','ignore')
            elif attribute_name == 'Resume-Summary':
                temp1[j] = data_json[i][j][attribute_name].encode('utf-8').decode('ascii','ignore')
            else:
                temp1[j] = data_json[i][j][attribute_name]
        temp2[i] = temp1
    return temp2

##########################################################################################################
def attributeDataCandidateID(attribute_name,fileIndex,candidateID,CandidateID_Data,data_json):
    """Description - Filter function for selecting a particular attribute for a particular
                     candidate
       Args :
            param1 (str) : attribute_name --> String for name of  attribute by which we want to filter our data
            param2 (int) : fileIndex --> Index of file
            param3 (int) : candidateID --> ID of candidate
            param4 (list): CandidateID_Data --> 2d List of dictionary index of each candidate of each file
            param5 (json): data_json --> Json representation of data.

       Returns :
            CandidateID_Data (dict) , total_candidates(list)
    """
    data = attributeData(data_json,attribute_name)
    c_idx = CandidateID_Data[fileIndex].index(candidateID)
    if candidateID in CandidateID_Data[fileIndex]:
        return data[fileIndex][c_idx]
    else:
        return  "Enter a valid candidate ID !"
##########################################################################################################
def cleanedData(data_json,attribute_tags,finalData = {}):
    """Description - Filtering original data with only required attributes necessary
                     for context of application

       Args :
            param1 (json) : data_json --> Json representation of data.
            param2 (list of str's) : attribute_tags --> Attributes for limiting data representation to context
            param3 (default empty dictionary) : finalData -->For storing cleaned data

       Returns :
            finalData (3d Dictionary)
    """
    for i in range(len(filenames)):
        _ , CandidateID_Data = no_of_candidates(filenames,data_json)
        temp2 = {}
        for j in CandidateID_Data[i]:
            temp1 =  {}
            for k in attribute_tags:
                skillData = attributeDataCandidateID(k,i,j,CandidateID_Data,data_json)
                temp1[k] = skillData
            temp2[j] = temp1
        finalData[i] = temp2
    return finalData
############################################################################################################
def fdata(data,candidates,currentJobStatusData = {},skillData = {},qualificationData={}):
    """Description - Filter function for seperating attributes like skill ,
                     job status and qualification in seperate data file
       Args :
            param1 (2d dictionary) : attribute_name --> String for name of  attribute by which we want to filter our data
            param2 (default empty dictionary) : currentJobStatusData --> Data of each candidate's current job
            param3 (default empty dictionary) : skillData --> Data of each candidate's skills acquired
            param4 (default empty dictionary): qualificationData --> Data of each candidate's qualification data

       Returns :
            currentJobStatusData (2d dict) , skillData (2d dict) , qualificationData (2d dict)
    """
    for i in range(len(filenames)):
        temp1 = {}
        temp2 = {}
        temp3 = {}
        for j in candidates[i]:
            t1= data[i][j]['Company'].split("&&")
            t2 = data[i][j]['Job Title'].split("&&")
            t3 = data[i][j]['Job-Duration'].split("&&")
            zipped = list(zip(t1,t2,t3))
            temp1[j] = zipped[0]
            temp2[j] = data[i][j]['Skills'].split("&&")
            temp3[j] = data[i][j]['Qualification'].split("&&")
        currentJobStatusData[i] = temp1
        skillData[i] = temp2
        qualificationData[i] = temp3
    return currentJobStatusData,skillData,qualificationData

############################################################################################################
attribute_tags = [
    'CandidateID',
    'Skills',
    'Company',
    'Job Title',
    'Job-Duration',
    'Location',
    'Qualification'
]
