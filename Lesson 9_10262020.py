
#Board Game, Lists and More - Python Basics with Sam

##x = ['Sam', 41, 'bob', 36, 'steven', '20']
##
####name = [False for i in x if str(i).isnumeric()]
##
##name = [False if str(i).isnumeric() else True for i in x]
##
##hello_split = hello.split()
##hello_split
###['Hello', 'everyone', 'how', 'are', 'you?']
##''.join(hello_split)
###'Helloeveryonehowareyou?'
##' '.join(hello_split)
###'Hello everyone how are you?'


from string import ascii_uppercase as letters

from random import choice

a_f = list(letters[:6])

num = iter(range(1,7))

hidden = [choice(a_f) + str(choice(list(range(1,7)))) for i in range(4)]

arr = [[ "O" for i in range(6)] for i in range(6)]


play = True

while play:
    print(hidden)
    num = iter(range(1,7))
    print(f"Find the {len(hidden)} X's")
    print('  '+' '.join(a_f))
    for i in arr:
        print(next(num), end = ' ')
        print(' '.join(i))
    move = input("""Q to Quit
Enter move (eg. A5):""")
    if move.lower() == 'q':
        play = False
    else:
        if move in hidden:
            hidden.pop(hidden.index(move))
            move = list(move)
            arr[int(move[1]) - 1][a_f.index(move[0])] = "X" #python goes rows then columns)
            #arr[a_f.index(move[0])][int(move[1]) - 1] = "V"
        else:
            move = list(move)
            arr[int(move[1]) - 1][a_f.index(move[0])] = " "
    if len(hidden) <= 0:
        play = False
        
    
            
