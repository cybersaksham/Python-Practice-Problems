"""
Take a list from user & reverse it using following methods : -
1. By inbuilt method of ptthon
2. By list[::-1]
3. By swapping first element by last & so on

If all 3 methods return same list then print it.
"""


def rev_inbuilt(menu):
    list(menu).reverse()
    return menu


def rev_colons(menu):
    rev = menu[::-1]
    return rev


def rev_swap(menu):
    for i in range(len(menu) // 2):
        menu[i], menu[len(menu) - 1 - i] = menu[len(menu) - 1 - i], menu[i]
    return menu


if __name__ == '__main__':
    menu_inp = input("Enter items of list seperated by space = ")
    menu = menu_inp.split(" ")
    print(menu)
    print(type(menu))
    rev1 = rev_inbuilt(menu)
    rev2 = rev_colons(menu)
    rev3 = rev_swap(menu)
    print(rev1)
    print(rev2)
    print(rev3)
