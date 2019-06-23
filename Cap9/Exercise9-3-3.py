'''
Created on 2 de mai de 2018

@author: Romulo
'''
from itertools import  combinations

def avoids(word, forbiddenLetters):
    for forbiddenLetter in forbiddenLetters:
        if forbiddenLetter in word:
            return False
    return True


if __name__ == '__main__':
    totalWords = 0
    allowedWords = 0
    ratioOfForbiddenWords = 1
    wordsOfFile = []
    lessLetters = ""
    forbiddenLettersGenerator = combinations('abcdefghijklmnopqrstuvwxyz', 5)
    fin = open("words.txt")
    for line in fin:
        totalWords += 1
        wordsOfFile.append(line.strip())
    
    while 1:
        forbiddenLetters = (next(forbiddenLettersGenerator))
        for word in wordsOfFile:
            if avoids(word, forbiddenLetters):
                allowedWords += 1
        partialRatioOfForbiddenWords = 1-allowedWords/totalWords
        if partialRatioOfForbiddenWords < ratioOfForbiddenWords:
            ratioOfForbiddenWords = partialRatioOfForbiddenWords
            lessLetters = forbiddenLetters
            print(  "%s : %.3f %%" %(lessLetters, ratioOfForbiddenWords*100))
        allowedWords = 0
        if forbiddenLetters == 'vwxyz':
            break

    
        