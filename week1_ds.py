# -*- coding: utf-8 -*-
"""week1_ds.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1RhkdXhPEwF5P9348YTUitc0N9LLWl63q

Function to Count Vowels
"""

def count_vowels(word):
    vowels = "aeiouAEIOU"
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    return count

print(count_vowels("elephant"))

"""2. Iterating Through List of Animals and Printing in All Caps"""

animals = ['tiger', 'elephant', 'monkey', 'zebra', 'panther']

for animal in animals:
    print(animal.upper())

# Output:
# TIGER
# ELEPHANT
# MONKEY
# ZEBRA
# PANTHER

"""3. Iterating from 1 to 20 and Printing Odd or Even"""

for i in range(1, 21):
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")

# Output:
# 1 is odd
# 2 is even
# 3 is odd
# ...
# 20 is even

"""4. Function to Sum Two Integers"""

def sum_of_integers(a, b):
    return a + b

# Input from user
a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))

# Example usage:
print("The sum is:", sum_of_integers(a, b))

# Output will vary based on user input

!apt-get install git

!git config --global user.name "SushieeK"
!git config --global user.email "sk10689@nyu.edu"

!git remote add origin git@github.com:SushieeK/Data-Science-Assignments.git
!git branch -M main
!git push -u origin main