'''
Created on 8 de mai de 2018

@author: Romulo
'''
def three_consecutive_pairs(word):
    flag = 0
    numOfConsecutivePairs = 0
    #print(len(word))
    for x in range(0,(len(word)-1)):
        #print(word[x], x)
        if(word[x] == word[x+1] and flag == 0):
            flag = 1
            numOfConsecutivePairs += 1
        elif(flag == 1):
            flag = 0
        elif(numOfConsecutivePairs == 3):
            break
        else:
            flag = 0
            numOfConsecutivePairs = 0
    if(numOfConsecutivePairs == 3):
        return word
    return None
            
        
    
if __name__ == '__main__':
    fin = open("words.txt")
    for line in fin:
        word = line.strip()
    #word = "aabbcc"
        if three_consecutive_pairs(word) != None:
            print(word)
    fin.close()
            
        