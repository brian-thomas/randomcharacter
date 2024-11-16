"""
Attributes and general information about the D&D Character Classes.
"""


"""
The traditional 6 attributes, in order.
"""
ATTRIBUTES = ['STR', 'INT', 'WIS', 'DEX', 'CON', 'CHA']


"""
Indexes into ATTRIBUTES
"""
STR, INT, WIS, DEX, CON, CHA = range(6)


"""
20 example languages from Moldvay.
"""
LANGUAGES = [
    'Bugbear', 'Doppleganger', 'Dragon', 'Dwarvish', 'Elvish', 'Gargoyle',
    'Gnoll', 'Gnome', 'Goblin', 'Halfling', 'Harpy', 'Hobgoblin', 'Kobold',
    'Lizard Man','Medusa', 'Minotaur', 'Ogre', 'Orc', 'Pixie', 'Human Dialect'
]


"""
The 5 traditional D&D saving throws.
"""
SAVES = {
    'poison': 'Death Ray or Poison',
    'wands': 'Magical Wands',
    'stone': 'Paralysis or Turn to Stone',
    'breath': 'Dragon Breath',
    'magic': 'Rods, Staves, or Spells'
}


"""
The 7 character classes from Basic D&D. Equipment lists from Brendan's post
on the topic.
"""

CLERIC = {
    'name': 'Cleric',
    'equipment': [
        ["Cudgel", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "10' Pole", "Wooden Cross", "4 gp"],
        ["Cudgel", "Shield", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "50' Rope", "Wooden Cross", "4 gp"],
        ["Mace", "Leather Armor", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "10' Pole", "Wooden Cross", "5 gp"],
        ["Quarter-Staff", "Leather Armor", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "50' Rope", "12 5x Iron Spikes", "Wooden Cross", "3 Stakes & Mallet", "Steel Mirror", "10 gp"],
        ["Chain Armor", "War Hammer", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "10' Pole", "Wooden Cross", "2 Small Sacks", "8 gp"],
        ["Chain Armor", "Shield", "Mace", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "50' Rope", "Wooden Cross", "2 Small Sacks", "8 gp"],
        ["Chain Armor", "Shield", "War Hammer", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "10' Pole", "Wooden Cross", "2 Small Sacks", "3 Stakes & Mallet", "Steel Mirror", "10 gp"],
        ["Plate Armor", "Shield", "Mace", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "50' Rope", "Wooden Cross", "10 gp"],
        ["Plate Armor", "Shield", "War Hammer", "Backpack", "Waterskin", "Lantern", "4 Flasks oil", "1 Week Iron Rations", "10' Pole", "Wooden Cross", "Small Sack", "2 gp"],
        ["Plate Armor", "Quarter-Staff", "Backpack", "Waterskin", "Lantern", "4 Flasks oil", "1 Week Iron Rations", "50' Rope", "Silver Cross", "4 gp"],
        ["Cudgel", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "10' Pole", "Wooden Cross", "Scroll", "4 gp"],
        ["Plate Armor", "Shield", "Mace", "Backpack", "Waterskin", "Lantern", "4 Flasks oil", "1 Week Iron Rations", "50' Rope", "Silver Cross", "10 gp"],
        ["Leather Armor", "Mace", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "10' Pole", "Wooden Cross", "Scroll", "2 Flasks oil", "1 gp"],
        ["Plate Armor", "Shield", "Helmet", "War Hammer", "Backpack", "Waterskin", "Lantern", "4 Flasks oil", "1 Week Iron Rations", "50' Rope", "Silver Cross", "3 Stakes & Mallet", "Steel Mirror", "12 gp"],
        ["Chain Armor", "War Hammer", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "10' Pole", "Wooden Cross", "Scroll", "10 gp"],
        ["Plate Armor", "Shield", "Helmet", "Mace", "Backpack", "Waterskin", "Lantern", "4 Flasks oil", "1 Week Iron Rations", "50' Rope", "Silver Cross", "Vial Holy Water", "12 5x Iron Spikes", "3 Stakes & Mallet", "Small Sack", "10 gp"]
    ],
    'hitdice': 6,
    'saves': {
        'poison': 11, 'wands': 12, 'stone': 14, 'breath': 16, 'magic': 15
    },
    'turn': [
        ('Skeleton', 7), ('Zombie', 9), ('Ghoul', 11), ('Wight', 'N')
    ],
}

FIGHTER = {
    'name': "Fighter",
    'equipment': [
        ["Spear", "Dagger", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "50' Rope", "3 gp"],
        ["Cudgel", "Leather Armor", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "10' Pole", "1 gp"],
        ["Leather Armor", "Morning Star", "Dagger", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "50' Rope", "3 gp"],
        ["Leather Armor", "Battle axe", "Hand axe", "Dagger", "Sling", "Pouch With 20 Sling Bullets", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "10' Pole", "7 gp"],
        ["Chain Armor", "Spear", "Dagger", "Sling", "Pouch With 20 Sling Bullets", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "50' Rope", "11 gp"],
        ["Chain Armor", "Shield", "Sword", "Dagger", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "10' Pole", "4 gp"],
        ["Chain Armor", "Spear", "Light Crossbow", "Case With 30 Quarrels", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "50' Rope", "11 gp"],
        ["Plate Armor", "Shield", "Sword", "Dagger", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "10' Pole", "4 gp"],
        ["Plate Armor", "Two-Handed Sword", "3 Daggers", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "50' Rope", "2 Flasks oil", "9 gp"],
        ["Plate Armor", "Shield", "Sword", "Light Crossbow", "Case With 30 Quarrels", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "10' Pole", "2 gp"],
        ["Plate Armor", "Flail", "Dagger", "35 Short bow", "Quiver of 20 Arrows", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "50' Rope", "Small Sack", "10 gp"],
        ["Plate Armor", "Shield", "Sword", "Light Crossbow", "Case With 30 Quarrels", "Backpack", "Waterskin", "Lantern", "4 Flasks oil", "1 Week Iron Rations", "10' Pole", "5 gp"],
        ["Plate Armor", "Helmet", "2 Battle Axes", "Dagger", "Light Crossbow", "Case With 30 Quarrels", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "50' Rope", "5 Flasks oil", "15 gp"],
        ["Plate Armor", "Two-Handed Sword", "Dagger", "Short bow", "Quiver of 20 Arrows", "Backpack", "Waterskin", "Lantern", "4 Flasks oil", "1 Week Iron Rations", "10' Pole", "2 Small Sacks", "15 gp"],
        ["Plate Armor", "Halberd", "Dagger", "Long bow", "Quiver of 20 Arrows", "2 Silver Tipped Arrows", "Backpack", "Waterskin", "Lantern", "4 Flasks oil", "1 Week Iron Rations", "50' Rope", "10 gp"],
        ["Plate Armor", "Shield", "Helmet", "Sword", "2 Daggers", "Light Crossbow", "Case With 30 Quarrels", "4 Silver Tipped Quarrels", "Backpack", "Waterskin", "Lantern", "4 Flasks oil", "1 Week Iron Rations", "10' Pole", "9 gp"]
    ],
    'hitdice': 8,
    'saves': {
        'poison': 12, 'wands': 13, 'stone': 14, 'breath': 15, 'magic': 16
    }
}

# For Carcosa we have the Sorcerer variant of a fighter.
SORCERER = {
    'name': "Sorcerer",
    'equipment': FIGHTER['equipment'],
    'hitdice': 8,
    'saves': {
        'poison': 12, 'wands': 13, 'stone': 13, 'breath': 15, 'magic': 14
    }
}

