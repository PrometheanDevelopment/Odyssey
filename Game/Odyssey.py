# MIT License
# Copyright (c) 2025 PrometheanDevelopment
# See LICENSE file: https://github.com/PrometheanDevelopment/Mini-life/blob/main/LICENSE

# Imports
import random
import os
import time

# Pre-set variables
inventory = []
object_num = 0

class debug:

    def clearscreen():
        os.system('cls')

    class area:

        def make(characters, description, name):
            print(f"{name}. {description}")

            count = 0
            for character in characters:
                count += 1
                print(f"\n{count}. {character.name}")

        def reset(object_num, objects):
            object_num = 0
            objects = [None]
            return object_num, objects

class titlescreen:

    def license():
        debug.clearscreen()
        print("Copyright (c) 2025 PrometheanDevelopment                                      ")
        print("                                                                              ")
        print("Permission is hereby granted, free of charge, to any person obtaining a copy  ")
        print("of this software and associated documentation files (the 'Software'), to deal ")
        print("in the Software without restriction, including without limitation the rights  ")
        print("to use, copy, modify, merge, publish, distribute, sublicense, and/or sell     ")
        print("copies of the Software, and to permit persons to whom the Software is         ")
        print("furnished to do so, subject to the following conditions:                      ")
        print("                                                                              ")
        print("The above copyright notice and this permission notice shall be included in all")
        print("copies or substantial portions of the Software.                               ")
        print("                                                                              ")
        print("THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR    ")
        print("IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,      ")
        print("FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE   ")
        print("AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER        ")
        print("LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, ")
        print("OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE ")
        print("'SOFTWARE'.                                                                   ")
        input("\n === PRESS ENTER TO EXIT ===")

    def menu(playing):
        while not playing:
            debug.clearscreen()
            print(".___  ___.  __  .__   __.  __                 __       __   _______  _______ ")
            print("|   \/   | |  | |  \ |  | |  |               |  |     |  | |   ____||   ____|")
            print("|  \  /  | |  | |   \|  | |  |     ______    |  |     |  | |  |__   |  |__   ")
            print("|  |\/|  | |  | |  . `  | |  |    |______|   |  |     |  | |   __|  |   __|  ")
            print("|  |  |  | |  | |  |\   | |  |               |  `----.|  | |  |     |  |____ ")
            print("|__|  |__| |__| |__| \__| |__|               |_______||__| |__|     |_______|")
            print("=============================================================================")
            print("                                                                             ")
            print(" 1. Play                                                                     ")
            print(" 2. Quit                                                                     ")
            print(" 3. License                                                                  ")
            print("                                                                             ")
            query = input(" Select: ")

            if query == "1":
                debug.clearscreen()
                playing = True
                pass

            elif query == "2":
                debug.clearscreen()
                time.sleep(1)
                exit()

            elif query == "3":
                titlescreen.license()

