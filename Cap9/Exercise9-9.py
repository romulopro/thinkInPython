'''
Created on 15 de mai de 2018

@author: Romulo
'''
def is_Palindrome_Age(myAge, motherAge):
    #print(str(myAge).zfill(2), str(motherAge)[::-1])
    return str(myAge).zfill(2) == str(motherAge)[::-1]
# differences between ages 
if __name__ == '__main__':
    agesList = []
    diffBetweenAges = 16
    myAge = 1
    myMothersAge = 17
    
    while diffBetweenAges < 81:
        for myAge in range (1,83):
            myMothersAge = myAge + diffBetweenAges
            if is_Palindrome_Age(myAge, myMothersAge):
                agesList.append((myAge, myMothersAge))
            myMothersAge += 1
            if is_Palindrome_Age(myAge, myMothersAge):
              agesList.append((myAge, myMothersAge))
        diffBetweenAges += 1
        if(len(agesList)== 8):
            break
        agesList = []
    print("My age My mothers age")
    for ages in agesList:
        print(ages[0], ages[1])
        
              
          
            
