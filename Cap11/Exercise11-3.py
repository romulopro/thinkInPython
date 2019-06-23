'''
Created on 14 de jun de 2018

@author: Romulo
'''

ackDict = {}
def ack(m, n):

    if(m == 0):
        return n+1
    elif (m>0 and n==0):
        return ack(m-1, 1)
    if (m, n) in ackDict:
        return ackDict[m, n]
    else:
        ackDict[m, n] = ack(m-1, ack(m, n-1))
        return ackDict[m, n]




if __name__ == '__main__':
    
    print(ack(2,411))
    print(ack(2,413))
    