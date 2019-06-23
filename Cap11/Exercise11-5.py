'''
Created on 14 de jun de 2018

@author: Romulo
'''
from bisect import bisect
def in_bisect(list, word):
    #print(word)
    
    #newList = list[:]
    indexOfNewWord = bisect(list, word)
    #print(newList)
    #print(indexOfNewWord, "----", newList[indexOfNewWord - 1], list[indexOfNewWord - 1])
    if list[indexOfNewWord-1] != word:
        return False
    return True

def rotate_word(word, numOfRotation):
    rotatedWord= []
    for letter in word:
        if((ord(letter) + numOfRotation) > 122):
           rotatedWord.append(chr(ord(letter) + numOfRotation - 26))
        else:
            rotatedWord.append(chr(ord(letter) + numOfRotation))
    return "".join(rotatedWord).lower()


if __name__ == '__main__':
    fin = open("words.txt")
    wordlist = []
    for line in fin:
        word = line.strip()
        wordlist.append(word)
    for word in wordlist:
        for x in range(1,26):
            if in_bisect(wordlist, rotate_word(word, x)):
                print(word, rotate_word(word, x))
    fin.close()