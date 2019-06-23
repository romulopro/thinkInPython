'''
Created on 14 de mai de 2018

@author: Romulo
'''
def odometerPuzzle():
    for odometer in range(0, 1000000):
        odometerLastPalidromeNumbers = (str(odometer).rjust(6, "0"))[2:]
        if is_Palindrome(odometerLastPalidromeNumbers):
            odometerLastPalidromeNumbers = (str(odometer+1).rjust(6, "0"))[1:]
            if is_Palindrome(odometerLastPalidromeNumbers):
                odometerLastPalidromeNumbers = (str(odometer+2).rjust(6, "0"))[1:5]
                if is_Palindrome(odometerLastPalidromeNumbers):
                    odometerLastPalidromeNumbers = (str(odometer+3).rjust(6, "0"))
                    if is_Palindrome(odometerLastPalidromeNumbers):
                        print(odometer)
    return None
def is_Palindrome(odometerCaracters):
    if odometerCaracters == odometerCaracters[::-1]:
        return True
    else:
        return False
    
if __name__ == '__main__':
    odometerPuzzle()
    