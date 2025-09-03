# School Cafeteria System

A Python CLI application for managing a school cafeteria. Students and teachers can select menu items, and the system tracks inventory using SQLAlchemy and Alembic.

---




## Project Overview

This CLI-based cafeteria system allows users to:

- Enter their ID (student or teacher)  
- Receive a personalized greeting  
- Choose an item from the menu  
- Receive the selected item  
- See the remaining inventory of that item  

Inventory starts at 70 for each menu item and is decremented automatically upon selection.

---

## Installation

1. Clone the repository:

git clone <repo-url>
Install dependencies using Pipenv:

phase-3-project/
├── alembic/
│   ├── env.py
│   ├── __pycache__/             # Python cache files
│   └── versions/                # Alembic migration scripts
├── app/
│   ├── __init__.py
│   ├── crud.py                  # CRUD functions
│   ├── db.py                    # Database connection & session
│   ├── logic.py                 # CLI logic
│   ├── models.py                # SQLAlchemy ORM models
│   ├── seed.py                  # Seed database with initial data
│   └── __pycache__/             # Python cache files
├── main.py                      # Entry point for CLI
├── cafeteria.db                 # SQLite database
├── Pipfile                      # Pipenv dependencies
├── Pipfile.lock                 # Pipenv lock file
├── README.md                     # Project documentation
└── alembic.ini                   # Alembic configuration

python main.py
Input your ID:

IDs 1–25 → Students 
IDs 26–30 → Teachers 


Welcome {name}, please choose an item from the menu:
Select a menu item:

Menu items:

Ugali & Matumbo

Rice & Beef

Rice & Beans

Tea & Mandazi

Chicken Sandwich

Receive item and inventory update:

Here is your {menu item}
Remaining quantity: {inventory_count}


Entry point for the CLI program

Calls cli.start() to begin interaction

cli.start() (cli.py)

Prompts user for ID

Validates ID and determines user role

Greets user by name

Displays menu and prompts selection

cli.show_menu()

Lists available menu items

Returns user selection

cli.update_inventory(item_id)

Reduces inventory for chosen item by 1

Prints remaining quantity

db.py

SessionLocal → creates a session for database transactions

engine → SQLAlchemy engine connected to SQLite or DB URL

models.py

User → Stores ID, name, role

MenuItem → Stores menu items

Inventory → Tracks quantities of menu items

Dependencies
SQLAlchemy → ORM for database interactions

Alembic → Database migrations

python-dotenv → Load .env variables

##Notes
Inventory starts at 70 for all items

User input is validated to prevent invalid IDs or menu choices


Slides presentation:https://onedrive.live.com/personal/dc07c1cdfc224f0d/_layouts/15/doc2.aspx?resid=2b973d42-79f3-4be8-8321-4325972b8b09&cid=dc07c1cdfc224f0d&wdPreviousSession=b7015586-462d-40e5-be65-e10728bad753&wdNewAndOpenCt=1756638799263&wdo=4&wdOrigin=wacFileNew&wdTpl=blankNew&wdPreviousCorrelation=3357217f-1593-4b71-9b4f-a154aee7250f&action=editnew&wdnd=1