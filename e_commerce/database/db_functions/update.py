import sqlite3
import sys


def update_data(query):
    ## attempts to connect to the database
    try:
        connection = sqlite3.connect("sqlite.db")

    except:
        print("Failed connection.")

        ## exits the program if unsuccessful
        sys.exit()

    ## cursor to send queries through
    cursor = connection.cursor()
    cursor.execute(query) # update data in the table
    connection.commit() # commit changes


    cursor.close()
    connection.close()