MAGICUSER = {
    'name': "Magic-User",
    'equipment': [
        ["Dagger", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "10' Pole", "4 gp"],
        ["2 Daggers", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "2 Flasks oil", "50' Rope", "7 gp"],
        ["Dagger", "Backpack", "Waterskin", "Lantern", "4 Flasks oil", "1 Week Iron Rations", "10' Pole", "7 gp"],
        ["Dagger", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "50' Rope", "Vial of Holy Water", "9 gp"],
        ["Dagger", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "10' Pole", "5 Flasks of oil", "Silver Mirror", "Belladona", "9 gp"],
        ["Dagger", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "50' Rope", "2 Vials Holy Water", "4 gp"],
        ["3 Daggers", "Backpack", "Waterskin", "Lantern", "4 Flasks oil", "1 Week Iron Rations", "10' Pole", "Vial of Holy Water", "16 gp"],
        ["Dagger", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "50' Rope", "2 Vials Holy Water", "24 gp"],
        ["Dagger", "Backpack", "Waterskin", "Lantern", "4 Flasks oil", "1 Week Iron Rations", "10' Pole", "67 gp"],
        ["Dagger", "Backpack", "Waterskin", "Lantern", "4 Flasks oil", "1 Week Iron Rations", "50' Rope", "77 gp"],
        ["Dagger", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "Scroll", "10' Pole", "4 gp"],
        ["2 Daggers", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "Scroll", "50' Rope", "11 gp"],
        ["Dagger", "Backpack", "Waterskin", "Lantern", "4 Flasks oil", "1 Week Iron Rations", "Scroll", "10' Pole", "7 gp"],
        ["Dagger", "Backpack", "Waterskin", "Lantern", "4 Flasks oil", "1 Week Iron Rations", "Scroll", "50' Rope", "17 gp"],
        ["Dagger", "Backpack", "Waterskin", "Lantern", "4 Flasks oil", "1 Week Iron Rations", "Scroll", "10' Pole", "27 gp"],
        ["Dagger", "Backpack", "Waterskin", "Lantern", "4 Flasks oil", "1 Week Iron Rations", "Scroll", "50' Rope", "37 gp"]
    ],
    'hitdice': 4,
    'saves': {
        'poison': 13, 'wands': 14, 'stone': 13, 'breath': 16, 'magic': 15
    },
    'spells': [
        # Original 8 D&D Spells
        'Detect Magic', 'Hold Portal', 'Read Magic', 'Read Languages',
        'Protection from Evil', 'Light', 'Charm Person', 'Sleep',
        # Basic D&D added 4 new Spells
        'Floating Disc', 'Magic Missile', 'Shield', 'Ventriloquism'
    ],
}

THIEF = {
    'name': "Thief",
    'equipment': [
        ["Cudgel", "Sling", "Pouch With 20 Sling Bullets", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "50' Rope", "4 gp"],
        ["Cudgel", "Leather Armor", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "10' Pole", "1 gp"],
        ["Cudgel", "Dagger", "Sling", "Pouch With 20 Sling Bullets", "Leather Armor", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "50' Rope", "6 gp"],
        ["Sword", "Dagger", "Leather Armor", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "10' Pole", "9 gp"],
        ["Cudgel", "Light Crossbow", "Case With 30 Quarrels", "Leather Armor", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "50' Rope", "6 gp"],
        ["Sword", "Light Crossbow", "Case of 30 Quarrels", "Leather Armor", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "10' Pole", "7 gp"],
        ["Sword", "2 Daggers", "35 Short bow", "Quiver of 20 Arrows", "Leather Armor", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "50' Rope", "1 gp"],
        ["Sword", "Dagger", "Leather Armor", "Backpack", "Waterskin", "Lantern", "4 Flasks oil", "1 Week Iron Rations", "10' Pole", "32 gp"],
        ["Sword", "Light Crossbow", "Case of 30 Quarrels", "2 Silver Tipped Quarrels", "Leather Armor", "Backpack", "Waterskin", "Lantern", "4 Flasks oil", "1 Week Iron Rations", "50' Rope", "10 gp"],
        ["Sword", "Dagger", "Short bow", "Quiver of 20 Arrows", "Leather Armor", "Backpack", "Waterskin", "Lantern", "4 Flasks oil", "1 Week Iron Rations", "10' Pole", "17 gp"],
        ["Sword", "Leather Armor", "Backpack", "Waterskin", "Lantern", "4 Flasks oil", "1 Week Iron Rations", "50' Rope", "65 gp"],
        ["Sword", "Light Crossbow", "Case of 30 Quarrels", "6 Silver Tipped Quarrels", "Leather Armor", "Backpack", "Waterskin", "Lantern", "4 Flasks oil", "1 Week Iron Rations", "10' Pole", "20 gp"],
        ["Sword", "Short bow", "Quiver of 20 Arrows", "6 Silver Tipped Arrows", "Leather Armor", "Backpack", "Waterskin", "Lantern", "4 Flasks oil", "1 Week Iron Rations", "50' Rope", "20 gp"],
        ["Sword", "4 Daggers", "Leather Armor", "Backpack", "Waterskin", "Lantern", "4 Flasks oil", "1 Week Iron Rations", "10' Pole", "98 gp"],
        ["Sword", "Light Crossbow", "Case of 30 Quarrels", "Leather Armor", "Backpack", "Waterskin", "Lantern", "4 Flasks oil", "1 Week Iron Rations", "50' Rope", "80 gp"],
        ["Sword", "3 Daggers", "Short bow", "Quiver of 20 Arrows", "8 Silver Tipped Arrows", "Leather Armor", "Backpack", "Waterskin", "Lantern", "4 Flasks oil", "1 Week Iron Rations", "10' Pole", "31 gp"]
    ],
    'hitdice': 4,
    'saves': {
        'poison': 13, 'wands': 14, 'stone': 13, 'breath': 16, 'magic': 15
    },
    'skills': [
        ('Open Locks', '15%'),
        ('Find Traps', '10%'),
        ('Remove Traps', '10%'),
        ('Climb Walls', '87%'),
        ('Move Silently', '20%'),
        ('Hide in Shadows', '10%'),
        ('Pick Pockets', '20%'),
        ('Hear Noise', '1-2')
    ],
}

DWARF = {
    'name': 'Dwarf',
    'hitdice': 8,
    'saves': {
        'poison': 10, 'wands': 11, 'stone': 12, 'breath': 13, 'magic': 14
    },
    'equipment': FIGHTER['equipment']
}

ELF = {
    'name': 'Elf',
    'hitdice': 6,
    'saves': {
        'poison': 12, 'wands': 13, 'stone': 13, 'breath': 15, 'magic': 15
    },
    'equipment': MAGICUSER['equipment'],
    'spells': MAGICUSER['spells']
}

HALFLING = {
    'name': 'Halfling',
    'hitdice': 6,
    'saves': {
        'poison': 10, 'wands': 11, 'stone': 12, 'breath': 13, 'magic': 14
    },
    'equipment': FIGHTER['equipment']
}


"""
In Pahvelorn characters start with a random retainer.
"""
RETAINERS = [
    'Bodyguard (leather, dagger, d4: 1 sword, 2 mace, 3 battle axe, 4 spear)',
    'Torchbearer (dagger, 6 torches)',
    'Porter (dagger, backpack, 3 small sacks, 1 large sack)',
    'Squire (dagger)',
    'Mercenary (leather, sword, dagger, light crossbow, case with 30 quarrels)',
    'Shieldbearer (leather, shield, dagger)',
    'Servant (dagger)',
    'Dog (spiked collar, leash)',
]


"""
In Pahvelorn characters begin with one spell book, and must hunt for others.
"""
STARTING_GRIMOIRE = ('Arcana Metaphysica, anonymous', [
        'Read Magic (1)',
        'Dispel Magic (3)',
        'Remove Curse (4)',
        'Anti-Magic Shell (6)',
    ]
)

