"""
The Wheel of Time - Text Adventure Game
Game functions and utilities
"""

import os
import sys
import time
import random
from data import *

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_colored(text, color):
    """Print text in specified color"""
    colors = {
        'black': '\033[30m',
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'magenta': '\033[35m',
        'cyan': '\033[36m',
        'white': '\033[37m',
        'reset': '\033[0m'
    }
    
    color_code = colors.get(color, colors['white'])
    print(f"{color_code}{text}{colors['reset']}")

def animated_print(text, color="white", delay=0.03):
    """Print text with animation effect"""
    colors = {
        'black': '\033[30m',
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'magenta': '\033[35m',
        'cyan': '\033[36m',
        'white': '\033[37m',
        'reset': '\033[0m'
    }
    
    color_code = colors.get(color, colors['white'])
    print(color_code, end='')
    
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    
    print(colors['reset'])

def select_character():
    """Character selection screen"""
    while True:
        clear_screen()
        print_colored("=" * 60, "cyan")
        print_colored("        THE WHEEL OF TIME - CHARACTER SELECTION", "cyan")
        print_colored("=" * 60, "cyan")
        
        for i, (key, char) in enumerate(CHARACTERS.items(), 1):
            print(f"\n{i}. {char['name']} - {char['class']}")
            print(f"   {char['description']}")
            print(f"   Health: {char['health']} | Attack: {char['attack']} | Defense: {char['defense']}")
        
        print_colored("\nEnter the number of your chosen character (1-4): ", "yellow")
        
        try:
            choice = int(input().strip())
            if 1 <= choice <= len(CHARACTERS):
                char_key = list(CHARACTERS.keys())[choice - 1]
                return CHARACTERS[char_key].copy()
            else:
                print_colored("Invalid choice. Please try again.", "red")
                time.sleep(2)
        except ValueError:
            print_colored("Please enter a valid number.", "red")
            time.sleep(2)

def display_location(game_state):
    """Display current location information"""
    clear_screen()
    location_key = game_state['current_location']
    location = LOCATIONS[location_key]
    
    # Mark location as visited
    game_state['visited_locations'].add(location_key)
    
    print_colored("=" * 60, "cyan")
    print_colored(f"  {location['name']}", "cyan")
    print_colored("=" * 60, "cyan")
    
    # Display location description
    print(f"\n{location['description']}")
    
    # Display items in location
    if location['items']:
        print_colored("\nYou can see: (use 'take <item>' to pick up)", "yellow")
        for item in location['items']:
            print(f"  - {item}")
    
    # Display exits
    if location['exits']:
        print_colored("\nExits: (use 'go <direction>' to move)", "green")
        for direction, dest in location['exits'].items():
            print(f"  {direction}: {LOCATIONS[dest]['name']}")
    
    # Display NPCs
    if location['npcs']:
        print_colored("\nPeople here: (use 'talk <person>' to speak with them)", "magenta")
        for npc in location['npcs']:
            print(f"  - {npc}")
    
    # Display enemies if any
    if location.get('enemies'):
        print_colored("\nDangerous creatures: (use 'attack <enemy>' to fight)", "red")
        for enemy in location['enemies']:
            print(f"  - {enemy}")
    
    # Display player status
    print_colored("\n" + "=" * 60, "cyan")
    print_colored(f"Health: {game_state['health']}/{game_state['max_health']} | " +
                 f"Level: {game_state['level']} | " +
                 f"Experience: {game_state['experience']}", "white")
    
    if game_state['inventory']:
        print_colored(f"Inventory: {', '.join(game_state['inventory'])}", "white")
    else:
        print_colored("Inventory: empty", "white")

