"""
Make jumbled names.
Take some names as input.
Then interchange their surnames to make fun.
"""

import random

if __name__ == '__main__':
    names = input("Enter names seperated by *\n")
    name_list = names.split("*")
    name_split = [items.split(" ") for items in name_list]
    f_names = [name_split[items][0] for items in range(len(name_split))]
    l_names = [name_split[items][1] for items in range(len(name_split))]
    print(name_list)
    print(name_split)
    print(f_names)
    print(l_names)

    for i in range(len(l_names) - 1):
        choice = random.randint(i + 1, len(l_names) - 1)
        l_names[i], l_names[choice] = l_names[choice], l_names[i]

    jumb_names = list(zip(f_names, l_names))
    print("Jumbled names are :-")
    for i in range(len(jumb_names)):
        print(f"{jumb_names[i][0]} {jumb_names[i][1]}")
