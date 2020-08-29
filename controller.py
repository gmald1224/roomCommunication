import pyautogui
import os
import time

time.sleep(5)
user = ''
password = ''
with open('loginuser.txt', 'r') as file:
    user = file.read()
    file.close()
with open('password.txt', 'r') as file:
    password = file.read()
    file.close()
    
pyautogui.write(user)
pyautogui.write(password)