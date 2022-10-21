# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 06:46:40 2022

@author: vac59186
"""
import os
import csv
import xml.etree.ElementTree as ET
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
      
def dateFormater():
    from datetime import date 
    _today = str(date.today())
    return _today

def parseXML(xmlFile):
       
    tree = ET.parse(xmlFile)
    root = tree.getroot()
    _today = dateFormater()
    _user = os.getlogin()
    saveFile = 'C:/users/'+_user+'/Documents/DW_IP_OUTPUT_'+_today+'.csv'
    with open(saveFile, 'w', newline='') as csvfile:
        fieldnames = ['Device_Name', 'IP_Address']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
               
        for _exportcontent in root:                         
            for _DeviceDefinition in _exportcontent.iter('DeviceDefinition'):                                                                                 
                for _property in _DeviceDefinition.iter("Property"):
                
                    deviceName = _exportcontent.get("name")
                    name = _property.get("name")
                    value = _property.get("value")
                
                    if name == 'ip_address':
                        temp = {'Device_Name': deviceName, 'IP_Address': value}
                        writer.writerow(temp)
        os.startfile(saveFile) 
              
def main():
    Tk().withdraw()     # we don't want a full GUI, so keep the root window from appearing
    filepath = askopenfilename()
    parseXML(filepath)
    
                          
main()

