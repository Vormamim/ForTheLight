"""
Dead Ship - Simple Text Adventure Game
Game functions
"""

from data import LOCATION_NAMES, LOCATION_DESCRIPTIONS, LOCATION_ITEMS

def show_location(location_number, inventory):
    """Display the current location description and available items"""
    print(f"\n--- {LOCATION_NAMES[location_number]} ---")
    print(LOCATION_DESCRIPTIONS[location_number])
    
    # Show exits
    exits = []
    if location_number not in [0, 1, 2]:  # Top row can go south
        exits.append("south")
    if location_number not in [7, 8, 9]:  # Bottom row can go north
        exits.append("north")
    if location_number not in [0, 3, 6]:  # Left column can go east
        exits.append("east")
    if location_number not in [2, 5, 8]:  # Right column can go west
        exits.append("west")
    
    if exits:
        print(f"You can go: {', '.join(exits)}")
    
    # Show if there's an item here (and player hasn't found it yet)
    if LOCATION_ITEMS[location_number] and LOCATION_ITEMS[location_number] not in inventory:
        print(f"You see something glinting: {LOCATION_ITEMS[location_number]}")

def move_player(current_location, direction):
    """Move the player in the given direction, return new location"""
    if direction == "north":
        if current_location >= 3:  # Can move north if not in top row
            return current_location - 3
        else:
            return current_location  # Can't move north from top row
    
    elif direction == "south":
        if current_location <= 6:  # Can move south if not in bottom row
            return current_location + 3
        else:
            return current_location  # Can't move south from bottom row
    
    elif direction == "east":
        if current_location not in [2, 5, 8]:  # Can move east if not in right column
            return current_location + 1
        else:
            return current_location  # Can't move east from right column
    
    elif direction == "west":
        if current_location not in [0, 3, 6]:  # Can move west if not in left column
            return current_location - 1
        else:
            return current_location  # Can't move west from left column
    
    else:
        return current_location  # Invalid direction

def check_for_item(location_number):
    """Check if there's an item at the current location"""
    return LOCATION_ITEMS[location_number]

def add_to_inventory(inventory, item):
    """Add an item to the player's inventory"""
    if item and item not in inventory:
        inventory.append(item)

def show_inventory(inventory):
    """Display the player's inventory"""
    print("\n--- INVENTORY ---")
    if inventory:
        print("Generator pieces found:")
        for i, item in enumerate(inventory, 1):
            print(f"  {i}. {item}")
    else:
        print("No generator pieces found yet.")
    print(f"Total pieces: {len(inventory)}/6")

def check_game_over(energy, inventory):
    """Check if the game is over (win or lose)"""
    # Check if player has won (found all 6 pieces)
    if len(inventory) >= 6:
        print("\n" + "=" * 50)
        print("🎉 CONGRATULATIONS! 🎉")
        print("You found all 6 generator pieces!")
        print("Your ship's energy generator is now complete!")
        print("You can escape this planet and return home!")
        print("=" * 50)
        return True
    
    # Check if player has lost (ran out of energy)
    if energy <= 0:
        print("\n" + "=" * 50)
        print("💀 GAME OVER 💀")
        print("You ran out of energy and collapsed!")
        print(f"You found {len(inventory)}/6 generator pieces.")
        print("Your ship remains stranded on this alien world...")
        print("=" * 50)
        return True
    
    # Game continues
    return False

def show_help():
    """Display help information"""
    print("\n--- HELP ---")
    print("Commands:")
    print("  go north/south/east/west - Move around the planet")
    print("  look - Look around your current location")
    print("  inventory - Check what pieces you've found")
    print("  map - Show the planet map")
    print("  quit - Quit the game")
    print("\nGoal: Find all 6 generator pieces before your energy runs out!")
    print("Moving costs 3 energy, finding pieces gives you 10 energy.")

def show_map(current_location, inventory):
    """Display a visual map of the planet"""
    print("\n" + "=" * 60)
    print("                    PLANET MAP")
    print("=" * 60)
    
    # Map symbols
    symbols = []
    for i in range(10):
        if i == current_location:
            symbols.append("[@]")  # Player location
        elif LOCATION_ITEMS[i] and LOCATION_ITEMS[i] in inventory:
            symbols.append("[✓]")  # Found item
        elif LOCATION_ITEMS[i]:
            symbols.append("[?]")  # Unknown item location
        else:
            symbols.append("[ ]")  # Empty location
    
    # Print the map grid
    print(f"  {symbols[0]}--{symbols[1]}--{symbols[2]}")
    print("   |    |    |")
    print(f"  {symbols[3]}--{symbols[4]}--{symbols[5]}")
    print("   |    |    |")
    print(f"  {symbols[6]}--{symbols[7]}--{symbols[8]}")
    print("        |")
    print(f"       {symbols[9]}")
    
    print("\nLEGEND:")
    print("[@] = Your current location")
    print("[✓] = Generator piece found")
    print("[?] = Unexplored area (may contain pieces)")
    print("[ ] = Empty area")
    
    print("\nLOCATIONS:")
    print("0: Crash Site       1: Rocky Outcrop    2: Crystal Cave")
    print("3: Dense Forest     4: Ancient Ruins    5: Frozen Lake")
    print("6: Volcanic Vents   7: Metal Wreckage   8: Strange Monolith")
    print("9: Energy Crater")
    print("=" * 60)