class items:

    class book:
        def __init__(self, name, desc, text):
            self.name = name
            self.desc = desc
            self.text = text

        items = [
            ("Guide to being annoying: Beginner", "A beginner guide to being annoying.", "A very simple and easy way to be annoying is to repeat someone as they are talking to you. This method is both simple, and effective, making it a prime strategy for beginners."),
            ("Guide to being annoying: Intermediate", "An intermediate guide to being annoying.", ""),
            ("Guide to being annoying: Expert", "An expert guide to being annoying.", "Potentially the most annoying action possible, is to interrupt someone. Do do this effectively, you will need: a safe distance of 62km, and a 1mt hydrogen bomb. Plant the bomb, move to minimum safe distance and detonate (Note: Do NOT look at the flash). This is guaranteed to interrupt your target sufficiently."),
            ("Cautionary Tales: Vol. 1", "A book containing cautionary tales.", "There was once a man who could not be harmed by reality. Punches deflected off him, rocks shattered, and bullets bounced off him. He thought he was invincible. Then he clipped through reality, into the backrooms, and died in the first 10 seconds."),
            ("Cautionary Tales: Vol. 2", "A book containing cautionary tales.", "There were once 3 evil kings, each had a prophecy. The first's said that no man could kill him. The second's; no weapon could harm him. And the third's was that no mortal hand could kill him. The first proceeded to be hacked apart by a woman, the second fell down some stairs, and the third was kicked to death by an angry mob."),
            ("Cautionary Tales: Vol. 3", "A book containing cautionary tales.", "There was once a boy named Boopy. Boopy was to ride the bus and collect some groceries, but he was too late. So he walked into a newsagent with $300 in hand, and began buying scratch tickets. The cashier told him to stop after he had spent $200, but it was already too late. Boopy had very little money left, and had to eat dirt for the next 2 weeks."),
        ]

    class weapon:
        def __init__(self, name, desc, damage):
            self.name = name
            self.desc = desc
            self.damage = damage

        items = [
            ("Bonkinator 2000", "Its a comically large, colorful mallet that makes a loud BONK! sound on impact", 17),
            ("Boxing glove", "Its a large, padded, red glove.", 5),
            ("Danger Fork", "Its a dangerous fork.", 5),
            ("Rubber Chicken", "It's squeaky and mildly threatening.", 2),
        ]

    class consumable:

            class food:

                def __init__(self, name, desc, health):
                    self.name = name
                    self.desc = desc
                    self.health = health

                debras_items = [
                    # Debra's cooking - Superfoods for deities
                    ("Ambrosia", "Crispy, flaky pastry sheet. Changes flavor as you eat.", 500),
                    ("Nectar", "Looks like apple juice. Absolutely delicious.", 500),
                ]

                items = [

                    #===========#
                    #  P A S T  #
                    #===========#

                    ("WWI Ration - Bread", "A metal can containing discs of rock-solid bread.", 2),
                    ("WWI Ration - Meat", "A metal can containing a mysterious pink-grey meat.", 2),
                    ("WWI Ration - Soup", "A metal can containing a grey, soupy liquid.", 2),
                    ("Dampbell's Soup - Tomato soup", "A red and white metal can containing tomato soup. Looks old.", 3),
                    ("Dampbell's Soup - Beef stew", "A red and white metal can containing beef stew. Looks old.", 3),
                    ("Dampbell's Soup - Vegetable soup", "A red and white metal can containing vegetable soup. Looks old.", 3),
                    ("Tinned Ham", "A cubic metal tin containing processed ham. 60% of daily reccomended intake of sodium. Expired in 1923.", 3),
                    ("Water Pie", "Everone's favourite great depression dessert! It looks like a sad custard tart, but it's water!", 4),
                    ("Chipped Beef", "Thinly sliced pieces of salted, pressed beef. ", 2),
                    ("Brown Bread", "A piece of dark, seedy bread. Smells medieval.", 2),
                    ("Jelly-in-a-box", "Its an extrememly old, crumbling cardboard box of jelly powder.", 2),
                    ("Stewed Prunes", "A handful of wet, mushy prunes. They are kinda-sticky and slimy. And now... Oh dear god! Your hands are kinda-sticky and slimy!", 2),
                    ("Venus Bar", "A caramel & nougat chocolate bar. Only 3 years past it's sell-by date!", 1),
                    ("Blood Soup", "A thin broth made from pigs blood and vegetables. THIS. IS. SPARTA!!!", 3),
                    ("Plonkie", "A fluffy finger-cake filled with cream. 200 years old, still safe to eat.", 1),
                    ("Mysterious Soup", "A strange, chunky soup.", (random.randint(-1, 5))),


                    #===============#
                    #  M O D E R N  # 
                    #===============#

                    ("Thick's Chips", "Thick and solid!", 3),
                    ("FettuccineOs", "No longer at risk of copyright issues!", 5),
                    ("Pickle chips", "Crinkle-cut slices of deep-fried pickles. They don't know what the hell a kilometre is."),

                    #===============#
                    #  F U T U R E  #
                    #===============#

                    # EazyEat CORP - Junk/Hyper-processed food
                    ("OmniChip™", "One, giant chip. 20x daily reccomended calorie intake.", 5),
                    ("Meatyblock™: Chik’n Nugget", "Hyper-proccessed cube of 'Chicken'.", 3),
                    ("Meatyblock™: Hickor’ee Ham", "Hyper-proccessed cube of 'Ham'.", 3),
                    ("Meatyblock™: Smok’d Rib", "Hyper-proccessed cube of 'Rib'. Unclear from which animal.", 3),
                    ("Cheezy Puffs™", "Alarmingly orange. Deemed a health hazard in 73 nations.", 1),

                    # Mealpod Inc - 'Edible' food discs
                    ("BreakfastPod™: Omelette", "A flavourless dark yellow disc.", 3),
                    ("BreakfastPod™: Bacon & Eggs", "A flavorless gray disc.", 3),
                    ("BreakfastPod™: Waffle", "A flavourless beige disc.", 3),
                    ("BreakfastPod™: Jam Toast", "A flavourless red and beige disc.", 3),
                    ("SnackPod™: Chips", "A small, flavourless yellow disc.", 3),
                    ("SnackPod™: Fruit Salad", "A small, flavourless, colorful disc.", 3),
                    ("SnackPod™: Chocolate Bar", "A small, brown  disc.", 3),
                    ("SnackPod™: Crackers and cheese", "A small, flavourless beige disc.", 3),
                    ("LunchPod™: BLT Sandwich", "A flavorless white disc.", 3),
                    ("LunchPod™: Sausage Roll", "A flavourless brown disc.", 3),
                    ("LunchPod™: Hamburger", "A flavourless beige, brown, and green striped disc.", 3),
                    ("LunchPod™: Fish & Chips", "A flavourless yellow disc.", 3),
                    ("DinnerPod™: Meat Pie", "A flavourless brown disc.", 3),
                    ("DinnerPod™: Chicken & Rice", "A flavourless white disc.", 3),
                    ("DinnerPod™: Tuna Casserole", "A flavourless pale yellow disc.", 3),
                    ("DinnerPod™: Mac & Cheese", "A flavourless yellow disc.", 3),
                    ("DessertPod™: Apple Pie & Custard", "A flavourless beige disc.", 3),
                    ("DessertPod™: Banana Split", "A flavourless white, pink, and brown striped disc.", 3),
                    ("DessertPod™: Chocolate Cake", "A flavourless brown disc.", 3),
                    ("DessertPod™: Pudding", "A flavourless light yellow disc.", 3),
                    ("SpecialPod™: Birthday Cake", "A flavourless light blue disc with colorful sprinkles.", 3),
                    ("SpecialPod™: Turkey", "A flavourless beige disc.", 3),
                    ("SpecialPod™: Christmas Pudding", "A flavourless brown disc with white icing.", 3),
                    ("SpecialPod™: Easter Egg", "A flavourless brown disc.", 3),

                    # Ultra-LUXE Ltd - Luxury, good food
                    ("TrueMeat™: Wagyu Beef", "Grown in a zero-gravity nutrient vat. Massaged hourly by robotic arms.", 7),
                    ("TrueMeat™: Iberico Ham", "Grown in a zero-gravity nutrient vat. Massaged hourly by robotic arms.", 7),
                    ("TrueMeat™: Ayam Cemani Chicken", "Grown in a zero-gravity nutrient vat. Massaged hourly by robotic arms.", 7),
                    ("PearlFoam Caviar™", "Spherical protein pearls with oceanic data imprints.", 2),
                    ("NeoTruffle Gelée™", "Infused with real truffle DNA. Possibly from fungus.", 3),
                    ("IvoryCrust Pizzaette™", "Crust made from albino cornmeal and 'white' tomatoes.", 7),
                    ("LuxeBar™: Ambrosia Blend", "Combines 47 extinct flavors.", 5),
                    ("LuxeBar™: Nectar Blend", "Combines 32 extinct flavors.", 5),
                    ("LuxeBar™: Deity Blend", "Combines 64 extinct flavors.", 5),
                    ("LuxeBar™: Aether Blend", "Combines 11 extinct flavors.", 5),
                    ("QuantumGrapes™", "They never taste the same twice. Literally.", 5),
                    ("StasisVintage WineShot™", "Aged in temporal suspension. A single 5ml vial.", 3),
                    ("CarbonTart™", "Pure black. Tastes like velvet and threats.", 10),

                ]

            class drink:

                items = [
                    "a"
                ]

            class medicine:

                debras_items = [
                    # Debra's Medicine - Miracle medicine for deities
                    ("Chicken Noodle Soup", "A white mug of steaming Chicken Noodle Soup.", 1000),
                ]


