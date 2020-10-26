
#Prime Numbers, Times Tables, & More - Python Basics with Sam

##def time_table():
##    while True:
##        try:
##            x = int(input("Please enter a number:"))
##            for row in range(x+1):
##                for col in range(x+1):
##                    print(f"{row*col:3}",end=" ")
##                print()
##        except ValueError:
##            print("Oops, please enter a number.")
##            q=input("Do you want another table? y/n ").lower()
##            if q[0] == 'n':
##                break
##            #time_table()

##time_table()
##
##def is_prime(num):
##    for i in range(2,num):
##        if num%i == 0:
##            return False
##    return True
##
##test=[3,9,11,31]
##
##for num in test:
##    print(f"{num} is a prime number {is_prime(num)}")

##y=[]
##def nth_prime(x):
##    actual_number = 3
##    prime_th_number = 2
##    if x == 1:
##        return 2
##    while prime_th_number < x:
##        actual_number += 2
##        if is_prime(actual_number): #if true will carry on to next line
##            prime_th_number += 1
##            y.append(actual_number)
##    print(f'The list of prime numbers are {y}')
##    return actual_number
##    
    

##primes = [i for i in range(2,101) if is_prime(i)]
##print(primes)


##import random



##while True:
##    number = random.randint(1,20)
##    #print(number)
##    try:
##        guess = int(input("Please enter a guess: "))
##        while guess != number:
##            if guess > number:
##                print('Please guess a smaller number')
##                guess = int(input("Please enter a guess: "))
##            else:
##                print ('Please guess a larger number')
##                guess = int(input("Please enter a guess: "))
##        else:
##            print('You guessed the correct number')
##           
##    except ValueError:
##        print("Ooops, please enter a number.")
##    q = input('Do you want to play again?').lower()
##    if q[0] == 'n':
##        break



##def leap_year(x):
##    if x % 4 == 0:
##        if x % 100 == 0:
##            if x % 400 == 0:
##                return True
##            else:
##                return False
##        else:
##            return True
##    else:
##        return False
##
##years = [ 1992, 1600, 1900, 2002, 2020 ]
##
##for year in years:
##    print (year, leap_year(year))
##              

names = ['Sam', 'Tom', 'Steve']

##for i in range(len(names)):
##    print(i+1,names[i])

##for i in enumerate(names, start=1):
##    print(i)
##
##(1, 'Sam')
##(2, 'Tom')
##(3, 'Steve')
##>>> type(i)
##<class 'tuple'>
##>>> i
##(3, 'Steve')
##>>> num, name = i
##>>> num
##3
##>>> name
##'Steve'
##>>> i
##(3, 'Steve')
##>>> type(i)
##<class 'tuple'>

for num, name in enumerate(names, start=1):
    print(num, name)

1 Sam
2 Tom
3 Steve
