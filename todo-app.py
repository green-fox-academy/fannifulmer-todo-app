import sys

def arguments():
    if len(sys.argv) == 1:
        help_printer()
    else:
        if sys.argv[1] == '-l':
            open_database()

def help_printer():
    usage_information = open('usage_information.txt', 'r')
    information = usage_information.read()
    print(information)
    usage_information.close()

def l_argument():
    if sys.argv[1] == '-l':
        open_database()

def a_argument():
    if sys.argv[1] == '-a':
        add_line()

def add_line():
    add = open('database.txt', 'a')
    add.write("\n0;" + sys.argv[2].rstrip())
    add.close()

def r_argument():
    if sys.argv[1] == '-r':
        open_database()

def c_argument():
    if sys.argv[1] == '-c':
        open_database()

def open_database():
    database = open('database.txt', 'r')
    newdata = database.read()
    print(newdata)
    database.close()

arguments()
a_argument()
open_database()
#print("3;Do homework".split(";"))
