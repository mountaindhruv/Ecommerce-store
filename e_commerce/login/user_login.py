import os
os.chdir('./e_commerce')

import database.db_functions.select as select
import classes.users as user
import menu.main as main

def login():
    while (1):
        print("Enter username")
        user_name = input()
            
        # check username from User table
        #usr_cmd = "SELECT username,password FROM Users WHERE Username = '%s'" %user_name
        usr_cmd= "SELECT username,password,first_name,last_name, user_id FROM Users WHERE Username = '%s'" %user_name
        user_details = select.selector(usr_cmd)
        if not user_details:
            print("Incorrect Username\tTry again")
            continue
        Corrent_password = user_details[0][1] #string edit to get actual username for comparison

        print("Enter password")
        password = input()
        if password != Corrent_password:
            print("Incorrect password\n")
            continue

        #Update user details        
        first_name = user_details[0][0]
        last_name = user_details[0][1]
        username = user_details[0][2]
        user_id = user_details[0][4]

        #create User Object
        current_user = user.User(first_name,last_name,username,password,user_id)


        # PROCEED to login page if password and email successfully matches
        login_page(current_user)


    ### SUCCESSFUL LOGIN PAGE
def login_page(current_user):
    while(1):    
        print("\n1. Edit user settings\
            \n2. Shop\
            \n3. Cart Information\
            \n4. User History\
            \n5. Logout\
            \n6. Exit Program")
        option = -1
        try:
            option = int(input())
        except:
            print("Incorrect input type\tEnter option 1-6\n")
            continue

        if option == 1:
            while (1):
                print("\n1. Edit payment information\
                    \n2. Edit shipping information\
                    \n3. Edit username\
                    \n4. Edit password\
                    \n5. Delete User Account\
                    \n6. Go back\n")
                try:
                    user_input = int(input())

                    #edit user payment info
                    if user_input == 1:
                        current_user.edit_payment_info()
                        print("Successfully edited payment information")
                        continue

                    #edit user shipping info
                    elif user_input == 2:
                        current_user.edit_shipping_info()
                        print("Successfully edited shipping information\n")
                        continue

                    #edit username
                    elif user_input == 3:
                        current_user.edit_username()
                        print("Successfully edited username\n")
                        continue

                    elif user_input == 4:
                        current_user.edit_password()
                        print("Successfully changed password\n")

                    #delete user acount 
                    elif user_input == 5: 
                        current_user.delete_user_account()
                        print("Successfully deleted account\n")
                        main.main_func()
                        continue

                    # go back to previous page block
                    elif user_input == 6: 
                        print("Going back")
                        break
                    else: #if input is incorrect
                        print("incorrect option\nTry again")
                        continue
                except:
                    print("Incorrect input type\nSelect from option 1-4\n")
                    continue


        #TODO: complete other options upon successful login
            # elif option == 2:
            #     shop()
            # elif option == 3:
            #     cart_information()
            # elif option == 4:
            #     user_history()

        elif option == 5:
            print("logging out\n")
            main.main_func()
        elif option == 6:
            print("Exiting\n")
            sys.exit()
        else:
            print("Wrong input:\tTry again\n")
    