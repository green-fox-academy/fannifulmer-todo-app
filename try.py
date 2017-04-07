import sys

def remove():
    remove = open('database.txt', 'r+')
    remover = remove.readlines()
    remove_element = sys.argv[2]
    # for i in range(len(remover)):
    #     print(i)
    #     if i == sys.argv[2]:
    #         print("in the statement")
    #         remover.remove(i)
    #         remover[i] = ''
    print(remover)
    remover.remove("0;Walk the dog\n")
    remover.remove(3)
    remove.close()
    return remover
    
print(remove())
