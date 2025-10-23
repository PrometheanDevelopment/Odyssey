# MIT License
# Copyright (c) 2025 PrometheanDevelopment
# See LICENSE file: https://github.com/PrometheanDevelopment/Odyssey/blob/main/LICENSE

import random
import os
import time
import sys
import builtins
import tkinter as tk
from tkinter import scrolledtext

# ----------------------
# Tkinter GUI - universal print/input replacements
# ----------------------

# Create main window
root = tk.Tk()
root.title("Odyssey (GUI)")
root.geometry("900x600")

# Output text area (scrollable)
output_text = scrolledtext.ScrolledText(root, wrap='word', font=("Courier New", 11))
output_text.pack(fill='both', expand=True, padx=6, pady=6)

# Input frame
input_frame = tk.Frame(root)
input_frame.pack(fill='x', padx=6, pady=(0,6))

input_var = tk.StringVar(value="")  # used to transfer input to waiting calls

entry = tk.Entry(input_frame, textvariable=input_var)
entry.pack(side='left', fill='x', expand=True, padx=(0,6))
entry.focus_set()

def on_enter_click(event=None):

    # set a sentinel variable used by gui_input to continue
    val = entry.get()
    input_var.set(val)

# Enter button
enter_btn = tk.Button(input_frame, text="Enter", command=on_enter_click)
enter_btn.pack(side='right')

# Ensure pressing Return triggers enter
entry.bind('<Return>', on_enter_click)

# Keep a reference to the current printed text count for auto-scroll if needed
def gui_print(*args, sep=' ', end='\n', flush=False):
    
    text = sep.join(str(a) for a in args) + end
    output_text.insert('end', text)
    output_text.see('end')
    
    try:
        output_text.update_idletasks()
    except Exception:
        pass

def gui_clear():
    
    output_text.delete('1.0', 'end')
    output_text.update_idletasks()

def gui_input(prompt=''):

    # Show prompt
    if prompt:
        # Show prompt on its own line (matching typical console behaviour)
        gui_print(prompt, end='')
    # clear any previous sentinel
    input_var.set('')
    # focus entry so keyboard is active
    entry.focus_set()
    # wait for user to set input_var via on_enter_click
    root.wait_variable(input_var)
    val = input_var.get()
    # after reading copy the user's input to the output for context (like terminal echo)
    gui_print(val)
    # clear the entry field
    entry.delete(0, 'end')
    input_var.set('')
    return val

# Monkeypatch builtins so existing code that calls print() / input() will use GUI
builtins.print = gui_print
builtins.input = gui_input

_real_os_system = os.system
def _os_system_replacement(cmd):
    if isinstance(cmd, str) and cmd.lower() in ('cls', 'clear'):
        gui_clear()
        return 0
    return _real_os_system(cmd)

os.system = _os_system_replacement

# ----------------------
# Original game code follows (unaltered except for the benefit of GUI)
# ----------------------

# Pre-set variables
inventory = []
object_num = 0

