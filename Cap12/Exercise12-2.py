'''
Created on 23 de jun de 2018

@author: Romulo
'''
from collections import OrderedDict

def biggest_to_smallest_anagram(dictionary):
    ordered_anagram_dict = OrderedDict()
    longest_list = len_of_longest_list_of_words_for_a_anagram(dictionary)
    for x in range(longest_list, 0, -1):
            for key in dictionary:
                if(len(dictionary[key]) == x):
                    #print(dictionary[key])
                    ordered_anagram_dict[key] = dictionary[key]
                    
    return ordered_anagram_dict
    

def len_of_longest_list_of_words_for_a_anagram(dictionary):
    longest_list = 0
    for key in dictionary:
        if (len(dictionary[key]) > longest_list):
            longest_list = len(dictionary[key])
    
    return longest_list

def print_anagram_of_x_words(dictionary, num_of_letters):
    longest_list = len_of_longest_list_of_words_for_a_anagram(dictionary)
    for x in range(longest_list, 0, -1):
        for key in dictionary:
            if(len(key) == num_of_letters):
                if(len(dictionary[key]) == x):
                    print(dictionary[key])
                    return None           
    return None

if __name__ == '__main__':

  fin = open("words.txt")
  dict_of_anagrams ={}
  for line in fin:
    word = line.strip()
    ordered_tuple_of_word = tuple(sorted(list(word)))
    if ordered_tuple_of_word not in dict_of_anagrams:
        dict_of_anagrams[ordered_tuple_of_word] = [word]
    else:
        (dict_of_anagrams[ordered_tuple_of_word]).append(word)
  fin.close()
  for key in dict_of_anagrams:
      if(len(dict_of_anagrams[key]) > 1):
          print(dict_of_anagrams[key])
'----Part two-----'
'print the anagram with most words in decrescent order'
  

big_to_small_anagrams = biggest_to_smallest_anagram(dict_of_anagrams)
for key in big_to_small_anagrams:
    print(big_to_small_anagrams[key])

'----part three----'
print_anagram_of_x_words(dict_of_anagrams, 8)
  
 
    
          