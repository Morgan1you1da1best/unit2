#Morgan Baughman
#9/14/17
#insulter.py - Insult your freinds

from random import randint
randint(1,4)
name = input('Enter your name here: ')
number = randint(1,4)
if number == 1:
    print(name,', your feet stink')
if number == 2:
    print(name,', what is wrong with your face?')
if number == 3:
    print(name,', you are lame.')
if number == 4:
    print( name,', did you get a haircut? Your hair looks different today.')
