# MIT License
# Copyright (c) 2025 PrometheanDevelopment
# See LICENSE file: https://github.com/PrometheanDevelopment/Odyssey/blob/main/LICENSE

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
        input("\n                      === PRESS ENTER TO EXIT ===")

    def menu(playing):
        while not playing:
            debug.clearscreen()
            print("Placeholder")

            if query == "start":
                debug.clearscreen()
                playing = True

            elif query == "quit":
                debug.clearscreen()
                time.sleep(1)
                exit()

            elif query == "license":
                titlescreen.license()

class items:

    class book:
        def __init__(self, name, desc, text):
            self.name = name
            self.desc = desc
            self.text = text

        items = [

            # Potentially offensive jokes
            ("Red book of jokes: Vol. 1", "A large, red book of jokes.", '"When can’t you have homemade Chinese food? Because you don’t have any pets. Just eat African food, you have plenty of neighbors!"'),
            ("Red book of jokes: Vol. 2", "A large, red book of jokes.", '"Yes, women do make less money than men. But it’s because they tend to go for lower-paying jobs. So it goes without saying women are going to be paid less. For example, men tend to become executives or lawyers. Women tend to become female executives or female lawyers."'),
            ("Red book of jokes: Vol. 3", "A large, red book of jokes.", '"What is the favourite sport of mexican immigrants? Cross country."'),
            ("Red book of jokes: Vol. 4", "A large, red book of jokes.", '"What do genders and the Twin Towers have in common? There used to be two, but now people get weird when you talk about them."'),
            ("Red book of jokes: Vol. 5", "A large, red book of jokes.", '"A Canadian, an Italian, and a Russian are looking at a painting of Adam and Eve. The Canadian starts, "See how polite and respectful they look? They must be Canadian."\n"Are you kidding?” exclaims the Italian. "They’re gorgeous. They must be Italian!" \nThe Russian finally says, \"They have nothing to wear, no house to live in, only one apple to eat, and they keep being told that they’re in heaven. They’re obviously Russian."'),
            ("Red book of jokes: Vol. 6", "A large, red book of jokes.", '"A major recent scientific study found that monkeys actually eat more bananas than humans. I guess it’s true. It’s been a long time since I fed my monkey a dead human."'),

            # Potentially legal activities
            ("How to Smuggle a Small Nation's Economy in a Carry-On", "A travel-sized guide to fiscal irresponsibility and compact corruption.", "Step 1: Convert entire GDP into rare, untraceable assets — gemstones, NFTs, or commemorative Beanie Babies.\nStep 2: Vacuum-seal into custom compartments inside your neck pillow.\nStep 3: At airport security, appear bored and underpaid.\nStep 4: When asked what’s in the bag, say ‘emotional baggage and a mild recession.’\nBonus tip: Distract customs with a decoy suitcase full of exotic cheeses and tax forms.\nCongratulations: You are now the proud carrier of a sovereign liquidity crisis."),
            ("How to Hide a Human-Sized Inanimate Object", "A suspiciously detailed guide to eternal hide-and-seek.", "Step 1: Do not panic.\nStep 2: Disguise the object as something people avoid on instinct — like a haunted mannequin, a cursed art piece, or a tax audit.\nStep 3: Place it in a liminal space: behind a church organ, in a locked janitor’s closet at a 24-hour bowling alley, or under the display table at an abandoned mattress store.\nRemember: the best place to hide is somewhere no sane person ever willingly returns — like the back row of a community theatre rehearsal of *Cats*."),
            ("How to Commit Totally Imaginary, Absolutely Legal, Not-Dubious-at-All Money Laundering", "A handbook for theoretical citizens in alternate dimensions.", "First of all, you need the money to look legit - send it through a washing cycle, crumple it, stomp on it - make it look like its been in circulation. Then you need a business - something cash based - and mix in your dirty cash with the real stuff. Then, take it to a bank, send it to an offshore account, and bam! Your money is legit!"),

            # Quantum shenanigans
            ("The Observer Effect and How to Use It to Win Arguments", "A book detailing a quantum approach to always being right.", '"According to quantum physics, simply observing something changes its state. So, stare at your opponent’s logic until it collapses. Their argument becomes both valid and invalid — but you observed it first, so yours wins. Advanced technique: wear Schrödinger’s Sunglasses to double your certainty while staying cool."'),
            ("How to Hijack the Higgs Boson", "A completely irresponsible and hypothetical guide to quantum meddling.", '"Step 1: Build a Large Hadron Collider in your backyard.\nStep 2: Lure the Higgs boson out of hiding with subatomic breadcrumbs (quarks work best).\nStep 3: Tackle it mid-field using a graviton lasso.\nStep 4: Place a sound or object into its quantum spin state.\nStep 5: Collapse the waveform. Now your object is encoded into reality.\nEnjoy your new universal constant."'),
            
            # Guides to being annoying
            ("Guide to being annoying: Beginner", "A beginner guide to being annoying.", '"A very simple and easy way to be annoying is to repeat someone as they are talking to you. This method is both simple, and effective, making it a prime strategy for beginners."'),
            ("Guide to being annoying: Intermediate", "An intermediate guide to being annoying.", '"Once you\'ve mastered basic tactics, try humming loudly during conversations, or responding to every statement with a question. Bonus points if you do both simultaneously."'),
            ("Guide to being annoying: Expert", "An expert guide to being annoying.", '"Potentially the most annoying action possible, is to interrupt someone. Do do this effectively, you will need: a safe distance of 62km, and a 1mt hydrogen bomb. Plant the bomb, move to minimum safe distance and detonate (Note: Do NOT look at the flash). This is guaranteed to interrupt your target sufficiently."'),
            ("Guide to being annoying: God-Tier", "A god-tier guide to being annoying.", "Transcending time and space to become an omnipresent echo in someone's thoughts is the peak of annoyance. To achieve this, you must first master quantum field theory, hijack the Higgs boson, and insert your voice into the fabric of reality itself. Every time they blink, breathe, or think, there you are, whispering 'What are you doing?' forever."),
            
            # Cautionary tales
            ("Cautionary Tales: Vol. 1", "A book containing cautionary tales.", '"There was once a man who could not be harmed by reality. Punches deflected off him, rocks shattered, and bullets bounced off him, etc. He thought he was invincible. Then he clipped through reality, into the backrooms, and died in the first 10 seconds."'),
            ("Cautionary Tales: Vol. 2", "A book containing cautionary tales.", '"There were once 3 evil kings, each had a prophecy. The first\'s said that no man could kill him. The second\'s; no weapon could harm him. And the third\'s was that no mortal hand could kill him. The first proceeded to be hacked apart by a woman, the second fell down some stairs, and the third was kicked to death by an angry mob."'),
            ("Cautionary Tales: Vol. 3", "A book containing cautionary tales.", '"There was once a boy named Boopy. Boopy was to ride the bus and collect some groceries, but he was too late. So he walked into a newsagent with $300 in hand, and began buying scratch tickets. The cashier told him to stop after he had spent $200, but it was already too late. Boopy had very little money left, and had to eat dirt for the next 2 weeks."'),
        
        ]

    class weapon:
        def __init__(self, name, desc, damage):
            self.name = name
            self.desc = desc
            self.damage = damage

        items = [
            ("Bonkinator 2000", "Its a comically large, colorful mallet that makes a loud BONK! sound on impact", 5),
            ("Boxing glove", "Its a large, padded, red glove.", 3),
            ("Danger Fork", "Its a dangerous fork.", 1),
            ("Rubber Chicken", "It's squeaky and mildly threatening.", 2),
            ("Garrotte", "A thin, sharp metal wire with 2 wooden handles.", 7),
            ("Longsword","Just like a shortsword, only longer!", 10),
            ("Musket", "You could shoot this. Mabye.")            
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

                        #=============#
                        #  R O M A N  #
                        #=============#

                        ("Panis Quadratus", "A round, scored loaf of bread carbonised in Pompeii. Crunchy. Permanently.", 2),
                        ("Moretum", "A paste of garlic, cheese, herbs, and olive oil. Romans ate it for breakfast and to keep people far away.", 3),
                        ("Dormouse in Honey", "A roasted dormouse stuffed with nuts, then dipped in honey. A delicacy for the rich.", 4),
                        ("Gustum de Praecoquis", "Stewed apricots with honey and wine. Tart and sweet at once.", 3),
                        ("Isicia Omentata", "Roman-style hamburger made with minced meat, pepper, wine, and pine nuts.", 4),
                        ("Patina de Apua", "Fish casserole baked with eggs and herbs. Smells... assertive.", 3),
                        ("Conditum Paradoxum", "Spiced wine sweetened with honey and flavoured with saffron. Both medicine and party fuel.", 4),
                        ("Ova Elixa", "Hard-boiled eggs sprinkled with pepper sauce. Simple and popular.", 2),
                        ("Garum", "Fermented fish sauce used on almost everything. The smell clears a room.", 1),
                        ("Puls", "A humble porridge of spelt grain, water, and salt. Soldier fuel.", 2),
                        ("Lucanian Sausage", "Spicy smoked sausage made with pork, pine nuts, and coriander.", 3),
                        ("Melones et Caseus", "Slices of melon served with soft cheese. Surprisingly modern-tasting.", 2),
                        ("Ostrea", "Fresh oysters eaten raw with garum. Wealth in a shell.", 3),
                        ("Globi", "Cheese fritters fried in honey. Sticky fingers guaranteed.", 3),
                        ("Posca", "Sour wine vinegar diluted with water. Legionary Gatorade.", 1),
                        ("Boiled Cabbage", "Served with vinegar and oil. Cato swore it cured everything.", 1),

                        #===================#
                        #  M E D I E V A L  #
                        #===================#

                        ("Pottage", "A thick stew of barley, beans, onions, and whatever fell in the pot that day.", 3),
                        ("Hardtack", "A rock-hard biscuit that can break both hunger and teeth.", 2),
                        ("Honeyed Mead", "Sweet fermented drink made from honey. Might be stronger than it tastes.", 4),
                        ("Salted Cod", "Preserved fish, chewy enough to be used as a weapon.", 3),
                        ("Hog Roast", "A spit-roasted pig with crispy skin and smoky flavour.", 6),
                        ("Turnip Stew", "Thin broth with chunks of turnip. Surprisingly filling.", 3),
                        ("Manchet Bread", "Fine white bread reserved for nobility. Soft, fluffy, and smug.", 4),
                        ("Ale-soaked Bread", "Bread dunked in ale for easy chewing. Both food and drink in one!", 3),
                        ("Boar Pie", "Pastry crust stuffed with boar meat, herbs, and questionable hygiene.", 5),
                        ("Apple Tarts", "Small pastries filled with sweet stewed apples. A rare treat.", 2),
                        ("Pickled Cabbage", "Fermented cabbage with a pungent smell and stronger taste.", 2),
                        ("Lamprey in Jelly", "A wriggly eel-like fish suspended in gelatin. Slimy and jiggly.", 4),
                        ("Blood Pudding", "A dense sausage made with animal blood, oats, and spices.", 3),
                        ("Cheese Wheel", "A hefty wheel of hard cheese. Can be eaten or rolled downhill at enemies.", 4),
                        ("Spiced Wine", "Warm red wine with cinnamon and cloves. Heals the body and the mood.", 4),

                        ("Stale Rye Bread", "Dense, dry bread made from rye flour. Will get caught in your throat.", 1),
                        ("Thin Onion Broth", "Hot water with the ghost of an onion waved over it.", 1),
                        ("Boiled Turnip", "A single turnip, boiled into submission.", 1),
                        ("Cabbage Gruel", "A watery sludge of cabbage and oats. Technically edible.", 1),
                        ("Oatcakes", "Flat, chewy oat discs baked on a stone. Doubles as a frisbee.", 1),
                        ("Root Mash", "Turnips, parsnips, and whatever else was dug up today. Mashed into mush.", 1),
                        ("Salted Herring", "Strong-smelling fish preserved in salt. Best eaten fast.", 2),
                        ("Acorn Bread", "Made from acorn flour. Slightly bitter. Slightly poisonous.", 1),
                        ("Foraged Greens", "Random weeds and leaves boiled until soft. Might be nettles.", 1),
                        ("Oaten Gruel", "A gloopy mixture of oats and water. Grey in colour and in spirit.", 1),
                        ("Boiled Beetroot", "Soft, earthy beets that stain everything they touch.", 1),
                        ("Boiled Barley", "Chewy barley boiled in water until vaguely edible.", 1),

                        #=========#
                        #  W W 1  #
                        #=========#

                        # WW1 Rations
                        ("WW1 Ration - Bread", "A metal can containing discs of rock-solid bread.", 2),
                        ("WW1 Ration - Meat", "A metal can containing a mysterious pink-grey meat.", 2),
                        ("WW1 Ration - Soup", "A metal can containing a grey, soupy liquid.", 2),

                        #===================#
                        #  C O L D   W A R  #
                        #===================#
                        ("Atomic Loaf", "Brightly packaged white bread fortified with 12 vitamins, 8 minerals, and one Cold War secret.", 3),
                        ("TV Dinner: Salisbury Steak", "A frozen compartment tray of steak, mashed potatoes, and peas. Best enjoyed in front of a boxy TV.", 4),
                        ("TV Dinner: Turkey & Gravy", "A frozen feast in aluminium. Tastes like Sunday lunch and mild regret.", 4),
                        ("Sham", "A cubic metal tin containing processed ham. 60% of daily reccomended intake of sodium.", 3),
                        ("Sham™ Fritters", "Slices of Sham coated in batter and deep-fried. The taste of postwar prosperity.", 3),
                        ("Tang™ Drink Mix", "Artificial orange drink mix. The future of space travel… in your cup.", 2),
                        ("Jell-O™ Salad", "Gelatin dessert with suspended fruit, marshmallows, and mystery.", 2),
                        ("Canned Pineapple Rings", "Golden rings of sweetness in syrup. Tropical luxury in a can.", 2),
                        ("Canned Peas", "Small, green, and soft enough to dent with a spoon.", 1),
                        ("Kraft Macaroni & Cheese", "Bright orange pasta in a box. Ready in minutes. Cheese optional.", 3),
                        ("Vienna Sausages", "Tiny pale sausages in brine. Slide right out of the can.", 2),
                        ("Milkshake Mix", "Powdered milk, sugar, and flavour. Just add milk and shake until bored.", 2),
                        ("Hot Dog Casserole", "Hot dogs baked with beans and tinned tomato soup. A family favourite.", 3),
                        ("Canned Chicken à la King", "Creamy chicken, peppers, and mushrooms in a tin. Luxury for the masses.", 3),
                        ("Root Beer Float", "Soda and vanilla ice cream. The drink you can chew.", 2),
                        ("Canned Brown Bread", "Sweet molasses bread steamed and sealed in a tin. Slice carefully.", 2),
                        ("Potted Meat", "Ground, cooked meat in a spreadable paste. Both lunch and survival ration.", 2),

                    # Dampbell's Soup - Canned soups
                    ("Dampbell's Soup - Tomato soup", "A red and white metal can containing tomato soup. Looks old.", 3),
                    ("Dampbell's Soup - Beef stew", "A red and white metal can containing beef stew. Looks old.", 3),
                    ("Dampbell's Soup - Vegetable soup", "A red and white metal can containing vegetable soup. Looks old.", 3),

                    ("Water Pie", "Everone's favourite great depression dessert! It looks like a sad custard tart, but it's water!", 4),
                    ("Chipped Beef", "Thinly sliced pieces of salted, pressed beef. ", 2),
                    ("Brown Bread", "A piece of dark, seedy bread. Smells medieval.", 2),
                    ("Jelly-in-a-box", "Its an extrememly old, crumbling cardboard box of jelly powder.", 2),
                    ("Stewed Prunes", "A handful of wet, mushy prunes. They are kinda-sticky and slimy. And now... Oh dear god! Your hands are kinda-sticky and slimy!", 2),
                    ("Venus Bar", "A caramel & nougat chocolate bar. Only 3 years past it's sell-by date!", 1),
                    ("Blood Soup", "A thin broth made from pigs blood and vegetables. THIS. IS. SPARTA!!!", 3),
                    ("Crinklie", "A fluffy finger-cake filled with cream. 200 years old, still safe to eat.", 1),
                    ("Mysterious Soup", "A mysterious, chunky soup.", (random.randint(-1, 5))),

                    #===============#
                    #  M O D E R N  # 
                    #===============#

                    ("Thick's Chips", "Thick and solid!", 3),
                    ("FettuccineOs", "No longer at risk of copyright issues!", 5),
                    ("Pickle Chips", "Crinkle-cut slices of deep-fried pickles. They don't know what the hell a kilometre is.", 3),
                    ("Glazed-Donut Cheeseburger", '"WARINING: 6500 Calories per serving."', 10),
                    ("Diet Brownie", "Gluten-Free, Sugar-Free, Nutrient-Free, Taste-Free. It exists. That's all.", 1),
                    ("Ghost Pepper Chips", "So hot they legally count as a poison in 2 states.", 3),
                    ("Craft Cola", "Locally brewed by a guy with a beard. Tastes like dirt and nostalgia.", 2),
                    ("Microwave Sushi", "Technically edible. Technically fish. Technically not legal in Japan.", 2),

                    # McRonalds - Fast-food chain
                    ("McRonald’s™ MegaStack™", "Six beef patties, twelve sauces, one bun. Requires two hands and three regrets.", 8),
                    ("McRonald’s™ Cheeseburger", "Bun, patty, sauce, cheese, pickle, bun. Simplicity at it's finest.", 3),
                    ("McRonald’s™ Quarter Kilo™", "2 patties, some sad lettuce, cheese and special sauce. Addictively delicious.", 4),
                    ("McRonald’s™ Icecream", "A miracle! The icecream machine was working!", 2),
                    ("McRonald’s™ Nuggets", "10 chicken nuggets, in 4 different shapes. Comes with sweet'n'sour sauce.", 3),
                    ("McRonald’s™ Fire Nuggets", "So spicy they must be McIllegal™ in three time zones.", 2),
                    ("McRonald’s™ Fries", "Fun Fact: Most fast-food chains use fries rather than thicker chips, because fries are faster to cook.", 1),
                    ("McRonald’s™ McSalad™", "Limp lettuce, a single tomato slice, and invisible dressing. For the illusion of health.", 1),
                    ("McRonald’s™ McSoup™", "A cup of salty beige liquid. Possibly rehydrated fryer grease.", 2),
                    ("McRonald’s™ McSunrise™", "Egg, bacon, and syrup between two waffles.", 5),
                    ("McRonald’s™ Banana Blizzard™", "Vanilla soft serve with banana sauce. Absolutely GOATed.", 1),
                    ("McRonald’s™ Chocolate Blizzard™", "Chocolate soft serve with a flake and choc-fudge.", 1),
                    ("McRonald’s™ Strawberry Blizzard™", "Vanilla soft serve with strawberry sauce.", 1),

                    # Burger Soverign - Fast-food chain
                    ("Burger Sovereign™ CrownBurger", "Two patties, one crown-shaped bun, endless hubris.", 5),
                    ("Burger Sovereign™ Fries Royale", "Curly fries dipped in faux-truffle aioli. For peasants who pretend to be kings.", 4),
                    ("Burger Sovereign™ Jester Meal", "Comes with a small Fries Royale, JesterBurger, Jester Jelly, and toy!", 2),
                    ("Burger Sovereign™ Knight's Icecream", "A hilt-shaped cane with a blade-shaped tower of soft serve.", 2),
                    ("Burger Sovereign™ Royal Nuggets", "10 nuggets marinated in truffle oil, double fried, and dipped in faux-truffle aioli.", 5),
                    ("Burger Sovereign™ CrownBurger", "Two patties, one crown-shaped bun, endless hubris.", 5),
                    
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
        class television:
            object_name = "Television"
            inspect = ""
            def interact():
                tv_shows = shows = [
                                        # News

                                            # NBN

                                            ("NBN Morning Update", 2,
                                            "Good morning, citizens! The sun is out, the birds are chirping, and so are the drones.",
                                            "Authorities assure us the drones are simply collecting weather data, not facial recognition samples.",
                                            "In unrelated news, a new law requires everyone to smile at least once per hour."
                                            ),

                                            ("NBN Midday Bulletin", 5,
                                            "Traffic update: there isn’t any. Cars have collectively decided to unionize, too.",
                                            "The Department of Transportation says they’re 'in talks' with the vehicles.",
                                            "Meanwhile, citizens are encouraged to walk, bike, or hover if possible."
                                            ),

                                            ("NBN Evening News", 1,
                                            "Good evening. I’m Stan Broadcast, and this is NBN News at Nine.",
                                            "Tonight’s top story: the city’s pigeons have unionized, demanding bread equality.",
                                            "Local authorities are negotiating, but the situation remains crumby.",
                                            "More on that as it develops."
                                            ),

                                            # Channel 8

                                            ("Channel 8 Late Report", 1,
                                            "Breaking news: local scientist claims to have discovered ‘reverse gravity.’",
                                            "When asked for proof, he and his lab promptly floated into the atmosphere.",
                                            "Experts call it ‘uplifting.’",
                                            "Weather next — spoilers, it’s still outside."
                                            ),

                                            #WZRD News

                                            ("WZRD News", 3,
                                            "This just in: mysterious orbs of light have been seen hovering over downtown.",
                                            "Eyewitnesses describe them as ‘beautiful,’ ‘terrifying,’ and ‘excellent selfie lighting.’",
                                            "Officials advise staying calm and keeping your tinfoil hats polished."
                                            ),

                                            ("WZRD News", 4,
                                            "Viewers are reporting strange voices coming from their televisions.",
                                            "Experts say it’s likely an audio feedback glitch.",
                                            "Still, if the voice knows your name... maybe change the channel."
                                            ),

                                            # Action 6 Breaking

                                            ("Action 6 Breaking", 4,
                                            "Emergency alert: something weird is happening in Sector 7.",
                                            "Residents report humming noises, flickering lights, and mild existential dread.",
                                            "Authorities deny rumors of interdimensional portals — again.",
                                            "More after the break, assuming reality holds."
                                            ),

                                            # WBLN

                                            ("WBLN Newsflash", 6,
                                            "Breaking: government reassures public that the power outages are ‘completely normal.’",
                                            "However, experts note the blackout map now covers the entire state.",
                                            "Stay tuned for our special report: ‘Darkness — nature’s nightlight.’"
                                            ),

                                            # Public Service Broadcast

                                            ("Public Service Broadcast", 1,
                                            "This is an official emergency transmission.",
                                            "Please remain calm and indoors.",
                                            "Reports of aggressive behavior should be treated as dangerous.",
                                            "If a loved one appears ill, isolate them and await further instructions."
                                            )

                                    # Cartoons

                                        # Captain Plan It

                                           ("Captain Plan It", 3,
                                            "The Planeteers face their toughest foe yet: Big Oil!",
                                            "When diplomacy fails, they recycle his yacht out from under him.",
                                            "Captain Plan It reminds us: heroes don’t litter — they compost.",
                                            "Stay tuned for next week’s episode: ‘The Smogfather Returns!’"
                                            ),

                                           ("Star Trip: The Slightly Off Generation", 2,
                                            "Captain’s log: day... something.",
                                            "We have encountered a spatial anomaly that smells faintly of burnt toast.",
                                            "Science Officer Glax insists it’s safe. The walls disagree.",
                                            "I can’t tell if we’re exploring the stars or just running in circles."
                                            ),

                                           ("The Walking Fed", 3,
                                            "Chef Rick discovers the last can of tomato paste on Earth.",
                                            "He must defend it from a horde of food critics.",
                                            "‘They’re not after your brains, Carl — they’re after your seasoning!’",
                                            "Dinner... is served."
                                            ),

                                           ("Knight School", 3,
                                            "Sir Chadwick attempts to impress Lady Gwen by jousting blindfolded.",
                                            "Meanwhile, the squires accidentally glue their armor shut.",
                                            "The King calls it ‘a fine display of enthusiasm and poor judgment.’",
                                            "Tune in next week for ‘Catapults and Consequences!’"
                                            ),

                                           ("Law & Order: Paranormal Unit", 1,
                                            "In the ghost justice system, spectral crimes are investigated by two equally spooky detectives.",
                                            "Detective Wraith and Officer Ghoul arrive at another cold case — literally cold.",
                                            "‘Looks like this stiff’s been dead... twice.’",
                                            "Dun-dun."
                                            ),

                                           ("Totally Not Aliens!", 2,
                                            "We return to our hosts pretending to be human.",
                                            "Today, they try grocery shopping — an ordeal of strange customs and loud announcements.",
                                            "‘Observe how they hoard milk during minor weather events,’ one whispers.",
                                            "Suspicion grows as they accidentally buy 400 rolls of aluminum foil."
                                            ),

                                           ("History Blunders", 2,
                                            "On today’s episode: The Great Wall of China — and the Great Receipt of Regret.",
                                            "Emperor Qin’s accountant discovers the wall went over budget by... a lot.",
                                            "‘It’s fine,’ says Qin. ‘We’ll just call it a tourist attraction later.’",
                                            "History: written by the mildly embarrassed."
                                            ),

                                           ("Galaxy High Dropouts", 1,
                                            "Two alien teens skip warp school and crash-land on Earth.",
                                            "They try to blend in at a human high school by claiming to be exchange students from ‘Pluto High.’",
                                            "Trouble brews when their anti-gravity backpacks start floating the cafeteria.",
                                            "Episode ends with a detention that defies physics."
                                            ),

                                           ("Reality? Check.", 1,
                                            "Ten contestants compete to prove who’s the most ‘real.’",
                                            "The twist: none of them actually exist outside the show.",
                                            "‘Wait,’ says contestant four, ‘am I scripted?’",
                                            "Cue dramatic music and one very confused camera operator."
                                            ),

                                           ("Detective Pigeon", 2,
                                            "Coop City’s finest returns for another case.",
                                            "Someone’s stolen the mayor’s breadcrumbs — again.",
                                            "‘Smells like trouble,’ coos the detective, adjusting his tiny hat.",
                                            "Justice is served, lightly toasted."
                                            ),

                                        # The Bloc

                                            ("The Bloc", 1,
                                            "Welcome comrades, to *The Bloc!*",
                                            "In this exiting new 5 part season ten brave workers compete"
                                            " to renovate a glorious Soviet apartment complex.",
                                            "There is no prize — only contribution to the collective good.",
                                            "Today’s challenge: repurpose old propaganda posters into tasteful wallpaper!",
                                            "Remember, creativity is permitted, but only within the approved guidelines."
                                            ),

                                            ("The Bloc", 2,
                                            "Welcome back comrades, to *The Bloc!*",
                                            "Day two in the glorious renovation of Building 47.",
                                            "Team Iron Hammer struggles with plumbing — the pipes refuse to share water equally.",
                                            "Team Red Star’s paint supply mysteriously vanishes overnight. Coincidence? The Committee will decide.",
                                            "Inspector Boris arrives to remind everyone that beige is the color of progress.",
                                            "Tune in tomorrow, same time, same quota."
                                            ),

                                            ("The Bloc", 3,
                                            "Welcome back comrades, to *The Bloc!*",
                                            "Day three in the glorious renovation of Building 47.",
                                            "Comrades awaken to discover the power has been cut for realism.",
                                            "By candlelight, Team Unity constructs a bookshelf strong enough to hold *The Collected Works of Lenin.*",
                                            "Team Perseverance is accused of hoarding nails — a serious offense.",
                                            ),

                                            ("The Bloc", 4,
                                            "Welcome back comrades, to *The Bloc!*",
                                            "Day four in the glorious renovation of Building 47.",
                                            "Today, contestants must design a ‘communal relaxation zone’ using only bricks and optimism.",
                                            "Tensions rise when Team Vanguard paints their wall in *nonstandard red.*",
                                            "Boris conducts a surprise inspection with his clipboard of destiny.",
                                            "After eight hours of debate, everyone agrees the best design is whichever the state prefers."
                                            ),

                                            ("The Bloc", 5,
                                            "Welcome back comrades, to *The Bloc!*",
                                            "Final day of renovation, morale is high and safety is... questionable.",
                                            "Each team unveils their apartment to the Party judges.",
                                            "Scores are based on durability, efficiency, and adherence to revolutionary spirit.",
                                            "The winner will receive a certificate of commendation and an extra loaf of bread.",
                                            "The judges have decided on the winner. Lets hear the verdict."
                                            "All apartments are winners, because all belong to the people!"
                                            "Glory to the Union!"
                                            ),

                ]

                query = input("Turn on?\n 1. Yes\n 2. No")
                if query == "1":
                    ep = random.choice(tv_shows)
                    show_name = ep[0]
                    episode_number = ep[1]
                    lines = ep[2:]

                    print(f"\n--- Now Playing: {show_name} (Episode {episode_number}) ---\n")
                    for line in lines:
                        print(line)
                        time.sleep(1)                  

class area:

    class debras_house:

        characters = [character.debra.Debra()]
        objects = [object.debra.bed, object.debra.dining, object.debra.fridge, object.debra.kitchen, object.debra.window]
        description = "Its a small, one roomed house."
        name = "Debra's House"

#=========#
#  D E V  #
#=========#

class dev:

    def console():
        while True:
            ccr = input("~ ")

            if ccr == "placeholder":
                print("Placeholder")

            else:
                print("[ERROR] Unknown command.")

# Run dev console
titlescreen.menu(playing=False)
dev.console()
