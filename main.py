#Topic: Fundamental Data Types

# int and float
# print(type(2 + 4))
# print(type(2 - 4))
# print(type(2 * 4))
# print(type(2 / 4)) # 0.5

# print(2 ** 3)
# print(5 // 4)
# print(5 % 4)



# Topic: math functions

#print(round(3.9))
#print(abs(-20))



#Topic: operator precedence

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

#Topic: Variables

# user_iq = 190
# user_age = user_iq/4
# a = user_age

# print(a)

#---------------------------------------#

#Topic: constants
#PI = 3.14

# a,b,c = 1,2,3
# print(a)
# print(b)
# print(c)

#---------------------------------------#

# Topic: augmented assignment operator
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

# Topic: string concatenation
#print('hello' + ' Piotr')

# a = str(100)
# b = int(a)
# c = type(b)
# print(c)

#Topic: Type Conversion

#print(type(int(str(100))))

# Escpae Sequence
#weather = "\t It\'s \"kind of\" sunny \n hope you have a good day!"

#print(weather)

#Topic: Formatted Strings

# name = 'Johnny'
# age = 55

# print('hi {0}. You are {1} years old.'.format(name, age))

#---------------------------------------#

#Topic: String Indexes

# selfish = 'me me me'
#         #  01234567
# # [start:stop]
# print(selfish[7])
# print(selfish[0:8:3])
# print(selfish)
# print(selfish[::-3])


#Topic: Built-In Functions + Methods

# greet = 'hellloooo'
# print(greet[0:len(greet)])

# quote = 'to be or not to be'
# print(quote.find('be'))
# quote2 = quote.replace('be', 'me')
# print(quote2)

#---------------------------------------#

#Topic: Booleans
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

# Topic: List
# li = [1, 2, 3, 4, 5]
# li2 = ['a', 'b', 'c']
# li3 = [1, 2.5, 'a', True]
# amazon_cart = ['notebooks', 'sunglasses']

# print(amazon_cart[1])
# Data Structure

# Topic: List slicing

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

# Topic: Matrix :D

# matrix = [
#   [1,5,1],
#   [0,1,0],
#   [1,0,1]
# ]

# print(matrix[0][1][][][])

# Topic: List Methods 1

# basket = [1,2,3,4,5]

#Topic: adding
# basket.insert(5, 100)
# new_list = basket.extend([100, 101])
# print(new_list)
# print(basket)

#Topic: removing

# new_list = basket.remove(4)
# new_list = basket.clear()
# basket.pop()
# print(new_list)

# Topic: List Methods 2

# basket = ['a','b','c','d','e', 'd']

# print('x' in basket)
# print(basket.count('d'))

# Topic: List Methods 3

# basket = ['a','x','b','c','d','e', 'd']
# basket.sort()
# print(sorted(basket))
# basket.reverse()
# print(basket)

# Topic: Common List Patterns
# basket = ['a','x','b','c','d','e', 'd']
# basket.sort()
# basket.reverse()

# print(basket[:])
# print(basket)

# print(list(range(1,100)))
# new_sentence = ' '.join(['hi','my','name','is','JOJO'])
# print(new_sentence)
#Topic: Task
# friends = ['Simon', 'Patty', 'Joy', 'Carrie', 'Amira', 'Chu']

# new_friend = ['Stanley']

# print(friends.sort() + new_friend)
# print(sorted(friends + new_friend))

# Topic: List Unpacking

# a,b,c, *other, d = [1,2,3,4,5,6,7,8,9]
# print(a)
# print(b)
# print(c)
# print(other)
# print(d)

# Topic: None

# weapons = None
# Null
# print(weapons)

# Topic: Dictionaries

# dictionary = {
#   'weapons': [1,2,3]
#   'greeting': 'hello',
#   'is_Magic': True
#   }

# print(dictionary)

# Topic: Dictionary Methods 1

# user = {
#   'basket': [1,2,3],
#   'greet': 'hello'
#   'age': 20
# }

# user2 = dict(name= 'JoJo')
# print(user.get('age', 55))
# print(user2)

# Topic: Dictionary Methods 2

# user = {
#   'basket': [1,2,3],
#   'greet': 'hello',
#   'age': 20
# }
# user2 = user.copy()
# print(user.clear())
# print(user.pop('age'))

# print(user.popitem())
# print(user)

# Topic: Tuple  

# my_tuple = (1,2,3,4,5)
# print(5 in my_tuple)
# user = {
#   'basket': [1,2,3],
#   'greet': 'hello'
#   'age': 20
# }

# print(user.items())

# Topic: Tuple 2

# my_tuple = (1,2,3,4,5,5)

# print(len(my_tuple))

