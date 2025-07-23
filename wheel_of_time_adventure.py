import time
import os
import sys
from colorama import init, Fore, Style

# Initialize colorama for colored text
init()

def clear_screen():
    """Clear the screen based on OS"""
    os.system('cls' if os.name == 'nt' else 'clear')

def slow_print(text, delay=0.03):
    """Print text with animation"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def get_input(prompt=""):    
    """Get user input with prompt"""
    return input(prompt).lower().strip()

def show_inventory(inventory):
    """Display player's inventory"""
    if not inventory:
        print("Your inventory is empty.")
    else:
        print("\nYour inventory:")
        for item in inventory:
            print(f"- {item}")

def show_health(health):
    """Display player's health"""
    print(f"\nHealth: {health}/100")

def show_help():
    """Display help menu and game instructions"""
    clear_screen()
    print(Fore.YELLOW + """
    ===============================
           HELP MENU
    ===============================
    """ + Style.RESET_ALL)
    
    print(Fore.GREEN + "OBJECTIVE:" + Style.RESET_ALL)
    print("Navigate through the Wheel of Time world, solve puzzles, collect items,")
    print("and discover multiple endings based on your choices and items collected.")
    
    print(Fore.GREEN + "\nCOMMANDS:" + Style.RESET_ALL)
    print("• Type a location name to move there (case-insensitive)")
    print("• Type 'help' or 'h' to see this help menu")
    print("• Type 'commands' or 'c' to see detailed command list")
    print("• Type 'puzzle' or 'p' to attempt the current location's puzzle")
    print("• Type 'inventory' or 'i' to see your items")
    print("• Type 'quit' or 'q' to exit the game")
    print("• Type 'map' or 'm' to see all locations")
    print("• Type 'health' to check your current health")
    
    print(Fore.GREEN + "\nLOCATIONS:" + Style.RESET_ALL)
    for location in game_locations:
        print(f"• {location}")
    
    print(Fore.GREEN + "\nGAMEPLAY TIPS:" + Style.RESET_ALL)
    print("• Each location has a puzzle to solve")
    print("• Solving puzzles gives you items")
    print("• Different items lead to different endings")
    print("• Pay attention to puzzle hints and descriptions")
    print("• Some locations may have dangers - be prepared!")
    
    print(Fore.GREEN + "\nPUZZLE HINTS:" + Style.RESET_ALL)
    print("• Two Rivers: Where do villagers gather for trade?")
    print("• White Tower: What do Aes Sedai serve and protect?")
    print("• Tel'aran'rhiod: What lights the way at night?")
    print("• Shadar Logoth: What weapon defeats darkness?")
    print("• Caemlyn: What quality makes a good ruler?")
    print("• Tar Valon: How do you approach dangerous power?")
    
    get_input("\nPress Enter to continue...")

def show_map():
    """Display a map of all locations and their connections"""
    clear_screen()
    print(Fore.CYAN + """
    ===============================
           WORLD MAP
    ===============================
    """ + Style.RESET_ALL)
    
    for location, data in game_locations.items():
        status = "✓" if data["puzzle_solved"] else "?"
        print(f"\n{Fore.YELLOW}{location}{Style.RESET_ALL} {status}")
        print(f"  {data['description']}")
        print(f"  Connects to: {', '.join(data['exits'])}")
        if data['items']:
            print(f"  Items available: {', '.join(data['items'])}")
    
    get_input("\nPress Enter to continue...")

def show_commands():
    """Display available commands"""
    clear_screen()
    print(Fore.CYAN + """
    ===============================
         AVAILABLE COMMANDS
    ===============================
    """ + Style.RESET_ALL)
    
    print(Fore.GREEN + "MOVEMENT COMMANDS:" + Style.RESET_ALL)
    print("• Type any location name to travel there")
    print("  Examples: 'white tower', 'caemlyn', 'two rivers'")
    print("")
    
    print(Fore.GREEN + "GAME COMMANDS:" + Style.RESET_ALL)
    print("• help (or h)      - Show help menu with hints")
    print("• commands (or c)  - Show this commands list")
    print("• inventory (or i) - View your items")
    print("• map (or m)       - View world map")
    print("• health           - Check your current health")
    print("• puzzle (or p)    - Attempt the puzzle at current location")
    print("• progress         - Check your overall game progress")
    print("• quit (or q)      - Exit the game")
    print("")
    
    print(Fore.GREEN + "PUZZLE COMMANDS:" + Style.RESET_ALL)
    print("• When prompted for puzzle solutions, choose 1, 2, 3, or 4")
    print("• Read each option carefully before choosing")
    print("• Use 'help' for puzzle hints if stuck")
    print("• Type 'skip' if you want to attempt the puzzle later")
    print("")
    
    print(Fore.GREEN + "BATTLE COMMANDS:" + Style.RESET_ALL)
    print("• 1 - Attack the enemy")
    print("• 2 - Run from battle")
    
    get_input("\nPress Enter to continue...")

