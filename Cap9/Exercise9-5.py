'''
Created on 8 de mai de 2018

@author: Romulo
'''
def uses_all(word, letters):
    listOfletters = list(map(str, letters))
    for letter in word:
        if letter in listOfletters:
            listOfletters.remove(letter)
    if len(listOfletters) == 0:
        return True
    else:
        return False
    

def uses_all(word, letters):
    listOfletters = list(map(str, letters))
    for letter in word:
        if letter in listOfletters:
            listOfletters.remove(letter)
    if len(listOfletters) == 0:
        return True
    else:
        return False
    
    

if __name__ == '__main__':
    print(uses_all("aehoooooo", "aeo"))