def parse_command(command, game_state):
    """Parse and execute player commands"""
    if not command:
        return
    
    parts = command.split()
    verb = parts[0] if parts else ""
    noun = parts[1] if len(parts) > 1 else ""
    
    # Two-word commands
    if verb in ["go", "move", "walk", "travel"]:
        return handle_movement(noun, game_state)
    elif verb in ["take", "get", "pick"]:
        return handle_take(noun, game_state)
    elif verb in ["drop", "leave"]:
        return handle_drop(noun, game_state)
    elif verb in ["look", "examine", "inspect"]:
        return handle_look(noun, game_state)
    elif verb in ["talk", "speak"]:
        return handle_talk(noun, game_state)
    elif verb in ["use", "activate"]:
        return handle_use(noun, game_state)
    elif verb in ["attack", "fight", "kill"]:
        return handle_attack(noun, game_state)
    
    # Single word commands
    elif verb in ["help", "h"]:
        show_help()
    elif verb in ["tutorial", "tut"]:
        show_tutorial()
    elif verb in ["inventory", "inv", "i"]:
        show_inventory(game_state)
    elif verb in ["health", "status"]:
        show_status(game_state)
    elif verb in ["hint", "hints"]:
        show_hint(game_state)
    elif verb in ["quit", "exit", "q"]:
        if confirm_quit():
            return "quit"
    elif verb in ["save"]:
        print_colored("Save feature not implemented yet.", "yellow")
    elif verb in ["load"]:
        print_colored("Load feature not implemented yet.", "yellow")
    else:
        print_colored("I don't understand that command. Type 'help' for assistance.", "red")
        print_colored("Remember: commands are TWO WORDS like 'take sword' or 'go north'", "yellow")
    
    return None

def handle_movement(direction, game_state):
    """Handle player movement"""
    if not direction:
        print_colored("Go where?", "red")
        location = LOCATIONS[game_state['current_location']]
        if location['exits']:
            directions = list(location['exits'].keys())
            print_colored(f"Available directions: {', '.join(directions)}", "yellow")
            print_colored(f"Example: 'go {directions[0]}'", "cyan")
        else:
            print_colored("There are no exits from here!", "yellow")
        return None
    
    location = LOCATIONS[game_state['current_location']]
    
    # Convert direction aliases
    direction_map = {
        'n': 'north', 'north': 'north',
        's': 'south', 'south': 'south',
        'e': 'east', 'east': 'east',
        'w': 'west', 'west': 'west',
        'ne': 'northeast', 'northeast': 'northeast',
        'nw': 'northwest', 'northwest': 'northwest',
        'se': 'southeast', 'southeast': 'southeast',
        'sw': 'southwest', 'southwest': 'southwest',
        'up': 'up', 'u': 'up',
        'down': 'down', 'd': 'down'
    }
    
    direction = direction_map.get(direction, direction)
    
    if direction in location['exits']:
        destination = location['exits'][direction]
        game_state['current_location'] = destination
        
        # Random encounters
        if random.random() < 0.3:  # 30% chance
            return handle_random_encounter(game_state)
        
        return None
    else:
        print_colored(f"You can't go {direction} from here.", "red")
        if location['exits']:
            directions = list(location['exits'].keys())
            print_colored(f"Available directions: {', '.join(directions)}", "yellow")
        return None

def handle_take(item, game_state):
    """Handle taking items"""
    if not item:
        print_colored("Take what?", "red")
        location = LOCATIONS[game_state['current_location']]
        if location['items']:
            print_colored(f"Available items: {', '.join(location['items'])}", "yellow")
            print_colored("Example: 'take sword' or 'take potion'", "cyan")
        else:
            print_colored("There are no items here to take.", "yellow")
        return None
    
    location = LOCATIONS[game_state['current_location']]
    
    # Check if item is in location
    item_found = None
    for loc_item in location['items']:
        if item.lower() in loc_item.lower():
            item_found = loc_item
            break
    
    if item_found:
        location['items'].remove(item_found)
        game_state['inventory'].append(item_found)
        print_colored(f"You take the {item_found}.", "green")
        
        # Check for special items
        if item_found in SPECIAL_ITEMS:
            trigger_special_event(item_found, game_state)
    else:
        print_colored(f"There's no {item} here.", "red")
        if location['items']:
            print_colored(f"Available items: {', '.join(location['items'])}", "yellow")
    
    return None

def handle_drop(item, game_state):
    """Handle dropping items"""
    if not item:
        print_colored("Drop what?", "red")
        return None
    
    # Find item in inventory
    item_found = None
    for inv_item in game_state['inventory']:
        if item.lower() in inv_item.lower():
            item_found = inv_item
            break
    
    if item_found:
        game_state['inventory'].remove(item_found)
        LOCATIONS[game_state['current_location']]['items'].append(item_found)
        print_colored(f"You drop the {item_found}.", "green")
    else:
        print_colored(f"You don't have a {item}.", "red")
    
    return None

