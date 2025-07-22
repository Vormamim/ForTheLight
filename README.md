# ANDOR: The Escape Begins — Text Adventure Game

This is a simple text-based adventure game written in Python, inspired by *Andor*. It is designed for **beginners learning Python**, with no classes or advanced features.

The game is split into three files:

- `main.py`: Runs the game.
- `data.py`: Stores the rooms and items.
- `functions.py`: Contains functions for moving, picking up items, and more.


## Why Do We Import `data` and `functions` into `main.py`?

In Python, you can **organize your code** into different files to keep things clean and easy to manage.

We split this game into three files:

* `main.py` → Runs the game
* `data.py` → Stores rooms, descriptions, and starting info
* `functions.py` → Contains reusable blocks of code (functions)

### Importing Means “Bring In”

In `main.py`, we use this line:

`from data import rooms, starting_room`

This means:

 “Get the `rooms` and `starting_room` from the `data.py` file so I can use them here in `main.py`.”

And we also use:

`from functions import show_location, get_command, move, take_item, check_end_game`

This means:

 “Bring in the functions I wrote in `functions.py` so I don’t have to rewrite them here.”

---

### Why This Is Helpful

* Keeps the code **neat** and **organised**
* You can **reuse functions**
* Easier to **fix bugs** when code is in smaller parts
* Makes it easier to **read** and **understand**

---

### Example

Instead of writing all the logic in one huge file, we just say:

`show_location(current_room, rooms)`

...and Python knows to **look in `functions.py`** to find out what that function does.

---

## Game Story

You are **Cassian Andor**, trapped in an imperial prison. Explore the base, collect useful items, and find a way to escape.

There are **multiple endings** based on what you do.

---

## How the Game Works

### Commands You Can Use

- `go north` / `go east` / `go west` / `go south`: Move around the map.
- `take blaster`, `take keycard`: Pick up items.
- `inventory`: Check what you are carrying.
- `quit`: End the game.

---

## File Descriptions

### `main.py`

- Starts the game.
- Loads the rooms and items.
- Waits for the player to type commands.
- Calls other functions (like move, take, etc).

### `data.py`

- Stores all the **rooms** in a Python dictionary.
- Each room has:
  - A description (what it looks like)
  - Exits (where you can go)
  - Items (what you can pick up)

Example:

`"armoury": {
    "description": "Stacks of weapons. There’s a blaster on the shelf.",
    "exits": {"east": "hallway"},
    "items": ["blaster"]
}`

### functions.py

#### Contains helper functions:

**show_location():** Tells you where you are and what you see.

**get_command():** Asks you what you want to do.

**move():** Lets you go in a direction (if it's allowed).

**take_item():** Lets you pick something up.

**check_end_game():** Checks if you reached an ending (like escape or getting caught).

## Endings

* If you reach the **escape pod** with the  **keycard** , you win!
* If you go into the hallway with a  **blaster** , you trigger a gunfight ending.
