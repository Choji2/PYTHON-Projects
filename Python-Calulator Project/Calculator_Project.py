# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 13:12:19 2021

@author: vac59186

This program is to allow the user to type in an equation.
The user is then able to append to the answer or create a new equation.
"""
import re

run = True
previous = 0

print("Our Magical Calculator\nType'quit' to exit")
def performMatch(): 
    
    global run 
    global previous
    equation = ''
    
    if previous == 0 and equation != 'quit':
        equation = input("Enter your equation:")
    else:
        equation = input(str(previous)+"\n")
    
    if equation == 'quit':
        print("\nGoodbye.")
        run = False
    
        
    
    else:
        equation=re.sub('[a-zA-Z,.:()""]', "", equation)

        
        if previous == 0:
            
            try:
                previous = eval(equation)
                print("Result:", previous)
                
            except SyntaxError:
                print('Invalid Input')
                
            except ZeroDivisionError:
                print('Can not divide by zero')
                

            
        elif str(equation)[0].isdigit():
            
            try:
                
                 previous = eval(equation)
                 print("Result:", previous)
                 
            except SyntaxError:
               print('Invalid Input')
               
            except ZeroDivisionError:
               print('Can not divide by zero')
        
        else:         
            
            try:
                
                previous = eval(str(previous) + equation)
                print("Result:", previous)
                
            except SyntaxError:
                print('Invalid Input')
            
            except ZeroDivisionError:
                print('Can not divide by zero')
                                   

while run:
    performMatch()