class object:

    #===========#
    # D E B R A #
    #===========#

    class debra:

        class fridge:
            object_name = "Fridge"
            inspect = "It is attached to the ceiling. You can't reach it."
        class bed:
            object_name = "Bed"
            inspect = "Its a single size bed with bright red sheets and pillow, with a white blanket."
        class dining:
            object_name = "Dining Area"
            inspect = "Its a wooden chair with a table on either side."
        class kitchen:
            object_name = "Kitchen"
            inspect = "Its a completely normal, modern-style kitchen."      
        class window:
            object_name = "Window"
            inspect = "The four-section, cross framed window, looks out into an endless void dotted with small lights."



    #===============================================#
    # L I B R A R Y  O F  T R A N S C E N D E N C E #
    #===============================================#

    class library_of_transcendence:

        class shelves:

            class shelf:
                object_name = "Shelves"
                inspect = "The shelves strech out of sight upwards into a dark void. Looking down the aisles, you cannot see where they end."
                def interact():
                    interact = input("Take a book?\n 1. Yes\n 2. No\n\nSelect: ")
                    if interact == "1":
                        inventory.append(random.choice(items.book.items))

            class desk:
                object_name = "Reception desk"
                inspect = "A large, rounded reception desk stands between the entrance and the reading room. It is piled high with books."

        class reading_room:

            class mural:
                object_name = "Mural"
                inspect = "A large mural dominates the far wall from the entrance. It shows half of the mural filled with rainbows, light and angels. The other half is full of demons, darkness, and fire. The creatures are shown fighting those on the opposing side."

            class table:
                object_name = "Reading tables"
                inspect = "Rows of tidy desks with green hooded lamps fill the centre of the room. Each can sit up to 4 people."

            class booth:
                object_name = "Reading booths"
                inspect = "Along the edges of the room, there are reading booths; glass boxes, each with 2 green leather couches facing each other, large table between them. The boothes are seperated by dark wooden panels."

            class snack_bar:
                object_name = "Snack bar"
                inspect = 'To the left of the entrance, there is a brass, steampunk vending machine,. It lacks a keypad or window, but has the collection and token slots. It has a warning sign taped to the front: "WARNING: Items from past may be expired. Eat at own risk."'
                def interact():
                    interact = input("Use machine?\n 1. Yes\n 2. No\n\nSelect: ")
                    vending_item = None
                    if interact == "1":
                        vending_item = random.choice([items.food.items])
                        



    #=====================#
    # B O I N G V I L L E #
    #=====================#

    class boingville:

        class outside:

            class sign:

                object_name = "Welcome sign"
                inspect = '"Welcome to Boingville! Pop. 5"'

            class bouncy_castle:

                object_name = "Bouncy castle"
                inspect = "Its a bouncy castle. It is still less bouncy than the ground though."

        class lettuce_house:

            class antipoline:

                object_name = "Antipoline"
                inspect = "It is sticky, and stops things on it from bouncing."

            class flatinator:

                object_name = "Flatinator MK.2"
                inspect = "Its a giant hydraulic press."


