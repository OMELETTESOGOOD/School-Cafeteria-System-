# app/crud.py
from sqlalchemy import select, update
from app.db import SessionLocal
from app.models import User, MenuItem, Inventory, Order

def get_user_by_id(user_id:int):
    with SessionLocal() as s:
        stmt = select(User).where(User.id == user_id)
        res = s.execute(stmt).scalars().first()
        return res

def list_menu_items():
    with SessionLocal() as s:
        stmt = select(MenuItem).order_by(MenuItem.id)
        return s.execute(stmt).scalars().all()

def get_inventory_for(menu_item_id:int):
    with SessionLocal() as s:
        stmt = select(Inventory).where(Inventory.menu_item_id == menu_item_id)
        return s.execute(stmt).scalars().first()

def place_order(user_id:int, menu_item_id:int):
    """
    Places an order: creates Order row and increments qty_sold in Inventory.
    Returns (success:bool, message:str, remaining_qty:int | None)
    """
    with SessionLocal() as s:
        inv = s.execute(select(Inventory).where(Inventory.menu_item_id == menu_item_id)).scalars().first()
        if not inv:
            return False, "Inventory item not found.", None
        if inv.remaining <= 0:
            return False, f"Sorry, {inv.menu_item.name} is out of stock.", 0

        # create order and increment qty_sold
        order = Order(user_id=user_id, menu_item_id=menu_item_id)
        inv.qty_sold += 1
        s.add(order)
        s.add(inv)
        s.commit()
        s.refresh(inv)
        return True, f"Here is your {inv.menu_item.name}.", inv.remaining

def seed_if_empty():
    """
    Creates users (IDs 1-30), menu items, inventory (70 each) if absent.
    """
    students = [
        "Adam","John","Nelly","Neol","Muthaura","Kihumba","Chasia","Moses","Aaron","Joshua",
        "Omondi","Racheal","Simone","Njeri","Onesmus","Atieno","Esther","Ruth","Preshy","Deborah",
        "Makaila","Karanja","Jonah","Peace","Micah"
    ]  # 25 names

    teacher = ["Kimani","Onyango","Kipkirui","Mburu","Nduta"]  # 5 names (26-30)

    menu_items = [
        ("ugali & matumbo", 100),
        ("rice & beef", 150),
        ("rice & beans", 120),
        ("tea & mandazi", 50),
        ("chicken sandwich", 180),
    ]

    with SessionLocal() as s:
        # users
        existing = s.query(User).count()
        if existing == 0:
            users = []
            for idx, name in enumerate(students, start=1):
                users.append(User(id=idx, name=name, role="student"))
            for idx, name in enumerate(teacher, start=26):
                users.append(User(id=idx, name=name, role="teacher"))
            s.add_all(users)

        # menu items & inventory
        if s.query(MenuItem).count() == 0:
            menu_objs = []
            inv_objs = []
            for name, price in menu_items:
                mi = MenuItem(name=name, price=price)
                menu_objs.append(mi)
            s.add_all(menu_objs)
            s.flush()  # populate IDs for menu items
            for mi in menu_objs:
                inv = Inventory(menu_item_id=mi.id, initial_qty=70, qty_sold=0)
                inv_objs.append(inv)
            s.add_all(inv_objs)

        s.commit()
