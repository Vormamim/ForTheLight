"""
The Wheel of Time - Text Adventure Game
Game data and constants
"""

# Game constants
TITLE_TEXT = """
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║                    THE WHEEL OF TIME                         ║
║                                                              ║
║                   A Text Adventure Game                      ║
║                                                              ║
║            "The Wheel of Time turns, and Ages come          ║
║             and pass, leaving memories that become          ║
║                    legend. Legend fades to myth,            ║
║                    and even myth is long forgotten          ║
║                    when the Age that gave it birth          ║
║                    comes again."                             ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
"""

PROMPT_SYMBOL = ">"

# Character classes
CHARACTERS = {
    'gleeman': {
        'name': 'Thom Merrilin',
        'class': 'Gleeman',
        'description': 'A skilled storyteller and performer with hidden depths',
        'health': 80,
        'attack': 12,
        'defense': 8,
        'starting_items': ['Throwing Knives', 'Flute', 'Coins'],
        'intro': 'You are Thom Merrilin, a gleeman with white mustaches and a talent for survival. Your knives are as sharp as your wit, and your stories have opened more doors than any key.'
    },
    'warder': {
        'name': 'Lan Mandragoran',
        'class': 'Warder',
        'description': 'A deadly warrior bound by honor and duty',
        'health': 120,
        'attack': 18,
        'defense': 14,
        'starting_items': ['Sword', 'Warder Cloak', 'Healing Herbs'],
        'intro': 'You are Lan Mandragoran, last king of Malkier and Warder to Moiraine Sedai. Your sword is your life, and your honor is your strength.'
    },
    'aes_sedai': {
        'name': 'Moiraine Damodred',
        'class': 'Aes Sedai',
        'description': 'A wielder of the One Power with mysterious knowledge',
        'health': 90,
        'attack': 15,
        'defense': 10,
        'starting_items': ['Angreal', 'Blue Stone', 'Ancient Scroll'],
        'intro': 'You are Moiraine Damodred of the Blue Ajah. The One Power flows through you, and the Pattern shows you glimpses of what must come to pass.'
    },
    'woodsman': {
        'name': 'Perrin Aybara',
        'class': 'Woodsman',
        'description': 'A skilled tracker with a connection to wolves',
        'health': 100,
        'attack': 16,
        'defense': 12,
        'starting_items': ['Axe', 'Bow', 'Wolf Medallion'],
        'intro': 'You are Perrin Aybara, a blacksmith turned woodsman. Your golden eyes see more than most, and the wolves call you brother.'
    }
}