GRIMOIRES = [
    ('The Hidden Knowledge, attributed to Cochyla the Younger', [
		'Detect Magic (1)',
		'Detect Evil (1)',
		'Locate Object (2)',
		'ESP (2)',
		'Clairvoyance (3)',
		'Clairaudience (3)',
		'Wizard Eye (4)',
    ]),
    ('Realms Seen and Unseen, attributed to the Fifth Council', [
		'Light (1)',
		'Detect Invisibility (2)',
		'Invisibility (2)',
		'Continual Light (2)',
		'Invisibility, 10\' Radius (3)',
		'Infravision (3)',
    ]),
    ('The Organ of the Inner Moon, attributed to Sezius Elfblood', [
		'Charm Person (1)',
		'Sleep (1)',
		'Hold Person (3)',
		'Confusion (4)',
		'Charm Monster (4)',
		'Feeblemind (5)',
		'Geas (6)',
    ]),
    ('Mastering Gates, attributed to Marlow Shadow-Walker', [
		'Hold Portal (1)',
		'Wizard Lock (2)',
		'Knock (2)',
		'Pass-Wall (5)',
    ]),
    ('Codex of the Cloud-Masters, anonymous', [
		'Levitate (2)',
		'Fly (3)',
		'Protection from Normal Missiles (3)',
		'Telekinesis (5)',
    ]),
    ('Illusio, anonymous', [
		'Phantasmal Forces (2)',
		'Hallucinatory Terrain (4)',
		'Massmorph (4)',
		'Projected Image (6)',
    ]),
    ('On Essence, attributed to Caleia', [
		'Polymorph Self (4)',
		'Polymorph Others (4)',
		'Transmute Rock-Mud (5)',
		'Growth of Animals (5)',
		'Stone-Flesh (6)',
    ]),
    ('Arbatel of Flame', [
		'Fire Ball (3)',
		'Lightning Bolt (3)',
		'Disintegrate (6)',
    ]),
    ('Songs of Three Winters, attributed to Taymar the Wise', [
		'Slow Spell (3)',
		'Haste Spell (3)',
    ]),
    ('Arcana Necromantica, anonymous', [
		'Animate Dead (5)',
		'Magic Jar (5)',
		'Reincarnation (6)',
		'Death Spell (6)',
    ]),
    ('Conjurations & Banishments (fragments), anonymous', [
		'Protection from Evil (1)',
		'Protection from Evil, 10\' Radius (3)',
		'Conjure Elemental (5)',
		'Contact Higher Plane (5)',
		'Invisible Stalker (6)',
    ]),
    ('The Roads Between the Stars (fragments), anonymous', [
		'Dimension Door (4)',
		'Teleport (5)',
    ]),
]

