# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 16:31:21 2021

@author: vac59186
"""

from datetime import datetime
import getpass
import sys


now = datetime.now()
curr = now.strftime("%d/%m/%Y %H:%M:%S")
dte = now.strftime("%d-%m-%Y")
start = datetime.now()
count = 0

user = getpass.getuser()
live = True
log = { }


print ('Enter # to stop and save the log. Press @ to stop and not save.')
while live:

    
    entry = input('> ')
    
    if entry == '#' and count == 0:
        print('No data for log to be created and saved.')

        
    elif entry == '#':
        live = False
        
    elif entry == '@':
        
        ext = input('Are you sure you want to quit without saving?(Y/N)')
        
        if ext == 'Y' or ext == 'y':
               print ('No log file created.')
               sys.exit()
        

        
    else:
        count += 1
        
        now = datetime.now()
        curr = now.strftime("%d/%m/%Y %H:%M:%S")
        
        log[curr] = entry
        print (f'{now.strftime("%H:%M:%S")}')
        


loc = input("Issue location: ")
cli = input("Client: ")

f = open(f'C:/Users/{user}/Desktop/{dte}_{loc}_{cli}.txt', "w")
log_len = len(log)

f.write (F'________________________Created {now.strftime("%d/%m/%Y %H:%M:%S")}________________________\n\n')
f.write (f'Issue location: {loc} \nClient: {cli}\n')
f.write (f'___________________________________________________________________________\n\n\n')

for i in range(log_len):
    
    tempk = list(log)
    tempv = list(log.values())
    
    f.write(f'{tempk[i]} | {tempv[i]}\n\n')
    
end = datetime.now()
down = end-start


f.write (f'*Estimated downtime:{down}')
    
f.close()

print (f'File saved as {user}/Desktop/{dte}_{loc}_{cli}.txt')





























#f = open(f'C:/Users/{user}/Desktop/{dte}_{loc}_{cli}.txt', "x")


