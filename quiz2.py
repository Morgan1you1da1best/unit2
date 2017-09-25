#Morgan Baughman
#9/25/17
#quiz2.py - Unit 2 quiz

num1 = float(input('Enter a number here: '))
num2 = float(input('Enter another number here: '))

if num1 == num2:
    print('These numbers are the same')
elif num1>num2:
    print(num1, 'is larger than', num2)
elif num2>num1:
    print(num2, 'is larger than', num1)

if num1% 3==0:
    print(num1, 'is divisible by three')
if num2% 3==0:
    print(num2, 'is divisivle by three')
else: 
    print('neither of these numbers are divible by 3')
answer = float(input('Product of your two numbers: '))
if answer == num1*num2:
    print('Correct')
if answer != num1*num2:
    print('Incorrect')
    