class character:

    class debra:

        class Debra:
            def __init__(self):
                self.name = "Debra (with a Q)"
                self.speech = random.choice([
                    '"Hello honey!"', '(Smiles)', '""'
                ])
                self.action = random.choice([
                    "She is busy washing rain", "Shes eating oxygen", "She is busy looking for her eyes", "Shes drowning her fish",
                    "She is walking her fridge", "Shes folding dishes", "Shes getting climbed by a tree"
                ])

    class library_of_transendence:

        class shelves:
                
            class Joan:

                def __init__(self):
                    self.name = "Joan the Librarian"
                    self.speech = random.choice([
                        '""'
                    ])
                    self.action = random.choice([
                        "She glances up from her book and stares at you.", "She is busy writing in a large tome.", 
                        "She places a finger to her lips, signalling quiet."
                    ])

            class Galadriel:

                def __init__(self):
                    self.name = "Galadriel (El)"

                    rare_line = random.randint(1,100)
                    if rare_line == 100:
                        self.speech = '"Everyone’s so obsessed with light and dark. Nobody talks about the shadows. That’s where I live."'
                    else:
                        self.speech = random.choice([
                            '"If you\'re here to save the world, I suggest starting by not blowing it up."', 
                            '"You’re still standing here. Is it bravery, or the inability to take a hint?"'
                        ])
                    self.action = random.choice([
                        "She is staring at the cover of a gilded book, but not openning it.", "Shes holding a fireball.",
                        "She is glaring at a palm-leaf scroll.", "Shes brooding."
                    ])

    class boingville:

        class lettuce:

            def __init__(self):
                self.name = "Lettuce the Flat"
                self.speech = random.choice([
                    '"Flat... Flat.. Flat..."', '"This is my Antipoline." he scuttles to the antipoline. "It’s not for sale. Or sharing. Or bouncing."',
                    '"Stupid blouncing people and their stupid happiness..."', '"Stop bouncing."', '"Imagine not being a leafy green! Hahaha!"'
                ])
                self.action = random.choice([
                    "He is muttering to himself.", "He is sitting on the antipoline, doing nothing.", "He is smoothing himself out.",
                    "Hes writing a visa application to go to Flatsville."
                ])

        class mrbouncmans:

            def __init__(self):
                self.name = "Mr Bouncmans"
                self.speech = random.choice([
                    '"Bouncing is great!"', '""'
                ])
                self.action = random.choice([
                    "He is bouncing"
                ])