def handle_look(target, game_state):
    """Handle looking at things"""
    if not target or target in ["around", "room"]:
        # Re-display current location
        return None
    
    location = LOCATIONS[game_state['current_location']]
    
    # Check items in location
    for item in location['items']:
        if target.lower() in item.lower():
            if item in ITEM_DESCRIPTIONS:
                print_colored(ITEM_DESCRIPTIONS[item], "white")
            else:
                print_colored(f"It's a {item}. Nothing special about it.", "white")
            return None
    
    # Check inventory
    for item in game_state['inventory']:
        if target.lower() in item.lower():
            if item in ITEM_DESCRIPTIONS:
                print_colored(ITEM_DESCRIPTIONS[item], "white")
            else:
                print_colored(f"It's a {item}. Nothing special about it.", "white")
            return None
    
    print_colored(f"You don't see a {target} here.", "red")
    return None

def handle_talk(target, game_state):
    """Handle talking to NPCs"""
    if not target:
        print_colored("Talk to whom?", "red")
        location = LOCATIONS[game_state['current_location']]
        if location['npcs']:
            print_colored(f"People here: {', '.join(location['npcs'])}", "yellow")
            npc_example = location['npcs'][0].split()[0].lower()
            print_colored(f"Example: 'talk {npc_example}'", "cyan")
        else:
            print_colored("There's no one here to talk to.", "yellow")
        return None
    
    location = LOCATIONS[game_state['current_location']]
    
    # Check NPCs in location
    for npc in location['npcs']:
        if target.lower() in npc.lower():
            if npc in NPC_DIALOGUES:
                dialogue = random.choice(NPC_DIALOGUES[npc])
                print_colored(f"{npc}: \"{dialogue}\"", "magenta")
            else:
                print_colored(f"{npc} doesn't seem interested in talking.", "yellow")
            return None
    
    print_colored(f"There's no {target} here to talk to.", "red")
    if location['npcs']:
        print_colored(f"People here: {', '.join(location['npcs'])}", "yellow")
    return None

def handle_use(item, game_state):
    """Handle using items"""
    if not item:
        print_colored("Use what?", "red")
        return None
    
    # Check if item is in inventory
    item_found = None
    for inv_item in game_state['inventory']:
        if item.lower() in inv_item.lower():
            item_found = inv_item
            break
    
    if not item_found:
        print_colored(f"You don't have a {item}.", "red")
        return None
    
    # Handle special item usage
    if item_found in USABLE_ITEMS:
        return use_special_item(item_found, game_state)
    else:
        print_colored(f"You can't use the {item_found} right now.", "yellow")
    
    return None

def handle_attack(target, game_state):
    """Handle combat"""
    if not target:
        print_colored("Attack what?", "red")
        return None
    
    location = LOCATIONS[game_state['current_location']]
    
    # Check for enemies
    if target in location.get('enemies', []):
        return start_combat(target, game_state)
    else:
        print_colored(f"There's no {target} here to attack.", "red")
    
    return None

def start_combat(enemy_name, game_state):
    """Start combat with an enemy"""
    if enemy_name not in ENEMIES:
        print_colored("Unknown enemy!", "red")
        return None
    
    enemy = ENEMIES[enemy_name].copy()
    player = game_state['player']
    
    print_colored(f"\nCombat begins with {enemy['name']}!", "red")
    print_colored(f"{enemy['description']}", "yellow")
    
    while enemy['health'] > 0 and game_state['health'] > 0:
        print_colored(f"\n{player['name']} (Health: {game_state['health']}) vs {enemy['name']} (Health: {enemy['health']})", "white")
        
        # Player attack
        player_damage = random.randint(player['attack'] - 2, player['attack'] + 2)
        enemy_defense = random.randint(0, enemy['defense'])
        actual_damage = max(1, player_damage - enemy_defense)
        
        enemy['health'] -= actual_damage
        print_colored(f"You attack {enemy['name']} for {actual_damage} damage!", "green")
        
        if enemy['health'] <= 0:
            print_colored(f"You defeated {enemy['name']}!", "green")
            
            # Gain experience
            exp_gained = enemy['experience']
            game_state['experience'] += exp_gained
            print_colored(f"You gained {exp_gained} experience!", "yellow")
            
            # Level up check
            if game_state['experience'] >= game_state['level'] * 100:
                level_up(game_state)
            
            # Remove enemy from location
            location = LOCATIONS[game_state['current_location']]
            if 'enemies' in location and enemy_name in location['enemies']:
                location['enemies'].remove(enemy_name)
            
            # Drop loot
            if 'loot' in enemy:
                for item in enemy['loot']:
                    location['items'].append(item)
                    print_colored(f"{enemy['name']} dropped {item}!", "green")
            
            break
        
        # Enemy attack
        enemy_damage = random.randint(enemy['attack'] - 1, enemy['attack'] + 1)
        player_defense = random.randint(0, player['defense'])
        actual_damage = max(1, enemy_damage - player_defense)
        
        game_state['health'] -= actual_damage
        print_colored(f"{enemy['name']} attacks you for {actual_damage} damage!", "red")
        
        if game_state['health'] <= 0:
            return "death"
        
        time.sleep(1)
    
    return None

