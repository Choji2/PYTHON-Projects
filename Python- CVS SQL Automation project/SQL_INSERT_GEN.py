# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 10:34:08 2022

@author: vac59186
"""
import os
import csv
from tkinter.filedialog import askopenfilename
from tkinter import Tk      # from tkinter import Tk for Python 3.x

def dateFormater():
    from datetime import date 
    _today = str(date.today())
    return _today

def parseValues(reader):
    saveFile = 'C:/users/'+_user+'/Documents/INSERT_STATEMENT_'+table.upper()+"_"+_today+'.txt'
    with open(saveFile, 'w', newline='') as sfile:
        c = 0
        for row in reader:
           
            row_len = len(row)
            value_list = ""
            
            for i in range(row_len):
            
                if i == 0:
                    value_list += "\'"+row[i].strip()+"\'"
                else:
                    value_list += ",\'"+row[i].strip()+"\'"
                        
            if c == 0:
                print('TEMPLATE:')
                print("INSERT INTO "+table.upper()+" VALUES("+str(row)+");")
                input("Press Enter...")
            else:
                
                sfile.write("INSERT INTO "+table+" VALUES("+value_list+");\n")
                
            c += 1
    print("File saved to: "+saveFile)
    os.startfile(saveFile) 
    input("Press Enter...")

_user = os.getlogin()
_today = dateFormater()

table = input("Enter table name and press ENTER: ")

print("SQL TABLE_______________\n"+table.upper())
input("\nYou will now be prompt to open a file. Press ENTER to Continue...")

Tk().withdraw()     # we don't want a full GUI, so keep the root window from appearing
filepath = askopenfilename()
try:
    with open(filepath, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        try:
            parseValues(reader)
        except Exception as e:
            print("Error| " + str(e))
            print("File must only contain data in columns.The first row will be use to show the Field Titles...")

except Exception as e:
    print("Error| "+str(e))

    
                
                    
    



