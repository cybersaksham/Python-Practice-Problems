"""
Take a positive number as input.
Find first number greater than input which is palindrome
"""


def is_palindrome(num):
    return str(num) == str(num)[::-1]


def next_palindrome(num):
    temp = num + 1
    while not is_palindrome(temp):
        temp += 1
    print(f"Next palindrome to {num} is {temp}")


if __name__ == '__main__':
    while True:
        number = input("Enter a positive integer = ")

        try:
            if int(number) > 0:
                next_palindrome(int(number))
            else:
                print("You have entered incorrect number")
        except:
            print("You have entered incorrect number")
