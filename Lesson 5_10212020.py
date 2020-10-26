
## Command Line and Recursion in Python - Python Basics with Sam

##def fact(x):
##    tot = 1
##    while x > 1:
##        tot *= x
##        x -= 1
##    print(tot)

##
##tests = [3,4,1,8,12,18,100]
##
##def fact(n):
##    if n > -1:
##        if n == 0:
##            return 1
##        else:
##            return n * fact(n-1)
##    else:
##        return 'Negative'
##
##
##
##
##for test in tests:
##    print(fact(test))
##






## 69/5 * 68/4 * 67/3 * 66/2 * 65/1 * 26

##  ( 69! / 5!*(69-5)!) * 26

##def odds(balls, pick, power=False):
##    """ Enter number a regular balls, number of balls
##picked, and if they are using a powerball, you will be asked
##for the number of powerballs"""
##    from math import factorial as fact
##    p_ball = 1
##    if power :
##        p_ball = int(input("Enter number of powerballs: "))
##    return (fact(balls))/(fact(5)*fact(balls-pick))*p_ball
##
##
#### print("{:,}".format(odds(69,6)))
##
##print(f"{odds(69,6,True):,}")


##import sys
##
##print(sys.argv)


##>>> a=[]
##>>> b={}
##>>> type(a)
##<class 'list'>
##>>> type(b)
##<class 'dict'>

fruit = {'banana':3, 'apples':1, 'grapes':2}

##>>> for i in fruit:
##	print(i)
##
##banana
##apples
##grapes
##>>> len(fruit)
##

for k,v in fruit.items():
    print(f'I have {v} {k}')













