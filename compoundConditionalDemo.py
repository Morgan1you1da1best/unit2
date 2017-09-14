#Morgan Baughman
#9/14/17
#compoundConditionalDemo.py - and/or statements

num = float(input('Enter a number: '))
if num>0 and num%7 == 0:
    print('Your number is postive and divisable by 7.')
elif num>0:
    print('Your number is positive and not divisable by 7.')
elif num<0 and num%7 == 0:
    print('Your number is negative and divisable by 7.')
elif num<0:
    print('Your number is negative and not divisable by 7.')
else:
        print('Your number is 0.')