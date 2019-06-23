'''
Created on 15 de jun de 2018

@author: Romulo
'''
import time
'''
start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))'''


phonectDict = {}
def isSamePhonetic(mainWordPhonetic, secondWord):
  phoneticOfAnotherWord = phonectDict.get(secondWord, "Empty")
  if phoneticOfAnotherWord is "Empty":
    return False
  if phoneticOfAnotherWord != mainWordPhonetic:
    return False
  return True

def threeWordsSamePhonetic(word):
  if word[0] == word[1]:
    return
  mainWordPhonetic = phonectDict.get(word, "Empty")
  if mainWordPhonetic is "Empty":
      return
  firstFourLettersWord = word[1:]
  if isSamePhonetic(mainWordPhonetic, firstFourLettersWord):
    secondFourLettersWord = word[0] + word[2:]
    if isSamePhonetic(mainWordPhonetic, secondFourLettersWord):
      print(word, firstFourLettersWord, secondFourLettersWord)
  return None
    

if __name__ == '__main__':
  finPhonetic = open("phonetic.txt")
  #start_time = time.time()  
  for line in finPhonetic:
      #print (line.strip().split("  ", 1))
      strippedLine = line.strip().split("  ", 1)
      phonectDict[strippedLine[0].lower()] = strippedLine[1]
  #print ("Done phase 1")
  finPhonetic.close()
    
    

  fin = open("words.txt")
  for line in fin:
    word = line.strip()
    if len(word) == 5:
      threeWordsSamePhonetic(word)
  fin.close()
  #print("--- %s seconds ---" % (time.time() - start_time))