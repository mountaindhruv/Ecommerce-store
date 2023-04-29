import sqlite3
import sys

## attempts to connect to the database
def delete_data(query):
    try:
        connection = sqlite3.connect("sqlite.db")

    except:
        print("Failed connection.")

        ## exits the program if unsuccessful
        sys.exit()

    ## cursor to send queries through
    cursor = connection.cursor()

    cursor.execute(query)
    connection.commit()

    print("Deleted Account")

    cursor.close()
    connection.close()


# cmd = "DELETE FROM Users"
# x = "DELETE  FROM Shipping_Info"
# y = "DELETE  FROM Payment_Info"
# delete_data(cmd)
# delete_data(x)
# delete_data(y)
