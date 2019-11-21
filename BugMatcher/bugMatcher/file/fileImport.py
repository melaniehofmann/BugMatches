'''
Created on 17.09.2019

@author: mhofmann
'''
import os

def readFile(filePath):
    if os.path.exists(filePath):
        with open(filePath, "r") as f:
            try:
                # read text file and split lines to get rid of \n at the end of each line
                return f.read().splitlines()
            except:
                raise Exception("Can't read file {}".format(filePath))
    else:
        raise Exception("File {} does not exist.".format(filePath))