'''
Created on 1 de mai de 2018

@author: Romulo
'''
def is_palindrome(word):
    return word == word[::-1]
    
if __name__ == '__main__':
    print(is_palindrome("arara"))
    