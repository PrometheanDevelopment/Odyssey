
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
        print("Program exited")
    except Exception:
        pass
    sys.exit()

# Launch dev console (this will block running under the GUI but uses gui_input so it's fine)
try:
    print("Running Successfully")

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
