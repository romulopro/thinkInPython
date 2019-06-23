'''
Created on 1 de mai de 2018

@author: Romulo
'''
def rotate_word(word, numOfRotation):
    rotatedWord= []
    for letter in word:
        rotatedWord.append(chr(ord(letter) + numOfRotation))
    return "".join(rotatedWord)
if __name__ == '__main__':
    print(rotate_word("IBM", -1))
