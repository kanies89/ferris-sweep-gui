# Import Module
import tkinter
from tkinter import *
from PIL import Image, ImageTk
from pynput import keyboard

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
#            print(f'Content length:{content_len}')
            index = content.find(word, index + len(word))
            start = index + len(word)
            end = content.find(' ', start)
            if end > content_len or index <0:
                break
            if word not in content:
                break
            kp_set.add(content[start:end])
            kp_list.append(content[start:end])
#            print(content[start:end])
#            print(index)



search_str(r'cradio.txt', '&')

print(kp_set)
print(kp_list)
print(len(kp_list))

def search_str(file_path, word):
    with open(file_path, 'r') as file:
        # read all content of a file
        content = file.read()
        # check if string present in a file
        if word in content:
            print('string exist in a file')
        else:
            print('string does not exist in a file')

search_str(r'cradio.txt', '&kp')
root.mainloop()

"""
import tkinter as tk # Python 3
root = tk.Tk()
# The image must be stored to Tk or it will be garbage collected.
root.attributes("-alpha", 0.3)

root.image = tk.PhotoImage(file='ferris_sweep_gui.png')
label = tk.Label(root, image=root.image, bg="white",)
root.overrideredirect(True)
root.geometry("+250+100")
root.lift()
root.wm_attributes("-topmost", True)
root.wm_attributes("-disabled", True)
root.wm_attributes("-transparentcolor", "white")
label.pack()
label.mainloop()
"""