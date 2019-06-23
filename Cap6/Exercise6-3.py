'''
Created on 22 de mar de 2018

@author: Romulo
'''

def first(word):
    return word[0]
def last(word):
    return word[-1]
def middle(word):
    return word[1:-1]

def is_palindrome(word):
    if(len(word)<2):
        return "No"
    originalWord = word[-1::-1]
    if (originalWord.lower() == word.lower()):
        return "Yes"
    return "No"

    
    



if __name__ == '__main__':
    print(is_palindrome("A7rara"))