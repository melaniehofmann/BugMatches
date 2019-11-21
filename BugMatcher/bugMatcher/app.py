'''
Created on 17.09.2019

@author: mhofmann
'''
import sys
import getopt
import os
from bugMatcher.file.fileImport import readFile
from bugMatcher.bugFinder import BugFinder

def main(argv):
    """ Arguments:
    
    -b -- path to bug text file
    -l -- path to landscape text file
    """
    bugFileName = str("resources" + os.path.sep + "bug.txt")
    landscapeFileName = "";
    
    opts, args = getopt.getopt(argv, "b:l:")

    for opt, arg in opts:
        if opt in "-b":
            bugFileName = arg;
        elif opt in "-l":
            landscapeFileName = arg;
            
    print ("Checking for {} in {}".format(bugFileName, landscapeFileName))
    
    bugContent = readFile(bugFileName)
    landscapeContent = readFile(landscapeFileName)

    bf = BugFinder(bugContent)
    print "Found {} matching bugs.".format(bf.countBugs(landscapeContent, False));
    
   
if __name__ == '__main__':
    print("Start application test of DI Melanie Hofmann")
    main(sys.argv[1:])
    pass