HOMEBREW = {
    'skills': [
        ('Athletics', 0),
        ('Languages', 0),
        ('Open Doors', 0),
        ('Search', 0),
        ('Stealth', 0),
        ('Social', 0),
        ('Arcana', 0),
        ('Armory', 0),
        ('Architecture', 0),
        ('Bushcraft', 0),
        ('Sleight of Hand', 0),
        ('Theology', 0),
        ('Tinker', 0),
    ],

    'occupations' : { 
        'Acrobat' : { 'equip' : ["10' pole"], 'stats' : {'DEX' : 1,}, 'skills' : {}, 'MB' : 0, 'RB' : 0, }, 
        'Apothecary' : { 'equip' : ["Bag of Herbs (1lb)"], 'stats' : {}, 'skills' : {'Arcana' : 1}, 'MB' : 0, 'RB' : 0, }, 
        'Architect' : { 'equip' : ["Drafting Kit"], 'stats' : {}, 'skills' : {'Architecture' : 1}, 'MB' : 0, 'RB' : 0, }, 
        'Armorer' : { 'equip' : ["Hammer, small"], 'stats' : {}, 'skills' : {'Armory' : 1}, 'MB' : 0, 'RB' : 0},
        'Artist' : { 'equip' : ["Pencils", "Book, blank"], 'stats' : {'CHA' : 1}, 'skills' : {}, 'MB' : 0, 'RB' : 0, }, 
        'Astrologer' : { 'equip' : ["Spyglass"], 'stats' : {'INT' : 1}, 'skills' : {}, 'MB' : 0, 'RB' : 0, }, 
        'Baker' : { 'equip' : ["Rolling Pin"], 'stats' : {}, 'skills' : {'Bushcraft' : 1}, 'MB' : 0, 'RB' : 0, }, 
        'Beggar' : { 'equip' : ["Crutch"], 'stats' : {}, 'skills' : {'Sleight of Hand' : 1}, 'MB' : 0, 'RB' : 0, }, 
        'Blacksmith' : { 'equip' : ['Chisel & Hammer, small'], 'stats' : {'STR' : 1}, 'skills' : {}, 'MB' : 0, 'RB' : 0, }, 
        'Bowyer' : { 'equip' : ["Shortbow"], 'stats' : {}, 'skills' : {}, 'MB' : 0, 'RB' : 1, }, 
        'Brewer' : { 'equip' : ["Bottle of Ale (rich)"], 'stats' : {'CON' : 1}, 'skills' : {}, 'MB' : 0, 'RB' : 0, }, 
        'Bricklayer' : { 'equip' : ["Trowel", "1d6 Bricks"], 'stats' : {}, 'skills' : {'Architecture' : 1}, 'MB' : 0, 'RB' : 0, }, 
        'Carpenter' : { 'equip' : ["Carpenter's Tools"], 'stats' : {'STR' : 1}, 'skills' : {}, 'MB' : 0, 'RB' : 0, }, 
        'Cartographer' : { 'equip' : ['Maps'], 'stats' : {'WIS' : 1}, 'skills' : {}, 'MB' : 0, 'RB' : 0, }, 
        'Clothier' : { 'equip' : ['Clothing, Extravagant'], 'stats' : {'CHA' : 1}, 'skills' : {}, 'MB' : 0, 'RB' : 0, }, 
        'Cook' : { 'equip' : ['Cleaver'], 'stats' : {}, 'skills' : {'Bushcraft' : 1}, 'MB' : 0, 'RB' : 0, }, 
        'Diplomat' : { 'equip' : ['Quill, Ink & Paper'], 'stats' : {}, 'skills' : {'Languages' : 1}, 'MB' : 0, 'RB' : 0, }, 
        'Dyer' : { 'equip' : ['Assorted Dye Vials'], 'stats' : {'CHA' : 1}, 'skills' : {}, 'MB' : 0, 'RB' : 0, }, 
        'Engraver' : { 'equip' : ['Engraving Kit'], 'stats' : {}, 'skills' : {'Tinker' : 1}, 'MB' : 0, 'RB' : 0, }, 
        'Farmer' : { 'equip' : ['Pet Dog'], 'stats' : {'CON' : 1}, 'skills' : {}, 'MB' : 0, 'RB' : 0, }, 
        'Fisherman' : { 'equip' : ['Fishing Gear'], 'stats' : {'CON' : 1}, 'skills' : {}, 'MB' : 0, 'RB' : 0, }, 
        'Forester' : { 'equip' : ["Woodcutter's Axe"], 'stats' : {}, 'skills' : {'Bushcraft' : 1}, 'MB' : 0, 'RB' : 0, }, 
        'Fortune-Teller' : { 'equip' : ['Tarot Deck'], 'stats' : {'WIS' : 1}, 'skills' : {}, 'MB' : 0, 'RB' : 0, }, 
        'Furrier' : { 'equip' : ['Clothing, Winter Travel'], 'stats' : {}, 'skills' : {'Bushcraft' : 1}, 'MB' : 0, 'RB' : 0, }, 
        'Gardener' : { 'equip' : ['Spade & Seeds'], 'stats' : {}, 'skills' : {'Bushcraft' : 1}, 'MB' : 0, 'RB' : 0, }, 
        'Glassblower' : { 'equip' : ['Tongs'], 'stats' : {'DEX' : 1}, 'skills' : {}, 'MB' : 0, 'RB' : 0, }, 
        'Gravedigger' : { 'equip' : ['Shovel'], 'stats' : {'CON' : 1}, 'skills' : {}, 'MB' : 0, 'RB' : 0, }, 
        'Hunter' : { 'equip' : ['Hunting Bow', 'Quiver with 20 Arrows'], 'stats' : {}, 'skills' : {}, 'MB' : 0, 'RB' : 1, }, 
        'Innkeeper' : { 'equip' : ['1d6 x 10 sp'], 'stats' : {'CHA' : 1}, 'skills' : {}, 'MB' : 0, 'RB' : 0, }, 
        'Interpreter' : { 'equip' : ['Quill, Ink & Paper'], 'stats' : {}, 'skills' : {'Languages' : 1}, 'MB' : 0, 'RB' : 0, }, 
        'Jailer' : { 'equip' : ['Manacles'], 'stats' : {}, 'skills' : {}, 'MB' : 1, 'RB' : 0, }, 
        'Jester' : { 'equip' : ['Sceptre'], 'stats' : {}, 'skills' : {'Sleight of Hand' : 1}, 'MB' : 0, 'RB' : 0, }, 
        'Juggler' : { 'equip' : ['Juggling Pins'], 'stats' : {}, 'skills' : {'Sleight of Hand' : 1}, 'MB' : 0, 'RB' : 0, }, 
        'Leatherworker' : { 'equip' : ['Leathercraft Kit'], 'stats' : {'STR' : 1}, 'skills' : {}, 'MB' : 0, 'RB' : 0, }, 
        'Locksmith' : { 'equip' : ["Specialist's Tools"], 'stats' : {}, 'skills' : {'Tinker' : 1}, 'MB' : 0, 'RB' : 0, }, 
        'Mercenary' : { 'equip' : ['Greatsword'], 'stats' : {}, 'skills' : {}, 'MB' : 1, 'RB' : 1, }, 
        'Messenger' : { 'equip' : ['Rucksack, quality'], 'stats' : {}, 'skills' : {'Languages' : 1}, 'MB' : 0, 'RB' : 0, }, 
        'Miner' : { 'equip' : ["Miner's Pick"], 'stats' : {'CON' : 1}, 'skills' : {}, 'MB' : 0, 'RB' : 0, }, 
        'Minstrel' : { 'equip' : ['Musical Instrument'], 'stats' : {'CHA' : 1}, 'skills' : {}, 'MB' : 0, 'RB' : 0, }, 
        'Musician' : { 'equip' : ['Musical Instrument'], 'stats' : {}, 'skills' : {'Social' : 2}, 'MB' : 0, 'RB' : 0, }, 
        'Moneylender' : { 'equip' : ['3d6 x 10 sp'], 'stats' : {'INT' : 1}, 'skills' : {}, 'MB' : 0, 'RB' : 0, }, 
        'Navigator' : { 'equip' : ['Compass'], 'stats' : {}, 'skills' : {'Search' : 1}, 'MB' : 0, 'RB' : 0, }, 
        'Painter' : { 'equip' : ["Painting Set"], 'stats' : {'CHA' : 1}, 'skills' : {}, 'MB' : 0, 'RB' : 0, }, 
        'Physician' : { 'equip' : ['Medical Kit'], 'stats' : {'INT' : 1}, 'skills' : {}, 'MB' : 0, 'RB' : 0, }, 
        'Rat Catcher' : { 'equip' : ["2d6 Rats (caged)"], 'stats' : {'CON' : 1}, 'skills' : {}, 'MB' : 0, 'RB' : 0, }, 
        'Sailor' : { 'equip' : ["50' Rope"], 'stats' : {}, 'skills' : {'Athletics' : 1}, 'MB' : 0, 'RB' : 0, }, 
        'Scribe' : { 'equip' : ['Quill, Ink & Pen'], 'stats' : {}, 'skills' : {'Languages' : 1}, 'MB' : 0, 'RB' : 0, }, 
        'Servant' : { 'equip' : ['Bottle of Wine (rich)'], 'stats' : {}, 'skills' : {'Open Doors' : 1}, 'MB' : 0, 'RB' : 0, }, 
        'Shipwright' : { 'equip' : ['Mallet'], 'stats' : {}, 'skills' : {'Tinker' : 1}, 'MB' : 0, 'RB' : 0, }, 
        'Spy' : { 'equip' : ['Wig & Fake Moustache'], 'stats' : {}, 'skills' : {'Stealth' : 1}, 'MB' : 0, 'RB' : 0, }, 
        'Stonecarver' : { 'equip' : ['Chisel & Hammer, small'], 'stats' : {'STR' : 1}, 'skills' : {}, 'MB' : 0, 'RB' : 0, }, 
        'Storyteller' : { 'equip' : ['Book of Fables'], 'stats' : {}, 'skills' : {'Social' : 2}, 'MB' : 0, 'RB' : 0, }, 
        #'' : { 'equip' : [], 'stats' : {}, 'skills' : {}, 'MB' : 0, 'RB' : 0, }, 
        }, 

    'specialist_builds': [
        # all have 5 slots
        ['Sleight of Hand', 'Stealth', 'Stealth', 'Sneak Attack', 'Sneak Attack'],
        ['Stealth', 'Stealth', 'Stealth', 'Sneak Attack', 'Sneak Attack'],
        ['Stealth', 'Stealth', 'Sneak Attack', 'Sneak Attack', 'Sneak Attack'],
        ['Stealth', 'Sneak Attack', 'Sneak Attack', 'Sneak Attack', 'Sneak Attack'],
        ['Search', 'Search', 'Tinker', 'Tinker', 'Tinker'],
        ['Search', 'Search', 'Search', 'Tinker', 'Tinker'],
        ['Athletics', 'Athletics', 'Open Doors', 'Search', 'Open Doors'],
        ['Athletics', 'Athletics', 'Open Doors', 'Search', 'Search'],
        ['Athletics', 'Stealth', 'Athletics', 'Search', 'Sneak Attack'],
        ['Stealth', 'Stealth', 'Athletics', 'Search', 'Sneak Attack'],
        ['Tinker', 'Sneak Attack', 'Sneak Attack', 'Sneak Attack', 'Stealth'],
        ['Search', 'Search', 'Search', 'Search', 'Search'],
        ['Tinker', 'Tinker', 'Tinker', 'Tinker', 'Search'],
        ['Tinker', 'Tinker', 'Tinker', 'Tinker', 'Athletics'],
        ['Architecture', 'Languages', 'Open Doors', 'Tinker', 'Languages'],
        ['Architecture', 'Languages', 'Open Doors', 'Tinker', 'Tinker'],
    ],

    'saves': {
        'poison': 'Health',
        'wands': 'Dodge',
        'stone': 'Perception',
        'breath': 'Willpower',
        'magic': 'Fortitude'
    },
}

