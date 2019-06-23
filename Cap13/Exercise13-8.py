'''
Created on 31 de ago de 2018

@author: Romulo

'''
from __future__ import print_function, division

import string

import random

from bisect import bisect
from structshape import structshape
#from rosaPesquisa import word


def moving_window(n, iterable):
  start, stop = 0, n
  while stop <= len(iterable):
      yield iterable[start:stop]
      start += 1
      stop += 1
      
def process_file(filename, skip_header):
    """Makes a histogram that contains the words from a file.

    filename: string
    skip_header: boolean, whether to skip the Gutenberg header
   
    returns: map from each word to the number of times it appears.
    """
    list_of_words = []
    fp = open(filename, encoding='utf-8')

    if skip_header:
        skip_gutenberg_header(fp)

    for line in fp:
        process_line(line, list_of_words)

    return list_of_words


def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.

    fp: open file object
    """
    for line in fp:
        if line.startswith('SINGULARIDADES'):
            break


def process_line(line, list_of_words):
    """Adds the words in the line to the histogram.

    Modifies list_of_words.

    line: string
    list_of_words: histogram (map from word to frequency)
    """
    # TODO: rewrite using Counter

    # replace hyphens with spaces before splitting
    line = line.replace('-', ' ')
    strippables =   string.whitespace + '_'
    
    for word in line.split():
        # remove punctuation and convert to lowercase
        word = word.strip(strippables)
        word = word.lower()

        # update the histogram
        list_of_words.append(word)
        
def markov_analisys_from_a_list(word_list, prefix_length):
    """
    receives a list and do a markov analisys
    input: list of words(list), prefix_lenght(int, min = 2)
    return dict"""
    markov_dict = {}
    total_words_in_tale = len(word_list)
    for x in range (prefix_length, total_words_in_tale - prefix_length -1):
        word = list_of_words[x + prefix_length]
        markov_dict.setdefault(tuple(list_of_words[x:x+prefix_length]), [])
        if word not in markov_dict[tuple(list_of_words[x:x+prefix_length])]:
            markov_dict[tuple(list_of_words[x:x+prefix_length])].append(word)
    return markov_dict

def print_new_setences(markov_dict, num_of_lines, num_of_words_per_line):
    
    key_of_dict = random.choice(list(markov_dict))
    line_to_print = " ".join(key_of_dict)
    for _ in range(num_of_lines):
        line_to_print = ""
        for _ in range (num_of_words_per_line):
            num_of_words_of_the_value = len(markov_dict[key_of_dict])
            word_of_list_of_values = markov_dict[key_of_dict][random.randint(0,num_of_words_of_the_value - 1)]
            line_to_print = line_to_print + " " + word_of_list_of_values
            key_of_dict = (key_of_dict[1], word_of_list_of_values)
        print(line_to_print)
            
    return

if __name__ == '__main__':       
    list_of_words = process_file('1984 - George Orwell.txt', skip_header=False)
    list_of_words += process_file('1989 O Ano Que Mudou o Mundo - Michael Meyer.txt', skip_header=False)
    markov_dict = markov_analisys_from_a_list(list_of_words, prefix_length = 2)
    num_of_lines = 13
    num_of_words_per_line = 25
    print_new_setences(markov_dict, num_of_lines, num_of_words_per_line)
    
        
 
    
    
        
    
    


