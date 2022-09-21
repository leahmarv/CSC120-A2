# Leah Marville
# Assignment 2: CSC 120
# 9/20/2022

class ResaleShop:

    from typing import Dict, Union, Optional

    inventory: Dict[int, Dict[str, Union[str, int, bool]]] = {}
    itemID: int = 0

    def __init__(self, inventory: dict, itemID: int):
        self.__inventory = inventory
        self.__itemID = itemID

    def buy(computer: Dict[str, Union[str, int, bool]]):
        global itemID
        global inventory
        itemID += 1 # increment itemID
        inventory[itemID] = computer
        return itemID

    def update_price(item_id: int, new_price: int):
        if item_id in inventory:
            inventory[item_id]["price"] = new_price
        else:
            print("Item", item_id, "not found. Cannot update price.")

    def sell(item_id: int):
        if item_id in inventory:
            del inventory[item_id]
            print("Item", item_id, "sold!")
        else: 
            print("Item", item_id, "not found. Please select another item to sell.")
    
    def print_inventory():
    # If the inventory is not empty
        if inventory:
        # For each item
            for item_id in inventory:
            # Print its details
                print(f'Item ID: {item_id} : {inventory[item_id]}')
        else:
            print("No inventory to display.")

    def refurbish(item_id: int, new_os: Optional[str] = None):
        if item_id in inventory:
            computer = inventory[item_id] # locate the computer
            if int(computer["year_made"]) < 2000:
                computer["price"] = 0 # too old to sell, donation only
            elif int(computer["year_made"]) < 2012:
                computer["price"] = 250 # heavily-discounted price on machines 10+ years old
            elif int(computer["year_made"]) < 2018:
                computer["price"] = 550 # discounted price on machines 4-to-10 year old machines
            else:
                computer["price"] = 1000 # recent stuff

            if new_os is not None:
                computer["operating_system"] = new_os # update details after installing new OS
        else:
            print("Item", item_id, "not found. Please select another item to refurbish.")