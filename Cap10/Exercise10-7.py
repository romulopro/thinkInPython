'''
Created on 16 de mai de 2018

@author: Romulo
'''
def has_duplicates(list):
    tempList = list[:]
    return len(set(tempList)) == len(list)
if __name__ == '__main__':
    print(has_duplicates([1, 5, 5, 7, 4]))
    
            
            
    