import random
random_number = random.randint(0, 80)
guess_number = int(input("Enter your guess number: "))

while random_number != guess_number:
    if random_number > guess_number:
        print("Your guess is less that the random number")
    else:
        print("Your guess is greater than the random number")
    guess_number = int(input("Enter your guess number: "))
print('you guessed right')
