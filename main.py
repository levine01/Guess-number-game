

import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess =int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('sorry, bettr luck next time. Too low')
        elif guess > random_number:
            print('sorry, try again! Too high')
            
    print(f'hurray congrats.You got it right{random_number}')

guess(10)