import sys
sys.path.append('/home/gabriel/Programs/SWE/Ecommerce-store/e_commerce')

import database.db_functions.select as select


def view_user_history(user_id):
    history_query = "SELECT * FROM User_History WHERE USER_ID = '%s'" %user_id
    history_result = select.selector(history_query)

    output_format ="ISBN= %s, Title='%s', Author='%s', Year=%s, Genre='%s', Quantity=%s, Price=$%s"
    #print out user history to user
    for data in history_result:
        print(output_format %(data[0],data[1],data[2],data[3],data[4],data[6],data[7]))
