import sys
sys.path.append('/home/gabriel/Programs/SWE/Ecommerce-store/e_commerce')

import create_account.create as create
import login.user_login as user_login

def main_func():
    while (1):
        print("\n1. Login\n2. Create Account\n3. Exit Program")
        choice = -1
        try:
            choice = int(input())
        except:
            print("\nIncorrect option\Try again")
            continue
        if choice == 1: 
            user_login.login()
        elif choice == 2:
            create.create_account()
        elif choice == 3:
            print("\nExiting...Good bye!\n")
            break
        else:
            print("Incorrect option: Try again")
        
    sys.exit()


if __name__ == '__main__':
    
    main_func()
