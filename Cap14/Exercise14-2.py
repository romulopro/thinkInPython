'''
Created on 1 de nov de 2018

@author: Romulo
'''

from anagram_sets import  all_anagrams, signature
import shelve
from builtins import str


def store_anagrams(file_to_analyze):
    write_data = shelve.open('anagram_dbEX.db', 'c')
    anagram_dict = all_anagrams(file_to_analyze)
    for word, word_list in anagram_dict.items():
        write_data[word] = word_list
    write_data.close()
    return

def read_anagrams(searched_string):
    ordered_searched_string = signature(searched_string)
    
    try:
        read_data = shelve.open('anagram_dbEX.db', 'r')
    except:
        print("Database not found")
        return
    try:
        print(read_data[ordered_searched_string])
        
    except:
        print("[]")
    read_data.close()
    return



def main():
    string_to_search = str(input("Digite a string a ser procurada, ou 2222 para construir database: \n"))
    #print(string_to_search)
    if(string_to_search == '2222'):
        store_anagrams('words.txt')
    else:
        read_anagrams(string_to_search)
    return
if __name__ == '__main__':
    main()