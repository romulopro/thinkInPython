'''
Created on 28 de jun de 2018

@author: Romulo
'''

    
def is_two_letters_swapped(word1, word2):
    swapped_letters = 0
    for letter in range(0, len(word1)):
        if word1[letter] != word2[letter]:
            swapped_letters += 1
    if swapped_letters == 2:
        return True
    else:
        return False
    

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
        if(len(dict_of_anagrams[key]) > 1): #number of words for anagram >= 2
            list_of_words = dict_of_anagrams[key] 
            for x in range(0, len(list_of_words) - 1):
                for y in range(x, len(list_of_words) - 1):
                    if is_two_letters_swapped(list_of_words[x], list_of_words[y + 1]):
                        print(list_of_words[x], list_of_words[y + 1])

                