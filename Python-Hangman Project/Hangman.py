# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 20:19:32 2022

@author: vac59186

Hang Man Game
We will set a word as the Answer 
We will display the characters as they guess right/wrong
Well have a count of tries

"""

import sys

def dateFormater():
  from datetime import date
  
  _today = str(date.today())
  return _today

def wordOfTheDay():
    import json
    from random_word import RandomWords

    _today = dateFormater()
    _r = RandomWords()
    _wordStr = _r.word_of_the_day(date=_today)
    _dict = json.loads(_wordStr)
    _txtlst = _dict.get("definations")

    if len(_txtlst) < 2:
        _txtdict = _txtlst[0]
    else:
        _txtdict = _txtlst[1]
    
    _answ = _dict.get("word")
    _def = _txtdict.get("text")
    _pos= _txtdict.get("partOfSpeech")


    _rtList = []
    _rtList.append(_answ)
    _rtList.append(_def)
    _rtList.append(_pos)
    return _rtList

def randoWord():
    from random_word import RandomWords
    _r = RandomWords()
    _word=_r.get_random_word(hasDictionaryDef="true",minLength=5,maxLength=20)
    return _word

_gameOn = True

_round=1
_win=0

while(_gameOn):
    _today = dateFormater()
    if _round == 1:
        _aList = wordOfTheDay()
        _answer = _aList[0].upper()
        _def = _aList[1]
        _pos = _aList[2].upper()
    else:
        _answer = randoWord().upper()
    
    _turns = len(_answer)-1
    _sep = " "
    _usedLetters = []
    _display = []

    for i in _answer:
        if i == '-' or i == ' ':
            _display.append(" ")
        elif i == '\'':
            _display.append(i)
        else:    
            _display.append("_")
            
    print("\n**|||WELCOME TO HANGMAN|||**")
    
    print(f'**|||{_today}|||\n\nRound {_round}   |   W/L: {_win} of {_round-1}\nYou get {_turns} tries. Let\'s begin.\n')
   
    
    if _round == 1:
        print("Word of the Day!\n")
        print(f'Parts of Speech:{_pos}\nDefinition:{_def}\n ')
    else:
        print("New Word!\n")
    ############################################The actual guessing stage     
    while _turns > 0:
        if '_' in _display:
            
            print(_sep.join(_display))
            print("Turns left: ",_turns)
            if _turns < 10:
                print("Used letters: ", _sep.join(_usedLetters))
            _guess = input("Your guess: ")
            
            while len(_guess) > 1 or _guess.isnumeric():
                print("Your guess can only be a single character.")
                print(_sep.join(_display))
                print("Turns left: ", _turns)
                _guess = input("Your guess: ")
                         
                         
            if _guess.upper() in _display:
                    print("letter already validated.")
                    
            elif _guess.upper() in _answer:
                count = 0
                for i in _answer:
                    if _guess.upper() == i:
                        _display[count] = i
                    count += 1
                                      
            else:
                
                if _guess.upper() in _usedLetters:
                    print("letter already used.")
                
                else:
                    _usedLetters.append(_guess.upper())
                    _turns -= 1
                
                if _turns == 0:
                    print("Answer: ",_answer)
                    ext = input("Sorry, you lost. Play again? Y/N: ")
                    
                    while ext != 'Y' and ext != 'y' and ext != 'N' and ext != 'n':
                        ext = input("Invalid Input. Y/N: ")
                    if ext == 'N' or ext=='n':
                        sys.exit()
                    else:
                        _round += 1
                                                    
        else:
            
            if _round == 1:
                print("\n", _sep.join(_display), "- ", _def)
            else:
                print("\n", _sep.join(_display))
                
           
            ext=input("You Win! Play again? Y/N: ")
            
            while ext != 'Y' and ext != 'y' and ext != 'N' and ext != 'n':
                ext = input("Invalid Input. Y/N: ")
                
            if ext == 'Y' or ext == 'y':
                _turns = 0
                _round += 1
                _win += 1
            else:
                sys.exit()
