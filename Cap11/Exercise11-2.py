'''
Created on 9 de jun de 2018

@author: Romulo
'''
def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        inverse.setdefault(val, []).append(key)
    return inverse

def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d
if __name__ == '__main__':
    h = histogram("xbrontosaurusxxx")
    h = invert_dict(h)
    print(h)
     
    
