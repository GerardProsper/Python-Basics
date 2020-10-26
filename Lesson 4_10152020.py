
##Find Longest Substring / Guessing Game - Python Basics with Sam

##sen = 'Hi Sam, nice to meet you'
##split = sen.split()
##>>> split
##['Hi', 'Sam,', 'nice', 'to', 'meet', 'you']
##
##
##comma = 'Sam,Tom,Pete,Matt'
##new = comma.split(',')
##>>> new
##['Sam', 'Tom', 'Pete', 'Matt']

##name = input("Please enter names use commas: ").split(',')
##
##names = [ i.strip() for i in name ] 
##
##
##print(names)
##
##Please enter names use commas: Sam, Tom, Pete, Matt
##['Sam', 'Tom', 'Pete', 'Matt']
##
##w/o strip()
##Please enter names use commas: Sam, Tom, Pete, Matt
##['Sam', ' Tom', ' Pete', ' Matt']
##
##w/o split(',')
##Please enter names use commas: Sam, Tom, Pete, Matt
##['Sam,', 'Tom,', 'Pete,', 'Matt']

# can add to a string using += but cannot -=
##>>> x += 'S'
##>>> x
##'abcaafahbaabdfgzS'
##>>> x -= m
##Traceback (most recent call last):
##  File "<pyshell#13>", line 1, in <module>
##    x -= m
##NameError: name 'm' is not defined



##x = 'abcaafahbaabdfgz'
##
##sub = x[0]
##long, length = sub, 1
##
##for letter in x[1:]:
##    print('------New Loop---------')
##    print(letter,'Main letter')
##    print(sub,'Main sub')
##    if ord(sub[-1]) <= ord(letter):
##        print('---------if-----------')
##        print(sub,'sub 1')
##        print(letter, 'letter 1')
##        sub += letter
##        print (sub, 'sub 2')
##        print (letter, 'letter 2')
##        print(len(sub),'is sub Length')
##        print(length,'is OR/New Length')
##        if len(sub) > length:
##            print(length, 'is old length in if statement')
##            length = len(sub)
##            print(length, 'is new length in if statement')
##            print(long, 'long 1')
##            long = sub
##            print (long, 'long 2')
##            print (sub, 'sub 3')
##    else:  
##        print('--------else-------')
##        print(sub,'sub 4')
##        sub = letter
##        print(letter,'letter 3')
##        print (sub, 'sub 5')
##
##print('---- FINALLY----')        
##print(long,'long 3')
##print('---- FINALLY----')
    

##dad ='dadaddadaadada'
##
##count, place = 0,0
##
##while dad.find('dad',place) >= 0:
##    place = dad.find('dad',place) + 1
##    print(place, 'place')
##    count += 1
##    print(count, 'count')




##>>> from math import pi
##>>> pi
##3.141592653589793
##>>> import math
##>>> dir(math)
##['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']
##>>> math.pi
##3.141592653589793


##from string import ascii_lowercase as lower
##import re
##
##x = 'abcaafahbaabdfgz'
##
##abc = ''
##
####for letter in lower:
####    abc += letter + '*'
####    print (abc)
##
####abc = '*'.join(lower)
####abc += '*'
##
##abc = 'a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z*'
##
##pat = re.compile(abc)
##
##print (max(pat.findall(x),key=len))




##ans = False
##
##high = 100
##low = 0
##
##input('Think of a number between 1 to 100. Press enter to continue.')
##
##while not ans:
##    guess = (high - low)//2 + low
##    print(guess,'   Guess')
##    print(low,'   Low')
##    print(high,'   High')
##    print(f'Is your number {guess}')
##    resp = input("""Enter 'h' to indicate the guess is too high.
##Enter 'l' to indicate the guess is too low.
##Enter 'c' to indicate I guessed correctly.
##Enter Answer: """).lower()
##    print()
##    if resp == 'h':
##        high = guess
##    elif resp == 'l':
##        low = guess
##    elif resp == 'c':
##        ans = True
##        print('Thanks for playing with me')



##import re
##
##dad ='dadaddadaadada'
##
##found = re.findall(r'(?=(\w\w\w))',dad)
##
##dads = [dad for dad in found if dad == 'dad']
##
##print(len(dads))


x = 4

def add(x):
    print(x + 2)

add(2)


