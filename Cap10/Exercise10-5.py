'''
Created on 16 de mai de 2018

@author: Romulo
'''
def is_sorted(list):
    return list == sorted(list)
if __name__ == '__main__':
    print(is_sorted([2, 3, 5, 8, 11]))