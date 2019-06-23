'''
Created on 21 de mar de 2018

@author: Romulo
'''

import turtle

def koch(t, length):
    if (length<15):
        t.fd(length)
        return None
    koch(t, length/3)
    t.lt(60)
    koch(t, length/3)
    t.rt(120)
    koch(t, length/3)
    t.lt(60)
    koch(t, length/3)
    
    return None

def snowflake(t, length):
    for _ in range(3):
        koch(t, length)
        t.rt(120)
    return None


if __name__ == '__main__':
    bob = turtle.Turtle()
    
    snowflake(bob, 330)
    turtle.mainloop()
    
    