class debug:

    def clearscreen():
        # previously: os.system('cls')
        # now it will call the os.system wrapper or directly gui_clear
        try:
            os.system('cls')
        except Exception:
            gui_clear()

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
            print("    .--~~--.    ...----~~~~~~------.........------~~~~~~----...     .--~~--.    ")
            print("   |       |   |      ___      _                               |   |       |    ")
            print("   |       `---'     / _ \  __| |_   _ ___ ___  ___ _   _      `---'       |    ")
            print("   |       |   |    | | | |/ _` | | | / __/ __|/ _ \ | | |     |   |       |    ")
            print("   |       |   |    | |_| | (_| | |_| \__ \__ \  __/ |_| |     |   |       |    ")
            print("   |       |   |     \___/ \__,_|\__, |___/___/\___|\__, |     |   |       |    ")
            print("   |       |   |                 |___/              |___/      |   |       |    ")
            print("   |.--~~--|   |...----~~~~~~------.........------~~~~~~----...|   |--~~--.|    ")
            print("           '._.`                                               '._.`            ")
            print("                    |--__                                                  .--. ")
            print("                    |                                                 _ .-'__   ")
            print("                    X                        -.- _ _             ,--.( (    )   ")
            print("           |-___   / \       |-__-                `          _,-(       (       ")
            print("           |      ~~~~~      |                              (_________(_______)_")
            print("         ~~~~~   |:  . |   ~~~~~--..__   --~~~-     ~~     --   ~--    _/]_\_   ")
            print("         |:O |__|  .O ::|__| O |       ``-..__   --~~-  ~   -~   ~~~~  '~~~~~^~~")
            print("         |  :|  |O.  ..O|  |:  |            ```--.._   ~~     ~~-      ~~--~    ")
            print("         |:  | .| . _   | :|  .|                    ```--..__      ~~~-     ~  ~")
            print("         |.. | :|: |_|::|__|:. |                             ``-..__     --~~   ")
            print("                   :::                                              ```---.___ ~")
            print("                   .:                                                         `-")
            query = input(" Select: ")

            if query == "start":
                debug.clearscreen()
                playing = True

            elif query == "quit":
                debug.clearscreen()
                time.sleep(1)
                try:
                    root.destroy()
                except Exception:
                    pass
                sys.exit()

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
                                            "If a loved one appears ill, isolate them and await further instructions.",
                                            ),

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
                                            "I can’t tell if we’re exploring the stars or just running in circles"
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

    #===============================================#
    # L I B R A R Y  O F  T R A N S C E N D E N C E #
    #===============================================#

    class arcane_university:
       
       class alchemy_labs:
           
           class periodic_table:
                visual = True
                object_name = "Periodic Table of Elements"
                inspect = "Its a table of the 118 known elements."
                def interact():
                        debug.clearscreen()
                        print(" __________________________________________________________________________ \n")
                        print("|  H                                                                   He  |\n")
                        print("|                                                                          |\n")
                        print("|  Li  Be                                          B   C   N   O   F   Ne  |\n")
                        print("|                                                                          |\n")
                        print("|  Na  Mg                                          Al  Si  P   S   Cl  Ar  |\n")
                        print("|                                                                          |\n")
                        print("|  K   Ca  Sc  Ti  V   Cr  Mn  Fe  Co  Ni  Cu  Zn  Ga  Ge  As  Se  Br  Kr  |\n")
                        print("|                                                                          |\n")
                        print("|  Rb  Sr  Y   Zr  Nb  Mo  Tc  Ru  Rh  Pd  Ag  Cd  In  Sn  Sb  Te  I   Xe  |\n")
                        print("|                                                                          |\n")
                        print("|  Cs  Ba  *   Hf  Ta  W   Re  Os  Ir  Pt  Au  Hg  Tl  Pb  Bi  Po  At  Rn  |\n")
                        print("|                                                                          |\n")
                        print("|  Fr  Ra  **  Rf  Db  Sg  Bh  Hs  Mt  Ds  Rg  Cn  Nh  Fl  Mc  Lv  Ts  Og  |\n")
                        print("|__________________________________________________________________________|\n")
                        print("|                                                                          |\n")
                        print("| Lantanoidi*   La  Ce  Pr  Nd  Pm  Sm  Eu  Gd  Tb  Dy  Ho  Er  Tm  Yb  Lu |\n")
                        print("|                                                                          |\n")
                        print("|  Aktinoidi**  Ac  Th  Pa  U   Np  Pu  Am  Cm  Bk  Cf  Es  Fm  Md  No  Lr |\n")
                        print("|__________________________________________________________________________|\n")
                        input("\n                      === PRESS ENTER TO EXIT ===")

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
                   inspect = 'To the left of the entrance, there is a brass, steampunk vending machine. It has a warning sign taped to the front: "WARNING: Eat items at own risk."'
                   def interact():
                       interact = input("Use machine?\n 1. Yes\n 2. No\n\nSelect: ")
                       vending_item = None
                       if interact == "1":
                           vending_item = random.choice([items.consumable.food.items])
                           inventory.append(vending_item)

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
                    self.action = random.choice([
                        "She glances up from her book and stares at you.", "She is busy writing in a large tome.", 
                        "She places a finger to her lips, signalling quiet."
                    ])

                def speech(self):
                    print(random.choice[
                        "Yes?", "How can I help you?", "Good day.", "Go ahead, please.", "Greetings to you."
                    ])
                    (" 1. Rumors")
                    (" 2. Return a book")
                    (" 3. ")
                    input("Ask: ")

            class Galadriel:

                def __init__(self):
                    self.name = "Galadriel"

                    rare_line = random.randint(1,100)
                    if rare_line == 100:
                        self.speech = '"Get away, "'
                    else:
                        self.speech = random.choice([
                            '"If you\'re here to save the world, I suggest starting by not blowing it up."', 
                            '"You’re still standing here. Is it bravery, or the inability to take a hint?"'
                        ])
                    self.action = random.choice([
                        "She is staring at the cover of a gilded book, but not openning it.", "Shes holding a fireball.",
                        "She is glaring at a palm-leaf scroll.", "Shes brooding."
                    ])

    class dungeon:

        class dungeon_name:

            class Bob:

                def __init__(self):
                    self.name = "Bob the Destroyer"                      
                    self.action = random.choice([
                        
                    ])

                def speech(self):
                    print(
                        "MERE MORTAL! DO YOU SEEK THE TRESURES OF MINE?"
                    )
                    ("1. The man outside told us there was icecream in here.")
                    ("2. What treasures exactly do you have?")
                    ("3. ")
                    talk = input("Ask: ")
                    if talk == "1":
                        print("Oh yes! Right over there! Now go get yourself a scoop or two, you cheeky devil!")
                    elif talk == "2":
                        print("Oh, you know, gems, coins, gold, miscellaneous treasures, the sorts.")
                        print("")

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
                    print(f"{i + 1}: {item[0]} - (Damage: {item[2]})")
                elif item in items.consumable.food.debras_items or items.consumable.food.items:
                    if item[0] == "Mysterious Soup":
                        print(f"{i + 1}: {item[0]} - (Heals: ???)")
                    else:
                        print(f"{i + 1}: {item[0]} - (Heals: {item[2]})")
                else:
                    print(f"{i + 1}: {item[0]}")

        def items():
            query = input("\nSelect: ")

            if query == "help":
                debug.clearscreen()
                print("COMMANDS:")
                print(" - help: displays commands")
                print(" - equip: equips a selected item (equip [item number])")
                print(" - inspect: gives description of a selected item ('inspect, (next line [item number])')")
                input("\n                      === PRESS ENTER TO EXIT ===")
                player.inventory.view()

            elif query == "equip":
                pass

            elif query == "inspect":
                query = int(input("\nSelect: "))
                for i, item in enumerate(inventory):
                    if query == i:
                        debug.clearscreen()
                        print(f"{item[0]}:")
                        print(f"\n{item[1]}")

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
        
    #class attack():
        #damage = random.choice(0, player.inventory.equipped_weapon[3] * (random.randint(0.5, 1.5)))

