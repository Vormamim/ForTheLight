# main.py

from data import rooms, starting_room
from functions import show_location, get_command, move, take_item, check_end_game

def main():
    current_room = starting_room
    inventory = []

    print("Welcome to *ANDOR: The Escape Begins*.")
    print("You are Cassian Andor, trapped on a corporate planet. Escape... or die.")

    while True:
        show_location(current_room, rooms)
        command = get_command()

        if command.startswith("go "):
            direction = command[3:]
            new_room = move(current_room, direction, rooms)
            if new_room:
                current_room = new_room
        elif command.startswith("take "):
            item = command[5:]
            take_item(current_room, item, rooms, inventory)
        elif command == "inventory":
            print("Inventory:", ", ".join(inventory) if inventory else "You have nothing.")
        elif command in ["quit", "exit"]:
            print("Game over.")
            break

        if check_end_game(current_room, inventory):
            break


main()
