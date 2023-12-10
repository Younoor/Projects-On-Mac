#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 11:52:10 2020

@author: yousefnoor
"""

import random

restaurantList = ['Subway','Taco Bell','Chilis','Panda Express','Chipotle','Chicken E']

def pickRestaurant():
    print(restaurantList[random.randint(0,len(restaurantList)-1)])
    
def addRestaurant(name):
    restaurantList.append(name)
    
def removeRestaurant(name):
    restaurantList.remove(name)
    
def listRestaurant():
    for restaurant in restaurantList:
        print(restaurant)
    
while True:
    print('''
          
          [1] - List restaurant
          [2] - Add restaurant
          [3] - Remove restaurant
          [4] - Pick restauarnt
          [5] - Exit
          
          ''')
    selection = input('Please select an option: ')
    
    if selection == '1':
        print('')
        listRestaurant()
    elif selection == '2':
        inName = input('\nType name of the restaurant you want to add: ')
        addRestaurant(inName)
    elif selection == '3':
        inName = input('\nType name of restaurant you want to remove: ')
        removeRestaurant(inName)
    elif selection == '4':
        print('')
        pickRestaurant()
    elif selection == '5':
        print('\nEnjoy your meal! :)\n')
        break
    else:
        print('\nError: Please select one of the options above.')
