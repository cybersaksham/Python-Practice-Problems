"""
Take a & b from user (a < b)
Generate a random number b/w a & b
You & your friend should guess numbers
who guesses correct number in less trials wins the game
"""

import random


def guess(player):
    trial = 0
    c_guess = random.randint(a + 1, b - 1)
    print(f"{player} :-")
    p_guess = int(input(f"Guess a number b/w {a} & {b} = "))
    while True:
        if p_guess > a and p_guess < c_guess:
            trial += 1
            p_guess = int(input("Wrong!!Guess greater = "))
        elif p_guess < b and p_guess > c_guess:
            trial += 1
            p_guess = int(input("Wrong!!Guess smaller = "))
        elif p_guess == c_guess:
            trial += 1
            print(f"Correct!!You guessed in {trial} trials")
            break
        else:
            p_guess = int(input("Guess correct number = "))
    return trial


if __name__ == '__main__':
    p1 = input("Enter player 1's name --> ")
    p2 = input("Enter player 2's name --> ")
    a = int(input("Guess min limit = "))
    b = int(input("Guess max limit = "))

    p1_trial = guess(p1)
    p2_trial = guess(p2)

    if p1_trial > p2_trial:
        print(f"{p2} won the game by {p1_trial - p2_trial} trials")
    elif p1_trial < p2_trial:
        print(f"{p1} won the game by {p2_trial - p1_trial} trials")
    else:
        print("Game tied!!")
