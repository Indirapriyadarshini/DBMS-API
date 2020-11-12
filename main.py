from connect import *
from view import *
from add import *
from delete import *

def All():
    Do= input("Enter 1 for view / 2 for add / 3 for delete / exit: ")
    if Do=='1':
        ViewAccess()
        con = input("do you want to continue y/n: ")
        if con=='y':
            All()
        else:
            end_conection()
    elif Do=='2':
        AddAccess()
        con = input("do you want to continue y/n: ")
        if con == 'y':
            All()
        else:
            end_conection()
    elif Do=='3':
        DeleteAccess()
        con = input("do you want to continue y/n: ")
        if con == 'y':
            All()
        else:
            end_conection()
    elif Do == 'exit':
        end_conection()
    else:
        print(""" Enter 1/2/3/exit """)

All()