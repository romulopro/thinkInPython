'''
Created on 31 de jul de 2018

@author: Romulo
'''
import string
freq_of_words = {}
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
  print(len(freq_of_words))
