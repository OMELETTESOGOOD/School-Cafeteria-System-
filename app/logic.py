# app/cli_logic.py
from app.crud import get_user_by_id, list_menu_items, get_inventory_for, place_order, seed_if_empty
from tabulate import tabulate

def greet_user(user_id:int):
    user = get_user_by_id(user_id)
    if not user:
        return None, f"ID {user_id} not found. Enter ID between 1 and 30."
    return user, f"Welcome {user.name}! Please choose an item from the menu."

def show_menu():
    items = list_menu_items()
    table = [(mi.id, mi.name, mi.price) for mi in items]  # list of tuples
    headers = ("ID", "Menu Item", "Price")
    print(tabulate(table, headers=headers, tablefmt="grid"))

def get_menu_ids():
    items = list_menu_items()
    return [mi.id for mi in items]  # list of ids

def show_remaining(menu_item_id:int):
    inv = get_inventory_for(menu_item_id)
    if inv:
        print(f"Remaining for '{inv.menu_item.name}': {inv.remaining}")
    else:
        print("No inventory record found.")

# used to seed DB from CLI if empty
def ensure_seeded():
    seed_if_empty()
