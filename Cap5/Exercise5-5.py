'''
Created on 20 de mar de 2018

@author: Romulo
'''
def draw(t, length, n):
    if n == 0:
        return None
    angle = 50
    t.fd(length*n)
    t.lt(angle)
    draw(t, length, n-1)
    t.rt(2*angle)
    draw(t, length, n-1)
    t.lt(angle)
    t.bk(length*n)
    return None


if __name__ == '__main__':
    import turtle
    bob = turtle.Turtle()
    draw(bob, 3, 6)