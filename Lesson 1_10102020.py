
## Intro to Python Livestream - Python Basics with Sam






name = 'Gerard'

####print(name)
##
##for _ in range(3):
##    print(name)
##
##for i in range(1,5):
##    print(i)

l_5=list(range(5))

##    
##for i in range(2,10,2):
##    print(i)

##for num in l_5:
##    print(num)
##    print(num*2)
##    print()
##
##letters = 'PTJB'
##
##for letter in letters:
##    print(letter + name[1:])

##def hello():
##    name = input("Enter name:")
##    print('Hello ' + name)
##
##hello()

##def blank():
##    print()
##
##def blank_3():
##    blank()
##    blank()
##    blank()
##
##def blank_9():
##    blank_3()
##    blank_3()
##    blank_3()
##
##blank_9()

numbers = [1,-5,2,-4,0,6,-10,3]

##for number in numbers:
##    if number % 2 == 0:
##        print(number, "is even")
##    else:
##        print (number, "is odd")
##            
    
##for number in numbers:
##    if number == 0:
##        print ("Zero")
##    elif number > 0:
##        print ("positive")
##    else:
##        print("negative")
##
##def even(x):
##    """ enter number to be checked if even"""
##    if x % 2 == 0:
##        return True


##def even(x):
##    return x % 2 == 0
##
##def odd(y):
##    return y % 2 != 0
##
##print (even(4))
##
##print (odd(3))

##for row in range (5):
##       for col in range(5):
##        print(col,end='') ##cannot use 'sep' as only calling out col and not row. 'end' makes a row become column (or everything one line) https://www.youtube.com/watch?v=1CGZ9YDCeWg 
##    print() # if have print with 'for col' then it's the same as just print(col) as print () supersedes print (col, end=''). Putting it here makes it break after finishing col
##
##
##01234
##01234
##01234
##01234
##01234
##
##
##>>> for row in range (5):
##	for col in range (5):
##		print(col,end='')
##
##		
##0123401234012340123401234
##
##
##>>> for row in range (5):
##	for col in range (5):
##		print(col,end='')
##		print()
##
##		
##0
##1
##2
##3
##4
##0
##1
##2
##3
##4
##0
##1
##2
##3
##4
##0
##1
##2
##3
##4
##0
##1
##2
##3
##4
##


adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
people = [" Malaysia", "Singapore", "China"]
for x in adj:
    for y in fruits:
	for z in people:
	print(x,y,z)
