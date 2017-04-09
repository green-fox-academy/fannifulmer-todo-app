import sys

def arguments():
    if len(sys.argv) == 1:
        help_printer()
    else:
        if sys.argv[1] == '-l':
            open_database()
        if sys.argv[1] == '-a':
            add_line()
        if sys.argv[1] == '-r':
            remove()
        if sys.argv[1] == '-c':
            open_database()

def help_printer():
    usage_information = open('usage_information.txt', 'r')
    information = usage_information.read()
    print(information)
    usage_information.close()

def open_database():
    database = open('database.txt', 'r')
    newdata = database.read()
    database.close()
    view()

def add_line():
    add = open('database.txt', 'a')
    add.write("\n0;" + sys.argv[2].rstrip())
    add.close()
    view()

def view():
    viewfile = open('database.txt', 'r')
    number = 1
    for line in viewfile:
        line1 = line.rstrip().split(";")
        if line1[0] == '1':
            print (number, "-", "[X]", line1[1])
        else:
            print (number,"-", "[ ]", line1[1])
        number += 1
    viewfile.close()


def remove():
    remove = open('database.txt', 'r+')
    remover = remove.readlines()
    remove_element = int(sys.argv[2])-1
    element = ''
    for i in range(len(remover)):
        if i == remove_element:
            element = remover[i]
    remover.remove(element)
    remove.close()
    newdata = open('database.txt', 'w')
    for j in range(len(remover)):
        newdata.write(remover[j])
    newdata.close()
    view()


arguments()
