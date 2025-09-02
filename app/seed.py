# app/seed.py
from app.crud import seed_if_empty

if __name__ == "__main__":
    seed_if_empty()
    print("Seeded DB (users, menu, inventory) if it was empty.")