# Game locations
game_locations = {
    "Two Rivers": {
        "description": "You stand in the peaceful village of Emond's Field. The White Tower looms in the distance.",
        "exits": ["White Tower", "Caemlyn"],
        "items": ["Herb", "Map"],
        "puzzle": "Find the hidden herb garden",
        "puzzle_solved": False
    },
    "White Tower": {
        "description": "The imposing White Tower rises before you. Aisles of books line the walls.",
        "exits": ["Two Rivers", "Tel'aran'rhiod", "Tar Valon"],
        "items": ["Book of Prophecy"],
        "puzzle": "Solve the Aes Sedai riddle",
        "puzzle_solved": False
    },
    "Tel'aran'rhiod": {
        "description": "You stand in the World of Dreams. Shadows dance around you.",
        "exits": ["White Tower", "Shadar Logoth"],
        "items": ["Dream Ter'angreal"],
        "puzzle": "Find the hidden dream path",
        "puzzle_solved": False
    },
    "Shadar Logoth": {
        "description": "You stand in the cursed city of Shadar Logoth. The air feels heavy with evil.",
        "exits": ["Tel'aran'rhiod", "Tar Valon"],
        "items": ["Sword of Light"],
        "puzzle": "Defeat the Myrddraal",
        "puzzle_solved": False
    },
    "Caemlyn": {
        "description": "You stand in the grand city of Caemlyn. The Royal Palace towers above the city.",
        "exits": ["Two Rivers", "Tar Valon"],
        "items": ["Royal Seal", "Golden Crown"],
        "puzzle": "Answer the Queen's riddle",
        "puzzle_solved": False
    },
    "Tar Valon": {
        "description": "You are in the great city of Tar Valon, built on an island in the River Erinin. The city gleams white in the sunlight.",
        "exits": ["White Tower", "Caemlyn", "Shadar Logoth"],
        "items": ["One Power Ring", "Amyrlin's Staff"],
        "puzzle": "Channel the One Power safely",
        "puzzle_solved": False
    }
}

# Game state variables
current_location = "Two Rivers"
inventory = []
health = 100
has_sword = False
has_book = False
has_map = False

# Puzzles and solutions (multiple choice format)
puzzles = {
    "Find the hidden herb garden": {
        "question": "The village Wisdom mentions that rare healing herbs grow in a secret garden. An old woman whispers: 'Where the heart of the village beats strongest, where people gather to trade and meet, there you'll find what makes the sick complete.'",
        "options": [
            "Search the village square",
            "Look in the forest",
            "Check the mayor's house",
            "Explore the inn"
        ],
        "correct": 1
    },
    "Solve the Aes Sedai riddle": {
        "question": "An ancient Aes Sedai appears before you in shimmering robes. She speaks: 'I am what Aes Sedai serve, what battles the Shadow's might. I am hope in darkest hour, I am the world's guiding... what?'",
        "options": [
            "Power",
            "Light",
            "Truth",
            "Peace"
        ],
        "correct": 2
    },
    "Find the hidden dream path": {
        "question": "In this realm of dreams, reality shifts like mist. A Dreamwalker's voice echoes: 'When night's silver guardian shows the way, and dreams take flight on beams so bright, the path reveals itself to those who... what?'",
        "options": [
            "Follow the stars",
            "Follow the moonlit path",
            "Follow the sun",
            "Follow the wind"
        ],
        "correct": 2
    },
    "Defeat the Myrddraal": {
        "question": "A massive Myrddraal blocks your path, its eyeless gaze filled with malice. Ancient words carved in stone read: 'When darkness seems to win the day, when evil's grip seems here to stay, what blade of hope can clear the way?'",
        "options": [
            "Steel sword",
            "Magic wand",
            "Sword of Light",
            "Silver blade"
        ],
        "correct": 3
    },
    "Answer the Queen's riddle": {
        "question": "Queen Morgase sits upon her throne and poses a challenge: 'To rule a kingdom fair and true, to guide when paths are not clear through, what quality must a ruler show, to earn the people's trust below?'",
        "options": [
            "Strength",
            "Wealth",
            "Wisdom",
            "Beauty"
        ],
        "correct": 3
    },
    "Channel the One Power safely": {
        "question": "The One Power flows around you like a raging river. A voice whispers from the Pattern itself: 'Power corrupts, absolute power destroys. To touch the Source and not be consumed, you must first... what?'",
        "options": [
            "Fight the power",
            "Embrace the source",
            "Reject the power",
            "Control the power"
        ],
        "correct": 2
    }
}