"""
Additional information for Lamentations of the Flame Princess characters.
"""
LOTFP = {
    'skills': [
        ('Architecture', 1),
        ('Bushcraft', 1),
        ('Climb', 1),
        ('Languages', 1),
        ('Open Doors', 1),
        ('Search', 1),
        ('Sleight of Hand', 1),
        ('Sneak Attack', 0),
        ('Stealth', 1),
        ('Tinker', 1),
    ],
    'specialist_builds': [
        ['Stealth', 'Stealth', 'Sneak Attack', 'Sneak Attack'],
        ['Search', 'Search', 'Tinker', 'Tinker'],
        ['Climb', 'Climb', 'Open Doors', 'Search'],
        ['Stealth', 'Climb', 'Search', 'Sneak Attack'],
        ['Sneak Attack', 'Sneak Attack', 'Sneak Attack', 'Stealth'],
        ['Search', 'Search', 'Search', 'Search'],
        ['Tinker', 'Tinker', 'Tinker', 'Tinker'],
        ['Architecture', 'Languages', 'Open Doors', 'Tinker'],
    ],
    'spells': [
        # Read Magic and ...
        'Bookspeak', 'Charm Person', 'Comprehend Languages', 'Detect Magic',
        'Enlarge', 'Faerie Fire', 'Feather Fall', 'Floating Disc',
        'Hold Portal', 'Identify', 'Light', 'Magic Aura', 'Magic Missile',
        'Mending', 'Message', 'Shield', 'Sleep', 'Spider Climb',
        'Unseen Servant'
    ],
    'hitdice': {
        'Cleric': 6,
        'Fighter': 8,
        'Magic-User': 6,
        'Thief': 6,
        'Dwarf': 10,
        'Elf': 6,
        'Halfling': 6
    },
    'lotfp_saves': {
        'Cleric': {'poison': 11, 'wands': 12, 'stone': 14, 'breath': 16, 'magic': 15,},
        'Fighter': {'poison': 12, 'wands': 13, 'stone': 14, 'breath': 15, 'magic': 16},
        'Magic-User': {'poison': 13, 'wands': 13, 'stone': 13, 'breath': 16, 'magic': 14},
        'Thief': {'poison': 16, 'wands': 14, 'stone': 14, 'breath': 15, 'magic': 14},
        'Dwarf': {'poison': 8, 'wands': 9, 'stone': 10, 'breath': 13, 'magic': 12},
        'Elf': {'poison': 12, 'wands': 13, 'stone': 13, 'breath': 15, 'magic': 15},
        'Halfling': {'poison': 8, 'wands': 9, 'stone': 10, 'breath': 13, 'magic': 12}
    },
    'min_hp': {
        'Cleric': 4,
        'Fighter': 8,
        'Magic-User': 3,
        'Thief': 4,
        'Dwarf': 6,
        'Elf': 4,
        'Halfling': 4
    },
    'saves': {
        'poison': 'Poison',
        'wands': 'Magical Devices',
        'stone': 'Paralyzation',
        'breath': 'Breath Weapon',
        'magic': 'Magic'
    },
    'non_enc_equipment': [
            "Locket",
            "Blank Scroll",
            "Small Rock",
            "Rag Doll",
            "Chalk",
            "Candle",
            "Garlic",
            "Quill and Ink Pot",
            "Silver Mirror",
            "Small Bag of Nails",
            "10 Sheets of Paper",
            "Soap",
            "Spyglass, cheap",
            "Clay Pipe and Tobacco",
            "Whistle",
            "3 Empty Vials",
            "3 Rags",
            "Map",
            "Trinket",
            "Promisory Note for 50 sp",
    ],
    'equipment': {
        'Thief': [
            ["Dagger", "Specialist Tools", "Garrote", "Waterskin", "Rucksack", "5x Rations", "Pot of Lard", "10 sp"],
            ["Short Sword", "Specialist Tools", "Waterskin", "Small Backpack", "50' Rope", "5x Rations", "Crowbar", "8 Cp"],
            ["Sword", "Specialist Tools", "Garotte", "Spear", "Waterskin", "Small Backpack", "50' Rope", "5x Rations", "Steel Mirror", "Pot of Lard", "11 Cp"],
            ["Dagger", "Leather Armor", "Specialist Tools", "3 Torches", "Waterskin", "Small Backpack", "Tinderbox", "50' Rope", "5x Rations", "Crowbar", "11 Cp"],
            ["Short Sword", "Leather Armor", "Specialist Tools", "Garotte", "3 Torches", "Waterskin", "Small Backpack", "Tinderbox", "50' Rope", "5x Rations", "1 sp, 11 Cp"],
            ["Sword", "Leather Armor", "Specialist Tools", "Garotte", "3 Torches", "Waterskin", "Small Backpack", "Tinderbox", "50' Rope", "Listening Horn", "5x Rations", "Crowbar", "11 Cp"],
            ["Sword", "Dagger", "Leather Armor", "Specialist Tools", "Dagger", "Garotte", "Hooded Lantern", "Waterskin", "Small Backpack", "Tinderbox", "50' Rope", "5x Rations", "Steel Mirror", "11 Cp"],
            ["Shortbow", "Short Sword", "Leather Armor", "Specialist Tools", "Garotte", "3 Torches", "Waterskin", "Small Backpack", "Small Drill", "Tinderbox", "50' Rope", "Quiver - 4 Arrows", "5x Rations", "1 Cp"],
            ["Light Crossbow", "Dagger", "Leather Armor", "Specialist Tools", "Hooded Lantern", "Waterskin", "Large Backpack", "Tinderbox", "50' Rope", "Quiver - 16 Bolts", "5x Rations", "1 Cp"],
            ["Shortbow", "Quiver With 20 Arrows", "Short Sword", "Leather Armor", "Specialist Tools", "Garotte", "Lamp", "Waterskin", "Small Backpack", "Tinderbox", "Grappling Hook", "50' Rope", "5x Rations", "Crowbar", "Steel Mirror", "11 Cp"],
            ["Shortbow", "Quiver With 20 Arrows", "Dagger", "Leather Armor", "Specialist Tools", "Waterskin", "Garotte", "Lamp", "Waterskin", "Large Backpack", "Tinderbox", "50' Rope", "5x Rations", "Crowbar", "1 Cp"],
            ["Light Crossbow", "Quiver With 12 Bolts", "Dagger", "Leather Armor", "Lamp", "Specialist Tools", "Garotte", "Waterskin", "Small Backpack", "Tinderbox", "Grappling Hook", "50' Rope", "3 Flasks of Oil", "Scroll Case", "2 day's Rations", "4 Cp"],
            ["Staff", "Dagger", "Leather Armor", "Specialist Tools", "Bullseye Lantern", "Crowbar", "Waterskin", "Small Backpack", "Tinderbox", "3 Flasks of Oil", "Crowbar", "Scroll Case", "2 day's Rations", "4 Cp"],
            ["Shortbow", "Quiver With 20 Arrows", "Club", "Leather Armor", "Specialist Tools", "Waterskin", "Large Backpack", "Tinderbox", "Grappling Hook", "50' Rope", "Bullseye Lantern", "3 Flasks of Oil", "Wood Drill", "Scroll Case", "Holy Water", "2 day's Rations", "4 Cp"],
            ["Spear", "Leather Armor", "Specialist Tools", "Waterskin", "Hooded Lantern", "Waterskin", "Large Backpack", "Tinderbox", "50' Rope", "3 Flasks of Oil", "Pot of Lard", "Scroll Case", "Holy Water", "2 day's Rations", "4 Cp"],
            ["Whip", "Dagger", "Leather Armor", "Specialist Tools", "Garotte", "3 Torches", "Scroll Case", "Waterskin", "Small Backpack", "Tinderbox", "Grappling Hook", "50' Rope", "Pot of Lard", "3x Holy Water", "2 day's Rations", "4 Cp"],
        ],
        'Cleric': [
            ["Spear", "Shield", "Large Knife", "Waterskin", "Rucksack", "5 x Rations", "3 Cp"],
            ["Spear", "Shield", "Mace", "Waterskin", "Small Backpack", "Incense Burner", "Tinderbox", "50' Rope", "3x Rations", "5x Iron Spike", "4 Cp"],
            ["Spear", "Shield", "Dagger", "Leather Armor", "5 x Rations", "50' Rope", "Waterskin", "Small Backpack", "5x Iron Spike", "3 Cp"],
            ["Mace", "Shield", "Leather Armor", "5 x Rations", "3 Torches", "Tinderbox", "50' Rope", "Waterskin", "Small Backpack", "5x Iron Spike", "6 Cp"],
            ["Mace", "Shield", "Spear", "Dagger", "Leather Armor", "5 x Rations", "3 Torches", "Tinderbox", "50' Rope", "Waterskin", "Small Backpack", "5x Iron Spike", "3 Cp"],
            ["Light Crossbow", "Quiver With 20 Bolts", "Leather Armor", "5 x Rations", "Waterskin", "Small Backpack", "3 Torches", "Tinderbox", "50' Rope", "5x Iron Spike", "4 Cp"],
            ["Spear", "Dagger", "Shield", "Leather Armor", "5 x Rations", "Waterskin", "Small Backpack", "Lamp", "Tinderbox", "50' Rope", "5x Iron Spike", "Short bow", "Quiver With 20 Arrows", "6 Cp"],
            ["Warhammer", "Shield", "Mace", "Leather Armor", "5 x Rations", "Lamp", "Tinderbox", "50' Rope", "Waterskin", "Small Backpack", "5x Iron Spike", "Light Crossbow", "Quiver With 10 Bolts", "5 Cp"],
            ["Mace", "Dagger", "Shield", "Mace", "Leather Armor", "5 x Rations", "3 Torches", "Tinderbox", "50' Rope", "Waterskin", "Small Backpack", "5x Iron Spike", "Short bow", "Quiver With 20 Arrows", "3 Cp"],
            ["Club", "Shield", "Chain Armor", "5 x Rations", "Lamp", "Tinderbox", "50' Rope", "Waterskin", "Small Backpack", "5x Iron Spike", "2 Cp"],
            ["Mace", "Shield", "Dagger", "Chain Armor", "5 x Rations", "3 Torches", "Tinderbox", "50' Rope", "Waterskin", "Large Backpack", "5x Iron Spike", "8 Cp"],
            ["Warhammer", "Shield", "Chain Armor", "Mace", "5 x Rations", "Hooded Lantern", "Tinderbox", "50' Rope", "Waterskin", "Large Backpack", "5x Iron Spike", "4 Cp"],
            ["Spear", "Shield", "Chain Armor", "Mace", "Short Sword", "5 x Rations", "Bullseye Lantern", "Tinderbox", "50' Rope", "Waterskin", "Large Backpack", "5x Iron Spike", "3 Cp"],
            ["Light Crossbow", "Quiver With 20 Bolts", "Chain Armor", "5 x Rations", "Hooded Lantern", "Tinderbox", "50' Rope", "Waterskin", "Small Backpack", "5x Iron Spike", "5 Cp"],
            ["Spear", "Shield", "Short Sword", "Chain Armor", "5 x Rations", "Lamp", "Tinderbox", "50' Rope", "3 Flasks of Oil", "Waterskin", "Large Backpack", "5x Iron Spike", "7 Cp"],
            ["Spear", "Mace", "Shield", "Chain Armor", "5 x Rations", "Waterskin", "3 Torches", "Tinderbox", "Large Backpack", "5x Iron Spike", "Shortbow", "Crowbar", "9 Cp"],
        ],
        'Fighter': [
            ["Sword", "Shield", "Rapier", "5 x Rations", "Waterskin", "Sack", "4 Cp"],
            ["Sword", "Shield", "5 x Rations", "Waterskin", "Rucksack", "Crowbar", "1 Cp"],
            ["Spear", "Shield", "Dagger", "Leather Armor", "5 x Rations", "Waterskin", "Small Backpack", "3 Torches", "Tinderbox", "50' Rope", "5x Iron Spike", "1 Cp"],
            ["Sword", "Shield", "Leather Armor", "5 x Rations", "Waterskin", "3 Torches", "Tinderbox", "50' Rope", "Small Backpack", "5x Iron Spike", "1 Cp"],
            ["Warhammer", "Shield", "Spear", "Dagger", "Leather Armor", "5 x Rations", "3 Torches", "Tinderbox", "50' Rope", "Waterskin", "Small Backpack", "5x Iron Spike", "1 Cp"],
            ["Spear", "Shield", "Leather Armor", "5 x Rations", "Lamp", "Tinderbox", "50' Rope", "Waterskin", "Small Backpack", "5x Iron Spike", "Short bow", "Quiver With 10 Arrows", "1 Cp"],
            ["Battleaxe", "Dagger", "Shield", "Leather Armor", "5 x Rations", "Lamp", "Tinderbox", "50' Rope", "Waterskin", "Large Backpack", "5x Iron Spike", "Short bow", "Quiver With 20 Arrows", "1 Cp"],
            ["Battleaxe", "Shield", "Sword", "Leather Armor", "5 x Rations", "Lamp", "Tinderbox", "50' Rope", "Waterskin", "Small Backpack", "5x Iron Spike", "Long bow", "Quiver With 10 Arrows", "1 Cp"],
            ["Spear", "Shield", "Sword", "Leather Armor", "5 x Rations", "3 Torches", "Tinderbox", "50' Rope", "Waterskin", "Large Backpack", "5x Iron Spike", "Long bow", "Quiver With 20 Arrows", "1 Cp"],
            ["Warhammer", "Shield", "Chain Armor", "5 x Rations", "3 Torches", "Tinderbox", "50' Rope", "Waterskin", "Small Backpack", "Mallet", "5x Iron Spike", "1 Cp"],
            ["Sword", "Shield", "Dagger", "Chain Armor", "5 x Rations", "Hooded Lantern", "Tinderbox", "50' Rope", "Waterskin", "Large Backpack", "Mallet", "5x Iron Spike", "1 Cp"],
            ["Greatsword", "Chain Armor", "Standard Sword", "5 x Rations", "Hooded Lantern", "Tinderbox", "50' Rope", "Waterskin", "Small Backpack", "5x Iron Spike", "1 Cp"],
            ["Greatsword", "Chain Armor", "Standard Sword", "Short Sword", "5 x Rations", "Bullseye Lantern", "Tinderbox", "Grappling Hook", "50' Rope", "Waterskin", "Large Backpack", "Crowbar", "5x Iron Spike", "1 Cp"],
            ["Mace", "Shield", "Chain Armor", "5 x Rations", "Lamp", "Tinderbox", "50' Rope", "Waterskin", "Large Backpack", "Grappling Hook", "Mallet", "5x Iron Spike", "1 Cp"],
            ["Polearm", "Short Sword", "Chain Armor", "5 x Rations", "3 Torches", "Tinderbox", "50' Rope", "Crowbar", "Waterskin", "Large Backpack", "Whetstone", "Mallet", "5x Iron Spike", "1 Cp"],
            ["Sword", "Shield", "Chain Armor", "5 x Rations", "Crowbar", "Waterskin", "Small Backpack", "5x Iron Spike", "Shortbow", "Whetstone", "1 Cp"],
        ],
        'Magic-User': [
            ["Knife", "Garotte", "Spellbook", "Waterskin", "Sack", "5x Rations", "11 Cp"],
            ["Dagger", "Spellbook", "3 Torches", "Waterskin", "Sack", "50' Rope", "5x Rations", "11 Cp"],
            ["Knife", "Spellbook", "3 Torches", "Waterskin", "Rucksack", "Tinderbox", "5x Rations", "1 sp 11 Cp"],
            ["Staff", "Spellbook", "3 Torches", "Waterskin", "Rucksack", "Tinderbox", "50' Rope", "5x Rations", "Steel Mirror", "11 Cp"],
            ["Dagger", "Spellbook", "Lamp", "Waterskin", "Rucksack", "Tinderbox", "50' Rope", "5x Rations", "Steel Mirror", "11 Cp"],
            ["Staff", "Grimoire", "Lamp", "Waterskin", "Small Backpack", "Tinderbox", "5x Rations", "15 Cp"],
            ["Athame", "Spellbook", "Hooded Lantern", "Waterskin", "Small Backpack", "Tinderbox", "50' Rope", "5x Rations", "1 Cp"],
            ["Athame", "Spellbook", "3 Torches", "Waterskin", "Small Backpack", "Tinderbox", "50' Rope", "5x Rations", "Steel Mirror", "11 Cp"],
            ["Light Crossbow", "Quiver With 20 Bolts", "Spellbook", "Lamp", "Waterskin", "Dagger", "Rucksack", "Tinderbox", "50' Rope", "5x Rations", "Steel Mirror", "1 Cp"],
            ["Dagger", "Spellbook", "Waterskin", "Small Backpack", "Tinderbox", "50' Rope", "Lamp", "3 Flasks of Oil", "Steel Mirror", "Scroll Case", "5x Rations", "4 Cp"],
            ["Staff", "Spellbook", "Waterskin", "Small Backpack", "Tinderbox", "50' Rope", "Lamp", "3 Flasks of Oil", "Steel Mirror", "Scroll Case", "5x Rations", "4 Cp"],
            ["Staff", "Spellbook", "Waterskin", "Small Backpack", "Tinderbox", "50' Rope", "Bullseye Lantern", "3 Flasks of Oil", "Steel Mirror", "Scroll Case", "5x Iron Rations", "4 Cp"],
            ["Light Crossbow", "Quiver With 20 Bolts", "Spellbook", "Large Knife", "Waterskin", "Small Backpack", "Tinderbox", "50' Rope", "Lamp", "3 Flasks of Oil", "Steel Mirror", "Scroll Case", "5x Iron Rations", "4 Cp"],
            ["Light Crossbow", "Quiver With 20 Bolts", "Spellbook", "Waterskin", "Dagger", "Small Backpack", "Tinderbox", "50' Rope", "Lamp", "3 Flasks of Oil", "Steel Mirror", "Scroll Case",  "5x Rations", "4 Cp"],
            ["Short Sword", "Spellbook", "Waterskin", "Small Backpack", "Tinderbox", "50' Rope", "Lamp", "3 Flasks of Oil", "Steel Mirror", "Scroll Case", "Holy Water", "5x Rations", "10 sp", "4 Cp"],
            ["Curved Dagger", "Spellbook", "Waterskin", "Small Backpack", "Tinderbox", "50' Rope", "Lamp", "3 Flasks of Oil", "Steel Mirror", "Scroll Case", "Holy Water", "5x Rations", "20 sp", "4 Cp"],
        ],
    }
}

