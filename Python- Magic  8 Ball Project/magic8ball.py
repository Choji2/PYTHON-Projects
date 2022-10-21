# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 19:16:05 2022

@author: vac59186
"""


import sys
import random

"""Magic 8 ball 

Keep running to exit 
    Ask for user question 
    Return stored answer 
    contine cycle til quit
"""

_continue = True
_ballList = ["No.", "Yes.", "Maybe.", "Soon.", "It is possible.",
           "You know the answer.", "It is up to fate.",
           "Listen to your Heart." ,
           "Do or die, but never don't.", "Joe Biden.",
           "Donald Trump.", "McDonalds.", "Buy crypto."]

while _continue:
    
    prophecy = random.randint(0, len(_ballList)-1)
    answ = input("Ask the Magic 8 ball your question.leave blank to exit\n:")
    
    if answ == "":
        sys.exit()
    else:
        print("Magic 8 ball says, \"", _ballList[prophecy], "\"")