def battle(enemy, damage):
    """Handle battle sequence"""
    global health
    clear_screen()
    slow_print(f"A {enemy} attacks!")
    
    while health > 0 and damage > 0:
        print("\nWhat will you do?")
        print("1. Attack")
        print("2. Run")
        
        choice = get_input("\n> ")
        
        if choice == "1":
            damage = max(0, damage - 10)
            health = max(0, health - 20)
            slow_print("You strike the enemy!")
            if damage <= 0:
                slow_print("You defeat the enemy!")
                break
        elif choice == "2":
            slow_print("You manage to escape!")
            break
        else:
            slow_print("Invalid choice!")
            
        show_health(health)
        
    if health <= 0:
        game_over()

def game_over():
    """End the game"""
    clear_screen()
    slow_print("\nGAME OVER")
    slow_print("\nYou have fallen in your quest.")
    sys.exit()

def check_puzzle(location):
    """Check and solve puzzles"""
    puzzle_name = game_locations[location]["puzzle"]
    puzzle_data = puzzles[puzzle_name]
    
    if not game_locations[location]["puzzle_solved"]:
        print(f"\n{Fore.MAGENTA}🧩 PUZZLE CHALLENGE: {puzzle_name}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}{'='*60}{Style.RESET_ALL}")
        slow_print(f"{Fore.CYAN}{puzzle_data['question']}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}{'='*60}{Style.RESET_ALL}")
        
        print(f"\n{Fore.YELLOW}Choose your answer:{Style.RESET_ALL}")
        for i, option in enumerate(puzzle_data['options'], 1):
            print(f"{Fore.WHITE}{i}. {option}{Style.RESET_ALL}")
        
        print(f"\n{Fore.YELLOW}💡 Select option 1, 2, 3, or 4{Style.RESET_ALL}")
        
        while True:
            answer = get_input(f"\n{Fore.WHITE}Enter your choice (1-4, or 'skip' to continue without solving): {Style.RESET_ALL}")
            
            if answer == "skip":
                slow_print("You decide to explore more before attempting this puzzle.")
                return
            
            # Validate input
            if answer in ['1', '2', '3', '4']:
                choice_num = int(answer)
                break
            else:
                slow_print(f"{Fore.RED}Please enter 1, 2, 3, 4, or 'skip'{Style.RESET_ALL}")
                continue
        
        # Check if answer is correct
        if choice_num == puzzle_data['correct']:
            clear_screen()
            slow_print(f"\n{Fore.GREEN}🎉 EXCELLENT! You chose correctly!{Style.RESET_ALL}")
            slow_print(f"{Fore.GREEN}Answer: {puzzle_data['options'][choice_num-1]}{Style.RESET_ALL}")
            game_locations[location]["puzzle_solved"] = True
            
            # Location-specific success messages
            success_messages = {
                "Two Rivers": "The village elder nods approvingly as you locate the secret herb garden!",
                "White Tower": "The Aes Sedai smiles and her form begins to fade, leaving wisdom behind.",
                "Tel'aran'rhiod": "The dream realm shimmers and reveals its hidden pathways to you.",
                "Shadar Logoth": "The Myrddraal shrieks as light banishes the shadows forever!",
                "Caemlyn": "Queen Morgase stands and bows to your wisdom. 'You understand what it means to rule.'",
                "Tar Valon": "The One Power flows through you safely, responding to your respectful approach."
            }
            
            slow_print(f"\n{Fore.BLUE}{success_messages[location]}{Style.RESET_ALL}")
            
            # Add items based on location
            items_to_add = game_locations[location]["items"]
            for item in items_to_add:
                if item not in inventory:
                    inventory.append(item)
                    slow_print(f"✨ You found: {Fore.CYAN}{item}{Style.RESET_ALL}")
            
            # Give health bonus for solving puzzles
            global health
            health = min(100, health + 15)
            slow_print(f"{Fore.GREEN}💚 Your health increases from solving the puzzle! (+15 HP){Style.RESET_ALL}")
            
        else:
            slow_print(f"\n{Fore.RED}❌ That's not quite right.{Style.RESET_ALL}")
            correct_answer = puzzle_data['options'][puzzle_data['correct']-1]
            slow_print(f"{Fore.YELLOW}The correct answer was: {correct_answer}{Style.RESET_ALL}")
            
            # Location-specific failure hints
            failure_hints = {
                "Two Rivers": "Think about where villagers gather daily for commerce and news...",
                "White Tower": "What do Aes Sedai fight against? What guides them?",
                "Tel'aran'rhiod": "What celestial body guides travelers at night?",
                "Shadar Logoth": "What kind of weapon would defeat pure darkness?",
                "Caemlyn": "What quality do all great leaders need to make good decisions?",
                "Tar Valon": "How do you safely approach something powerful and dangerous?"
            }
            
            slow_print(f"{Fore.CYAN}💡 Hint: {failure_hints[location]}{Style.RESET_ALL}")
            slow_print("The puzzle remains unsolved. You can try again when you return!")
            
    else:
        print(f"\n{Fore.GREEN}✅ You have already solved the puzzle here.{Style.RESET_ALL}")
        print(f"   The {game_locations[location]['puzzle']} has been completed.")
        print(f"   All items have been collected from this location.")

