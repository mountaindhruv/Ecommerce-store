import sqlite3
import sys


def insert_data(query):
    ## attempts to connect to the database
    try:
        connection = sqlite3.connect("sqlite.db")

    except:
        print("Failed connection.")

        ## exits the program if unsuccessful
        sys.exit()

    ## cursor to send queries through
    cursor = connection.cursor()
    cursor.execute(query) # insert into table
    connection.commit() # commit changes

    cursor.close()
    connection.close()
