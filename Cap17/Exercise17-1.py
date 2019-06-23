"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division


class Time:
    """Represents the time of day.
       
    attributes: hour, minute, second
    """
    def __init__(self, hour=0, minute=0, second=0):
        """Initializes a time object.

        hour: int
        minute: int
        second: int or float
        
        
        """
        self.seconds_since_midnigth = self.time_to_int(hour, minute, second)


    def __str__(self):
        """Returns a string representation of the time."""
        return '%.2d:%.2d:%.2d' % (int_to_time(self.seconds_since_midnigth))

    def print_time(self):
        """Prints a string representation of the time."""
        print(str(self))

    def time_to_int(self, hour, minutes, seconds):
        """Computes the number of seconds since midnight."""
        minutes = hour * 60 + minutes
        seconds = minutes * 60 + seconds
        return seconds

    def is_after(self, other):
        """Returns True if t1 is after t2; false otherwise."""
        return self.seconds_since_midnigth > other.seconds_since_midnigth

    def __add__(self, other):
        """Adds two Time objects or a Time object and a number.

        other: Time object or number of seconds
        """
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    def __radd__(self, other):
        """Adds two Time objects or a Time object and a number."""
        return self.__add__(other)

    def add_time(self, other):
        """Adds two time objects."""
        new_time = Time()
        new_time.seconds_since_midnigth = self.seconds_since_midnigth + other.seconds_since_midnigth
        return new_time

    def increment(self, seconds):
        """Returns a new Time that is the sum of this time and seconds."""
        new_time = Time()
        new_time.seconds_since_midnigth = self.seconds_since_midnigth + seconds
        return new_time

    def is_valid(self, hour, minute, second):
        """Checks whether a Time object satisfies the invariants."""
        if hour < 0 or minute < 0 or second < 0:
            return False
        if minute >= 60 or second >= 60:
            return False
        return True


def int_to_time(seconds_since_midnigth):
    """Makes a new Time object.

    seconds: int seconds since midnight.
    """
    minutes, second = divmod(seconds_since_midnigth, 60)
    hour, minute = divmod(minutes, 60)
    
    return hour, minute, second


def main():
    start = Time(9, 45, 0)
    start.print_time()

    end = start.increment(1337)
    #end = start.increment(1337, 460)
    end.print_time()

    print('Is end after start?')
    print(end.is_after(start))

    print('Using __str__')
    print(start, end)

    start = Time(9, 45)
    duration = Time(1, 35)
    print(start + duration)
    print(start + 1337)
    print(1337 + start)

    print('Example of polymorphism')
    t1 = Time(7, 43)
    t2 = Time(7, 41)
    t3 = Time(7, 37)
    total = sum([t1, t2, t3])
    print(total)


if __name__ == '__main__':
    main()