from random import choice
from time import time
from math import ceil
from termcolor import colored

print(" " * 2)

time_start = time()
correct_answers = 0
loop_end = 0

with open('words.txt', 'r', encoding='utf-8') as f:
    words = [line.strip() for line in f]

while time() < time_start + 60:
    remaining_time = time_start - time() + 60

    word = choice(words)  # draws the word

    if remaining_time > 5:
        print("Zostało ci " + str(ceil(remaining_time)) + " sekund!")
        print(word)
    else:
        print(colored("Zostało ci " + str(ceil(remaining_time)) + " sekund!", 'red'))
        print(word)

    answer = input("Przepisz powyższe wyrazy: ")
    words.remove(word)  # deleting used words
    loop_end += 1

    if word == answer:  # checking answer
        correct_answers += 1

WPM = correct_answers / 60 * 100
WPM = ceil(WPM)

print(" ")
print("WPM wynosi " + str(WPM))
