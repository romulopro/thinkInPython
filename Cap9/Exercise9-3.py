'''
Created on 4 de mai de 2018

@author: Romulo
'''
def avoids(word, forbiddenLetters):
    for forbiddenLetter in forbiddenLetters:
        if forbiddenLetter in word:
            return False
    return True


if __name__ == '__main__':
    totalWords = 0
    allowedWords = 0
    ratioOfForbiddenWords = 1
    fin = open("words.txt")
    forbiddenLetters = str(input())
    for line in fin:
        totalWords += 1
        word = line.strip()
        if avoids(word, forbiddenLetters): #return False if word contains at least one of forbiddenLetters
            allowedWords += 1
    print(  "%s : %d words allowed of %d" %(forbiddenLetters, allowedWords, totalWords))
        