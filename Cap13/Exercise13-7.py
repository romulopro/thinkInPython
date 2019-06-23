'''
Created on 30 de ago de 2018

@author: Romulo
'''
import string
from random import randint
from bisect import bisect
import time

freq_of_words = {}

def in_bisect(list, index):
    indexOfNewWord = bisect(list, index)
    
    return indexOfNewWord - 1

def cumsum(lista): 
    #input : a list
    #output : a list
    listOfCumulativeSum = []
    result = 0
    for item in lista:
        result += item
        listOfCumulativeSum.append(result)
    return listOfCumulativeSum

def choose_from_hist(list_of_hist):
    hist_dict = {}
    for item in list_of_hist:
        if item not in hist_dict:
            hist_dict[item] = 1
        else:
            hist_dict[item] += 1
    probly_dict = {}
    total_items = len(list_of_hist)
    for key, value in hist_dict.items():
        probly_dict[key] = str(value) + "/" + str(total_items)
    return(probly_dict)

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
  fin.close()
  most_frequent_words(list_of_words)
  words_of_book = list(freq_of_words.keys())
  cum_sum_list = cumsum(freq_of_words.values())
  for _ in range(100):
    random_number_of_wordtale = randint(1, cum_sum_list[-1])
    num_of_index = in_bisect(cum_sum_list, random_number_of_wordtale)
    print(words_of_book[num_of_index], end=" ")
  