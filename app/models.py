# app/models.py
from sqlalchemy import Column, Integer, String, Enum, ForeignKey, DateTime, func
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.ext.hybrid import hybrid_property

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    role = Column(String(20), nullable=False)  # 'student' or 'teacher'

    orders = relationship("Order", back_populates="user")

    def __repr__(self):
        return f"<User id={self.id} name={self.name} role={self.role}>"

class MenuItem(Base):
    __tablename__ = "menu_items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True)
    price = Column(Integer, nullable=False, default=0)  # cents or whole currency units

    inventory = relationship("Inventory", uselist=False, back_populates="menu_item")
    orders = relationship("Order", back_populates="menu_item")

    def __repr__(self):
        return f"<MenuItem id={self.id} name={self.name} price={self.price}>"

class Inventory(Base):
    __tablename__ = "inventory"
    id = Column(Integer, primary_key=True)
    menu_item_id = Column(Integer, ForeignKey("menu_items.id"), unique=True, nullable=False)
    initial_qty = Column(Integer, nullable=False, default=70)
    qty_sold = Column(Integer, nullable=False, default=0)

    menu_item = relationship("MenuItem", back_populates="inventory")

    # hybrid property provides Python-side logic based on columns
    @hybrid_property
    def remaining(self):
        return max(self.initial_qty - self.qty_sold, 0)

    def __repr__(self):
        return f"<Inventory {self.menu_item.name if self.menu_item else self.menu_item_id} remaining={self.remaining}>"

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    menu_item_id = Column(Integer, ForeignKey("menu_items.id"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User", back_populates="orders")
    menu_item = relationship("MenuItem", back_populates="orders")

    def __repr__(self):
        return f"<Order id={self.id} user={self.user_id} menu_item={self.menu_item_id} at={self.created_at}>"
