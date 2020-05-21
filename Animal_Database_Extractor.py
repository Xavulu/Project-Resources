
import pymysql

import getpass

#If you want to learn more about pymysql look here:
#http://zetcode.com/python/pymysql/

#Insert your mysql
host = "localhost" #No need to modify if you are using goorm
username = input("\n\n\n\nEnter username: ") #FILL THIS OUT 
password = getpass.getpass("\n\n\n\nEnter your password: ")  #FILL THIS OUT
database = "animals" #FILL THIS OUT, This database should exist already.

con = pymysql.connect(host,username,password,database)



#Database functions
def databaseFetchOne(query): #This function will return only ONE row the top/first row
    cur = con.cursor()
    cur.execute(query)
    return cur.fetchone()

def databaseFetchAll(query):
    cur = con.cursor()
    cur.execute(query)
    return cur.fetchall()

def databaseRunQuery(query):
    cur = con.cursor()
    amount = cur.execute(query)
    con.commit()
    return amount

count = 0

entry = ''


states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY', 'AS', 'PR', 'VI', 'UM', 'GU', 'DC']

databaseRunQuery("DROP DATABASE IF EXISTS animals;")

databaseRunQuery("CREATE DATABASE IF NOT EXISTS animals;")

databaseRunQuery("USE animals;")

databaseRunQuery("CREATE TABLE species(oT VARCHAR(20), name VARCHAR(100), status VARCHAR(30), refuge VARCHAR(100), state VARCHAR(20));")

databaseRunQuery("CREATE TABLE states(state VARCHAR(2), count INT);")

with open('Endangered Species List.txt') as file:
    for line in file:
        count += 1
        if count > 1:
            line = line.split(', ')
        if line[0] in states:
            if entry != '':
                if len(line) == 2:
                    entry += '"' + line[0] + '"'
                    success = databaseRunQuery("INSERT INTO species VALUES (" + entry + ")")
                    if(success == True):
                        print("\nCreated new row with data!\n")
                    else:
                        print("\nError!\n")
                    entry = ''
                else:
                    x = 0
                    entry += '"'
                    while x < len(line) - 2:
                        entry += line[x] + ", "
                        x += 1
                        if x == len(line) - 2:
                            entry += line[x] + '"'
                            x += 1
                            success = databaseRunQuery("INSERT INTO species VALUES (" + entry + ")")
                            if(success == True):
                                print("\nCreated new row with data!\n")
                            else:
                                print("\nError!\n")
                            entry = ''
        if len(line) == 5:
            if line[0] != 'Plant' and line[0] not in states:
                entry += '"' + line[0] + '", '
                entry += '"' + line[1] + '", '
                entry += '"' + line[2] + '", '
                entry += '"' + line[3] + '", '
        elif len(line) == 6:
            if line[0] == 'Bird':
                entry += '"' + line[0] + '", '
                entry += '"' + line[2] + line[1] + '", '
                entry += '"' + line[3] + '", '
                entry += '"' + line[4] + '", '
            elif line[0] == 'Fish':
                entry += '"' + line[0] + '", '
                entry += '"' + line[1] + '", '
                entry += '"' + line[3] + '", '
                entry += '"' + line[4] + '", '             
file.close()
    
for state in states:
    count = 0
    oldname = ''
    name = ''
    with open('Endangered Species List.txt') as file:
        file.seek(0)
        for line in file:
            line = line.split(', ')
            if len(line) > 4:
                if len(line[0]) > 2:
                    name = line[1]            
            else:
                if name != oldname:
                    if line[0] == state:
                        count += 1
                        oldname = name
                    if len(line) > 1:
                        if line[1] == state:
                            count += 1
                            oldname = name
                    if len(line) > 2:
                        if line[2] == state:
                            count += 1
                            oldname = name
                    if len(line) > 3:
                        if line[3] == state:
                            count += 1
                            oldname = name
    file.close()
    success = databaseRunQuery('INSERT INTO states VALUES ( "' + state + '", ' + str(count) + ")")
    if(success == True):
        print("\nCreated new row with data!\n")
    else:
        print("\nError!\n")










