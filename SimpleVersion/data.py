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

# The 6 generator pieces are scattered at locations 1, 2, 3, 4, 5, 6
# Locations 0, 7, 8, 9 have no items but can be explored
