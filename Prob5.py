"""
Take a number list as input.
Find first number which is palindrome, greater than items of list only if number is greater then 10
"""


def is_palindrome(num):
    return str(num) == str(num)[::-1]


def next_palindrome(num_list):
    num_list2 = []
    for items in list(num_list):
        if int(items) > 10:
            temp = int(items)
            while not is_palindrome(temp):
                temp += 1
        else:
            temp = int(items)
        num_list2.append(temp)
    print(f"The new list is {num_list2}")


if __name__ == '__main__':
    while True:
        numbers = input("Enter a positive integer's list seperate by space = ")
        num_list = numbers.split(" ")
        print(f"The old list is {num_list}")

        try:
            result = 1
            i = 0
            while i < len(num_list):
                if int(num_list[i]) > 0:
                    result = 0
                else:
                    result = 1
                    break
                i += 1
            if result == 0:
                next_palindrome(num_list)
            else:
                print("You must have to enter positive numbers")
        except:
            print("You must have to enter integers")
