"""
Dead Ship - Simple Text Adventure Game
Game data using lists
"""

# Location names (10 locations in a 3x3 grid plus crash site)
LOCATION_NAMES = [
    "Crash Site",           # 0
    "Rocky Outcrop",        # 1
    "Crystal Cave",         # 2
    "Dense Forest",         # 3
    "Ancient Ruins",        # 4
    "Frozen Lake",          # 5
    "Volcanic Vents",       # 6
    "Metal Wreckage",       # 7
    "Strange Monolith",     # 8
    "Energy Crater"         # 9
]

# Location descriptions
LOCATION_DESCRIPTIONS = [
    "The twisted remains of your ship lie scattered here. Smoke still rises from the wreckage.",  # 0
    "Jagged rocks jut from the ground like broken teeth. The wind howls between them.",           # 1
    "Sparkling crystals line the walls of this cave, casting rainbow reflections everywhere.",    # 2
    "Towering alien trees block most of the light. Strange sounds echo in the darkness.",        # 3
    "Crumbling stone structures hint at an ancient civilization. Vines cover everything.",       # 4
    "A lake of perfectly still, frozen water reflects the alien sky like a mirror.",             # 5
    "Steam and heat rise from cracks in the ground. The air shimmers with thermal energy.",      # 6
    "Pieces of unknown technology are scattered among the rocks. Some still spark with power.",  # 7
    "A tall, black stone pillar hums with mysterious energy. Strange symbols glow on its surface.", # 8
    "A massive crater pulses with blue energy. The ground here feels warm to the touch."         # 9
]

# Items at each location (None means no item)
LOCATION_ITEMS = [
    None,                    # 0 - Crash Site (no item)
    "Power Core Fragment",   # 1 - Rocky Outcrop
    "Energy Crystal",        # 2 - Crystal Cave
    "Bio-Fuel Cell",         # 3 - Dense Forest
    "Ancient Battery",       # 4 - Ancient Ruins
    "Cooling Unit",          # 5 - Frozen Lake
    "Heat Exchanger",        # 6 - Volcanic Vents
    None,                    # 7 - Metal Wreckage (no item)
    None,                    # 8 - Strange Monolith (no item)
    None                     # 9 - Energy Crater (no item)
]

# Grid layout for reference:
# [0] [1] [2]
# [3] [4] [5]
# [6] [7] [8]
#     [9]

# Visual Map Layout:
#  [0]--[1]--[2]     Crash Site -- Rocky Outcrop -- Crystal Cave
#   |    |    |              |            |              |
#  [3]--[4]--[5]   Dense Forest -- Ancient Ruins -- Frozen Lake  
#   |    |    |              |            |              |
#  [6]--[7]--[8]  Volcanic Vents -- Metal Wreckage -- Strange Monolith
#       |                        |
#      [9]                  Energy Crater

# The 6 generator pieces are scattered at locations 1, 2, 3, 4, 5, 6
# Locations 0, 7, 8, 9 have no items but can be explored

def print_game_map():
    """Print a static visual representation of the game map"""
    print("\n" + "=" * 70)
    print("                        DEAD SHIP - PLANET MAP")
    print("=" * 70)
    print()
    print("  [0]────[1]────[2]      Crash Site ──── Rocky Outcrop ──── Crystal Cave")
    print("   │      │      │              │               │                │")
    print("   │      │      │              │               │                │") 
    print("  [3]────[4]────[5]    Dense Forest ──── Ancient Ruins ──── Frozen Lake")
    print("   │      │      │              │               │                │")
    print("   │      │      │              │               │                │")
    print("  [6]────[7]────[8]   Volcanic Vents ─── Metal Wreckage ─── Strange Monolith")
    print("         │                      │")
    print("         │                      │")
    print("        [9]              Energy Crater")
    print()
    print("GENERATOR PIECES LOCATIONS:")
    print("  [1] Rocky Outcrop    - Power Core Fragment")
    print("  [2] Crystal Cave     - Energy Crystal") 
    print("  [3] Dense Forest     - Bio-Fuel Cell")
    print("  [4] Ancient Ruins    - Ancient Battery")
    print("  [5] Frozen Lake      - Cooling Unit")
    print("  [6] Volcanic Vents   - Heat Exchanger")
    print()
    print("EMPTY LOCATIONS (no generator pieces):")
    print("  [0] Crash Site       - Starting location")
    print("  [7] Metal Wreckage   - Exploration area")
    print("  [8] Strange Monolith - Exploration area") 
    print("  [9] Energy Crater    - Exploration area")
    print("=" * 70)
