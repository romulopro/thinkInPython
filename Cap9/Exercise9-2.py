'''
Created on 1 de mai de 2018

@author: Romulo
'''
def has_no_e(word):
    if "e" not in word:
        return True
    return False

if __name__ == '__main__':
    fin = open("words.txt")
    wordsThatHasNoLetterE = 0
    totalWords = 0
    for line in fin:
        word = line.strip()
        if has_no_e(word):
            print(word)
            wordsThatHasNoLetterE += 1
        totalWords += 1
    print("%.3f %%" %((wordsThatHasNoLetterE/totalWords)*100))
    