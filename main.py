# Import Module
import tkinter
from tkinter import *
from PIL import Image, ImageTk
from pynput import keyboard

#-----------------------------------------------------------------------------
# Create Tkinter Object
root = Tk()
root.wm_attributes("-transparentcolor", "white")
root.wm_attributes("-topmost", True)
root.attributes("-alpha", 0.6)
root.overrideredirect(True)

title_bar = Frame(root, bg="grey", relief='raised', bd=0)
title_bar.pack(expand=1, fill=X)
title_label = Label(title_bar, text="Ferris Sweep GUI", bg="grey", fg="black")
title_label.pack(side=LEFT, pady=2)

# Create c;pse button on titlebar
def quitter(e):
    root.quit()
close_label = Label(title_bar, text=" X ", bg="black", fg="white")
close_label.pack(side=RIGHT, pady=2)
close_label.bind("<Button-1>", quitter)

# Bind the title bar
def move_app(e):
    root.geometry(f'+{e.x_root}+{e.y_root}')

title_bar.bind("<B1-Motion>", move_app)
# Read the Image
image = Image.open("ferris_sweep_gui.png")

# Resize the image using resize() method
x = 4
resize_image = image.resize((250*x, 100*x))

img = ImageTk.PhotoImage(resize_image)

# create label and add resize image

label1 = Label(image=img, bg="white")
#label1.image = img
label1.pack()

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    #if key == keyboard.Key.esc:
        # Stop listener
    #$    return False

listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()
#-----------------------------------------------------------------------------
#Key Binding - this should load a config file and load key bind from it.
"""
| kl1  | kl2  | kl3  | kl4  | kl5  |      | kp5  | kp4  | kp3  | kp2  | kp1  |
| kl6  | kl7  | kl8  | kl9  | kl10 |      | kp10 | kp9  | kp8  | kp7  | kp6  |
| kl11 | kl12 | kl13 | kl14 | kl15 |      | kp15 | kp14 | kp13 | kp12 | kp11 |
                     | kl16 | kl17 |      | kp17 | kp16 |
"""
kp_set = set()
kp_list = []
def search_str(file_path, word):
    with open(file_path, 'r') as file:
        content = file.read()
        index = content.find('keymap')
    while True:
        with open(file_path, 'r') as file:
            content = file.read()
            content_len = len(content)
            #print(f'Content length:{content_len}')
            index = content.find(word, index + len(word))
            start = index + len(word)
            #Need to find the end but it is not a single search. Sometimes in ZMK .config file there are tabs or new lines.
            end1 = content.find(' ', start)
            end2 = content.find('\n', start)
            end3 = content.find('\t', start)
            #We are intrested in the shortest string - because this will have the data we are looking for.
            lowest = [end1, end2, end3]
            end = min(lowest)

            print(end)
            #We want to check if the end is > than content_len because if we will not check it this will be an endless loop
            if end > content_len or index <0:
                break
            #We want to check if word is in content
            if word not in content:
                break
            #Want to make a set to know what type of keys are used in ZMK
            kp_set.add(content[start:end])
            if content[start:end] == 'kp':
                print('')
            elif content[start:end] == 'mt':
                print('')
            elif content[start:end] == 'to':
                print('')
            elif content[start:end] == 'trans':
                print('')
            elif content[start:end] == 'mmv':
                print('')
            elif content[start:end] == 'td':
                print('')
            elif content[start:end] == 'mkp':
                print('')
            elif content[start:end] == 'mwh':
                print('')
            elif content[start:end] == 'bt':
                print('')
            #print(content[start:end])
            #print(index)



search_str(r'cradio.txt', '&')

print(kp_set)
print(kp_list)
print(len(kp_list))

#-----------------------------------------------------------------------------


root.mainloop()
