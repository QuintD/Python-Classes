# def greet():
#     # big = 2+3
#     # print(big)
#     name = input("what is your name? ")
#     intro = "Hello " + name
#     return intro

# introduction = greet()
# print(introduction)

# ****Fuction Parameter and Argument: to do these we introduce variables that whose values will be passed as a parameter while invoking the function
# *****lets refactor the above code so that it can carter for a situation where the name maynot be coming from an input instruction.- name is the parameter, username is the argument that corresponds to that parameter.
# def greet(name):
#     intro = "Hello " + name
#     return intro

# **** it can now get the musername from either input of just normal assignment statement
# user_name = "John Doe"
# user_name = input("what is your name? ")
# introduction = greet(user_name)
# print(introduction)


# **** When we have multiple arguments to a function
def greet(name, gender):
    if gender == "male":
        title = "Mr. "
    else:
        title = "Ms. "
    intro = "Hello " + title + name
    return intro


user_name = input("what is your name? ")
user_gender = input ("are you male or female? type in small letters ")
introduction = greet(user_name, user_gender)
print(introduction)

