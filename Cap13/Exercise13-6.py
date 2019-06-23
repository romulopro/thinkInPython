'''
Created on 31 de jul de 2018

@author: Romulo
'''
from collections import OrderedDict

import string
list_of_words_on_tale = []

def print_unknown_words(list_of_words_on_tale, list_of_words_of_dict):
    s = set(list_of_words_on_tale) - set(list_of_words_of_dict)
    for word in s:
        print(word, sep= "/t")
    print(len(s), len(list_of_words_on_tale), len(list_of_words_of_dict))
    return

               
        
def words_on_tale(list_of_words):
    for word in list_of_words:
        if word is not "":
            if word.lower() not in list_of_words_on_tale:
                list_of_words_on_tale.append(word.lower())
    return None
    
if __name__ == '__main__':
  fin = open("tale1.txt")
  translate_dict = {} 
  non_letter_caracters = string.punctuation 
  for caracter in non_letter_caracters:
      translate_dict[ord(caracter)] = ""
  translate_dict[ord("\n")] = None
  
  dict_of_words = open("words.txt")
  list_of_words_of_dict = []
  for word in dict_of_words:
      list_of_words_of_dict.append(word)
  dict_of_words.close()
  
  
  
  #print(non_letter_caracters)
  for line in fin:
    line_without_punctuation = line.translate(translate_dict)
    list_of_words = line_without_punctuation.split(" ")
    words_on_tale(list_of_words)
  fin.close()  
  
  print_unknown_words(list_of_words_on_tale, list_of_words_of_dict)
  
  
  

