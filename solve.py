#On your computer, in /home/dataset_01/, you have a dataset with lots of text files
#that contains children stories in plain text format (ascii). Files are small in size,
#but the size of the entire dataset is around 1T. You are required to extract all
#unique palindromes from the dataset.

import shutil
from os import listdir, makedirs, walk, getcwd, scandir
from os.path import isfile, join, normpath, relpath


#O(n*m*t); n = numar fisiere; t = numar cuvinte din fisier; m = lungime palindrom

class Solution:

    def __init__(self, path):
        self.folderPath = path
        self.palindromList = []

    #function which checks if a word is a palindrom
    def isPalindrom(self,word):
        wordHalfLen = len(word) // 2
        wordLen = len(word)
        for i in range(0, wordHalfLen):  
            if word[i] != word[wordLen-i-1]: 
                return False
        return True
    #function goes to the bottom of the folders and extracts a list of palindroms
    def getPalindromsFromFolderNames(self,path):
        bottom = True
        foldersList = [f.path for f in scandir(path) if f.is_dir()]
        for folder in foldersList:
            bottom = False
            path = join(path,folder)
            self.getPalindromsFromFolderNames(path)
        if bottom:
            #print(path)
            palindrom = "".join(relpath(path, self.folderPath).split("\\")) 
            self.palindromList.append(palindrom)

    #function returns a list of palindroms
    def getPalindroms(self):
        self.getPalindromsFromFolderNames(self.folderPath)
        return self.palindromList

    #function reads all text files and creates recursive folders with the deepest path representing the name of palindrom
    def findPalindroms(self):
        for f in listdir(self.folderPath):
            filePath = join(self.folderPath, f)
            if isfile(filePath):
                with open(filePath,'r') as textFile:
                    for line in textFile:
                        for word in line.split():
                            if (self.isPalindrom(word)):
                                newPath = join(folderPath,word[0])
                                for i in range(1, len(word)):
                                    newPath = join(newPath,word[i])

                                makedirs(newPath, mode=0o777, exist_ok=True)   
                    
#creez foldere recursiv cu nume cate un caracter pana la length/2


if __name__ == '__main__':
    currentPath = getcwd()
    folderPath = "dataset_01"
    folderPath = join(currentPath,folderPath)
    s = Solution(folderPath)
    s.findPalindroms()
    print(s.getPalindroms())