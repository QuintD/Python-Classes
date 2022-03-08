import random
random_number = random.randint(0, 20)
guess_number = input("enter your guess number: ")
guess_number = int(guess_number)
while random_number != guess_number:
    if random_number > guess_number:
        print("your guess is less than the random number")
    else:
        print("your guess is higher than the random number")
    guess_number = input("enter your guess number")
    guess_number = int(guess_number)
print("you guessed right")