def level_up(game_state):
    """Handle player level up"""
    game_state['level'] += 1
    game_state['max_health'] += 10
    game_state['health'] = game_state['max_health']  # Full heal on level up
    game_state['player']['attack'] += 2
    game_state['player']['defense'] += 1
    
    print_colored(f"\nLevel up! You are now level {game_state['level']}!", "cyan")
    print_colored(f"Health increased to {game_state['max_health']}!", "green")
    print_colored(f"Attack increased to {game_state['player']['attack']}!", "green")
    print_colored(f"Defense increased to {game_state['player']['defense']}!", "green")

def handle_random_encounter(game_state):
    """Handle random encounters while traveling"""
    encounter_type = random.choice(["nothing", "item", "enemy", "helpful"])
    
    if encounter_type == "nothing":
        pass
    elif encounter_type == "item":
        item = random.choice(RANDOM_ITEMS)
        print_colored(f"\nWhile traveling, you found a {item}!", "green")
        game_state['inventory'].append(item)
    elif encounter_type == "enemy":
        enemy_name = random.choice(list(ENEMIES.keys()))
        print_colored(f"\nYou encounter a {enemy_name} on the road!", "red")
        return start_combat(enemy_name, game_state)
    elif encounter_type == "helpful":
        healing = random.randint(5, 15)
        game_state['health'] = min(game_state['max_health'], game_state['health'] + healing)
        print_colored(f"\nYou find a healing spring and recover {healing} health!", "green")
    
    return None

def show_help():
    """Display help information"""
    print_colored("\n" + "=" * 60, "cyan")
    print_colored("                         HELP", "cyan")
    print_colored("=" * 60, "cyan")
    
    print_colored("\nMOVEMENT:", "yellow")
    print("  go <direction>     - Move in a direction (north, south, east, west)")
    print("  go n/s/e/w        - Short form movement")
    print("  Examples: 'go north', 'go n', 'go east'")
    
    print_colored("\nINTERACTING WITH ITEMS:", "yellow")
    print("  take <item>       - Pick up an item you can see")
    print("  drop <item>       - Drop an item from your inventory")
    print("  look <item>       - Examine something closely for details")
    print("  look around       - Re-examine your current location")
    print("  use <item>        - Use an item from your inventory")
    print("  Examples: 'take sword', 'look dagger', 'use potion'")
    
    print_colored("\nINTERACTING WITH PEOPLE:", "yellow")
    print("  talk <person>     - Have a conversation with someone")
    print("  Examples: 'talk tam', 'talk merchant', 'talk guard'")
    print("  Tip: Use part of their name - 'talk bran' works for 'Bran al'Vere'")
    
    print_colored("\nCOMBAT:", "yellow")
    print("  attack <enemy>    - Attack an enemy in the current location")
    print("  Examples: 'attack trolloc', 'attack bandit'")
    
    print_colored("\nINFORMATION COMMANDS:", "yellow")
    print("  inventory/inv/i   - Show what you're carrying")
    print("  health/status     - Show your character's stats")
    print("  hint              - Get a helpful hint for your current area")
    print("  help              - Show this help message")
    
    print_colored("\nHOW TO SEE THINGS:", "yellow")
    print("  - Items you can take are listed under 'You can see:'")
    print("  - People are listed under 'People here:'")
    print("  - Exits are listed under 'Exits:'")
    print("  - Use 'look around' to see the location description again")
    
    print_colored("\nOTHER COMMANDS:", "yellow")
    print("  quit/exit         - Quit the game")
    print("  tutorial          - Show a quick tutorial")
    
    print_colored("\nIMPORTANT TIPS:", "green")
    print("  • Commands are TWO WORDS: verb + noun (e.g., 'take sword')")
    print("  • You can use partial names: 'talk tam' for 'Tam al'Thor'")
    print("  • Look at everything! Use 'look <item>' for detailed descriptions")
    print("  • Talk to everyone! NPCs give valuable information and hints")
    print("  • Check your inventory often with 'inv' or 'i'")
    print("  • Use 'hint' if you're stuck in any location")

