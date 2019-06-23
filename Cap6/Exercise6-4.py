'''
Created on 22 de mar de 2018

@author: Romulo
'''

def is_power(a, b):
    if(a%b != 0):
        return "No"
    else:
        if(a/b == 1):
            return "Yes"
    return is_power(a/b, b)
    



if __name__ == '__main__':
    print(is_power(43046721*81, 9))
    