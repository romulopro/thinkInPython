'''
Created on 19 de mai de 2018

@author: Romulo
'''
from bisect import bisect
from builtins import str
def in_bisect(list, word):
    #print(word)
    
    #newList = list[:]
    indexOfNewWord = bisect(list, word)
    #print(newList)
    #print(indexOfNewWord, "----", newList[indexOfNewWord - 1], list[indexOfNewWord - 1])
    if list[indexOfNewWord-1] == word:
        return False
    return True
    
def has_reverse(list, word):
    if in_bisect(list, word[::-1]) is False:
        print(word, word[::-1])
    return
    
if __name__ == '__main__':
    fin = open("words.txt")
    wordList = []
    for line in fin:
        wordList.append(line.strip())
    for word in wordList:
        #print("+++", word, word[::-1])
        has_reverse(wordList, word)