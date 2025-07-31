# Dead Ship - Simple Text Adventure Game

A beginner-friendly Python text adventure game for learning programming concepts.

## Story

Your spaceship has crashed on an alien planet! The energy generator has been smashed into 6 pieces scattered across the planet. You must find all 6 pieces before your energy runs out, or you'll be stranded forever!

## Map
======================================================================
                        DEAD SHIP - PLANET MAP
======================================================================

  [0]────[1]────[2]      Crash Site ──── Rocky Outcrop ──── Crystal Cave
   │      │      │              │               │                │
   │      │      │              │               │                │ 
  [3]────[4]────[5]    Dense Forest ──── Ancient Ruins ──── Frozen Lake
   │      │      │              │               │                │
   │      │      │              │               │                │
  [6]────[7]────[8]   Volcanic Vents ─── Metal Wreckage ─── Strange Monolith
         │                      │
         │                      │
        [9]              Energy Crater

GENERATOR PIECES LOCATIONS:
  [1] Rocky Outcrop    - Power Core Fragment
  [2] Crystal Cave     - Energy Crystal 
  [3] Dense Forest     - Bio-Fuel Cell
  [4] Ancient Ruins    - Ancient Battery
  [5] Frozen Lake      - Cooling Unit
  [6] Volcanic Vents   - Heat Exchanger

EMPTY LOCATIONS (no generator pieces):
  [0] Crash Site       - Starting location
  [7] Metal Wreckage   - Exploration area
  [8] Strange Monolith - Exploration area 
  [9] Energy Crater    - Exploration area
======================================================================

## How to Play

### Starting the Game
```bash
python main.py
```

### Commands
- `go north` - Move north
- `go south` - Move south  
- `go east` - Move east
- `go west` - Move west
- `look` - Look around your current location
- `inventory` - Check what generator pieces you've found
- `help` - Show help information
- `quit` - Quit the game

### Game Mechanics

#### Energy System
- You start with 50 energy
- Moving costs 3 energy
- Finding a generator piece gives you 10 energy
- Energy slowly decays over time (1 point every 3 turns)
- If energy reaches 0, you lose!

#### Winning
- Find all 6 generator pieces to win
- Generator pieces are scattered across the planet
- You need to explore different locations to find them

### Map Layout

The planet has 10 locations arranged like this:

```
[Crash Site] [Rocky Outcrop] [Crystal Cave]
[Dense Forest] [Ancient Ruins] [Frozen Lake]  
[Volcanic Vents] [Metal Wreckage] [Strange Monolith]
               [Energy Crater]
```

### Generator Pieces Locations
1. **Power Core Fragment** - Rocky Outcrop
2. **Energy Crystal** - Crystal Cave
3. **Bio-Fuel Cell** - Dense Forest
4. **Ancient Battery** - Ancient Ruins
5. **Cooling Unit** - Frozen Lake
6. **Heat Exchanger** - Volcanic Vents

## Files Structure

### main.py
- Contains the main game loop
- Handles user input and game flow
- Simple and easy to understand for beginners

### functions.py
- Contains all game functions:
  - `show_location()` - Display current location
  - `move_player()` - Handle player movement
  - `check_for_item()` - Check if location has an item
  - `add_to_inventory()` - Add items to player inventory
  - `show_inventory()` - Display player's items
  - `check_game_over()` - Check win/lose conditions
  - `show_help()` - Display help information

### data.py
- Contains game data using simple lists:
  - `LOCATION_NAMES` - List of location names
  - `LOCATION_DESCRIPTIONS` - List of location descriptions
  - `LOCATION_ITEMS` - List of items at each location

## Learning Goals

This game demonstrates:
- **Functions** - Breaking code into reusable functions
- **Lists** - Using lists to store game data
- **Variables** - Tracking game state with variables
- **Loops** - Main game loop with while
- **Conditionals** - if/elif/else statements
- **User Input** - Getting and processing player commands
- **Imports** - Organizing code across multiple files

## Example Gameplay

```
==================================================
           DEAD SHIP
==================================================

--- Crash Site ---
The twisted remains of your ship lie scattered here. Smoke still rises from the wreckage.
You can go: north, west

Energy: 50
Generator pieces found: 0/6

What do you do? go north

--- Dense Forest ---
Towering alien trees block most of the light. Strange sounds echo in the darkness.
You can go: south, east, west
You see something glinting: Bio-Fuel Cell

You found a Bio-Fuel Cell!

Energy: 57
Generator pieces found: 1/6
```

Good luck escaping the planet!