# Topic: Sets 1

# my_list = {1,2,3,4,5,5}
# my_set = {1,2,3,4,5,5}
# my_set.add(100)
# my_set.add(2)
# print(set(my_list))
# my_set = {1,2,3,4,5,5}
# new_set = my_set.copy()
# my_set.clear()
# print(len(my_set))
# print(new_set)
# print(my_set)

# Topic: Sets 2

# my_set = {4,5}
# your_set = {4,5,6,7,8,9,10}

# print(my_set.difference(your_set))
# print(my_set.discard(5))
# print(my_set.difference_update(your_set))
# print(my_set.intersection(your_set))
# print(my_set.issubset(your_set))
# print(your_set.issuperset(my_set))
# print(your_set.union(my_set))

# Topic: Breaking The Flow

# Topic: Conditional Logic

# is_old = bool('hello')
# is_licenced = bool(5)

# print(bool('o'))
# print(bool(0))
# # Truthy and Falsy

# if is_old and is_licenced: 
#   print('you are old enought to drive, and you have a licence!')
# # elif: condition:
# else:
#  print('you are not of age!')

#  print('okoko')

# Topic: Ternary Operator

# condition_if_true if condition else condition_if_false

# is_friend = False
# can_message = "message allowed" if is_friend else "not allowed to message"

# print(can_message)



# Topic: Short Circuiting

# is_Friend = True
# is_User = True

# if is_Friend and is_User:
#   print('best friends forever')


# Topic: Logical Operators

# >
# <
# ==
# print(4>5)
# print(4==5)
# print(4<5)
# print('b'>'x') #False
# print('m'=='n') #False
# print('a' > 'A') "a" ascii is 97 --> ord("a"); "A" ascii is 65 --> ord("A")

# is_magician = True
# is_expert = False

# if is_magician and is_expert:
#   print('You are a master magician')

# elif is_magician and not is_expert:
#   print("at least you're getting there")

# elif not is_magician :
#   print("You need magic powers")

# Topic: is vs ==

# print(True == 1)
# print('' == 1)
# print([] == 1)
# print(10 == 10.0)
# print([] == [])


# Topic: For Loops

# for item in (1,2,3,4,5):
#   for x in ['a', 'b', 'c']:
#     print(item, x)
    
# Topic: Iterables - list, dictionary, tuple, set, string
#iterated -> one by one check each item in the collection.

# user = {
#   'name': 'Golem',
#   'age': 5006,
#   'can_swim': False
# }

# for item in user.items():
#   key, value = item;
#   print(item)

# for item in user.values():
#   print(item)

# for item in user.keys():
#   print(item)

# Topic: Tricky Counter - Exercise

#counter
# my_list = [1,2,3,4,5,6,7,8,9,10]

# counter = 0
# for item in my_list:
#   counter = counter + item
# print(counter)

# Topic: range()

# for _ in range (10, 0, -2):
#   print(list(range(10)))

# Topic: enumerate()

# for i,char in enumerate(list(range(100))):
#   if char == 50:
#     print(f'index of 50 is: {i}')

# Topic: While Loops 1&2

# i = 0
# while i < 50:
#   print(i)
#   i += 1
#   break
# else:
#   print('done with all the work')
# my_list = [1,2,3]
# for item in [1,2,3]:
#   print(item)

# i = 0
# while i < len(my_list):
#   print(my_list[i])
#   i += 1

# while True:
#   response = input('say something!:')
#   if (response == 'bye'):
#     break

# Topic: break, continue, pass

# my_list = [1,2,3]
# for item in my_list:
#   pass

# i = 0
# while i < len(my_list):
#   print(my_list[i])
#   i += 1
#   pass

# Topic: First GUI

#Exercise!
# picture = [
#   [0,0,0,1,0,0,0],
#   [0,0,1,1,1,0,0],
#   [0,1,1,1,1,1,0],
#   [1,1,1,1,1,1,1],
#   [0,0,0,1,0,0,0],
#   [0,0,0,1,0,0,0]
# ]
# for row in picture:
#   for pixel in row:
#     if(pixel):
#       print('*', end='')

#     else:
#       print(' ', end='')
#   print('') # need a new line after a row\

# Remember: clean, Readability, predictability, DRY

# Exercise: Check for duplicates in list:

# some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

# duplicates = []
# for value in some_list:
#   if some_list.count(value) > 1:
#     if value not in duplicates:
#       duplicates.append(value)

# print(duplicates)

# DRY

# picture = [
#   [0,0,0,1,0,0,0],
#   [0,0,1,1,1,0,0],
#   [0,1,1,1,1,1,0],
#   [1,1,1,1,1,1,1],
#   [0,0,0,1,0,0,0],
#   [0,0,0,1,0,0,0]
# ]
# def show_tree():
#   for row in picture:
#     for pixel in row:
#       if(pixel):
#         print('*', end='')
  
