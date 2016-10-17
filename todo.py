# This script manages a basic todolist

#list: lists the items.
#add: adds a new item.
#mark: marks an item by the number of the line.
#archive: the marked item gets deleted.
#quit: exit the code.

#modul import for script to terminate on the quit command.
import sys

#this creates the empty global todolist which we will manipulate.
todo_list = []
#markerinput defined as a global variable.
markerinput = ''
#This variable is only to keep a forever loop alive.
indefinitloop = 'unknown'

#list function
def show_list():
    global todo_list
    global markerinput
    a = 1
    for y in todo_list:
        if a == markerinput:
            print ('%s%s %s %s' %(a,'.','[x]',y))
        else:
            print('%s%s %s %s' % (a, '.', '[ ]', y))
        a += 1

#add function
def addto_list():
    global todo_list
    itemtoadd = input("Add an item:")
    todo_list.append(itemtoadd)

# mark fuction. Only 1 item can be marked symultaniously.
def mark_item():
    global markerinput
    global indefinitloop
    print("You saved the following to-do items:")
    show_list()
    while (indefinitloop != 'forever'):
        markerinput = input("Which one you want to mark as completed:")
        if markerinput.isdigit():
            markerinput = int(markerinput)
            break
        else:
            print("This is not a number. Please enter the number of the line you wish to select.")

#archive function
def archive_item():
    global todo_list
    global markerinput
    a = 0
    for y in todo_list:
        if a == markerinput:
            b = a -1
            todo_list.pop(b)
            markerinput = ''
        a += 1


#Quit function
def quit_app():
    sys.exit()


#this while loop is which will ask the user for input.
while (indefinitloop != 'forever'):
    userinput = input("Please specify a command [list, add, mark, archive, quit]:")
    if userinput == 'list':
        show_list()
    elif userinput == 'add':
        addto_list()
    elif userinput == 'mark':
        mark_item()
    elif userinput == 'archive':
        archive_item()
    elif userinput == 'quit':
        quit_app()
    else:
        print ("That command is not handeled by this scrip please use one of these [list, add, mark, archive, quit] ")