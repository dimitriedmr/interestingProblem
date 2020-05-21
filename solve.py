#On your computer, in /home/dataset_01/, you have a dataset with lots of text files
#that contains children stories in plain text format (ascii). Files are small in size,
#but the size of the entire dataset is around 1T. You are required to extract all
#unique palindromes from the dataset.

import os
from pathlib import Path
#abccba
#6/2=3


def isPalindrom(word):
    halfLen = word.length // 2
    len = word.length 
    for (i = 0; word[i] == word[len-i], i < halfLen;++i)
    {
    }
    return i == halfLen
    
def getPalindroms(currentPath,listaPalindroms):
        
    for x,nume,y in os.walk(currentPath):
        listaPalindroms.append()
        currentPath = os.path.join(currentPath,nume)
        getPalindroms(currentPath)
#a
#b
#c
#O(n*m*t); n = numar fisiere; t = numar cuvinte din fisier; m = lungime palindrom /2
folderPath = "/home/dataset_01/"
for fisier in os.listdir(folderPath):
    with open(fisier,'r') as f:
        for line in f:
            for word in f.split():
                if (isPalindrom(word)):
                    for ch in word:
                        folderPath = os.path.join(folderPath,ch) #?
                        Path(folderPath),mkdir(parents=True, exist_ok=True)   
                        #folder/a/b/c
                    
#creez foldere recursiv cu nume cate un caracter pana la length/2
