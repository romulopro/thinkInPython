'''
Created on 8 de mai de 2018

@author: Romulo
'''
def is_abecedarian(word):
    wordInLowercase = word.lower()
    asciiLetterCode = 0
    for letter in wordInLowercase:
        if ord(letter) >= asciiLetterCode:
            asciiLetterCode = ord(letter)
        else:
            return False
    return True
            
    
if __name__ == '__main__':
    print(is_abecedarian("aeiou"))