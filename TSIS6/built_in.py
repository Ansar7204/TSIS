#1
from functools import reduce
import operator
import time
import math

def multiply_list(numbers):
    if not numbers:
        return 0
    return reduce(operator.mul, numbers)


numbers = [1, 2, 3, 4, 5]
result = multiply_list(numbers)
print(f"The result of multiplying all numbers in the list {numbers} is: {result}")



#2

def count_upper_lower(text):
    if not text:
        return 0, 0  
    upper_count = sum(1 for char in text if char.isupper())
    lower_count = sum(1 for char in text if char.islower())

    return upper_count, lower_count


text = input("Enter a string: ")
upper, lower = count_upper_lower(text)
print(f"Number of upper case letters: {upper}")
print(f"Number of lower case letters: {lower}")

#3

def is_palindrome(s):
    s = s.replace(" ", "").lower()
    reversed_s = s[::-1]
    return s == reversed_s
print(is_palindrome("abba"))


#4

def calculate_square_root(number, milliseconds):
    time.sleep(milliseconds / 1000)  # Convert milliseconds to seconds
    result = math.sqrt(number)
    print(f"Square root of {number} after {milliseconds} milliseconds is {result}")

number = int(input("Enter the number to calculate square root: "))
milliseconds = int(input("Enter the delay in milliseconds: "))
calculate_square_root(number, milliseconds)


#5

def all_true(t):
    return all(t)


tuple1 = (True, True, True)
tuple2 = (True, False, True)
tuple3 = ()
print(all_true(tuple1))  # Output: True
print(all_true(tuple2))  # Output: False
print(all_true(tuple3))  # Output: True 
