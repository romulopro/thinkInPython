'''
Created on 5 de mai de 2018

@author: Romulo
'''
def uses_only(word, allowedLetters):
    for letter in word:
        if letter not in allowedLetters:
            if letter != " ":
                return False
    return True


if __name__ == '__main__':
    print(uses_only("hoe alfafa", "acefhlo"))
    