LOTFP['equipment']['Elf'] = LOTFP['equipment']['Magic-User']
LOTFP['equipment']['Dwarf'] = LOTFP['equipment']['Fighter']
LOTFP['equipment']['Halfling'] = LOTFP['equipment']['Fighter']

APPEARENCE = [
    ['Male', 'Female'],
    ['Child', 'Youth', 'Adult', 'Mature', 'Old', 'Decrepit'],
    ['Messy Clothing', 'Scant Clothing', 'Immaculate Clothing',
     'Formal Attire', 'Threadbare Clothing', 'Elaborate Attire', 'Drab Clothing',
     'in Uniform'],
    ['Missing Limb', 'Obese', 'Scrawny', 'Muscular', 'Bald', 'Hairy', 'Tall',
     'Short', 'Ugly']
]


PERSONALITY = [
    'Accusative', 'Active', 'Adventurous', 'Affable', 'Aggressive',
    'Agreeable', 'Aimless', 'Aloof', 'Altruistic', 'Analytical', 'Angry',
    'Animated', 'Annoying', 'Anxious', 'Apathetic', 'Apologetic',
    'Apprehensive', 'Argumentative', 'Arrogant', 'Articulate', 'Attentive',
    'Bigoted', 'Bitter', 'Blustering', 'Boastful', 'Bookish', 'Bossy',
    'Braggart', 'Brash', 'Brave', 'Bullying', 'Callous', 'Calm', 'Candid',
    'Cantankerous', 'Capricious', 'Careful', 'Careless', 'Caring', 'Casual',
    'Catty', 'Cautious', 'Cavalier', 'Charming', 'Chaste', 'Chauvinistic',
    'Cheeky', 'Cheerful', 'Childish', 'Chivalrous', 'Clueless', 'Clumsy',
    'Cocky', 'Comforting', 'Communicative', 'Complacent', 'Condescending',
    'Confident', 'Conformist', 'Confused', 'Conscientious', 'Conservative',
    'Contentious', 'Contrary', 'Contumely', 'Conventional', 'Cooperative',
    'Courageous', 'Courteous', 'Cowardly', 'Coy', 'Crabby', 'Cranky',
    'Critical', 'Cruel', 'Cultured', 'Curious', 'Cynical', 'Daring',
    'Deceitful', 'Deceptive', 'Defensive', 'Defiant', 'Deliberate', 'Deluded',
    'Depraved', 'Discreet', 'Discreet', 'Dishonest', 'Disingenuous',
    'Disloyal', 'Disrespectful', 'Distant', 'Distracted', 'Distraught',
    'Docile', 'Doleful', 'Dominating', 'Dramatic', 'Drunkard', 'Dull',
    'Earthy', 'Eccentric', 'Elitist', 'Emotional', 'Energetic', 'Enigmatic',
    'Enthusiastic', 'Epicurean', 'Excited', 'Expressive', 'Extroverted',
    'Faithful', 'Fanatical', 'Fastidious', 'Fatalistic', 'Fearful', 'Fearless',
    'Feral', 'Fierce', 'Feisty', 'Flamboyant', 'Flippant', 'Flirtatious',
    'Foolhardy', 'Foppish', 'Forgiving', 'Friendly', 'Frightened', 'Frivolous',
    'Frustrated', 'Funny', 'Furtive', 'Generous', 'Genial', 'Gentle', 'Gloomy',
    'Goofy', 'Gossip', 'Graceful', 'Gracious', 'Grave', 'Gregarious',
    'Grouchy', 'Groveling', 'Gruff', 'Gullible', 'Happy', 'Harsh', 'Hateful',
    'Helpful', 'Honest', 'Hopeful', 'Hostile', 'Humble', 'Humorless',
    'Humorous', 'Idealistic', 'Idiosyncratic', 'Imaginative', 'Imitative',
    'Impatient', 'Impetuous', 'Implacable', 'Impractical', 'Impulsive',
    'Inattentive', 'Incoherent', 'Indifferent', 'Indiscreet', 'Individualist',
    'Indolent', 'Indomitable', 'Industrious', 'Inexorable', 'Inexpressive',
    'Insecure', 'Insensitive', 'Instructive', 'Intolerant', 'Intransigent',
    'Introverted', 'Irreligious', 'Irresponsible', 'Irreverent', 'Irritable',
    'Jealous', 'Jocular', 'Joking', 'Jolly', 'Joyous', 'Judgmental', 'Jumpy',
    'Kind', 'Know-it-all', 'Languid', 'Lazy', 'Lethargic', 'Lewd', 'Liar',
    'Likable', 'Lippy', 'Listless', 'Loquacious', 'Loving', 'Loyal', 'Lust',
    'Madcap', 'Magnanimous', 'Malicious', 'Maudlin', 'Mean', 'Meddlesome',
    'Melancholy', 'Melodramatic', 'Merciless', 'Merry', 'Meticulous',
    'Mischievous', 'Miscreant', 'Miserly', 'Modest', 'Moody', 'Moralistic',
    'Morbid', 'Morose', 'Mournful', 'Mousy', 'Mouthy', 'Mysterious', 'Naive',
    'Narrow-minded', 'Needy', 'Nefarious', 'Nervous', 'Nettlesome', 'Neurotic',
    'Noble', 'Nonchalant', 'Nurturing', 'Obdurate', 'Obedient', 'Oblivious',
    'Obnoxious', 'Obsequious', 'Obsessive', 'Obstinate', 'Obtuse', 'Odd',
    'Ornery', 'Optimistic', 'Organized', 'Ostentatious', 'Outgoing',
    'Overbearing', 'Paranoid', 'Passionate', 'Pathological', 'Patient',
    'Peaceful', 'Pensive', 'Pertinacious', 'Pessimistic', 'Philanderer',
    'Philosophical', 'Phony', 'Pious', 'Playful', 'Pleasant', 'Poised',
    'Polite', 'Pompous', 'Pondering', 'Pontificating', 'Practical',
    'Prejudiced', 'Pretentious', 'Preoccupied', 'Promiscuous', 'Proper',
    'Proselytizing', 'Proud', 'Prudent', 'Prudish', 'Prying', 'Puerile',
    'Pugnacious', 'Quiet', 'Quirky', 'Racist', 'Randy', 'Rascal', 'Rash', 'Realistic',
    'Rebellious', 'Reckless', 'Refined', 'Repellent', 'Reserved', 'Respectful',
    'Responsible', 'Restless', 'Reticent', 'Reverent', 'Rigid', 'Risk-taking',
    'Rude', 'Sadistic', 'Sarcastic', 'Sardonic', 'Sassy', 'Savage', 'Scared',
    'Scolding', 'Secretive', 'Self-effacing', 'Selfish', 'Selfless', 'Senile',
    'Sensible', 'Sensitive', 'Sensual', 'Sentimental', 'Serene', 'Serious',
    'Servile', 'Sexist', 'Sexual', 'Shallow', 'Shameful', 'Shameless',
    'Shifty', 'Shrewd', 'Shy', 'Sincere', 'Slanderous', 'Sly', 'Smug',
    'Snobbish', 'Sober', 'Sociable', 'Solemn', 'Solicitous', 'Solitary',
    'Solitary', 'Sophisticated', 'Spendthrift', 'Spiteful', 'Stern', 'Stingy',
    'Stoic', 'Stubborn', 'Submissive', 'Sultry', 'Superstitious', 'Surly',
    'Suspicious', 'Sybarite', 'Sycophantic', 'Sympathetic', 'Taciturn',
    'Tactful', 'Tawdry', 'Teetotaler', 'Temperamental', 'Tempestuous',
    'Thorough', 'Thrifty', 'Timid', 'Tolerant', 'Transparent', 'Treacherous',
    'Troublemaker', 'Trusting', 'Truthful', 'Uncommitted', 'Understanding',
    'Unfriendly', 'Unhinged', 'Uninhibited', 'Unpredictable', 'Unruly',
    'Unsupportive', 'Vague', 'Vain', 'Vapid', 'Vengeful', 'Vigilant',
    'Violent', 'Vivacious', 'Vulgar', 'Wanton', 'Wasteful', 'Weary',
    'Whimsical', 'Whiny', 'Wicked', 'Wisecracking', 'Wistful', 'Witty',
    'Zealous'
]


