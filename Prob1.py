"""
Take age or year of birth as input from user.
Tell them when they will turn 100 yeras old.
Do not use any module.
They can then optionally provide a year & program must tell their age in that particular year.
You must handle all errors.
"""

while True:
    user = int(input("Enter your age or Year of Birth = "))
    if user > 0 and user < 100:
        year100 = 2021 - user + 100
        print(f"You will turn 100 in {year100}")
    elif user > 1920 and user < 2021:
        year100 = user + 100
        print(f"You will turn 100 in {year100}")
    else:
        print("It seems that you entered incorrect input")
        continue

    while 1:
        add_choice = input("Do you want to get your age in specific year (Y/N) = ")
        if add_choice.lower() == 'y':
            add_year = int(input("Enter that specific year = "))
            if add_year > year100 - 100 and add_year < 2021:
                print(f"Your age in {add_year} was {-year100 + 100 + add_year}")
            elif add_year >= 2021 and add_year < year100 + 50:
                print(f"Your age in {add_year} will be {-year100 + 100 + add_year}")
            elif add_year == year100 - 100:
                print(f"You had just born in {add_year}")
            elif add_year >= year100 + 50:
                print("You will turn too old. Please enter again.")
            else:
                print(f"You had not born in {add_year}")
        elif add_choice.lower() == 'n':
            break
        else:
            print("Enter correct input")
            continue
