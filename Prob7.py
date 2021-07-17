"""
Rohan makes a function to print multiplication table of a number.
But he intentionally make a random number incorrect.
You cannot tolerate this so you made a function.
You finds the wrong value in table & then correct this.
"""

import random


def rohanTable(num):
    table = []
    for i in range(10):
        table.append(num * (i + 1))
    error_index = random.randint(1, 8)
    while table[error_index] == num * (error_index + 1):
        error = random.randint(num * (error_index) + 1, num * (error_index + 2) - 1)
        table[error_index] = error

    return table


def correct(table, num):
    i = 0
    while i < 10:
        if table[i] != num * (i + 1):
            print(f"Rohan mistakes at index no {i}")
            print(f"According to him value is {table[i]}")
            table[i] = num * (i + 1)
            print(f"But correct value is {table[i]}")
            break
        else:
            i += 1
            continue


if __name__ == '__main__':
    number = int(input("Enter a number to make multiplication table = "))
    table = rohanTable(number)
    print(f"The multiplication table of {number} is :-\n{table}")
    correct(table, number)
