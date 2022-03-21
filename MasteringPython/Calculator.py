operation = input('''Please type in the maths operation you would like to complete:
+ for Addition
- for Subtraction
* for Division
/ for Multiplication
''')
number_1 = int(input("Enter your first number: "))
number_2 = int(input("Enter your second number: "))

if operation == "+":
    print("{} + {} = ".format(number_1, number_2))
    print(number_1 + number_2)
elif operation == "-":
    print("{} - {} = ".format(number_1, number_2))
    print(number_1 - number_2)
elif operation == "*":
    print("{} * {} = ".format(number_1, number_2))
    print(number_1 * number_2)
elif operation == "/":
    print("{} / {} = ".format(number_1, number_2))
    print(number_1 / number_2)
else:
    print("You have typed an invalid operator, please run the program again")
