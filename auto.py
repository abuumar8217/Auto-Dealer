#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 17:45:16 2021

@author: abuumar
"""

class Auto():
    def __init__(self,make,model,year,mileage=0):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = 0
        
    def get_info(self):
        return f"The requested vehicle is {self.year} {self.make} {self.model} with {self.mileage} miles."
    
    def update_mile(self,mileage):
        self.mileage = mileage

class Autosalon:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.cars_instock = 0 
        self.cars = []
        
    def add_car(self,car):
        self.cars.append(car)
        self.cars_instock +=1
        
        
    def get_name(self):
        return self.name
    
    def get_carlist(self):
        return[car.get_info() for car in self.cars]
    
    def get_carsamount(self):
        return self.cars_instock
    
def see_methods(klass):
    return [method for method in dir(klass) if method.startswith('__') is False]    




