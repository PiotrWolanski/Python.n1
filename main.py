#Fundamental Data Types
# int and float
# print(type(2 + 4))
# print(type(2 - 4))
# print(type(2 * 4))
# print(type(2 / 4)) # 0.5

# print(2 ** 3)
# print(5 // 4)
# print(5 % 4)

# math functions
#print(round(3.9))
#print(abs(-20))

#operator precedence
#print((20 - 3) + 2 ** 2)

# ()
# **
# * /
# + -

#First try to make something in Ark Survival Evolved

# import time
# import pyautogui

# def press_key(key):
#     pyautogui.press(key)

# def press_combo(combo):
#     pyautogui.hotkey(*combo)

# def main():
#     press_key("a")
#     time.sleep(30)
#     press_key("esc")
#     press_combo(("4", "5"))
#     press_key("f")

# if __name__ == "__main__":
#     main()

# //////////////////////////////////////////////////////
# //////////////////////////////////////////////////////

# int float
# complex

# print(bin(5))
# print(int('0b101', 2))

#Variables

# user_iq = 190
# user_age = user_iq/4
# a = user_age

# print(a)

#---------------------------------------#

#constants
#PI = 3.14

# a,b,c = 1,2,3
# print(a)
# print(b)
# print(c)

#---------------------------------------#

# augmented assignment operator
#some_value = 5
#some_value = some_value + 2
#some_value -= 2

#print(some_value)

# print(type("hi hello there 24!"))
# username = 'supercoder'
# password = 'supersecret'
# long_string = '''
# WOW
# O O
# ---
# '''

#print(long_string)
# first_name = 'Piotr'
# last_name = 'Wolanski'
# full_name = first_name + ' ' + last_name
# print(full_name)

#---------------------------------------#

# string concatenation
#print('hello' + ' Piotr')

# a = str(100)
# b = int(a)
# c = type(b)
# print(c)

#Type Conversion

#print(type(int(str(100))))

# Escpae Sequence
#weather = "\t It\'s \"kind of\" sunny \n hope you have a good day!"

#print(weather)

#Formatted Strings

# name = 'Johnny'
# age = 55

# print('hi {0}. You are {1} years old.'.format(name, age))

#---------------------------------------#

#String Indexes

# selfish = 'me me me'
#         #  01234567
# # [start:stop]
# print(selfish[7])
# print(selfish[0:8:3])
# print(selfish)
# print(selfish[::-3])


#Built-In Functions + Methods

# greet = 'hellloooo'
# print(greet[0:len(greet)])

# quote = 'to be or not to be'
# print(quote.find('be'))
# quote2 = quote.replace('be', 'me')
# print(quote2)

#---------------------------------------#

#Booleans
# name = 'Piotr'
# is_cool = False

# is_cool = True

# print(bool('True'))

#Exercise: Type Conversion
# name = 'Piotr Wolanski'
# age = 50
# relationship_status = 'single'

# relationship_status = 'it\'s complicated'

# print(relationship_status)

# birth_year = input('what year were you bron?')

# age = 2019 - int(birth_year)

# print(f'your age is: {age})


#---------------------------------------#

# # assign namevariable a value of Piotr string
# name = 'Piotr'
# is_cool = False

# is_cool = True

# print(bool('True'))


# Password checker

# input('Joker')
# input('secret')

# print('{username}, your password {******} is {6} letters long')

# print(password * 6(lenght))

# input = ('username')
# input = ('secret')

# database = {'piotr': {'password':'123456'}, 'piotr2': {'password':'xyz123'}}

# username = input('What\'s your username?:\n')
# password = input('What\'s your password?:\n')

#---------------------------------------#

# import time
# import sys
# import getpass

# database = [
#     ("Piotr1", "123"),
#     ("Piotr2", "456")
#     ]


# def login():
#     time.sleep(1)
#     print("Welcome. Please login.")
#     while True:
#         time.sleep(1)
#         username = input("Username: ")
#         password = getpass.getpass("Password: ")
#         time.sleep(1)
#         if (username, password) in database:
#             print("Welcome, " + username)
#             main()
#         else:
#             print("User not found. Try again.")

# def logout():
#     time.sleep(1)
#     print("Logout?")
#     lgout = input(">>")
#     if lgout == ("yes") or lgout == ("Yes") or lgout == ("YES"):
#         time.sleep(1)
#         print("Logout successful")
#         main2()
#     elif lgout == ("no") or lgout == ("No") or lgout == ("NO"):
#         print("Logout unsuccessful")
#         main()
#     else:
#         print("Command not valid")



# def main():
#     time.sleep(1)
#     print("Current commands: Logout")
#     while True:
#         command = input(">>")
#         if command == ("Logout"):
#             logout()
#         else:
#             print("Command not valid")

# def main2():
#     time.sleep(1)
#     print("Hello, would you like to login, register or exit?")
#     while True:
#         command2 = input(">>")
#         if command2 == ("Login") or command2 == ("login") or command2 == ("LOGIN"):
#             login()
#         elif command2 == ("Register") or command2 == ("register") or command2 ==      ("REGISTER"):
#             register()
#         elif command2 == ("Exit") or command2 == ("exit") or command2 == ("EXIT"):
#             sys.exit()
#         else:
#             print("Command not valid")

# def register():
#     print("Register your information below")
#     (newusername == input("Username: "))
#     (newpassword == getpass.getpass("Password: "))

#     print("Success! Please login!")
#     login()


# main2() 

#---------------------------------------#

# username = input('What is your username?')
# password = input('What is your password?')

# password_length = len(password)
# hidden_password = '*' * password_length

# print(f'{username}, your password, {hidden_password}, is {len(password)} letters long')

#---------------------------------------#

# List
# li = [1, 2, 3, 4, 5]
# li2 = ['a', 'b', 'c']
# li3 = [1, 2.5, 'a', True]
# amazon_cart = ['notebooks', 'sunglasses']

# print(amazon_cart[1])
# Data Structure

# List slicing

# amazon_cart = ['notebooks',
#                'sunglasses',
#                'toys',
#                'grapes'
#               ]
# amazon_cart[0] = 'laptop'
# new_cart = amazon_cart[:]
# new_cart[0] = 'gum'
# print(new_cart)
# print(amazon_cart)

# Matrix :D

# matrix = [
#   [1,5,1],
#   [0,1,0],
#   [1,0,1]
# ]

# print(matrix[0][1][][][])

# List Methods 1

basket = [1,2,3,4,5]

#adding
basket.append(100)
new_list = (basket)
print(new_list)
print(basket)

