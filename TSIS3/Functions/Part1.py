from itertools import permutations
import math
import random


def grams_to_ounces(grams):
    return 28.3495231 * grams


def fahrenheit_to_celsius(fahrenheit): 
    return (5 / 9) * (fahrenheit - 32)

def solve(numheads, numlegs):
    for num_chickens in range(numheads + 1):
        num_rabbits = numheads - num_chickens
        if (2 * num_chickens) + (4 * num_rabbits) == numlegs:
            return "Chickens:" + str(num_chickens), "Rabbits:" + str(num_rabbits)
    return "No solution"

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def filter_prime(numbers):
    result = []
    for i in numbers:
        if(is_prime(i)):
            result.append(i)
    return result        
    

def print_permutations():
    input_string = input("Enter a string: ")
    perms = permutations(input_string)
    for perm in perms:
        print(perm)




def reverse_sentence():
    input_string = input("Enter a sentence: ")
    words = input_string.split()
    reversed_words = reversed(words)
    reversed_sentence = ' '.join(reversed_words)

    return reversed_sentence







def has_adjacent_3(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

def spy_game(nums):
    target = "007"
    index = 0
    for i in nums:
        if(i == target[index]):
            index += 1
        if(index == 3):
            break
    if(index == 3):
        return True
    else:
        return False
    

def sphere_volume(radius):
    volume = (4/3) * math.pi * (radius ** 3)
    return volume


def unique_elements(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

def is_palindrome(word):
    word = word.replace(" ", "").lower()
    return word == word[::-1]


def histogram(numbers):
    for num in numbers:
        print('*' * num)
        

def guess_the_number():
    target_number = random.randint(1, 20)
    name = input("Hello what is your name?")
    print("Well " + name + " I am thinking number between 1 and 20.")
    counter = 1
    
    while True:
        guess = int(input("Guess the number (between 1 and 20): "))
        if guess == target_number:
            print("Congratulations! You guessed the number in " + str(counter) + " guesses!")
            break  
        elif guess < target_number:
            print("Too low! Try again.")
            counter += 1
        else:
            print("Too high! Try again.")
            counter += 1