# print("*" * 10)

# 1. Variables

""" price = 10 # numbers(int())
rating = 5.8 # numbers (float())
name = "Shutter Island" # string
is_published = True # boolean """
# print(price)

# 2. Getting input
""" name = input("What is your name? ") # it will ask you the question to take a input from you and name variable will hold your input
color = input("whats your favourite color? ")
# print(name + " likes " + color) """

# 3. Converting str to number
""" birt_year = input("Birth year? ")
age = 2024 - int(birt_year)
weight_pounds = input("Your weight? ")
weight_Kg = int(weight_pounds) / 2.205
print(weight_Kg) """

# 4. More about strings aka String Methods
""" email = '''Hello Saif, 
This is multiline variable in python'''

print(email)
print(email[-2])
print(email[:]) # it will take 0 as starting index and the last length as ending index 
print(email[0:4]) # it will print index 0 to 3(4-1) which is "Hell" """

""" firstName = "Saif"
lastName = "Rahman"
# print(firstName[1:-1])

# -> Formated string in python equibilant to `${}` in JavaScript
msg = f'{firstName} [{lastName}] is a coder'
print(msg) """

""" course = "Learning python"
print(len(course)) # counting the total character of a string
print(course.upper()) # converts everything to uppercase; doesn't changes the real str but creates a new uppercase str and return it
print(course.find("e"))
print(course.replace("python", "python and JavaScript"))
print("JavaScript" in course) # checks if course includes "JavaScript" and returns boolean """

# Arithmetic operations
""" print(10 / 3) # returns float
print(10 // 3) # returns integer
print(10 ** 3) # returns as to the power
print(10 % 3) # returns remaider """


# Math function

""" print(round(2.9))
print(abs(-2.9)) """

""" is_hot = False
is_cold = False

if is_hot:
    print("It's a hot day")
elif is_cold:
    print("It's a cold day")
else:
    print("It's a lovely day")
print("Enjoy your day") """

""" price = 100000
has_good_credit = False

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down payment {down_payment}") """


# Logical operators
""" has_goodCredit = True
has_high_income = True

if has_goodCredit and not has_high_income:
    print("Eligible for loan")
else:
    print("not eligible") """

name = "Jaco"
if len(name) > 4:
    print("Name must be in 4 characters")
elif len(name) <= 2: 
    print("name should be greater than 2 characters")
else:
    print("Your names fine")



