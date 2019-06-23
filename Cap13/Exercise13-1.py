'''
Created on 31 de jul de 2018

@author: Romulo
'''
import string

if __name__ == '__main__':
  fin = open("tale1.txt")
  translate_dict = {} 
  non_letter_caracters = string.punctuation 
  for caracter in non_letter_caracters:
      translate_dict[ord(caracter)] = ""
  translate_dict[ord("\n")] = None
  
  
  
  print(non_letter_caracters)
  for line in fin:
    line_without_punctuation = line.translate(translate_dict)
    list_of_words = line_without_punctuation.split(" ")
    for word in list_of_words:
        if word is not "":
            print(word.lower())