class player:

    class inventory:

        @staticmethod
        def view():
            if not inventory:
                print("[EMPTY] Inventory is empty.")
                return

            print("[INVENTORY]")
            for i, item in enumerate(inventory):
                if item in items.book.items:
                    print(f"{i + 1}: {item[0]}")
                elif item in items.weapon.items:
                    print(f"{i + 1}: {item[0]} - {item[1]} (Damage: {item[2]})")
                elif item in items.consumable.food.debras_items or items.consumable.food.items:
                    if item[0] == "Mysterious Soup":
                        print(f"{i + 1}: {item[0]} - {item[1]} (Heals: ???)")
                    else:
                        print(f"{i + 1}: {item[0]} - {item[1]} (Heals: {item[2]})")
                else:
                    print(f"{i + 1}: {item[0]} - {item[1]}")

    class speech:

        def easy(charisma):
            chance = min(charisma * 20, 100)
            return random.randint(1, 100) <= chance

        def medium(charisma):
            chance = min(charisma * 10, 100)
            return random.randint(1, 100) <= chance

        def hard(charisma):
            chance = min(charisma * 5, 100)
            return random.randint(1, 100) <= chance
        
    class attack():
        damage = random.randint(3, 12)
        

class area:

    class debras_house:

        characters = [character.debra.Debra()]
        objects = [object.debra.bed, object.debra.dining, object.debra.fridge, object.debra.kitchen, object.debra.window]
        description = "Its a small, one roomed house."
        name = "Debra's House"

    class library_of_transcendence:

        class shelves:
        
            characters = []
            objects = [object.library_of_transcendence.shelves]
            description = "It is an endless library of arcane knowledge."
            name = "Library of Transcendence: Shelves"

        class reading_room:

            characters = []
            objects = [object.library_of_transcendence.reading_room]
            description = "It is an endless library of arcane knowledge."
            name = "Library of Transcendence: Reading room"

    class boingville:

        class boingville_store:

            characters = []
            objects = []            
            description = "Its a store that sells bouncy objects."
            name = "KLOMP'S SPRING-THING EMPORIUM"

        class boingville_diner:

            characters = []
            objects = []
            description = "Its the famous Boingville Diner!"

        class outside:

            characters = []
            objects = []
            description = "You are in a small town sitting on a plateu overlooking a desert."
            name = "Boingville"





#=========#
#  D E V  #
#=========#

class dev:

    def console():
        while True:
            ccr = input("~ ")

            if ccr == "listitems":
                categories = {
                    "Book": items.book.items,
                    "Weapon": items.weapon.items,
                    "Consumable": (
                        items.consumable.food.debras_items +
                        items.consumable.food.items
                    )
                }

                for cat, itemlist in categories.items():
                    print(f"\n[{cat.upper()}]")
                    for i, item in enumerate(itemlist):
                        print(f"{i}: {item[0]}")


            elif ccr.startswith("player.additem"):
                parts = ccr.split()
                if len(parts) != 3:
                    print("[ERROR] Use: player.additem <category> <index>")
                    return

                cat_name, index = parts[1], parts[2]

                categories = {
                    "0": items.book.items,
                    "1": items.weapon.items,
                    "2": (
                        items.consumable.food.items +
                        items.consumable.food.debras_items
                    )
                }

                if cat_name not in categories:
                    print(f"[ERROR] Unknown category '{cat_name}'. Try: {', '.join(categories.keys())}")
                    return

                try:
                    idx = int(index)
                    item_list = categories[cat_name]
                    item = item_list[idx]
                    if len(inventory) < 10:
                        inventory.append(item)
                        print(f"[OK] Added: {item[0]}")
                    else:
                        print("[ERROR] Inventory full.")
                except (ValueError, IndexError):
                    print("[ERROR] Invalid index.")

            elif ccr == "player.inventory":
                player.inventory.view()

            else:
                print("[ERROR] Unknown command.")

# Run dev console
titlescreen.menu(playing=False)
inventory.append(random.choice(items.book.items))
dev.console()
