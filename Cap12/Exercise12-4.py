'''
Created on 16 de jul de 2018

@author: Romulo
'''

if __name__ == '__main__':
    fin = open("words.txt")
    dict_of_anagrams = {}
    for line in fin:
        word = line.strip()
        ordered_tuple_of_word = tuple(sorted(list(word)))
        if ordered_tuple_of_word not in dict_of_anagrams:
            dict_of_anagrams[ordered_tuple_of_word] = [word]
        else:
            (dict_of_anagrams[ordered_tuple_of_word]).append(word)
    fin.close()
    
    for key in dict_of_anagrams:
        letters_of_word = key
        
        print(key)