#       else:
#         print(' ', end='')
#     print('')

# show_tree()

#parameters
# def say_hello(name, emoji):
#   print(f'helllloooo {name} {emoji}')

# # positional arguments
# say_hello(':D', 'Piotr')
# say_hello('Pawel', ':p')
# say_hello('Ola', ':*')

# keyword arguments
# say_hello(emoji=':D', name='Bibi')

# def sum(num1, num2):
#   def another_func(n1, n2):
#     return n1 + n2
#   return another_func(num1, num2)
# total = sum(10, 20)
# print(total) #watch 83 lesson again for bether understand

# Exercise: Tesla

# Methods vs Functions

# Docstrings

# def test(a):
#   '''
#   Info: this function tests and prints param a
#   '''
#   print(a)

# print(test.__doc__)

# clean code

# def is_even(num):
#   return num % 2 == 0

# print(is_even(51))

# *args and **kwargs

# def super_func(name, *args, i='hi', **kwargs):
#   total = 0
#   for items in kwargs.values():
#     total += items
#   return sum(args) + total

# print(super_func('Piotr', 1,2,3,4,5, num1=5, num2=10))

#Rule: params, *args, default parameters, **kwargs

# Exercise: Functions

# def highest_even(li):
#   evens = []
#   for item in li:
#     if item % 2 == 0:
#       evens.append(item)
#   return max(evens)

# print(highest_even([10,2,3,4,8,11]))

# Walarus Operator

# a = 'helloooooooooo'

# if ((n := len(a)) > 10):
#     print(f"too long {n} elements")

# while ((n := len(a)) > 1):
#     print(n)
#     a = a[:-1]

# print(a)

# Scope - what variables do I have access to?\
# if True:
#   x = 10

# def some_func():
#   total = 100

# print(x)

# a = 1

# def parent():
#   def confusion():
#     return sum
#   return confusion()

# print(a)
# print(parent())

#1 - start with local
#2 - Parent local?
#3 - global
#4 - built in python functions.

# global Keyword

# total = 0 

# def count(total):
#   total += 1
#   return total

# print(count(count(count(total))))

# nonlocal Keyword

# def outer():
#   x = "local"
#   def inner():
#     nonlocal x
#     x = "nonlocal"
#     print("inner:", x)

# inner()
# print("outer:", x)

# outer()

# Why Do We Need Scope?

# What is OOP 1

# <class 'NoneType'>
# <class 'bool'>
# <class 'int'>
# <class 'float'>
# <class 'str'>
# <class 'list'>
# <class 'tuple'>
# <class 'dict'>

# class BigObject:
#     pass

# obj1 = BigObject()
# obj2 = BigObject()
# obj3 = BigObject()

# print(type(None))
# print(type(True))
# print(type(5))
# print(type(5.5))
# print(type('hi'))
# print(type([]))
# print(type(()))
# print(type({}))
# print(type(obj1))



  #OOP Exercise Cat-1


# class Cat:
#     species = 'mammal'
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# # Instantiate the Cat object with 3 cats
# puszek = Cat("Puszek", 3)
# maciek = Cat("Maciek", 11)
# rudy = Cat("Rudy", 1)


# # Find the oldest cat
# def get_oldest_cat(*args):
#     return max(args)


# # Output
# print(f"The oldest cat is {get_oldest_cat(puszek.age, maciek.age, rudy.age)} years old.")

# Topic: Encapsulation (talk)
# Topic: Abstraction  (talk)

# class PlayerCharacter:
#   # Class Object Attribute
#   membership = True
#   def __init__(self, name, age):
#     self.name = name #attributes  
#     self.age = age
      

#   def shout(self): 

#   @classmethod
#   def adding_things(cls, num1, num2):
#     return num1 + num2

#   @staticmethod
#   def adding_thins2(num1, num2):
#     return num1 + num2

# # player1 = PlayerCharacter('Piotr', 24)

# print(player1.adding_things(2,3))


class User:
  def sign_in(self):
    print('logged in')

class Wizard():
  def __init__(self, name, power):
    self.name = name
    self.power = power
    
  def attack(self):
    print(f'attacking with power of {self.power}')

class Archer():
  def __init__(self, name, num_arrows):
    self.name = name
    self.num_arrows = num_arrows

  def attack(self):
    print(f'attacking with arrows: arrows left- {self.num_arrows}')

wizard1 = Wizard('Merlin', 50)
archer1 = Archer('Robin', 100)
wizard1.attack()
archer1.attack()