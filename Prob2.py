"""
Take input as no of apples, maximum to check, minimum to check.
Print numbers from min to max that are divisors of no of apples.
"""

while True:
    apples = input("Enter the number of apples = ")
    mn = input("Enter the minimum number to check = ")
    mx = input("Enter the maximum number to check = ")

    try:
        if int(apples) > 0 and int(mx) > 0 and int(mn) > 0:
            if int(mx) > int(mn):
                if int(mx) <= int(apples):
                    for i in range(int(mn), int(mx) + 1):
                        if int(apples) % i == 0:
                            print(f"{i} is a divisor of {int(apples)}")
                        else:
                            print(f"{i} is not a divisor of {int(apples)}")
                else:
                    print("maximum value cannot be greater than number of apples.")
            else:
                print("You have entered incorrect range")
        else:
            print("You can only enter positive integers")

    except Exception as e:
        print("You can enter only integer values")