# Game locations
LOCATIONS = {
    'emond_field': {
        'name': "Emond's Field",
        'description': 'A peaceful village in the Two Rivers, with thatched roofs and a large green. The Winespring Inn stands prominently in the center, and you can hear the sound of Master Luhhan\'s hammer from the smithy.',
        'exits': {
            'north': 'whitebridge',
            'east': 'watch_hill',
            'south': 'tinker_camp'
        },
        'items': ['Village Map', 'Tabac Pouch', 'Wool Cloak'],
        'npcs': ['Tam al\'Thor', 'Bran al\'Vere', 'Nynaeve al\'Meara'],
        'enemies': []
    },
    'whitebridge': {
        'name': 'Whitebridge',
        'description': 'A large stone bridge spans the river here, gleaming white in the sunlight. The town bustles with merchants and travelers. You can see the Tower of Memory rising above the other buildings.',
        'exits': {
            'south': 'emond_field',
            'north': 'caemlyn',
            'east': 'shadar_logoth'
        },
        'items': ['Merchant\'s Purse', 'River Stone', 'Travel Rations'],
        'npcs': ['River Merchant', 'Bridge Guard', 'Traveling Minstrel'],
        'enemies': ['Bandit']
    },
    'caemlyn': {
        'name': 'Caemlyn',
        'description': 'The magnificent capital of Andor rises before you with its tall spires and gleaming walls. The Royal Palace dominates the skyline, and the streets are filled with people from all walks of life.',
        'exits': {
            'south': 'whitebridge',
            'east': 'tar_valon',
            'west': 'four_kings'
        },
        'items': ['Royal Seal', 'Guard\'s Helmet', 'Silver Coin'],
        'npcs': ['Queen Morgase', 'Captain Tallanvor', 'Palace Guard'],
        'enemies': ['Darkfriend']
    },
    'tar_valon': {
        'name': 'Tar Valon',
        'description': 'The White Tower rises majestically from the island city, its bone-white walls seeming to glow with their own light. Aes Sedai walk the streets in their colored shawls, and the very air seems to thrum with the One Power.',
        'exits': {
            'west': 'caemlyn',
            'south': 'shadar_logoth'
        },
        'items': ['Ter\'angreal', 'White Tower Ring', 'Healing Potion'],
        'npcs': ['Aes Sedai', 'Warder', 'Tower Guard'],
        'enemies': ['Black Ajah']
    },
    'shadar_logoth': {
        'name': 'Shadar Logoth',
        'description': 'The cursed city of Aridhol lies in ruins around you. Broken buildings and empty streets stretch as far as the eye can see. A sense of malevolent presence fills the air, and shadows seem to move of their own accord.',
        'exits': {
            'west': 'whitebridge',
            'north': 'tar_valon'
        },
        'items': ['Cursed Dagger', 'Ancient Tome', 'Shadowy Cloak'],
        'npcs': [],
        'enemies': ['Mashadar', 'Shadow Spawn']
    },
    'watch_hill': {
        'name': 'Watch Hill',
        'description': 'A small village built on a hill overlooking the surrounding countryside. The Wisdom\'s house sits at the top, and you can see smoke rising from chimneys throughout the settlement.',
        'exits': {
            'west': 'emond_field',
            'south': 'tinker_camp'
        },
        'items': ['Hill Stone', 'Wisdom\'s Herbs', 'Shepherd\'s Crook'],
        'npcs': ['Village Wisdom', 'Hill Shepherd', 'Farmer'],
        'enemies': ['Trolloc']
    },
    'tinker_camp': {
        'name': 'Tinker Camp',
        'description': 'Brightly colored wagons form a circle around a central campfire. The Tuatha\'an, the Traveling People, welcome you with music and dancing. Their wagons are painted in vibrant hues, and the smell of exotic spices fills the air.',
        'exits': {
            'north': 'emond_field',
            'northeast': 'watch_hill'
        },
        'items': ['Tinker Pot', 'Colorful Ribbon', 'Spice Pouch'],
        'npcs': ['Raen', 'Ila', 'Tinker Child'],
        'enemies': []
    },
    'four_kings': {
        'name': 'Four Kings',
        'description': 'A rough inn town where four roads meet. The buildings are weathered and the people suspicious. Dark clouds gather overhead, and you sense danger in the shadows.',
        'exits': {
            'east': 'caemlyn'
        },
        'items': ['Rusty Sword', 'Ale Mug', 'Torn Map'],
        'npcs': ['Innkeeper', 'Suspicious Stranger', 'Drunk Soldier'],
        'enemies': ['Darkfriend', 'Cutthroat']
    }
}

# Enemy types
ENEMIES = {
    'Trolloc': {
        'name': 'Trolloc',
        'description': 'A massive creature with the body of a man but the head of a beast. It carries a crude sword and snarls menacingly.',
        'health': 40,
        'attack': 12,
        'defense': 6,
        'experience': 25,
        'loot': ['Trolloc Blade', 'Beast Hide']
    },
    'Bandit': {
        'name': 'Bandit',
        'description': 'A desperate man with wild eyes and a rusted blade. He looks hungry and dangerous.',
        'health': 25,
        'attack': 8,
        'defense': 4,
        'experience': 15,
        'loot': ['Stolen Coins', 'Rusty Dagger']
    },
    'Darkfriend': {
        'name': 'Darkfriend',
        'description': 'A servant of the Shadow with eyes that gleam with malice. Dark power seems to radiate from them.',
        'health': 35,
        'attack': 10,
        'defense': 5,
        'experience': 30,
        'loot': ['Dark Medallion', 'Shadow Cloak']
    },
    'Mashadar': {
        'name': 'Mashadar',
        'description': 'A writhing mass of shadow and malevolence, the very essence of Shadar Logoth\'s corruption given form.',
        'health': 60,
        'attack': 15,
        'defense': 8,
        'experience': 50,
        'loot': ['Shard of Corruption', 'Shadowy Essence']
    },
    'Shadow Spawn': {
        'name': 'Shadow Spawn',
        'description': 'A creature of living darkness with burning red eyes and claws like razors.',
        'health': 45,
        'attack': 13,
        'defense': 7,
        'experience': 35,
        'loot': ['Shadow Fang', 'Dark Crystal']
    },
    'Black Ajah': {
        'name': 'Black Ajah',
        'description': 'A fallen Aes Sedai who has sworn to the Shadow. Power crackles around her fingers.',
        'health': 50,
        'attack': 16,
        'defense': 9,
        'experience': 60,
        'loot': ['Corrupted Angreal', 'Black Ring']
    },
    'Cutthroat': {
        'name': 'Cutthroat',
        'description': 'A vicious criminal with multiple scars and a wicked smile. He twirls a pair of daggers.',
        'health': 30,
        'attack': 11,
        'defense': 5,
        'experience': 20,
        'loot': ['Twin Daggers', 'Leather Armor']
    }
}

