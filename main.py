import math
# Ten numbers are input by the user. There are three choices for each number:
#
# a) Multiply the number by 2.
# b) Add 6 to the number.
# c) Divide the number by 2, then test to see if the answer is odd or even. If the answer is even, an appropriate message must be printed.
#
# The number, choice and answer must be printed. Should option c be chosen, the appropriate message must also be printed.


for x in range(10):
    num = int(input("num? "))
    choice = input("Choice? ")

    if choice == 'A' or choice == 'a':
        new_num1 = (num * 2)
        print(f'{num} {choice} {new_num1}')

    elif choice == 'B' or choice == 'b':
        new_num2 = (num + 6)
        print(f'{num} {choice} {new_num2}')

    elif choice == 'C' or choice == 'c':
        divided_result = (num/2)
        if divided_result % 2 == 0:
            (print)(f"{num} {choice} {divided_result} is an even number")

        elif divided_result % 2 != 0:
            (print)(f"{num} {choice} {divided_result} is an odd number")


