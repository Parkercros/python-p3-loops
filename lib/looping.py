#!/usr/bin/env python3
# Write a function happy_new_year() using a while loop that outputs numbers starting at 10
#  and counting down to 1. After reaching 1, print out "Happy New Year!"

def happy_new_year():
    count = 10
    while count >= 1:
        print(count)
        count -= 1
    print("Happy New Year!")


# Write a function square_integers() that takes one argument, 
# a list of integers and returns the list of squared elements.


def square_integers(lst):
    return [num ** 2 for num in lst if isinstance(num, int)]



# Write a function fizzbuzz() that prints the numbers from 1 to 100. 
# For multiples of three, print "Fizz" instead of the number and for 
# the multiples of five print "Buzz". For numbers which are multiples of both three and five, print "FizzBuzz".

def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
