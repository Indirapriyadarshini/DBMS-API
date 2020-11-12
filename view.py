from connect import *

def viewproduct():
    sql_select_query: str = """select * from product"""
    cursor.execute(sql_select_query)
    record = cursor.fetchall()
    print(record)

def viewdepot():
    sql_select_query: str = """select * from depot"""
    cursor.execute(sql_select_query)
    record = cursor.fetchall()
    print(record)

def viewstock():
    sql_select_query: str = """select * from stock"""
    cursor.execute(sql_select_query)
    record = cursor.fetchall()
    print(record)

def ViewAccess():
    viewproduct()
    viewdepot()
    viewstock()