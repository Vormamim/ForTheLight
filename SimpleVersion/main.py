#!/usr/bin/env pyth    print("Commands: go north, go south, go east, go west, look, inventory, map, help, quit")n3
"""
Dead Ship - Simple Text Adventure Game
Main game loop
"""

from functions import show_location, move_player, check_for_item, add_to_inventory, show_inventory, check_game_over, show_help, show_map
from data import *

def main():
    """Main game loop"""
    # Game introduction
    print("=" * 50)
    print("           DEAD SHIP")
    print("=" * 50)
    print("\nYour ship has crashed on an alien planet!")
    print("The energy generator is broken into 6 pieces.")
    print("You must find all 6 pieces before your energy runs out!")
    print("Moving around costs energy, but finding pieces restores some.")
    print("\nCommands: go north, go south, go east, go west, look, inventory, quit")
    print("=" * 50)
    
    # Initialize game state
    player_location = 0  # Start at location 0 (crash site)
    player_energy = 50   # Starting energy
    inventory = []       # Empty inventory
    turn_count = 0       # Track turns for energy decay
    
    # Main game loop
    while True:
        # Show current location
        show_location(player_location, inventory)
        
        # Show player status
        print(f"\nEnergy: {player_energy}")
        print(f"Generator pieces found: {len(inventory)}/6")
        
        # Check if game is over
        if check_game_over(player_energy, inventory):
            break
        
        # Get player input
        command = input("\nWhat do you do? ").strip().lower()
        
        # Handle quit command
        if command == "quit":
            print("Thanks for playing!")
            break
        
        # Handle look command
        elif command == "look":
            continue  # Just redisplay location
        
        # Handle inventory command
        elif command == "inventory":
            show_inventory(inventory)
            continue
        
        # Handle help command
        elif command == "help":
            show_help()
            continue
        
        # Handle map command
        elif command == "map":
            show_map(player_location, inventory)
            continue
        
        # Handle movement commands
        elif command.startswith("go "):
            direction = command[3:]  # Get direction after "go "
            new_location = move_player(player_location, direction)
            
            if new_location != player_location:
                player_location = new_location
                player_energy -= 3  # Moving costs energy
                turn_count += 1
                
                # Check for items at new location
                found_item = check_for_item(player_location)
                if found_item and found_item not in inventory:
                    print(f"\nYou found a {found_item}!")
                    add_to_inventory(inventory, found_item)
                    player_energy += 10  # Finding item restores energy
            else:
                print("You can't go that way!")
        
        # Handle unknown commands
        else:
            print("Unknown command. Try: go north/south/east/west, look, inventory, quit")
        
        # Energy decays over time
        if turn_count > 0 and turn_count % 3 == 0:
            player_energy -= 1
            if player_energy <= 0:
                player_energy = 0

if __name__ == "__main__":
    main()
