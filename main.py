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

import time
import pyautogui

def press_key(key):
    pyautogui.press(key)

def press_combo(combo):
    pyautogui.hotkey(*combo)

def main():
    press_key("a")
    time.sleep(30)
    press_key("esc")
    press_combo(("4", "5"))
    press_key("f")

if __name__ == "__main__":
    main()