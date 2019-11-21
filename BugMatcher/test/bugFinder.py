'''
Created on 17.09.2019

@author: mhofmann
'''
import unittest
import os
from bugMatcher.bugFinder import BugFinder
from bugMatcher.file.fileImport import readFile


class Test(unittest.TestCase):


    def testDefaultLandscape(self):
        self._assertBugMatcher("resources/bug.txt", "resources/landscape.txt", 3)
        pass

    def testDefaultLandscape2(self):
        self._assertBugMatcher("resources/bug.txt", "resources/landscape2.txt", 4)
        pass
    
    def testDefaultLandscape3(self):
        self._assertBugMatcher("resources/bug.txt", "resources/landscape3.txt", 4)
        pass
    
    def testDefaultLandscape4(self):
        self._assertBugMatcher("resources/bug.txt", "resources/landscape4.txt", 0)
        pass
    
    def testDefaultLandscape5_NotIgnoringWhitespaces(self):
        self._assertBugMatcher("resources/bug.txt", "resources/landscape5.txt", 2, False)
        pass
    
    def testDefaultLandscape5_IgnoreWhitespaces(self):
        self._assertBugMatcher("resources/bug.txt", "resources/landscape5.txt", 3, True)
        pass
    
    def testDefaultLandscape6(self):
        self._assertBugMatcher("resources/bug.txt", "resources/landscape6.txt", 4)
        pass
    
    def _assertBugMatcher(self, bugFile, landscapeFile, expectedMatches, ignoreWhiteSpaces = True):
        # Given -b resources/bug.txt -l test/resources/landscape.txt
        
        bugFile = os.path.join(os.path.dirname(__file__), bugFile)
        landscapeFile = os.path.join(os.path.dirname(__file__), landscapeFile)

        bugContent = readFile(bugFile)
        landscape = readFile(landscapeFile)
        
        # When
        bugFinder = BugFinder(bugContent);
        
        # Then
        result = bugFinder.countBugs(landscape, ignoreWhiteSpaces)
        self.assertIs(expectedMatches, result, "Bugs went unnoticed. Expected {} but was {}.".format(expectedMatches, result))
        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testDefaultLandscape']
    unittest.main()