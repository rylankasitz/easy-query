import sqlite3
import os

def run_sqlfile(database_name: str, sql_file: str, location: str):
    if not os.path.isdir(location + '/db'): os.mkdir(location + '/db')
    conn = sqlite3.connect(location + '/db/' + str(database_name) + ".db") 
    c = conn.cursor()

    with open(sql_file, 'r') as content_file:
        c.execute(content_file.read())
    
    conn.commit()
    conn.close() 

def print_table(database_name: str, table_name: str, location: str):
    conn = sqlite3.connect(location + '/db/' + str(database_name) + ".db") 
    c = conn.cursor()
    for row in c.execute('SELECT * FROM ' + table_name):
        print(row)
    conn.commit()
    conn.close()

def insert_into_table(database_name: str, table_name: str, attributes: str, values: str, location: str):
    conn = sqlite3.connect(location + '/db/' + str(database_name) + ".db") 
    c = conn.cursor()
    
    str_attributes = ""
    v_count = "?,"*len(values)
    v_count = v_count[0:len(v_count) - 1]
    for a in attributes: str_attributes += a
    c.execute('INSERT OR REPLACE INTO ' + table_name + '(' + str_attributes + ') VALUES (' + v_count + ')', values)
    
    conn.commit()
    conn.close()