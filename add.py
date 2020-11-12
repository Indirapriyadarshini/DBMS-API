from connect import *

def Prod_add(prod,pname,price):
   postgres_insert_query = """ INSERT INTO product (prod, pname, price) VALUES (%s,%s,%s)"""
   record_to_insert = (prod, pname, price)
   cursor.execute(postgres_insert_query, record_to_insert)

   connection.commit()
   count = cursor.rowcount
   print (count, "Record inserted successfully into Product table")



def depot_add(dep, addr, volume):
   postgres_insert_query = """ INSERT INTO depot (dep, addr, volume) VALUES (%s,%s,%s)"""
   record_to_insert = (dep, addr, volume)
   cursor.execute(postgres_insert_query, record_to_insert)

   connection.commit()
   count = cursor.rowcount
   print (count, "Record inserted successfully into Depot table")

def stock_add(prodId, depId, quantity):
   postgres_insert_query = """ INSERT INTO stock (prod, dep, quantity) VALUES (%s,%s,%s)"""
   record_to_insert = (prodId, depId, quantity)
   cursor.execute(postgres_insert_query, record_to_insert)

   connection.commit()
   count = cursor.rowcount
   print (count, "Record inserted successfully into Stock table")

def AddAccess():
    try:
        Do= input("Enter 1 for Prod/2 for Depot/3 for stock: ")
        if Do=='1':
            prod = input("Id: ")
            pname = input("Name: ")
            price = input("price: ")
            Prod_add(prod,pname,price)
        elif Do=='2':
            dep = input("Id: ")
            addr = input("Address: ")
            volume = input("Volume: ")
            depot_add(dep, addr, volume)
        elif Do=='3':
            prodId = input("prodId: ")
            depId = input("depId: ")
            quantity = input("Quantity: ")
            stock_add(prodId, depId, quantity)
        else:
            print(""" Enter 1/2/3 """)
            AddAccess()

    except (Exception, psycopg2.Error) as error:
        if (connection):
            print("Failed...!!", error)