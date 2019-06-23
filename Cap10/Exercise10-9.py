'''
Created on 17 de mai de 2018

@author: Romulo
'''
import time
'''
start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))'''
if __name__ == '__main__':
    fin = open("words.txt")
    listOfWords1 = []
    start_time = time.time()
    for line in fin:
        listOfWords1 = listOfWords1 + [line.strip()]
    print("--- %s seconds ---" % (time.time() - start_time))
    fin.close()
    listOfWords2 = []
    start_time = time.time()
    fin = open("words.txt")
    for line in fin:
        listOfWords2.append(line.strip())
    print("--- %s seconds ---" % (time.time() - start_time))
    fin.close()