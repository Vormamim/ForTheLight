# data.py

rooms = {
    "cell": {
        "description": "A cold detention cell with dim lights and a locked door to the north.",
        "exits": {"north": "hallway"},
        "items": []
    },
    "hallway": {
        "description": "A narrow hallway patrolled by droids. East leads to a control room. West leads to an armoury.",
        "exits": {"south": "cell", "east": "control_room", "west": "armoury"},
        "items": []
    },
    "armoury": {
        "description": "Stacks of weapons and equipment. There’s a blaster on the shelf.",
        "exits": {"east": "hallway"},
        "items": ["blaster"]
    },
    "control_room": {
        "description": "Screens flash with security alerts. A terminal glows. North leads to the escape pod.",
        "exits": {"west": "hallway", "north": "escape_pod"},
        "items": ["keycard"]
    },
    "escape_pod": {
        "description": "A single escape pod sits waiting. The panel blinks: Insert Keycard.",
        "exits": {"south": "control_room"},
        "items": []
    }
}

starting_room = "cell"
