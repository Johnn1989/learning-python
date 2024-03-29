'''
Dev: John E.
Script description: Configure  SQLite3 data base
'''

#Import engine database package
import sqlite3

#Create a database connection (Database name)
con = sqlite3.connect('market.db')

#Creating cursor object by conection => Let us execute sql commands or operations (Query)
cur = con.cursor()

#Create users table
user_table = '''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        firstname TEXT NOT NULL,
        lastname TEXT NOT NULL,
        ident_number TEXT UNIQUE NOT NULL,
        email TEXT  UNIQUE NOT NULL,
        password TEXT NOT NULL
        );
'''

#Execute SLQ (Query)
cur.execute(user_table)

#Save changes in database => push to database
con.commit()

#print(":::Database market has been create :::")

#Close connection
#con.close()