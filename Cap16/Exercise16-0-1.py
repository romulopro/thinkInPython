from __future__ import print_function, division
'''
Created on 30 de nov de 2018

@author: Romulo
'''
"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""


from copy import deepcopy


class Time:
    """Represents the time of day.
       
    attributes: hour, minute, second
    """
    




def print_time(t):
    """Prints a string representation of the time.

    t: Time object
    """
    return print("%.2d:%.2d:%.2d" %(t.hour, t.minute, t.second))



def int_to_time(seconds):
    """Makes a new Time object.

    seconds: int seconds since midnight.
    """
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time



def time_to_int(time):
    """Computes the number of seconds since midnight.

    time: Time object.
    """
    return (time.hour*3600 + time.minute*60 + time.second)



def add_times(t1, t2):

    """Adds two time objects.

    t1, t2: Time

    returns: Time
    """
    assert valid_time(t1) and valid_time(t2)
    '''if(not valid_time(t1) or (not valid_time(t2))):
        raise ValueError('invalid Time object in add_time' )
        print('invalid Time object in add_time' )'''
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)
    



def valid_time(time):
    """Checks whether a Time object satisfies the invariants.

    time: Time

    returns: boolean
    """
    if (time.hour < 0 or time.minute < 0 or time.second < 0):
        return False
    if (time.minute >= 60 or time.second >= 60):
        return False
    return True



def is_after(t1, t2):
  absolute_time_t1 = time_to_int(t1)
  absolute_time_t2 = time_to_int(t2)

  return absolute_time_t1 < absolute_time_t2


def increment(time, seconds):
  '''time.second += seconds
  if time.second > 60:
    time.minute += time.second//60
    time.second = time.second%60

  if time.minute > 60:
    time.hour += time.minute//60
    time.minute = time.minute%60'''

  total_seconds = time_to_int(time) + seconds
  return int_to_time(total_seconds)

  return

def pure_version_of_increment(time, seconds):
  new_time = deepcopy(time)
  increment(new_time, seconds)
  return new_time

def mul_time(time1, mult_factor):
  total_seconds = int(mult_factor*time_to_int(time1))
  return(int_to_time(total_seconds))

def time_per_mile(time1,  distance ):
  return(mul_time(time1, 1/distance))
  #intTime = int(1/distance * time_to_int(time1))




  



def main():
  t1 = Time()
  t1.hour = 11
  t1.minute = 59
  t1.second = 55

  t2 = Time()
  t2.hour = 11
  t2.minute = 48
  t2.second = 50
  print(valid_time(t2))
  print(time_to_int(t2))
  print(is_after(t1, t2))
  increment(t2, 0)
  print_time(pure_version_of_increment(t2, 195))
  print_time(t2)
  print_time(mul_time(t2, 4))
  print_time(time_per_mile(t2, 2))
  

  return 
if __name__ == '__main__':
    main()
