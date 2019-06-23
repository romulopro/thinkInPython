'''
Created on 20 de mar de 2018

@author: Romulo
'''

import time
if __name__ == '__main__':
    secondsSinceEpoch = int(time.time())
    seconds = secondsSinceEpoch%60
    minutes = int((secondsSinceEpoch - seconds)/60)%60
    hours = int((secondsSinceEpoch - seconds - minutes*60)/3600)%24
    daysSinceEpoch = int(secondsSinceEpoch/86400)
    print(daysSinceEpoch, hours, minutes, seconds)
    