class GONZO:
    """
    Information we use when making Carcosa characters.
    """

    METERIAL = ["Obsidian", "Insect Carapace", "Insect Mandible",
                "Wood", "Space Alien Ceramic", "Giant Tooth",
                "Bone", "Bronze", "Iron"]
    WEAPONS = ['Battle-Axe', 'Trident', 'Sword', 'War-Hammer', 'Spear',
               'Scythe', 'Staff']
    ARMOUR = ['Boiled Dinosaur Leather Armour', 'Mail of Ceramic Discs',
              'Copper Scale Armour', 'Bone Scale Mail', 'Horn Scale Mail',
              'Tooth Scale Mail', 'Carved Wooden Armour', 'Dinosaur Scale Armour',
              'Giant Insect Chitin Plates', 'Bright Orange Breast Plate',
              'Bright Purple Breast Plate', 'Bamboo Mail', 'Rattan Armour',
              'Giant Centipede Carapace', 'Beetle Horn Mail']
    GEAR = ["Water Skin", "50' of Rope", "5 Torches", "2 Daggers",
            "2 Wooden Stakes", "Backpack", "Whip", "Fur Top", "Horned Helmet",
            "Grappling Hook"]
    STRANGE = [
        "Incomprehensible Book of Snake-Men Rituals",
        "Broken Space Alien Laser Pistol",
        "Dehydrated Tentacles",
        "Painted Bones",
        "Fermented Bug Juice",
        "5 Dead Snakes",
        "Space Alien Key Card",
        "Powder that turns 10 cubic feet of liquid to gel",
        "A power cell to ... something",
        "A map printed on skin",
        "A glowing Jale necklace",
        "A small potted plant that talks to your dreams",
        "A compass that points to the nearest alien",
        "A box that makes an occasional ticking sound that speeds up around certain craters",
        "A three-gallon jug that's neutrally buoyant in air",
        "Goggles that make dolm, jale and ulfire look gray",
        "A three inches tall dinosaur",
        "A book of lead sheets embossed with pictures of all the spiders in the world and then some",
        "A tiny bit of quivering red pudding in a vial",
        "A 30' rope made from the dried intestines of you tribe's enemies",
        "A zinc canteen in the shape of a turtle",
        "A package of pink salt crystals",
        "A large dried squid",
        "A cask of red liqour",
        "A large meat and lentil pastry",
        "Black smoked goggles",
        "10' of rusted iron chain, with manacles (50% you have the key)",
        "A clay flask of crushed beetle paste sunscreen",
        "1D8 shrunken heads",
    ]

