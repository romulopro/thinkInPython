'''
Created on 25 de mai de 2018

@author: Romulo
'''
from bisect import bisect
def in_bisect(list, word):
    #print(word)
    
    #newList = list[:]
    indexOfNewWord = bisect(list, word)
    #print(newList)
    #print(indexOfNewWord, "----", newList[indexOfNewWord - 1], list[indexOfNewWord - 1])
    if list[indexOfNewWord-1] == word:
        return False
    return True
def interlock (word, list):
    for secWord in list:
        if len(word) > 3:
            if (len(secWord) == len(word)):
                res = [''] * len(word) * 2  
                res[::2] = word
                res[1::2] = secWord
                if in_bisect(list, ''.join(res)) is False:
                    print(word, secWord, ''.join(res))
            elif (len(secWord) + 1 == len(word)):
                res = [''] * len(word) * 2  
                res[::2] = word
                res[1:-1:2] = secWord
                if in_bisect(list, ''.join(res)) is False:
                    print(word, secWord, ''.join(res))
            
    return None
def three_interlock(word, list):
    n = 3
    for i in range(n):
        inter = word[i::n]
        if not in_bisect(list, inter):
            print(word, word[0::3], word[1::3], word[2::3])
    return None
    
    
    
if __name__ == '__main__':
    fin = open("words.txt")
    wordList = []
    for line in fin:
        wordList.append(line.strip())
    for word in wordList:
        three_interlock(word, wordList)
    for word in wordList:
        interlock(word, wordList)
        
        