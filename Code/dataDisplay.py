#!/usr/bin/env python
"""Displays the data as per file index and candidate index values
"""
__author__ = "Deval Shah"
__email__ = "devalshah1619@gmail.com"

from dataPreprocessing import filenames

def dataDisplay(candidates,currentJobStatusData,skillData,qualificationData,fileIndex,candidateID):
    """Description - Displays all data in 3 ways (Valid = Existent)

                     1)If fileIndex >= 0 and valid and candidateID is >=0 and
                     valid then displays data of that candidate in that file index

                     2)If fileIndex >= 0 and valid and candidateID is = -1 then
                     displays data of all candidates in that file index

                     3)If fileIndex == -1 and candidateID is = -1 then
                     displays data of all candidates in all files.
       Args :
            param1 (2d list) : candidates --> Stores candidate ID's of all files where candidate ID's of one file is stored in one list
            param2 (dictionary) : skillData
            param3 (dictionary) : qualificationData
            param4 (dictionary): fileIndex  --> Index for each file stored in folder in chronological order.

    """
    try:
        if fileIndex == -1 and candidateID == -1:
            for i in range(len(filenames)):
                print("#################")
                print("File Index : "+str(i))
                for j in candidates[i]:
                    print("\n##################")
                    print("Candidate ID : ",j)
                    print("##################")
                    print("\nCurrent Job Status\n")
                    print(currentJobStatusData[i][j])
                    print("\nSkill Data\n")
                    print(skillData[i][j])
                    print("\nQualification Data\n")
                    print(qualificationData[i][j])
        elif fileIndex != -1 and candidateID == -1:
            try:
                print("File Index : "+str(fileIndex)+"\n")
                for j in candidates[fileIndex]:
                    print("#################")
                    print("Candidate ID : "+str(j)+"\n")
                    print("\nCurrent Job Status\n")
                    print(currentJobStatusData[fileIndex][j])
                    print("\nSkill Data\n")
                    print(skillData[fileIndex][j])
                    print("\nQualification Data\n")
                    print(qualificationData[fileIndex][j])
                    print("\n")
            except Exception as e:
                print("File with given index does not exist!")
        elif fileIndex != -1 and candidateID != -1:
            try:
                print("\n#################")
                print("\nFile Index   : "+str(fileIndex)+"\n")
                print("Candidate ID : "+str(candidateID)+"\n")
                print("#################\n")
                temp = currentJobStatusData[fileIndex][candidateID]
                print("Current Job Status\n")
                print(temp)
                print("\nSkill Data\n")
                print(skillData[fileIndex][candidateID])
                print("\nQualification Data\n")
                print(qualificationData[fileIndex][candidateID])
                print("\n")
            except Exception as e:
                print("The combination of fileIndex and candidateID does not exist")
        else:
            print("Enter valid values of fileIndex and candidateID")
    except Exception as e:
            print("Enter valid values of fileIndex and candidateID")