def show_inventory(game_state):
    """Display player inventory"""
    print_colored("\nInventory:", "yellow")
    if game_state['inventory']:
        for item in game_state['inventory']:
            print(f"  - {item}")
    else:
        print("  Your inventory is empty.")

def show_status(game_state):
    """Display player status"""
    player = game_state['player']
    print_colored(f"\n{player['name']} the {player['class']}", "cyan")
    print(f"Health: {game_state['health']}/{game_state['max_health']}")
    print(f"Level: {game_state['level']}")
    print(f"Experience: {game_state['experience']}/{game_state['level'] * 100}")
    print(f"Attack: {player['attack']}")
    print(f"Defense: {player['defense']}")

def show_hint(game_state):
    """Show hints for current location"""
    location_key = game_state['current_location']
    location = LOCATIONS[game_state['current_location']]
    
    print_colored("\n💡 HINT:", "yellow")
    
    # Location-specific hints
    if location_key in LOCATION_HINTS:
        hint = random.choice(LOCATION_HINTS[location_key])
        print_colored(f"   {hint}", "white")
    
    # Context-sensitive hints based on what's available
    context_hints = []
    
    if location['items']:
        context_hints.append(f"There are {len(location['items'])} items here you can 'take'")
        context_hints.append(f"Try 'look {location['items'][0].split()[0].lower()}' to examine the {location['items'][0]}")
    
    if location['npcs']:
        npc_name = location['npcs'][0].split()[0].lower()
        context_hints.append(f"Try 'talk {npc_name}' to speak with {location['npcs'][0]}")
        context_hints.append("NPCs often have valuable information or items!")
    
    if location.get('enemies'):
        context_hints.append(f"Be careful! There are enemies here. Use 'attack {location['enemies'][0].lower()}' to fight")
        context_hints.append("Make sure you have good health before fighting!")
    
    if location['exits']:
        directions = list(location['exits'].keys())
        context_hints.append(f"You can go: {', '.join(directions)}")
        if len(directions) > 1:
            context_hints.append(f"Try 'go {random.choice(directions)}' to explore")
    
    # Add a context hint if we have any
    if context_hints:
        print_colored(f"   {random.choice(context_hints)}", "white")
    
    # General gameplay hints
    general_hints = [
        "Use 'inv' to check what you're carrying",
        "Try 'look around' to see the area description again",
        "Use 'status' to check your health and level",
        "Don't forget to 'look <item>' to examine things closely",
        "Talk to everyone! They often have helpful information",
        "Some items can be used with the 'use <item>' command",
        "Explore thoroughly - some areas have hidden secrets"
    ]
    
    print_colored(f"   {random.choice(general_hints)}", "cyan")

def confirm_quit():
    """Confirm if player wants to quit"""
    print_colored("Are you sure you want to quit? (y/n): ", "yellow")
    response = input().strip().lower()
    return response in ['y', 'yes']

def trigger_special_event(item, game_state):
    """Trigger special events for certain items"""
    if item in SPECIAL_ITEMS:
        event = SPECIAL_ITEMS[item]
        print_colored(f"\n{event}", "magenta")
        
        # Add special effects based on item
        if "ring" in item.lower():
            game_state['player']['defense'] += 2
            print_colored("Your defense has increased!", "green")
        elif "sword" in item.lower():
            game_state['player']['attack'] += 3
            print_colored("Your attack has increased!", "green")

