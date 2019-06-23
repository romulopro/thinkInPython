'''
Created on 1 de mai de 2018

@author: Romulo
'''

if __name__ == '__main__':
    fin = open("words.txt")
    for line in fin:
        word = line.strip()
        if (len(word) > 20):
            print(word)
