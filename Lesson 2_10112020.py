## Python For Loops, Functions, and Random - Python Basics with Sam

##numbers = [1,-5,2,-4,0,6,-10,3]
##
##
##def Pos_Neg(x):
##    if x == 0:
##        print ("Zero")
##    else:
##        if x > 0:
##            print ("positive")
##        else:
##            print("negative")
##
##for number in numbers:
######    print (number)
##    Pos_Neg(number)

##for row in range(5):
##    for col in range(5):
##        print(col,end='')
##    print()



#for row in range(1,11):
#    for col in range(1,row+1): 
#        print(col,end="")
#   print()

#per above code there is a difference between the above and
# for row in range(1,11):
#   for col in range (1,11):
#       etc...
# the column range would have the same length as row (10) here but
# would have length of 9 for col in Original code.


#for row in range(1,14):
#    for col in range(1,row+1): 
#        print('{:3}'.format(col),end="") #this '{:3}' is a placeholder
#    print()


##def hello():
##    name = input("Enter name:")
##    print("Hello {} nice to meet you." .format(name))  #this {} is a placeholder
##
##hello()

##
##count=int(input("Enter a number: "))
##print("ready")
##while count >= 0:
##    print (count)
##    count -= 1
##print("Isabel is a dumbasss!!!!")
##


numbers = [1,-5,2,-4,0,6,-10,3] #this is a list

##pos = [] 
##neg = []
##
##for number in numbers:
##    if number > 0:
##        pos.append(number)
##    else:
##        neg.append(number)

## pos = [i for i in numbers if i > 0]

##list_numbers = []
##
##for i in range (3):
##    list_numbers.append(list(range(1,6)))

import random

## number = [random.randint(1,5) for i in range(10)]

##numbers = [i for i in range(1,26)]
##
##random.shuffle(numbers)

shuffled = [12, 1, 14, 21, 7,
            4, 16, 10, 22, 25,
            5, 8, 18, 23, 20,
            2, 3, 6, 24, 15,
            13, 17, 11, 19, 9]

horses = [[],
          [],
          [],
          [],
          []
          ]

##for i in range(5):
##    for j in range(5):
##        horses[j].append(shuffled.pop())

horses = [[9, 15, 20, 25, 7],
[19, 24, 23, 22, 21],
[11, 6, 18, 10, 14],
[13, 2, 5, 4, 12],
[17, 3, 8, 16, 1],
]


for race in horses:
##    race.sort()
    race.sort()
    print(race)

def last(x):
    return x[-1]

print()
new_horses = sorted(horses,key=last, reverse=True)

print()
for race in new_horses:
    race.sort()
    print(race)


## 1  3 13 19 25
## 5 14 18 20 24
## 6  7 15 17 23
## 4  8  9 10 22
## 2 11 12 16 21
