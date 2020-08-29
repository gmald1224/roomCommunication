import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import requests
import bluetooth
import os
import pyautogui
   
def pullXML():
    url = 'https://raw.githubusercontent.com/gmaldona/communicationTest/master/communication.xml'

    response  = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    with open('communication.xml', 'w') as file:
        file.write(str(soup))
        
def readXML():
    tree = ET.parse('communication.xml')
    root = tree.getroot()
    for message in root.findall('message'):
        message = message.text
        print(message)
        
def discover():
    devices = []
    times = 1
    while len(devices) == 0:
        devices = bluetooth.discover_devices(lookup_names=True)
        print('devices not found ({})'.format(times))
        times = times + 1 
    print('')
    print('{} devices found:'.format(len(devices)))
    print(devices)
    for device in devices:
        _, name = device

        if name != 'iPhoneRoom317Greg':
            discover()
        else:
            changeXML('1')    
    
def changeXML(m):
    tree = ET.parse('communication.xml')
    root = tree.getroot()
    for message in root.findall('message'):
        message.text = str(m)
        tree.write('communication.xml')
    os.system("git commit -am 'update'")
    os.system('xdg-open lxterminal.desktop')
    pyautogui.write('python3 controller.py')
    pyautogui.press('enter')
    pyautogui.hotkey('alt', 'tab')
    pyautogui.write('cd')
    pyautogui.press('enter')
    pyautogui.write('cd Desktop/roomCommunication/')
    pyautogui.write('git push')
    pyautogui.press('enter')

os.system('clear')
discover()