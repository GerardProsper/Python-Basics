

##  Build a Shopping List for the Command Line - Python Basics with Sam
##
##f = open('test_1.txt','w')

##f = open('test_1.txt','w')
##
##f.write('Hi how are you?')
##
##f.close()
##
##f = open('test_1.txt')
##
##print(f.read())
##
##f.close()


##
##with open('test_1.txt') as f:
##    print(f.read())
##



def my_list():
    while True:
        with open('shopping_list.txt', 'a+') as file:
##            print(file.tell())
            print("""Type anytime
EXIT : To Quit
List : To read and Delete
""")
            item = input('Enter item: ')
            if item == "EXIT":
                break
            elif item == 'please tell':
                print(file.tell())
            elif item == 'LIST':
##                print(file.tell())
                file.seek(0)
##                print(file.read())
                items = list(enumerate(file.read().split(),1))
                for count,item in items:
                    print(f'{count:3d}) {item}')
                
                while True:
                    try:
                        remove = int(input('Enter number to delete or 0 to continue: '))
                        if remove == 0:
##                            continue
                            break
                        else:
                            del items[remove - 1]
##                            print(items)
                            with open('shopping_list.txt','w+') as file:
                                for item in items:
                                    file.write(item[1] + '\n')
                                file.seek(0)
                                items = list(enumerate(file.read().split(),1))
                                for count,item in items:
                                    print(f'{count:3d}) {item}')
                                            
                    except ValueError:
                        print("If you don't want to delete enter 0")
            else:
                file.write(item + '\n')


my_list()

        

