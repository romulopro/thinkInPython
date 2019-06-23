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
    lettersAndRatio = []
    wordsOfFile = []
    lessLetters = ""
    fin = open("words.txt")
    for line in fin:
        totalWords += 1
        wordsOfFile.append(line.strip())
    for forbiddenLetter in "abcdefghijklmnopqrstuvwxyz" :
        for word in wordsOfFile:
            if avoids(word, forbiddenLetter):
                allowedWords += 1
        partialRatioOfForbiddenWords = 1 - allowedWords / totalWords
        if partialRatioOfForbiddenWords < ratioOfForbiddenWords:
            ratioOfForbiddenWords = partialRatioOfForbiddenWords
            lessLetters = forbiddenLetter
        lettersAndRatio.append((forbiddenLetter, partialRatioOfForbiddenWords * 100))
        allowedWords = 0
    lettersAndRatio = sorted(lettersAndRatio, key=lambda x : x[1])[:5]
    lessCommonLetters = "".join([x[0] for x in lettersAndRatio])
    print (lessCommonLetters)
    for word in wordsOfFile:
        if avoids(word, lessCommonLetters):
            allowedWords += 1
    partialRatioOfForbiddenWords = 1 - allowedWords / totalWords
    print("%s : %.3f %%" % (lessCommonLetters, partialRatioOfForbiddenWords * 100))
    
    
