'''
Created on 5 de jun de 2018

@author: Romulo
'''
import time
'''
start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))'''
from bisect import bisect
def in_bisect(dict, word):
    #indexOfNewWord = bisect(list, word)
    
    if word in dict:
        return True
    return False
    
if __name__ == '__main__':
    fin = open("words.txt")
    wordDict = {}
    start_time = time.time()
    for line in fin:
        wordDict[line.strip()] = 0
    print(in_bisect(wordDict, "fish"))
    print("--- %s seconds ---" % (time.time() - start_time))
    