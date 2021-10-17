#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 18:14:57 2021

@author: abuumar
"""

from auto import Auto
from auto import Autosalon

ford = Autosalon("Ford Dealer", "Seattle")
toyota = Autosalon("Toyota", "Tacoma")
car1 = Auto("Ford", "F-150", 2015)
car2 = Auto("Toyota", "Tundra", 2003)
car3 = Auto("Toyota", "Prius",2012)
car4 = Auto("Toyota", "Sienna", 2006)

ford.add_car(car1)
toyota.add_car(car2)
toyota.add_car(car3)
toyota.add_car(car4)

ford_num=ford.get_carsamount()

toyota_num=toyota.get_carsamount()

