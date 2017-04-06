import sys

def help_printer():
    usage_information = open('usage_information.txt', 'r')
    usage_information = usage_information.read()
    print(usage_information)

def arg_reader():
    if len(sys.argv) == 1:
        help_printer()


arg_reader()
#print("3;Do homework".split(";"))