def check_endings():
    """Check for different endings based on game state"""
    global has_sword, has_book, has_map
    
    # Update item flags
    has_sword = "Sword of Light" in inventory
    has_book = "Book of Prophecy" in inventory
    has_map = "Map" in inventory
    has_crown = "Golden Crown" in inventory
    has_ring = "One Power Ring" in inventory
    has_staff = "Amyrlin's Staff" in inventory
    
    # Check for different endings
    if current_location == "Shadar Logoth" and has_sword:
        clear_screen()
        slow_print(Fore.RED + "\n🗡️  THE WARRIOR'S PATH  🗡️" + Style.RESET_ALL)
        slow_print("\nWith the Sword of Light in hand, you banish the evil from Shadar Logoth!")
        slow_print("The city crumbles to dust, and the world is safer from its corruption.")
        slow_print("\nYou have become a legendary warrior!")
        slow_print(Fore.YELLOW + "\n*** THE END - WARRIOR ENDING ***" + Style.RESET_ALL)
        sys.exit()
        
    elif current_location == "White Tower" and has_book and has_ring:
        clear_screen()
        slow_print(Fore.BLUE + "\n📚  THE AES SEDAI PATH  📚" + Style.RESET_ALL)
        slow_print("\nWith the Book of Prophecy and One Power Ring, you master the ways of the Aes Sedai!")
        slow_print("You become a powerful channeler, dedicated to fighting the Shadow.")
        slow_print("\nYou have achieved the rank of Aes Sedai!")
        slow_print(Fore.YELLOW + "\n*** THE END - AES SEDAI ENDING ***" + Style.RESET_ALL)
        sys.exit()
        
    elif current_location == "Tel'aran'rhiod" and "Dream Ter'angreal" in inventory:
        clear_screen()
        slow_print(Fore.MAGENTA + "\n🌙  THE DREAMER'S PATH  🌙" + Style.RESET_ALL)
        slow_print("\nWith the Dream Ter'angreal, you become master of Tel'aran'rhiod!")
        slow_print("You can walk between dreams and guide the fate of nations.")
        slow_print("\nYou have become a Dreamwalker!")
        slow_print(Fore.YELLOW + "\n*** THE END - DREAMWALKER ENDING ***" + Style.RESET_ALL)
        sys.exit()
        
    elif current_location == "Caemlyn" and has_crown and "Royal Seal" in inventory:
        clear_screen()
        slow_print(Fore.GREEN + "\n👑  THE RULER'S PATH  👑" + Style.RESET_ALL)
        slow_print("\nWith the Golden Crown and Royal Seal, you claim the throne of Andor!")
        slow_print("You rule with wisdom and justice, bringing peace to the land.")
        slow_print("\nYou have become a great monarch!")
        slow_print(Fore.YELLOW + "\n*** THE END - ROYAL ENDING ***" + Style.RESET_ALL)
        sys.exit()
        
    elif current_location == "Tar Valon" and has_staff and len(inventory) >= 5:
        clear_screen()
        slow_print(Fore.CYAN + "\n⚡  THE AMYRLIN'S PATH  ⚡" + Style.RESET_ALL)
        slow_print("\nWith the Amyrlin's Staff and great wisdom from your journey,")
        slow_print("you are chosen as the Amyrlin Seat, leader of all Aes Sedai!")
        slow_print("Your decisions will shape the fate of the world.")
        slow_print("\nYou have achieved the highest honor!")
        slow_print(Fore.YELLOW + "\n*** THE END - AMYRLIN ENDING ***" + Style.RESET_ALL)
        sys.exit()

