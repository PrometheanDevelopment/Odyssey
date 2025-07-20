# MIT License
# Copyright (c) 2025 PrometheanDevelopment
# See LICENSE file: https://github.com/PrometheanDevelopment/Mini-life/blob/main/LICENSE

# Imports
import random
import os

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
        print("MIT License                                                                   ")
        print("                                                                              ")
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
                playing = True
                pass

            elif query == "2":
                debug.clearscreen()
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
            ("Brave New World", "A sci-fi dystopian novel by Aldous Huxley", "\n'Not to mention the right to grow old and ugly and impotent; the right to have syphilis and cancer; the right to have too little to eat; the right to be lousy; the right to live in constant apprehension of what may happen tomorrow; the right to catch typhoid; the right to be tortured by unspeakable pains of every kind.' There was a long silence. 'I claim them all,' said the Savage at last. Mustapha Mond shrugged his shoulders. \n'You're welcome,' he said."),
            ("The Art Of Simple Sabotage", "A book on how to sabotage and be annoying", "Section 3: Managers and Supervisors: To lower morale and production,  think of the worst boss you’ve had and act like that. Be pleasant to inefficient workers; give them undeserved promotions. Discriminate against efficient workers; complain unjustly about their work. When possible, refer all matters to committees for 'further study and consideration.' Attempt to make the committees as large and bureaucratic as possible."),
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
            ("Disruptor Pistol", "A futuristic blaster that fires bolts of energy", 10),
            ("Disruptor Rifle", "A bulky futuristic rifle that fires bolts of energy.", 15),
        ]

    class consumable:
        def __init__(self, name, desc, health):
            self.name = name
            self.desc = desc
            self.health = health

        items = [

            #=========#
            #  M E D  #
            #=========#


            # Debra's Medicine - Miracle medicine for deities
            ("Chicken Noodle Soup", "A white mug of steaming Chicken Noodle Soup.", 1000),

            #===========#
            #  F O O D  #
            #===========#

            # Debra's cooking - Superfoods for deities
            ("Ambrosia", "Crispy, flaky pastry sheet. Changes flavor as you eat.", 500),
            ("Nectar", "Looks like apple juice. Absolutely delicious.", 500),

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
            ("CarbonTart™", "Pure black. Tastes like velvet and threat.", 10),

            ("RealFruit Stripz™ (Yes, Really!)", "Allegedly 100% real fruit.", 2),
            ("FettuccineOs", "No longer at risk of copyright issues!", 5),

        ]

class object:

    class debra:

        class fridge:
            object_name = "Ceiling fridge"
            inspect = "Attached to the ceiling. You can't reach it."
        class bed:
            object_name = "Bed"
            inspect = "Single size bed with bright red sheets and pillow, with a white blanket."
        class dining:
            object_name = "Dining Area"
            inspect = "A wooden chair with a table on either side."
        class kitchen:
            object_name = "Kitchen"
            inspect = "A completely normal, modern-style kitchen."      
        class window:
            object_name = "Window"
            inspect = "A four-section, cross framed window, looking out into an endless void dotted with small lights."

class character:

    class Debra:
        def __init__(self):
            self.name = "Debra (with a Q)"
            self.speech = random.choice([
                ""
            ])
            self.action = random.choice([
                "Washing rain", "Eating oxygen", "Looking for her eyes", "Drowning her fish",
                "Walking her fridge", "Folding dishes", "Getting climbed by a tree"
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
                if item in items.weapon.items:
                    print(f"{i + 1}: {item[0]} - {item[1]} (Damage: {item[2]})")
                elif item in items.consumable.items:
                    print(f"{i + 1}: {item[0]} - {item[1]} (Heals: {item[2]})")
                elif item in items.book.items:
                    print(f"{i + 1}: {item[0]} - {item[1]}")
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
        

class area:

    class debras_house:

        characters = [character.Debra()]
        objects = [object.debra.bed, object.debra.dining, object.debra.fridge, object.debra.kitchen, object.debra.window]
        description = "A small, one roomed house."
        name = "Debra's House"



#=========#
#  D E V  #
#=========#

class dev:

    def console():
        while True:
            ccr = input("~ ")

            if ccr == "player.additem":
                print("\n[Books]")
                for i, item in enumerate(items.book.items):
                    print(f"{i}: {item[0]}")

                print("\n[Weapons]")
                for i, item in enumerate(items.weapon.items):
                    print(f"{i + 100}: {item[0]}")  # +100 offset

                print("\n[Consumables]")
                for i, item in enumerate(items.consumable.items):
                    print(f"{i + 200}: {item[0]}")  # +200 offset

                try:
                    itemadd = int(input("Item ID to add: "))
                    addrepeat = int(input("Amount: "))

                    for _ in range(addrepeat):
                        if len(inventory) >= 10:
                            print("[INVENTORY FULL] Cannot add more items.")
                            break

                        if 0 <= itemadd < len(items.book.items):
                            inventory.append(items.book.items[itemadd])
                        elif 100 <= itemadd < 100 + len(items.weapon.items):
                            inventory.append(items.weapon.items[itemadd - 100])
                        elif 200 <= itemadd < 200 + len(items.consumable.items):
                            inventory.append(items.consumable.items[itemadd - 200])
                        else:
                            print("[ERROR] Invalid Item ID.")
                            break

                    print(f"[OK] Inventory now has {len(inventory)} items.")

                except ValueError:
                    print("[ERROR] Please enter valid numbers.")

            elif ccr == "player.inventory":
                player.inventory.inventory()

            else:
                print("[ERROR] Unknown command.")

# Run dev console
titlescreen.menu(playing=False)
debug.area.make(area.debras_house.characters, area.debras_house.description, area.debras_house.name)
dev.console()
