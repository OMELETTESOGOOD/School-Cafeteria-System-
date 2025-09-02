# main.py
import click
from app.logic import greet_user, show_menu, get_menu_ids, show_remaining, ensure_seeded
from app.crud import place_order, get_user_by_id

@click.command()
def run():
    """
    School cafeteria CLI:
    - asks for ID,
    - greets the user,
    - shows menu,
    - lets user pick an item,
    - deducts inventory (70 initial each)
    """
    # ensure DB seeded with users / menu / inventory
    ensure_seeded()

    click.echo("School Cafeteria System\n-----------------------")
    # validate ID input
    while True:
        user_id_str = click.prompt("Enter your ID number (1-30)", type=str)
        if not user_id_str.isdigit():
            click.echo("IDs must be numeric. Try again.")
            continue
        user_id = int(user_id_str)
        if user_id < 1 or user_id > 30:
            click.echo("ID out of range (1-30). Try again.")
            continue
        user, message = greet_user(user_id)
        if user is None:
            click.echo(message)
            continue
        click.echo(message)
        break

    # show menu and prompt for choice
    show_menu()
    valid_ids = get_menu_ids()
    while True:
        choice_str = click.prompt("Enter menu ID you want", type=str)
        if not choice_str.isdigit():
            click.echo("Invalid input; please enter the menu ID number.")
            continue
        choice = int(choice_str)
        if choice not in valid_ids:
            click.echo(f"Please choose one of the menu IDs: {valid_ids}")
            continue

        # place order
        success, msg, remaining = place_order(user.id, choice)
        click.echo(msg)
        if remaining is not None:
            click.echo(f"Inventory remaining for selected item: {remaining}")
        break

    click.echo("Thank you — have a great meal!")

if __name__ == "__main__":
    run()
