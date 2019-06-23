'''
Created on 16 de mai de 2018

@author: Romulo
'''
def is_anagram(str1, str2):
    listStr1=sorted(list(str1.lower()))
    listStr2=sorted(list(str2.lower()))
    return listStr1 == listStr2
    

if __name__ == '__main__':
    print(is_anagram('arara', 'raarA'))