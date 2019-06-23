'''
Created on 14 de jun de 2018

@author: Romulo
'''
def has_duplicates(list):

    dictDuplicade = {}
    for element in list:
        if  element in dictDuplicade :
            return True
        dictDuplicade[element] = True
    return False
if __name__ == '__main__':
    print(has_duplicates([1, 5, 45, 7, 4]))
