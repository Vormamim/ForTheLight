#!/usr/bin/env python3
"""
The Wheel of Time - Text Adventure Game
Main game loop and initialization
"""

import os
import sys
import time
import random
from functions import *
from data import *

def main():
    """Main game loop"""
    # Initialize the game
    clear_screen()
    print_colored(TITLE_TEXT, "cyan")
    time.sleep(2)
    
    # Character selection
    player = select_character()
    if not player:
        return
    
    # Game introduction
    clear_screen()
    animated_print(f"\nWelcome, {player['name']}!\n", "green")
    animated_print(player['intro'], "white")
    time.sleep(2)
    
    # Initialize game state
    game_state = {
        'player': player,
        'current_location': 'emond_field',
        'inventory': player['starting_items'].copy(),
        'health': player['health'],
        'max_health': player['health'],
        'experience': 0,
        'level': 1,
        'game_flags': {},
        'visited_locations': set()
    }
    
    # Main game loop
    animated_print("\n🎮 Welcome to your adventure!", "green")
    animated_print("Type 'help' to see all commands, or 'tutorial' for a quick guide.", "yellow")
    animated_print("Remember: Use TWO WORDS like 'take sword' or 'go north'\n", "cyan")
    
    while True:
        try:
            # Display current location
            display_location(game_state)
            
            # Get player input
            command = input(f"\n{PROMPT_SYMBOL} ").strip().lower()
            
            if not command:
                continue
                
            # Parse and execute command
            result = parse_command(command, game_state)
            
            if result == "quit":
                break
            elif result == "death":
                game_over(game_state)
                break
            elif result == "victory":
                victory_screen(game_state)
                break
                
        except KeyboardInterrupt:
            print_colored("\n\nGame interrupted. Farewell!", "red")
            break
        except Exception as e:
            print_colored(f"\nAn error occurred: {e}", "red")
            continue
    
    print_colored("\nMay you always find water and shade.\n", "cyan")

if __name__ == "__main__":
    main()
