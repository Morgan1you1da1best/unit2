#Morgan Baughman
#9/14/17
#fortuneTeller.py

color = input('Enter a color (red or blue): ')
red = 'red'
blue = 'blue'
number = int(input('Enter a number between 1-4: '))
if color == red and number == 1:
    print('You will die by gunshot')
if color == red and number == 2:
    print('You will die by asphyxiation')
if color == red and number == 3:
    print('You have been awarded a lifetime supply of chicken nuggets')
if color == red and number == 4:
    print('You will achieve great things')
if color == blue and number == 1:
    print('You will win the lottery')
if color == blue and number == 2:
    print('You will die by disease')
if color == blue and number == 3:
    print('You will die of heat exhaustion')
if color == blue and number == 4:
    print('You will die by blood loss')