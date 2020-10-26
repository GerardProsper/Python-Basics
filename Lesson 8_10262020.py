
# Generators and Classes - Python Basics with Sam

# x = 5
# x is a object, its a variable that 5 is assigned to x and that
# type of variable in an int



##class rect():
##
##    def __init__(self,length,width):
##        self.length = length
##        self.width  = width
####        print(f"Your rectangle is {length} by {width}")
##        
##    def __repr__(self):
##        return "rect({self.length},{self.width})".format(self=self)
##    
##    def __str__(self):
##        return f"Your rectangle is {self.width} by {self.length}"
##    
##    def perim(self):
##        print(2*self.width*self.length)
##
##    def area(self):
##        print(self.width*self.length)
##
##
##
##
##
##class Dog():
##
##    species = "Canine"
##    voice   = "Bark"
##
##
##class poodle(Dog):
##    pass





# iterate through iterable objects
# You can iterate through iterable and iterators
# but not all iterables are iterators


##name = 'Sam'
##
##name = iter(name)
##
##for i in name:
##    print(i)




##def series(num):
##    n = 0
##    while n < num:
##        yield n
##        n += 1
##
##five = series(5)



'''
78 --> 80
77 --> 77
93 --> 95
72 --> 72
74 --> 75

'''

##def fives(x):
##    if x%5 == 4:
##        x += 1
##    elif x%5 == 3:
##        x += 2
##    print(x)


def fives(x):
    if x%5 == 3 or x%5 == 4:
        x += ( 5 - x%5)
    print(x)

grades = [72,98,94,83,71,73,100]

for grade in grades:
    print(grade, end =" "), fives(grade)


