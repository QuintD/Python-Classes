# print('The program starts here')
# answer = input("enter any letter from A to D in Capital letter: ")
# if answer == "A":
#     print("You entered A")
# elif answer == "B":
#     print("You entered B")
# elif answer == "C":
#     print('You entered C')
# elif answer == "D":
#     print("You entered D")
# else:
#     print("Please Follow the instruction")
# print('The program ends here')

# scores = input("enter the score from 0-100: ")
# scores = int(scores)
# if 70 <= scores <= 100:
#     print("Grade = A ")
# elif 60 <= scores <= 69:
#     print("Grade = B ")
# elif 50 <= scores <= 59:
#     print("Grade = C ")
# elif 45 <= scores <= 49:
#     print("Grade = D ")
# elif 40 <= scores <= 44:
#     print("Grade = E ")
# elif 0 <= scores <= 39:
#     print("Grade = F ")
# else:
#     print("INVALID SCORE")

number = input("enter a number: ")
number = int(number)
if number % 6 == 0:
    print("the number is divisible by 2 and 3")
elif number % 2 == 0:
    print("number is a multiple of 2")
elif number % 3 == 0:
    print("number is a multiple of 3")
else:
    print("number is not a multiple of 2 or 3")
# the order matters a lot. you have to start with the interception point in your if statement, and then the other conditions come to your elif so long as it has an inclusive if else if statement.

