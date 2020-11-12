from connect import *

def Prod_add(prod):
   postgres_insert_query = """delete from stock where prod in (select prod from product where prod=%s);
delete from product where prod = %s"""
   record_to_insert = (prod,prod)
   cursor.execute(postgres_insert_query, record_to_insert)

   connection.commit()
   count = cursor.rowcount
   print (count, "Record deleted successfully into product table")

def depot_add(dep):
   postgres_insert_query = """delete from stock where dep in (select dep from depot where dep=%s);
delete from depot where dep = %s"""
   record_to_insert = (dep,dep)
   cursor.execute(postgres_insert_query, record_to_insert)

   connection.commit()
   count = cursor.rowcount
   print (count, "Record deleted successfully into Depot table")

def DeleteAccess():
    try:
        Do= input("Enter 1 for Prod / 2 for Depot: ")
        if Do=='1':
            prod = input("Id: ")
            Prod_add(prod)
        elif Do=='2':
            dep = input("Id: ")
            depot_add(dep)
        else:
            print(""" Enter 1/2 """)
            DeleteAccess()

    except (Exception, psycopg2.Error) as error:
        if (connection):
            print("Failed...!!", error)