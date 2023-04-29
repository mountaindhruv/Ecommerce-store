import sys
sys.path.append('/home/gabriel/Programs/SWE/Ecommerce-store/e_commerce')

import database.db_functions.select as select
import database.db_functions.delete as delete
import classes.inventory as inventory
import login.user_history as user_history



class Cart():

    def __init__(self, user_id) -> None:
        self.user_id = user_id


    # view items in cart method
    def view_cart(self):
        cart = select.selector("SELECT * FROM Cart")

        count = 1
        output_format ="%s. ISBN= %s, Title='%s', Author='%s', Year=%s, Genre='%s', Quantity=%s, Price=$%s"

        for data in cart:
            print(output_format %(count,data[0],data[1],data[2],data[3],data[4],data[6],data[7]))
            count += 1


    # remove item from cart method
    def remove_from_cart(self, ISBN):
        inv = inventory.Inventory()
        quantity = select.selector("SELECT Quantity FROM Cart WHERE ISBN=%s" %ISBN)
        delete.delete_data("DELETE FROM Cart WHERE ISBN=%s" %ISBN) # delete item from cart

        # add removed items to stock inventory
        quantity = quantity[0][0]
        inv.increase_inv_item(ISBN, quantity)

        
    #checkout method
    def checkout(self):
        # items from cart to user_history
        user_history.add_to_user_history()

        # remove everything from cart
        delete.delete_data("DELETE FROM Cart")
    