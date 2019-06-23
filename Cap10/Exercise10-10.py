'''
Created on 17 de mai de 2018

@author: Romulo
'''
'''
start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))'''
from bisect import bisect
import time
def in_bisect(list, word):
    indexOfNewWord = bisect(list, word)
    
    if list[indexOfNewWord - 1] == word:
        return False
    return True
    
if __name__ == '__main__':
    fin = open("words.txt")
    wordList = []
    start_time = time.time()
    for line in fin:
        wordList.append(line.strip())
    print(in_bisect(wordList, "abba"))
    print("--- %s seconds ---" % (time.time() - start_time))
    