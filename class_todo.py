import sys
class Todo():
    def __init__(self):
        if len(sys.argv) == 1:
            self.help_printer

    def help_printer(self):
        usage_information = open('usage_information.txt', 'r')
        usage_information = usage_information.read()
        print(usage_information)

class ArgumentL(Todo):
    def argl_reader(self):
        if sys.argv[1] == '-l':
            open_database()

    def open_database():
        database = open('database.txt', 'r')
        database = database.readlines()
        print(database)

'''def help_printer():
    usage_information = open('usage_information.txt', 'r')
    usage_information = usage_information.read()
    print(usage_information)

def arg_reader():
    if len(sys.argv) == 1:
        help_printer()
    else:
        if sys.argv[1] == '-l':
            open_database()

def open_database():
    database = open('database.txt', 'r')
    database = database.readlines()
    print(database)'''


open = Todo()
