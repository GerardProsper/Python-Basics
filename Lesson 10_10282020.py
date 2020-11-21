
## Chicken Nuggets and itertools - Python Basics with Sam

##t,n,s = 20,9,6
##
##def nuggets(ttl):
##    #global x
##    x = {}
##    for i in range(10):
##        for j in range(10):
##            for k in range(10):
##                tot = i*t+j*n+k*s
##                #print(tot)
##                #print(i,j,k)
##                #print()
##                x[tot] = i,j,k
##                if ttl == tot:
##                    break
##            if ttl == tot:
##                break
##        if ttl == tot:
##            break
##    print()
##    print(f"""{ttl}
##{x[ttl][2]}: 6 peice
##{x[ttl][1]}: 9 peice
##{x[ttl][0]}: 20 peice""")
##                
##comb = []
##
##for i in range(101):
##    try:
##        nuggets(i)
##        comb.append(i)
##    except:
##        print(i, 'no results')




##from itertools import chain
##
##x = 'abc'
##y = 'def'
##z = 'ghi'
##
####for i in chain(x,y,z):
####    print(i)
##
##arr = [x,y,z]
##
##for i in chain.from_iterable(arr):
##    print(i)



##from itertools import combinations as comb
##
##letter = 'ABCDEFG'
##
##x = comb(letter,3)
##
##y = [''.join(i) for i in x]

##
##from itertools import count
##
##x = count(1)



##
##>>> print()
##
##>>> print('\n')
##
##
##>>> print('\n',end='') #The end='' supress the line)
##
##>>> 
##


##
##
##'''
##   1
## 2 3 4
##5 6 7 8 9
##
##'''
##
##
##from itertools import count
##
##start = count(1,2)
##
##num = count(1)
##
##for i in range(1,4):
##    print(('  ')*(3-i),end = '')
##    #for j in range(next(start)):
##        #print(next(num),end = ' ')
##    #print()










##for a in range(3):
##    print(a)#, end='')
##    for b in range(3):
##            print(a,b)#, end='')
##
##		
##0
##0 0
##0 1
##0 2
##1
##1 0
##1 1
##1 2
##2
##2 0
##2 1
##2 2
##
##
##
###Below here shows the triangle number game(s) with reverse and a
### better understanding of the print(end='') function on how it works


##
##
##>>> for i in range(10):
##	for j in range(1,i+1):
##		print(j,end='')
##	print()
##
##	
##
##1
##12
##123
##1234
##12345
##123456
##1234567
##12345678
##123456789





##
##>>> for i in range(1,10):
##	for j in range(10-i,1,-1):
##		print(' ', end='')
##	for k in range(1,i+1):
##		print(k,end='')
##	print()
##
##	
##        1
##       12
##      123
##     1234
##    12345
##   123456
##  1234567
## 12345678
##123456789
##>>> for i in range(1,10):
##	for j in range(10-i,1,-1):
##		print('x', end='')
##	for k in range(1,i+1):
##		print(k,end='')
##	print()
##
##	
##xxxxxxxx1
##xxxxxxx12
##xxxxxx123
##xxxxx1234
##xxxx12345
##xxx123456
##xx1234567
##x12345678
##123456789
##>>> for i in range(1,10):
##	for j in range(10-i,1,-1):
##		print('', end=' ')
##	for k in range(1,i+1):
##		print(k,end='')
##	print()
##
##	
##        1
##       12
##      123
##     1234
##    12345
##   123456
##  1234567
## 12345678
##123456789
##>>> for i in range(1,10):
##	for j in range(10-i,1,-1):
##		print('', end='x')
##	for k in range(1,i+1):
##		print(k,end='')
##	print()
##
##	
##xxxxxxxx1
##xxxxxxx12
##xxxxxx123
##xxxxx1234
##xxxx12345
##xxx123456
##xx1234567
##x12345678
##123456789
##>>> for i in range(1,10):
##	for j in range(10-i,1,-1):
##		print('x', end=' ')
##	for k in range(1,i+1):
##		print(k,end='')
##	print()
##
##	
##x x x x x x x x 1
##x x x x x x x 12
##x x x x x x 123
##x x x x x 1234
##x x x x 12345
##x x x 123456
##x x 1234567
##x 12345678
##123456789
##>>> for i in range(1,10):
##	for j in range(10-i,1,-1):
##		print('x', end='x')
##	for k in range(1,i+1):
##		print(k,end='')
##	print()
##
##	
##xxxxxxxxxxxxxxxx1
##xxxxxxxxxxxxxx12
##xxxxxxxxxxxx123
##xxxxxxxxxx1234
##xxxxxxxx12345
##xxxxxx123456
##xxxx1234567
##xx12345678
##123456789
##>>> for i in range(1,10):
##	for j in range(10-i,1,-1):
##		print(' ', end='')
##	for k in range(1,i+1):
##		print(k,end=' ')
##	print()
##
##	
##        1 
##       1 2 
##      1 2 3 
##     1 2 3 4 
##    1 2 3 4 5 
##   1 2 3 4 5 6 
##  1 2 3 4 5 6 7 
## 1 2 3 4 5 6 7 8 
##1 2 3 4 5 6 7 8 9 
##>>> for i in range(1,10):
##	for j in range(10-i,1,-1):
##		print(' ', end='')
##	for k in range(1,i+1):
##		print(k,end='x')
##	print()
##
##	
##        1x
##       1x2x
##      1x2x3x
##     1x2x3x4x
##    1x2x3x4x5x
##   1x2x3x4x5x6x
##  1x2x3x4x5x6x7x
## 1x2x3x4x5x6x7x8x
##1x2x3x4x5x6x7x8x9x
##>>> for i in range(1,10):
##	for j in range(10-i,1,-1):
##		print(' ', end=' ')
##	for k in range(1,i+1):
##		print(k,end=' ')
##	print()
##
##	
##                1 
##              1 2 
##            1 2 3 
##          1 2 3 4 
##        1 2 3 4 5 
##      1 2 3 4 5 6 
##    1 2 3 4 5 6 7 
##  1 2 3 4 5 6 7 8 
##1 2 3 4 5 6 7 8 9 
##>>> for i in range(1,10):
##	for j in range(10-i,1,-1):
##		print('a', end='b')
##	for k in range(1,i+1):
##		print(k,end='c')
##	print()
##
##	
##abababababababab1c
##ababababababab1c2c
##abababababab1c2c3c
##ababababab1c2c3c4c
##abababab1c2c3c4c5c
##ababab1c2c3c4c5c6c
##abab1c2c3c4c5c6c7c
##ab1c2c3c4c5c6c7c8c
##1c2c3c4c5c6c7c8c9c
##>>>



##
##
##def pyramid(x):
##    for i in range(x,-1,-1):
##        print(' '*i, end='')
##        for j in range(x + 1 - i):
##            print(j,end='')
##        for k in range(x - i - 1, -1,-1):
##            print(k,end='')
##        print()
##
##pyramid(4)
##


##
##def dia(x):
##    for i in range(x,-1,-1):
##        print(' '*i, end='')
##        for j in range(x + 1 - i):
##            print(j,end='')
##        for k in range(x - 1 - i, -1,-1):
##            print(k,end='')
##        print()
##    for q in range(1,x+1):
##        print(' '*q, end='')
##        for a in range(x + 1 - q):
##            print(a, end='')
##        for b in range(a - 1, -1,-1): #can also be range(x - 1 - q, -1, -1)
##            print(b,end='')
##        print()
##        
##dia(4)
##dia(9)
##
##