class area:

    class debras_house:

        characters = [character.debra.Debra()]
        objects = [object.debra.bed, object.debra.dining, object.debra.fridge, object.debra.kitchen, object.debra.window]
        description = "Its a small, one roomed house."
        name = "Debra's House"

    class arcane_university:

        class library_of_transcendence:

            class shelves:
        
                characters = []
                objects = [object.arcane_university.library_of_transcendence.shelves]
                description = "It is an endless library of arcane knowledge."
                name = "Library of Transcendence: Shelves"

            class reading_room:

                characters = []
                objects = [object.arcane_university.library_of_transcendence.reading_room]
                description = "It is an endless library of arcane knowledge."
                name = "Library of Transcendence: Reading room"

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

# Ensure debug.clearscreen uses GUI clear function explicitly (in case os.system wrapper missed something)
debug.clearscreen = staticmethod(lambda: gui_clear())

# Start with the titlescreen menu
try:
    titlescreen.menu(playing=False)
except SystemExit:
    # user chose to quit
    try:
        root.destroy()
    except Exception:
        pass
    sys.exit()

# Launch dev console (this will block running under the GUI but uses gui_input so it's fine)
try:
    dev.console()
except SystemExit:
    try:
        root.destroy()
    except Exception:
        pass
    sys.exit()

try:
    if root.winfo_exists():
        root.mainloop()
except Exception:
    pass