# NPC dialogues
NPC_DIALOGUES = {
    'Tam al\'Thor': [
        "The Wheel weaves as the Wheel wills, lad.",
        "There are strange rumors coming from the north.",
        "Keep your sword sharp and your wits sharper.",
        "The old blood runs strong in the Two Rivers."
    ],
    'Bran al\'Vere': [
        "Welcome to the Winespring Inn! What brings you to Emond's Field?",
        "Trade has been slow lately. Too many strange happenings.",
        "My Egwene has been having the strangest dreams.",
        "The Mayor's burdens are heavy these days."
    ],
    'Nynaeve al\'Meara': [
        "You look like you could use some healing herbs.",
        "The Wisdom sees much that others miss.",
        "Trust your instincts. They'll serve you well.",
        "The Pattern weaves us all together."
    ],
    'Queen Morgase': [
        "The throne of Andor requires constant vigilance.",
        "I sense great changes coming to the world.",
        "The Dragon Reborn... if the prophecies are true.",
        "Andor will stand against the Shadow."
    ],
    'Aes Sedai': [
        "The Wheel of Time turns, and Ages come and pass.",
        "The One Power flows through all creation.",
        "Trust in the Light, but prepare for darkness.",
        "The Pattern shows us what must be."
    ],
    'Raen': [
        "The Way of the Leaf teaches us patience.",
        "Violence solves nothing, young one.",
        "We search for the song that was lost.",
        "All are welcome in our caravan."
    ],
    'Ila': [
        "Come, share our fire and food.",
        "The Traveling People have seen much sorrow.",
        "Even in darkness, we must find joy.",
        "The song will be found again someday."
    ]
}

# Item descriptions
ITEM_DESCRIPTIONS = {
    'Village Map': 'A hand-drawn map of the Two Rivers, showing all the villages and major landmarks.',
    'Tabac Pouch': 'A leather pouch containing fine Two Rivers tabac, prized throughout the land.',
    'Wool Cloak': 'A warm cloak made from the finest Two Rivers wool, dyed a deep brown.',
    'Throwing Knives': 'A set of perfectly balanced throwing knives, deadly in the right hands.',
    'Flute': 'A gleeman\'s flute, capable of producing hauntingly beautiful melodies.',
    'Sword': 'A finely crafted sword with a heron-mark on the blade, sign of a blademaster.',
    'Warder Cloak': 'A cloak that seems to shift and blur, making its wearer hard to see.',
    'Angreal': 'An ancient ter\'angreal that allows a channeler to draw more of the One Power.',
    'Blue Stone': 'A smooth blue stone that seems to pulse with inner light.',
    'Ancient Scroll': 'A scroll covered in the Old Tongue, containing forgotten knowledge.',
    'Axe': 'A perfectly balanced axe, as much a work of art as a weapon.',
    'Bow': 'A Two Rivers longbow, capable of incredible accuracy in skilled hands.',
    'Wolf Medallion': 'A medallion carved in the shape of a wolf\'s head, warm to the touch.',
    'Cursed Dagger': 'A dagger from Shadar Logoth, beautiful but tainted with evil.',
    'Ter\'angreal': 'An object of the One Power from the Age of Legends.',
    'Healing Potion': 'A potion that can heal wounds and restore vitality.'
}

# Special items that trigger events
SPECIAL_ITEMS = {
    'Cursed Dagger': 'The dagger pulses with malevolent energy. You feel its corruption trying to seep into your soul.',
    'Angreal': 'The angreal resonates with power. If you could channel, this would amplify your abilities greatly.',
    'Wolf Medallion': 'The wolf medallion grows warm against your chest. You hear the distant howl of wolves.',
    'Ter\'angreal': 'The ter\'angreal hums with ancient power. You sense it has abilities beyond your understanding.',
    'Warder Cloak': 'The cloak seems to shimmer and fade. You feel harder to see while wearing it.',
    'Sword': 'The heron-mark sword feels perfectly balanced in your hand. Your skill with blades increases.',
    'Ancient Scroll': 'The scroll contains prophetic text that fills you with knowledge of your enemies.'
}

# Usable items
USABLE_ITEMS = [
    'Healing Potion',
    'Ancient Scroll',
    'Angreal',
    'Ter\'angreal'
]

