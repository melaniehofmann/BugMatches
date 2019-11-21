'''
Created on 17.09.2019

@author: mhofmann
'''

class BugFinder():
    '''
    Counts bug matches in a text file.
    '''


    def __init__(self, bug):
        self.bug = bug
        
    def countBugs(self, landscape, ignoreWhitespaces = True):
        """ Returns the counted bug matches in the given landscape 2-D string.
        
        Keyword arguments:
        landscape -- the text to search for bugs as a 2-D string
        ignoreWhitespaces -- if set to true whitespaces inside the bug pattern will be ignored 
        (replacing them with a different char is possible) (default True)
        """
        bugCount = 0;
        
        for y, landscapeLine in enumerate(landscape):
            for x, landscapeChar in enumerate(landscapeLine):
                if(landscapeChar is self.bug[0][0]):
                    # if first char of the bug pattern matches the current landscape char, check if whole pattern matches.
                    if self.__matchesPattern(landscape, x, y, ignoreWhitespaces):
                        bugCount += 1
        
        return bugCount
    
    def __matchesPattern(self, landscape, startX, startY, ignoreWhitespaces):
        """ Checks if next characters of landscape is matching the bug pattern.
        Keyword arguments:
        
        landscape -- the text to search for bugs as a 2-D string
        startX -- the landscapes x position (char) of the first bug pattern char match
        startY -- the landscapes y position (line) of the first bug pattern char match
        ignoreWhitespaces -- if set to true whitespaces inside the bug pattern will be ignored
        """
        for y, bugLine in enumerate(self.bug):
            for x, bugChar in enumerate(bugLine):
                if ignoreWhitespaces and bugChar.isspace():
                    continue
                try: 
                    checkedLandscapeChar = landscape[startY + y][startX + x];
                    if checkedLandscapeChar is not bugChar:
                        return False
                except:
                    # array index out of bounds for landscape, end of string to match is reached
                    return False
        return True;