def main():
    """Main game loop"""
    global current_location
    
    # Show initial instructions
    clear_screen()
    print(Fore.CYAN + "Welcome to your adventure!" + Style.RESET_ALL)
    print("\n" + Fore.YELLOW + "📖 QUICK START GUIDE:" + Style.RESET_ALL)
    print("• Type 'help' for full instructions and puzzle hints")
    print("• Type 'commands' to see all available commands")
    print("• Type location names to travel (e.g. 'white tower')")
    print("• Type 'inventory' to check your items")
    print("• Type 'map' to see the world")
    print("\n" + Fore.GREEN + "TIP: All commands are case-insensitive!" + Style.RESET_ALL)
    get_input("\nPress Enter to begin your journey...")
    
    while True:
        clear_screen()
        
        # Display location description
        slow_print(Fore.CYAN + f"\n=== {current_location} ===" + Style.RESET_ALL)
        slow_print(game_locations[current_location]["description"])
        
        # Show puzzle status
        if game_locations[current_location]["puzzle_solved"]:
            print(Fore.GREEN + "✅ Puzzle solved!" + Style.RESET_ALL)
        else:
            print(Fore.YELLOW + f"🧩 Puzzle available: {game_locations[current_location]['puzzle']}" + Style.RESET_ALL)
            print(Fore.CYAN + "   → Type 'puzzle' to attempt it!" + Style.RESET_ALL)
        
        # Show progress
        total_puzzles = len(game_locations)
        solved_puzzles = sum(1 for loc in game_locations.values() if loc["puzzle_solved"])
        print(f"\n{Fore.MAGENTA}📊 Progress: {solved_puzzles}/{total_puzzles} puzzles solved{Style.RESET_ALL}")
        
        # Show inventory and health
        show_inventory(inventory)
        show_health(health)
        
        # Check for endings
        check_endings()
        
        # Show available exits
        print(f"\n{Fore.GREEN}Available exits:{Style.RESET_ALL}")
        for exit_location in game_locations[current_location]["exits"]:
            print(f"  → {exit_location}")
        
        print(f"\n{Fore.CYAN}═══ COMMANDS ═══{Style.RESET_ALL}")
        print(f"🏃 Move: Type location name (e.g. 'white tower')")
        print(f"❓ help | 📋 commands | 🎒 inventory | 🗺️  map | ❤️  health | 🧩 puzzle | � progress | �🚪 quit")
        
        # Get player input
        choice = get_input(f"\n{Fore.WHITE}What would you like to do? {Style.RESET_ALL}").lower().strip()
        
        # Handle special commands
        if choice in ["help", "h"]:
            show_help()
            continue
        elif choice in ["commands", "c"]:
            show_commands()
            continue
        elif choice in ["inventory", "i"]:
            clear_screen()
            print(Fore.CYAN + "\n=== YOUR INVENTORY ===" + Style.RESET_ALL)
            show_inventory(inventory)
            get_input("\nPress Enter to continue...")
            continue
        elif choice in ["health"]:
            clear_screen()
            print(Fore.RED + "\n=== HEALTH STATUS ===" + Style.RESET_ALL)
            show_health(health)
            if health >= 80:
                print(Fore.GREEN + "You feel strong and healthy!" + Style.RESET_ALL)
            elif health >= 50:
                print(Fore.YELLOW + "You have some minor injuries." + Style.RESET_ALL)
            elif health >= 20:
                print(Fore.RED + "You are badly wounded!" + Style.RESET_ALL)
            else:
                print(Fore.RED + "You are near death!" + Style.RESET_ALL)
            get_input("\nPress Enter to continue...")
            continue
        elif choice in ["puzzle", "p"]:
            clear_screen()
            print(Fore.MAGENTA + f"\n=== PUZZLE AT {current_location.upper()} ===" + Style.RESET_ALL)
            check_puzzle(current_location)
            get_input("\nPress Enter to continue...")
            continue
        elif choice in ["progress"]:
            clear_screen()
            print(Fore.CYAN + "\n=== GAME PROGRESS ===" + Style.RESET_ALL)
            
            total_puzzles = len(game_locations)
            solved_puzzles = sum(1 for loc in game_locations.values() if loc["puzzle_solved"])
            
            print(f"\n{Fore.YELLOW}Puzzles Solved: {solved_puzzles}/{total_puzzles}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}Items Collected: {len(inventory)}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}Current Health: {health}/100{Style.RESET_ALL}")
            
            print(f"\n{Fore.GREEN}Completed Locations:{Style.RESET_ALL}")
            for location, data in game_locations.items():
                status = "✅" if data["puzzle_solved"] else "❌"
                print(f"  {status} {location}")
            
            print(f"\n{Fore.CYAN}Collected Items:{Style.RESET_ALL}")
            if inventory:
                for item in inventory:
                    print(f"  ✨ {item}")
            else:
                print("  No items collected yet")
                
            completion = (solved_puzzles / total_puzzles) * 100
            print(f"\n{Fore.MAGENTA}Overall Completion: {completion:.1f}%{Style.RESET_ALL}")
            
            if completion == 100:
                print(f"{Fore.GREEN}🎉 All puzzles solved! You're ready for the final endings!{Style.RESET_ALL}")
            
            get_input("\nPress Enter to continue...")
            continue
        elif choice in ["map", "m"]:
            show_map()
            continue
        elif choice in ["quit", "q", "exit"]:
            clear_screen()
            slow_print("\nThank you for playing The Wheel of Time Adventure!")
            slow_print("May you always find water and shade.")
            sys.exit()
        
        # Handle movement
        valid_exits = [exit.lower() for exit in game_locations[current_location]["exits"]]
        if choice in valid_exits:
            # Find the actual location name (case-insensitive)
            for exit_location in game_locations[current_location]["exits"]:
                if exit_location.lower() == choice:
                    current_location = exit_location
                    break
            
            # Handle location-specific events
            if current_location == "Shadar Logoth" and "Sword of Light" not in inventory:
                battle("Myrddraal", 50)
            elif current_location == "Tel'aran'rhiod":
                slow_print("\nThe air shimmers as you enter the World of Dreams...")
            elif current_location == "Caemlyn":
                slow_print("\nGuards nod respectfully as you enter the royal city...")
            elif current_location == "Tar Valon":
                slow_print("\nThe One Power thrums in the air around this great city...")
            elif current_location == "White Tower":
                slow_print("\nYou feel the weight of centuries of knowledge here...")
        else:
            clear_screen()
            slow_print(f"\n❌ You cannot go to '{choice}' from here.")
            print(f"\n{Fore.YELLOW}Available locations from {current_location}:{Style.RESET_ALL}")
            for exit_location in game_locations[current_location]["exits"]:
                print(f"  → {exit_location}")
            
            print(f"\n{Fore.CYAN}Available commands:{Style.RESET_ALL}")
            print("  help | commands | inventory | map | health | puzzle | quit")
            
            slow_print(f"\n{Fore.GREEN}💡 Tip: Type 'commands' to see detailed instructions!{Style.RESET_ALL}")
            get_input("\nPress Enter to continue...")

if __name__ == "__main__":
    clear_screen()
    print(Fore.YELLOW + """
    =========================================
       Welcome to The Wheel of Time Adventure
    =========================================
    
    🌟 Journey through 6 iconic locations
    🧩 Solve puzzles to collect powerful items  
    ⚔️  Battle dangerous foes
    👑 Discover 5 different endings
    
    The Wheel weaves as the Wheel wills...
    Your choices will determine your destiny.
    """ + Style.RESET_ALL)
    
    get_input("Press Enter to begin your adventure...")
    main()
