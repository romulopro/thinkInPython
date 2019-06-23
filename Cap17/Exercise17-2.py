'''
Created on 31 de dez de 2018

@author: Romulo
'''

from copy import deepcopy
class Kangaroo:
    
    def __init__(self, name, pouch = []):
        
        self.pouch = pouch
        self.name = name
        
        return None
    
    def put_in_pouch(self, obj):
        self.pouch.append(obj)
        return None

    def __str__(self):
        
        t = [ self.name + ' has pouch contents:' ]
        for obj in self.pouch:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)    
    
def main():
    kanga = Kangaroo("kanga")
    roo = Kangaroo("roo")
    kanga.put_in_pouch('wallet')
    kanga.put_in_pouch('car keys')
    kanga.put_in_pouch(roo)
    print(kanga)
    print(roo)
    return
if __name__ == '__main__':
    main()