def use_special_item(item, game_state):
    """Use special items with unique effects"""
    if item == "Healing Potion":
        if game_state['health'] < game_state['max_health']:
            healing = random.randint(20, 30)
            game_state['health'] = min(game_state['max_health'], game_state['health'] + healing)
            game_state['inventory'].remove(item)
            print_colored(f"You drink the healing potion and recover {healing} health!", "green")
        else:
            print_colored("You're already at full health.", "yellow")
    elif item == "Ancient Scroll":
        print_colored("The scroll reveals hidden knowledge about your enemies!", "magenta")
        print_colored("All enemies now deal 1 less damage to you.", "green")
        game_state['game_flags']['scroll_protection'] = True
        game_state['inventory'].remove(item)
    else:
        print_colored(f"You can't use the {item} right now.", "yellow")
    
    return None

def game_over(game_state):
    """Handle game over"""
    clear_screen()
    print_colored("=" * 60, "red")
    print_colored("                        GAME OVER", "red")
    print_colored("=" * 60, "red")
    
    print_colored(f"\n{game_state['player']['name']} has fallen...", "red")
    print_colored("The Wheel weaves as the Wheel wills.", "white")
    print_colored(f"You reached level {game_state['level']} and explored {len(game_state['visited_locations'])} locations.", "yellow")

def victory_screen(game_state):
    """Handle victory condition"""
    clear_screen()
    print_colored("=" * 60, "green")
    print_colored("                        VICTORY!", "green")
    print_colored("=" * 60, "green")
    
    print_colored(f"\nCongratulations, {game_state['player']['name']}!", "green")
    print_colored("You have completed your quest and brought glory to your name!", "white")
    print_colored("The Wheel of Time turns, and Ages come and pass...", "cyan")
    print_colored(f"Final Level: {game_state['level']}", "yellow")
    print_colored(f"Locations Explored: {len(game_state['visited_locations'])}", "yellow")

def show_tutorial():
    """Display a quick tutorial for new players"""
    clear_screen()
    print_colored("=" * 60, "cyan")
    print_colored("                   QUICK TUTORIAL", "cyan")
    print_colored("=" * 60, "cyan")
    
    print_colored("\n🎮 HOW TO PLAY:", "green")
    print("This is a text adventure game. You control your character by typing commands.")
    
    print_colored("\n📖 READING THE SCREEN:", "yellow")
    print("• The game shows you a description of where you are")
    print("• 'You can see:' lists items you can pick up")
    print("• 'People here:' lists people you can talk to")
    print("• 'Exits:' shows where you can go")
    print("• Your health, level, and inventory are shown at the bottom")
    
    print_colored("\n💬 COMMANDS ARE TWO WORDS:", "yellow")
    print("• VERB + NOUN format: 'take sword', 'go north', 'talk merchant'")
    print("• You can use partial names: 'talk tam' works for 'Tam al'Thor'")
    
    print_colored("\n🚶 MOVING AROUND:", "yellow")
    print("• Type 'go north' or just 'go n' to move")
    print("• Available directions are shown under 'Exits:'")
    
    print_colored("\n🎒 ITEMS:", "yellow")
    print("• 'take <item>' to pick up things you see")
    print("• 'look <item>' to examine items closely")
    print("• 'use <item>' to use items from your inventory")
    print("• 'inv' to see what you're carrying")
    
    print_colored("\n👥 TALKING TO PEOPLE:", "yellow")
    print("• 'talk <person>' to have conversations")
    print("• People give hints, information, and sometimes items!")
    print("• Example: 'talk bran' to talk to Bran al'Vere")
    
    print_colored("\n⚔️ COMBAT:", "yellow")
    print("• 'attack <enemy>' to fight hostile creatures")
    print("• Combat is automatic once started")
    print("• Gain experience and level up by winning fights")
    
    print_colored("\n🎯 GETTING HELP:", "yellow")
    print("• 'hint' - Get hints for your current location")
    print("• 'help' - Show all available commands")
    print("• 'status' - Check your character's health and stats")
    
    print_colored("\n✨ EXAMPLE COMMANDS:", "green")
    print("  take sword          look dagger         go north")
    print("  talk tam            use potion          attack trolloc")
    print("  inv                 hint                help")
    
    print_colored("\nPress Enter to continue...", "cyan")
    input()
