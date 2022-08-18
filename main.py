from random import choice
from time import time
from math import ceil

words = ["kokos", "Nairobi", "cytryna", "Jowisz", "Adam",
         "Afryka", "Polska", "banan", "Ateny", "Barbara",
         "Azja", "gość", "zły", "szczęśliwy", "marynarz",
         "wściekły", "przyjaciel", "pies", "żółw", "zupa",
         "statek", "Argentyna", "kowal", "rymarz", "rynek",
         "wóz", "Andrzej", "kochany", "idealny", "zielony",
         "jest", "tak", "nie", "dlaczego", "lub", "wschód",
         "Europa", "Niemcy", "karabin", "granat", "czerwony",
         "mango", "Francja", "limonka", "Mars", "Mateusz",
         "gruz", "przyczepa", "Barbados", "Warszawa", "Moskwa",
         "Benin", "start", "koniec", "książka", "bosman",
         "głupi", "mądry", "lód", "śnieg", "co",
         "twarz", "jelita", "noga", "skóra", "krupier",
         "kasyno", "neon", "prezydent", "jadalny", "las",
         "lis", "samolot", "lotnisko", "wiatr", "fale", "kosmos",
         "Belize", "dzięcioł", "trzcina", "łopata", "telefon"]

print(" " * 2)

time_start = time()
correct_answers = 0
loop_end = 0


while time() < time_start + 60:
    remaining_time = time_start - time() + 60

    word = choice(words)  # draws the word
    print("Zostało ci " + str(ceil(remaining_time)) + " sekund!")
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
