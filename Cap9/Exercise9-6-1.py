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
    numOfWords = 0
    abecedarianwords = 0
    allowedWords = 0
    fin = open("words.txt")
    letters = str(input("Digit needed letters: \n"))
    for line in fin:
        word = line.strip()
        numOfWords += 1
        if is_abecedarian(word):
            abecedarianwords += 1
        if uses_all(word, letters):
            allowedWords +=1
    print("abecedariam words are %d of %d" %(abecedarianwords, numOfWords))
    print("allowed words are %d of %d" %(allowedWords, numOfWords))
    fin.close()
    
        