'''
Created on 10 de jun de 2018

@author: Romulo
'''

if __name__ == '__main__':
    fin = open("words.txt")
    for line in fin:
        word = line.strip()
        if len(word) == 10:
            if word[1].lower() == "e" and word[4:].lower() == "icista":
                print(word)
