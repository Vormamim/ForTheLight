#!/usr/bin/env python3
"""
Dead Ship - Map Viewer
Display the visual map of the game world
"""

from data import print_game_map

def main():
    """Display the game map"""
    print("DEAD SHIP - Game World Map")
    print_game_map()
    
    print("\nThis shows the layout of all 10 locations on the alien planet.")
    print("Players start at [0] Crash Site and must explore to find 6 generator pieces.")
    print("The map helps players understand the spatial relationships between locations.")

if __name__ == "__main__":
    main()