# Random items for encounters
RANDOM_ITEMS = [
    'Healing Potion',
    'Silver Coin',
    'Travel Rations',
    'Rope',
    'Torch',
    'Blanket',
    'Waterskin',
    'Flint and Steel',
    'Lucky Charm',
    'Merchant\'s Note'
]

# Location-specific hints
LOCATION_HINTS = {
    'emond_field': [
        "Talk to the villagers to learn about the wider world - try 'talk tam' or 'talk nynaeve'.",
        "There might be useful items here you can 'take' - look around carefully.",
        "The Wisdom always has helpful advice - use 'talk nynaeve' to speak with her.",
        "Check the inn and smithy for supplies - use 'look' commands to examine things.",
        "Try 'take map' or 'take cloak' to gather useful items before you leave."
    ],
    'whitebridge': [
        "Merchants often have interesting items - try 'talk merchant' to learn more.",
        "The bridge guards might have information about dangers ahead - use 'talk guard'.",
        "Be careful of bandits near trading routes - keep your weapon ready.",
        "River stones are said to bring good luck - try 'take stone' to pick one up.",
        "Try 'look purse' to examine the merchant's belongings more closely."
    ],
    'caemlyn': [
        "The Royal Palace holds many secrets - talk to guards and nobles.",
        "City guards patrol regularly - they might help or provide information.",
        "Important people gather in capital cities - use 'talk' commands liberally.",
        "Look for signs of political intrigue - examine items and talk to everyone.",
        "Try 'talk morgase' if you encounter the Queen - royalty has valuable knowledge."
    ],
    'tar_valon': [
        "The White Tower is a center of power and knowledge - talk to Aes Sedai.",
        "Aes Sedai have many useful items and information - don't miss talking to them.",
        "The One Power flows strongly here - magical items might be more powerful.",
        "Warders are skilled fighters and allies - they can teach you about combat.",
        "Look for ter'angreal and other objects of power - use 'look' and 'take' commands."
    ],
    'shadar_logoth': [
        "This place is extremely dangerous - be prepared for combat with 'attack' commands.",
        "Valuable items might be hidden in ruins - but beware their corruption.",
        "The shadows themselves are your enemy here - fight anything that moves.",
        "Don't stay here too long - the corruption spreads. Get what you need and leave.",
        "Try 'look dagger' if you find cursed items, but be very careful with them."
    ],
    'watch_hill': [
        "Hill folk are hardy and self-reliant - they respect strength and honesty.",
        "The Wisdom here might have different herbs - try 'talk wisdom' for healing items.",
        "Shepherds know the lay of the land well - ask them about safe travel routes.",
        "Higher ground gives good views - try 'look around' to survey the area.",
        "Try 'take herbs' or 'take crook' if you see useful items from the hillfolk."
    ],
    'tinker_camp': [
        "The Tuatha'an are peaceful but knowledgeable - talk to Raen and Ila.",
        "Exotic spices and items might be found here - look for colorful objects.",
        "Music and stories can lift spirits - enjoy the peaceful atmosphere.",
        "The Traveling People have seen many places - they have valuable travel advice.",
        "Try 'take ribbon' or 'take spices' to gather unique tinker items."
    ],
    'four_kings': [
        "This is a dangerous place - watch for enemies and keep weapons ready.",
        "Suspicious characters gather here - be careful who you trust.",
        "The inn might have information, but be cautious - try 'talk innkeeper' carefully.",
        "Keep your weapons ready and gold hidden - danger lurks everywhere.",
        "Try 'look stranger' to examine suspicious people, but be prepared to fight."
    ]
}

# Victory conditions
VICTORY_CONDITIONS = {
    'items_collected': ['Cursed Dagger', 'Ancient Scroll', 'Ter\'angreal'],
    'enemies_defeated': ['Mashadar', 'Black Ajah'],
    'locations_visited': ['tar_valon', 'shadar_logoth'],
    'min_level': 3
}

# Game messages
DEATH_MESSAGES = [
    "The Wheel of Time turns, and your thread has been cut from the Pattern.",
    "The Shadow has claimed another victim.",
    "Your journey ends here, but the Wheel will turn again.",
    "The Pattern weaves around your fallen form."
]

LEVEL_UP_MESSAGES = [
    "You feel stronger and more experienced!",
    "Your skills have improved through trial and hardship!",
    "The Pattern has woven you into something greater!",
    "Knowledge and power flow through you!"
]

# Easter eggs and secrets
EASTER_EGGS = {
    'konami': 'The Creator\'s own cheat code has been activated!',
    'woolhead': 'Nynaeve would not approve of such language.',
    'taveren': 'The Pattern bends around you in strange ways.',
    'flaming': 'Mind your tongue! There are ladies present.'
}
