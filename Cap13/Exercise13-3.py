'''
Created on 31 de jul de 2018

@author: Romulo
'''
from collections import OrderedDict

import string
freq_of_words = {}
def print_most_20_words(list_and_quant_of_words):
    num_of_dff_words = len(list_and_quant_of_words)
    #print(num_of_dff_words)
    most_20_freq_words = OrderedDict()
    num_of_words_in_ord_dict = 0
    for x in range (num_of_dff_words, 1, -1):
        for key, value in list_and_quant_of_words.items():
            if x == value:
                most_20_freq_words[key] = value
                num_of_words_in_ord_dict += 1
                if num_of_words_in_ord_dict == 20:
                    break
        if num_of_words_in_ord_dict == 20:
            break
    for key, value in most_20_freq_words.items():
        print(key, value)
        
    return None
               
        
def most_frequent_words(list_of_words):
    for word in list_of_words:
        if word is not "":
            freq_of_words.setdefault(word.lower(), 0)
            freq_of_words[word.lower()] += 1
    return None
    
if __name__ == '__main__':
  fin = open("tale1.txt")
  translate_dict = {} 
  non_letter_caracters = string.punctuation 
  for caracter in non_letter_caracters:
      translate_dict[ord(caracter)] = ""
  translate_dict[ord("\n")] = None
  
  
  
  #print(non_letter_caracters)
  for line in fin:
    line_without_punctuation = line.translate(translate_dict)
    list_of_words = line_without_punctuation.split(" ")
    most_frequent_words(list_of_words)
  print_most_20_words(freq_of_words.copy())