WILD_TALENTS = [
    "Know Direction - The character knows which way is North.",
    "Far Hearing - For one turn the character hears all sounds within 50' as if they were being whispered directly into their ear. The character may choose what sounds to focus on.",
    "Far Seeing - For one turn the character may view a scene up to 50' away as if they were right there. They may see through walls and other obstacles, but not through lead.",
    "Thought Projection - The character may communicate a brief message mentally with a creature up to 50' away. The target understands the character, even if they share no common language.",
    "Object Projection - The character may teleport a small object in their possession up to 50' away.",
    "Telekinetic Grasp - For one turn the character may manipulate small objects from up to 50' away.",
    "Spark - The character may ignite any flammable object within 50' of them. (The 'heat' this power generates is no greater than that of a candle.)",
    "Levitate - For 1 turn, the character can float above the ground (up to 10').",
    "Minor ESP: For 1 turn the character may read the mind of another creature. (The character understand the creature even if they share no common language.)",
    "Cell Adjustment - The character regains up to 1d3 lost hit points. (This increases to 1d6 at level 3, 1d8 at level 6, 1d10 at level 9 and 1d12 at level 12.) The character may make a Save vs. Poison to cure themselves of any non-magical disease.",
    "'Invisiblity': For 1 turn the character can completely hide his presence from up to one sentient creature per level. The target may make a Save vs. Magic to resist the character's power.",
    "Id Insituation: All sentient characters, friend or foe, within 25' of the character feel an uncontrollable urge to eat, murder or fornicate.",
    "Psychic Distress: All sentient characters, friend or foe, within 25' of the character are immobilized for 1 turn.",
    "Minor Mind Control: For 1 turn, the character may manipulate the target into doing whatever the character wants. The target will have no memory of any events that transpire while under this mind control. The target my make a Save vs. Magic to resist the mind control.",
    "Minor Precognition: The character may re-roll any saving throw.",
    "Psionic Defence - Once per day per level, the character may make a Save vs. Magic to avoid the effects of any psionic power that targets them. (This is in addition to any saving throws the power may allow for.)",
    "Psionic Immunity: The character can not be the target of any psionic power.",
    "The Haitian: no character within 10' of the character, friend or foe, may use their psionic powers. The character also gains Psionic Immunity.",
]

# Map from a given attribute to most appropriate character class
PRIME_REQUISITE = {
    'STR': FIGHTER,
    'INT': MAGICUSER,
    'WIS': CLERIC,
    'DEX': THIEF
}

CLASSES = [FIGHTER, MAGICUSER, CLERIC, THIEF, DWARF, ELF, HALFLING]
VALID_CLASS_NAMES = [c['name'].lower().replace('-', '') for c in CLASSES]
CLASS_BY_NAME = dict(zip(VALID_CLASS_NAMES, CLASSES))
