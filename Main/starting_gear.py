# starting_gear.py

starting_gear_data = {
    "Warrior": {
        "Human": {
            "inventory": ["Iron Sword", "Starter Armor", "Health Potion", "Health Potion"],
            "equipped": {"weapon": "Iron Sword", "body": "Starter Armor"},
            "intro": "As a human warrior, you grasp your sturdy iron sword, and don your starter armor. A new day of adventure dawns as you step out from your home."
        },
        "Elf": {
            "inventory": ["Iron Sword", "Starter Armor", "Health Potion"],
            "equipped": {"weapon": "Iron Sword", "body": "Starter Armor"},
            "intro": "Your elven hands instinctively reach for your sword, its familiar hilt a comfort. Though a warrior, the forest still calls to your ancient blood as you leave your dwelling."
        },
        "Dwarf": {
            "inventory": ["Battle Axe", "Starter Armor", "Health Potion", "Health Potion"],
            "equipped": {"weapon": "Battle Axe", "body": "Starter Armor"},
            "intro": "The heavy chainmail clinks softly as you, a stout dwarf warrior, heft your battle axe. The mountain calls, but first, the town awaits."
        },
        "Dragonborn": {
            "inventory": ["Battle Axe", "Starter Armor", "Health Potion"],
            "equipped": {"weapon": "Battle Axe", "body": "Starter Armor"},
            "intro": "Your scales shimmer in the morning light as you, a dragonborn warrior, feel the solid grip of your axe. The roar of adventure echoes in your draconic heart."
        },
        "Tiefling": {
            "inventory": ["Iron Sword", "Starter Armor", "Health Potion"],
            "equipped": {"weapon": "Iron Sword", "body": "Starter Armor"},
            "intro": "With a flick of your tail, you, a tiefling warrior, test the balance of your iron sword. The world may fear your heritage, but your strength will speak for itself."
        },
        "Halfling": {
            "inventory": ["Dagger", "Starter Armor", "Health Potion", "Health Potion"],
            "equipped": {"weapon": "Dagger", "body": "Starter Armor"},
            "intro": "Small but mighty, you, a halfling warrior, strap on your Starter Armor and dagger. Even the smallest hero can make the biggest difference."
        }
    },
    "Wizard": {
        "Human": {
            "inventory": ["Magic Staff", "Starter Robe", "Mana Potion"],
            "equipped": {"weapon": "Magic Staff", "body": "Starter Robe"},
            "intro": "As a human wizard, your fingers tingle with latent magic as you grip your staff. The ancient texts have been studied, and now, the world awaits your arcane prowess."
        },
        "Elf": {
            "inventory": ["Magic Staff", "Starter Robe", "Mana Potion", "Mana Potion"],
            "equipped": {"weapon": "Magic Staff", "body": "Starter Robe"},
            "intro": "Your elven eyes, keen with centuries of knowledge, focus as you, a wizard, prepare your magic staff. The weave of magic is strong, and your journey into its mysteries continues."
        },
        "Dwarf": {
            "inventory": ["Magic Staff", "Starter Armor", "Mana Potion"],
            "equipped": {"weapon": "Magic Staff", "body": "Starter Armor"},
            "intro": "An unusual sight, a dwarf wizard, you adjust your Starter Armor and tap your staff on the stone floor. Your mastery of the arcane will prove dwarven wisdom goes beyond the forge."
        },
        "Dragonborn": {
            "inventory": ["Magic Staff", "Starter Robe", "Mana Potion"],
            "equipped": {"weapon": "Magic Staff", "body": "Starter Robe"},
            "intro": "The air crackles around you, a dragonborn wizard, as you brandish your magic staff. Your draconic heritage blends with powerful spells, ready to reshape the world."
        },
        "Tiefling": {
            "inventory": ["Magic Staff", "Starter Robe", "Mana Potion"],
            "equipped": {"weapon": "Magic Staff", "body": "Starter Robe"},
            "intro": "With arcane symbols traced on your skin, you, a tiefling wizard, channel nascent power through your staff. Let the world witness the might of your intellect, not just your lineage."
        },
        "Halfling": {
            "inventory": ["Magic Staff", "Leather Vest", "Mana Potion", "Mana Potion"],
            "equipped": {"weapon": "Magic Staff", "body": "Leather Vest"},
            "intro": "A halfling wizard, you clutch your staff, a formidable conduit of power in your small hands. Never underestimate the magic that brews behind a cheerful demeanor."
        }
    },
    "Rogue": {
        "Human": {
            "inventory": ["Dagger", "Leather Vest", "Health Potion"],
            "equipped": {"weapon": "Dagger", "body": "Leather Vest"},
            "intro": "As a human rogue, your movements are silent, your dagger glints in the shadows. The city's underbelly holds many secrets, and you are just the one to uncover them."
        },
        "Elf": {
            "inventory": ["Longbow", "Leather Vest", "Health Potion", "Antidote"],
            "equipped": {"weapon": "Longbow", "body": "Leather Vest"},
            "intro": "Your elven senses are sharp, your longbow strung and ready. As a rogue, you blend seamlessly with the forest, a silent hunter of secrets and shadows."
        },
        "Dwarf": {
            "inventory": ["Dagger", "Leather Vest", "Health Potion"],
            "equipped": {"weapon": "Dagger", "body": "Leather Vest"},
            "intro": "Sneaky for a dwarf, you, a rogue, check the edge of your dagger. There's more than one way to find treasure in the dark, and you know them all."
        },
        "Dragonborn": {
            "inventory": ["Dagger", "Leather Vest", "Health Potion"],
            "equipped": {"weapon": "Dagger", "body": "Leather Vest"},
            "intro": "Though a dragonborn, you move with unexpected grace. Your rogue's dagger is a silent promise of swift justice in the shadows."
        },
        "Tiefling": {
            "inventory": ["Dagger", "Leather Vest", "Antidote"],
            "equipped": {"weapon": "Dagger", "body": "Leather Vest"},
            "intro": "Your tiefling charm is as sharp as your rogue's dagger. With a mischievous glint in your eye, you're ready to outsmart and outmaneuver any challenge."
        },
        "Halfling": {
            "inventory": ["Dagger", "Leather Vest", "Health Potion"],
            "equipped": {"weapon": "Dagger", "body": "Leather Vest"},
            "intro": "A halfling rogue, you slip through cracks unseen. Your small stature is your greatest asset, perfect for reaching places others can't."
        }
    },
    "Barbarian": {
        "Human": {
            "inventory": ["Greatsword", "Health Potion", "Health Potion"],
            "equipped": {"weapon": "Greatsword", "body": "No Armor"},
            "intro": "Raw power surges through you, a human barbarian. Your greatsword feels like an extension of your rage, ready to meet any foe with a primal roar."
        },
        "Elf": {
            "inventory": ["Greataxe", "Health Potion"],
            "equipped": {"weapon": "Greataxe", "body": "No Armor"},
            "intro": "Wild, untamed, an elven barbarian. You grip your greataxe, finding strength in the ancient ways of the forest, far from elven courtly manners."
        },
        "Dwarf": {
            "inventory": ["Warhammer", "Health Potion", "Health Potion"],
            "equipped": {"weapon": "Warhammer", "body": "No Armor"},
            "intro": "A dwarven barbarian, you bellow as you swing your warhammer. Your fury is as unyielding as the mountains, and your enemies will feel its might."
        },
        "Dragonborn": {
            "inventory": ["Greataxe", "Health Potion"],
            "equipped": {"weapon": "Greataxe", "body": "No Armor"},
            "intro": "Your draconic blood boils with primal fury. As a dragonborn barbarian, your greataxe is but a tool for the immense power you unleash."
        },
        "Tiefling": {
            "inventory": ["Greatsword", "Health Potion"],
            "equipped": {"weapon": "Greatsword", "body": "No Armor"},
            "intro": "A tiefling barbarian, you embrace the wild strength within. Your greatsword cleaves through doubt, and your wrath is a force to be reckoned with."
        },
        "Halfling": {
            "inventory": ["Handaxe", "Shield", "Health Potion", "Health Potion"],
            "equipped": {"weapon": "Handaxe", "offhand": "Shield", "body": "No Armor"},
            "intro": "Never underestimate the rage of a halfling barbarian. With handaxe and shield, you stand defiantly, a small but fierce whirlwind of fury."
        }
    },
    "Cleric": {
        "Human": {
            "inventory": ["Mace", "Chainmail", "Mana Potion"],
            "equipped": {"weapon": "Mace", "body": "Chainmail"},
            "intro": "As a human cleric, you feel the divine grace flowing through you. Your mace and chainmail are tools of your faith, ready to bring healing or judgment to the world."
        },
        "Elf": {
            "inventory": ["Mace", "Leather Vest", "Mana Potion"],
            "equipped": {"weapon": "Mace", "body": "Leather Vest"},
            "intro": "An elven cleric, you commune with the ancient spirits of nature. Your mace holds the power of life, and your leather vest is your shield against darkness."
        },
        "Dwarf": {
            "inventory": ["Warhammer", "Chainmail", "Mana Potion", "Mana Potion"],
            "equipped": {"weapon": "Warhammer", "body": "Chainmail"},
            "intro": "The dwarven gods guide your hammer, cleric. Clad in chainmail, you are a beacon of hope and a bulwark against evil, embodying the strength of your people."
        },
        "Dragonborn": {
            "inventory": ["Mace", "Chainmail", "Mana Potion"],
            "equipped": {"weapon": "Mace", "body": "Chainmail"},
            "intro": "Your draconic lineage merges with divine purpose. As a dragonborn cleric, your mace delivers powerful blessings and righteous fury."
        },
        "Tiefling": {
            "inventory": ["Mace", "Leather Vest", "Mana Potion"],
            "equipped": {"weapon": "Mace", "body": "Leather Vest"},
            "intro": "Despite the whispers, you, a tiefling cleric, carry the light of your deity. Your mace strikes down injustice, and your presence inspires hope where it's needed most."
        },
        "Halfling": {
            "inventory": ["Mace", "Leather Vest", "Mana Potion"],
            "equipped": {"weapon": "Mace", "body": "Leather Vest"},
            "intro": "A halfling cleric, you embody gentle kindness and fierce devotion. Your mace is small, but the faith behind it is boundless, ready to protect the innocent."
        }
    },
    "Ranger": {
        "Human": {
            "inventory": ["Longbow", "Leather Vest", "Antidote"],
            "equipped": {"weapon": "Longbow", "body": "Leather Vest"},
            "intro": "As a human ranger, your keen eyes scan the horizon. Your longbow is an extension of your will, and the wilderness is your true home. Adventure awaits just beyond your doorstep."
        },
        "Elf": {
            "inventory": ["Longbow", "Leather Vest", "Antidote", "Health Potion"],
            "equipped": {"weapon": "Longbow", "body": "Leather Vest"},
            "intro": "An elven ranger, you are one with the forest. Your longbow sings in harmony with the wind, and your path is guided by the whispers of ancient trees."
        },
        "Dwarf": {
            "inventory": ["Crossbow", "Leather Vest", "Health Potion"],
            "equipped": {"weapon": "Crossbow", "body": "Leather Vest"},
            "intro": "Though more at home underground, you, a dwarven ranger, wield your crossbow with deadly precision. The surface world holds new hunting grounds."
        },
        "Dragonborn": {
            "inventory": ["Longbow", "Leather Vest", "Antidote"],
            "equipped": {"weapon": "Longbow", "body": "Leather Vest"},
            "intro": "Your draconic senses enhance your hunter's skill. A dragonborn ranger, your longbow delivers precision shots, and your breath weapon adds an unexpected element to your arsenal."
        },
        "Tiefling": {
            "inventory": ["Longbow", "Leather Vest", "Antidote"],
            "equipped": {"weapon": "Longbow", "body": "Leather Vest"},
            "intro": "A tiefling ranger, you navigate the wilds with stealth and cunning. Your longbow brings down foes from afar, a silent testament to your adaptability."
        },
        "Halfling": {
            "inventory": ["Shortbow", "Leather Vest", "Health Potion"],
            "equipped": {"weapon": "Shortbow", "body": "Leather Vest"},
            "intro": "Small but nimble, a halfling ranger, you nock an arrow in your shortbow. The world is full of hidden paths, and you're eager to explore them all."
        }
    },
    "Paladin": {
        "Human": {
            "inventory": ["Longsword", "Plate Armor", "Health Potion"],
            "equipped": {"weapon": "Longsword", "body": "Plate Armor"},
            "intro": "As a human paladin, your longsword gleams with divine light, and your plate armor is a testament to your sacred oath. Justice and righteousness are your guiding stars."
        },
        "Elf": {
            "inventory": ["Longsword", "Chainmail", "Health Potion"],
            "equipped": {"weapon": "Longsword", "body": "Chainmail"},
            "intro": "An elven paladin, you are a graceful defender of the light. Your longsword dances with holy energy, and your chainmail protects a heart devoted to good."
        },
        "Dwarf": {
            "inventory": ["Warhammer", "Plate Armor", "Health Potion", "Health Potion"],
            "equipped": {"weapon": "Warhammer", "body": "Plate Armor"},
            "intro": "A dwarven paladin, you are an unyielding force of good. Your warhammer crushes evil, and your plate armor is as solid as the mountains you protect."
        },
        "Dragonborn": {
            "inventory": ["Longsword", "Plate Armor", "Health Potion"],
            "equipped": {"weapon": "Longsword", "body": "Plate Armor"},
            "intro": "Your draconic might is tempered by your sacred vows. As a dragonborn paladin, your longsword delivers divine retribution, and your presence inspires awe."
        },
        "Tiefling": {
            "inventory": ["Longsword", "Chainmail", "Health Potion"],
            "equipped": {"weapon": "Longsword", "body": "Chainmail"},
            "intro": "A tiefling paladin, you defy expectations, your devotion shining brighter than any shadow. Your longsword cuts through prejudice, fighting for a world that accepts all."
        },
        "Halfling": {
            "inventory": ["Shortsword", "Shield", "Chainmail", "Health Potion"],
            "equipped": {"weapon": "Shortsword", "offhand": "Shield", "body": "Chainmail"},
            "intro": "A halfling paladin, you prove that heroism comes in all sizes. With shortsword and shield, clad in chainmail, you bravely stand against injustice."
        }
    }
}
