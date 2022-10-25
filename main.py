# Import Module
import tkinter
from tkinter import *
from PIL import Image, ImageTk
from pynput import keyboard
import math
from tkinter import ttk
import tkinter as tk

#-----------------------------------------------------------------------------
# Create Tkinter Object
root = Tk()
root.wm_attributes("-transparentcolor", "white")
root.wm_attributes("-topmost", True)
root.attributes("-alpha", 0.6)
root.overrideredirect(True)
root.configure(background='white')

title_bar = Frame(root, bg="grey", relief='raised', bd=0)
title_label = Label(title_bar, text="Ferris Sweep GUI", bg="grey", fg="black")


# Create c;pse button on titlebar
def quitter(e):
    root.quit()
close_label = Label(title_bar, text=" X ", bg="black", fg="white")

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
#label1.pack() - (delete # to show img)

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
each key is on layer - layer[0][...] according to below scheme
Layer = 0

| 0  | 1  | 2  | 3  | 4  |      | 5  | 6  | 7  | 8  | 9  |
| 10 | 11 | 12 | 13 | 14 |      | 15 | 16 | 17 | 18 | 19 |
| 20 | 21 | 22 | 23 | 24 |      | 25 | 26 | 27 | 28 | 29 |
               | 30 | 31 |      | 32 | 33 |
"""
key_dict = {
    'A': ['A', 'a'],
    'B': ['B', 'b'],
    'C': ['C', 'c'],
    'D': ['D', 'd'],
    'E': ['E', 'e'],
    'F': ['F', 'f'],
    'G': ['G', 'g'],
    'H': ['H', 'h'],
    'I': ['I', 'i'],
    'J': ['J', 'j'],
    'K': ['K', 'k'],
    'L': ['L', 'l'],
    'M': ['M', 'm'],
    'N': ['N', 'n'],
    'O': ['O', 'o'],
    'P': ['P', 'p'],
    'R': ['R', 'r'],
    'S': ['S', 's'],
    'T': ['T', 't'],
    'Q': ['Q', 'q'],
    'U': ['U', 'u'],
    'W': ['W', 'w'],
    'X': ['X', 'x'],
    'Y': ['Y', 'y'],
    'Z': ['Z', 'z'],
    'LALT': ['ALT', 'Key.alt_l'],
    'RALT': ['ALT', 'Key.alt_r'],
    'MINUS': ['-', '-'],
    'BKSP': ['<--', 'Key.backspace'],
    'LGUI': ['LWIN', 'Key.cmd'],
    'RGUI': ['RWIN', 'Key.menu'],
    'UNDERSCORE': ['_', '_'],
    'EXCL': ['!', '!'],
    'LC(LS(LALT))': ['', ''],
    'LSHIFT': ['SHIFT', 'Key.shift'],
    'ESC': ['ESC', 'Key.esc'],
    'ATSN': ['', ''],
    'LC(LG(LS(N4)))': ['have no clue', '<52>'],
    'DLLR': ['$', '$'],
    'PRCNT': ['%', '%'],
    'CARET': ['^', '^'],
    'LS(COMMA)': ['<', '<'],
    'LS(DOT)': ['>', '>'],
    'SEMI': [';', ';'],
    'TAB': ['TAB', 'Key.tab'],
    'EQUAL': ['=', '='],
    'LA(RBKT)': ['', ''], #??????????????????????????
    'LA(LS(RBKT))': ['', ''], #??????????????????????????
    'SQT': ["'", "'"],
    'BSLH': ['\\', '\\'],
    'LBRC': ['{', '{'],
    'RBRC': ['}', '}'],
    'PIPE': ['|', '|'],
    'ENTER': ['ENTER', 'Key.enter'],
    'TILDE': ['~', '~'],
    'LA(N3)': ['', ''], #??????????????????????????
    'LA(LBKT)': ['', ''], #??????????????????????????
    'LA(LS(LBKT))': ['', ''], #??????????????????????????
    'DQT': ['"', '"'],
    'LBKT': ['[', '['],
    'LPRN': ['(', '('],
    'RPRN': [')', ')'],
    'RBKT': [']', ']'],
    'CC_PP': ['', ''], #??????????????????????????
    'CC_PREV': ['', ''], #??????????????????????????
    'CC_NEXT': ['', ''], #??????????????????????????
    'LS(MINUS)': ['', ''], #??????????????????????????
    'N7': ['7', '7'],
    'N8': ['8', '8'],
    'N9': ['9', '9'],
    'C_VOL_DN': ['VOL-', 'Key.media_volume_down'],
    'C_VOL_UP': ['VOL+', 'Key.media_volume_up'],
    'LS(EQUAL)': ['+', '+'],
    'N4': ['4', '4'],
    'N5': ['5', '5'],
    'N6': ['6', '6'],
    'AMPS': ['&', '&'],
    'SLASH': ['/', '/'],
    'STAR': ['*', '*'],
    'N0': ['0', '0'],
    'N1': ['1', '1'],
    'N2': ['2', '2'],
    'N3': ['3', '3'],
    'SCROLL_LEFT': ['', ''], #??????????????????????????
    'SCROLL_RIGHT': ['', ''], #??????????????????????????
    'MOVE_UP': ['', ''], #??????????????????????????
    'NUM_5': ['', ''], #??????????????????????????
    'LG(LBKT)': ['', ''], #??????????????????????????
    'LC(LS(TAB))': ['', ''], #??????????????????????????
    'RC(TAB)': ['', ''], #??????????????????????????
    'LG(RBKT)': ['', ''], #??????????????????????????
    'F1': ['F1', 'Key.f1'],
    'MOVE_LEFT': ['', ''], #??????????????????????????
    'MOVE_DOWN': ['', ''], #??????????????????????????
    'MOVE_RIGHT': ['', ''], #??????????????????????????
    'DEL': ['DEL', 'Key.delete'],
    'LEFT': ['LEFT', 'Key.left'],
    'DOWN': ['DOWN', 'Key.down'],
    'UP': ['UP', 'Key.up'],
    'RIGHT': ['RIGHT', 'Key.right'],
    'LG(GRAVE)': ['', ''], #??????????????????????????
    'RCLK': ['', ''], #??????????????????????????
    'SCROLL_UP': ['', ''], #??????????????????????????
    'SCROLL_DOWN': ['', ''], #??????????????????????????
    'LCLK': ['', ''], #??????????????????????????
    'PG_DN': ['PAGE DN', 'Key.page_down'],
    'K_VOL_DN': ['', ''], #??????????????????????????
    'BT_PRV': ['', ''], #??????????????????????????
    'BT_NXT': ['', ''], #??????????????????????????
    'BT_CLR': ['', ''], #??????????????????????????
    '0': ['L_0', ''],
    '1': ['L_1', ''],
    '2': ['L_2', ''],
    '3': ['L_3', ''],
    '4': ['L_4', '']
}
kp_set = set()
kp_list = []
layer = list()
def findkey(start, file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        end1 = content.find(' ', start)
        end2 = content.find('\n', start)
        end3 = content.find('\t', start)
        if end1 < 0:
            lowest = [end2, end3]
        elif end2 < 0:
            lowest = [end1, end3]
        elif end3 < 0:
            lowest = [end1, end2]
        else:
            lowest = [end1, end2, end3]
        # We are intrested in the shortest string - because this will have the data we are looking for.

        print(lowest)
        end = min(lowest)
        return content[start:end]


def search_str(file_path, word):
    #Number of binded keys in ZMK config file
    i = 0
    keys_binded = 0

    #Start looking from keymap section of the ZMK config file
    with open(file_path, 'r') as file:
        content = file.read()
        index = content.find('keymap')
    #First need to know how many layers there are
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

            #print(end)
            #We want to check if the end is > than content_len because if we will not check it this will be an endless loop
            if end > content_len or index <0:
                break
            #We want to check if word is in content
            if word not in content:
                break
            #Want to make a set to know what type of keys are used in ZMK
            kp_set.add(content[start:end])
            kp_list.append(content[start:end])

    print(len(kp_list))
    layers_number = len(kp_list)/34
    print(layers_number)
    for n in range(0,int(layers_number)):
        layer.append([' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '])
    print(layer)
    print(layer[0][33])

    #Start looking from keymap section of the ZMK config file
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

            #print(end)
            #We want to check if the end is > than content_len because if we will not check it this will be an endless loop
            if end > content_len or index <0:
                break
            #We want to check if word is in content
            if word not in content:
                break
            #Want to make a set to know what type of keys are used in ZMK
            kp_set.add(content[start:end])

            if math.floor(keys_binded /34) > 4:
                break
            if content[start:end] == 'kp':
                #Want to know in which layer we are
                if i > 33:
                    i = 0
                    print(math.floor(keys_binded / 34), i)
                layer[math.floor(keys_binded / 34)][i] = findkey(end+1, r'cradio.txt')
            elif content[start:end] == 'mt':
                if i > 33:
                    i = 0
                    print(math.floor(keys_binded / 34), i)
                layer[math.floor(keys_binded / 34)][i] = findkey(end+1, r'cradio.txt')
            elif content[start:end] == 'to':
                if i > 33:
                    i = 0
                    print(math.floor(keys_binded / 34), i)
                layer[math.floor(keys_binded / 34)][i] = findkey(end+1, r'cradio.txt')
            elif content[start:end] == 'trans':
                if i > 33:
                    i = 0
                    print(math.floor(keys_binded / 34), i)
                layer[math.floor(keys_binded / 34)][i] = 'Empty'
            elif content[start:end] == 'mmv':
                if i > 33:
                    i = 0
                    print(math.floor(keys_binded / 34), i)
                layer[math.floor(keys_binded / 34)][i] = findkey(end+1, r'cradio.txt')
            elif content[start:end] == 'td':
                if i > 33:
                    i = 0
                    print(math.floor(keys_binded / 34), i)
                layer[math.floor(keys_binded / 34)][i] = findkey(end+1, r'cradio.txt')
            elif content[start:end] == 'mkp':
                if i > 33:
                    i = 0
                    print(math.floor(keys_binded / 34), i)
                layer[math.floor(keys_binded / 34)][i] = findkey(end + 1, r'cradio.txt')
            elif content[start:end] == 'mwh':
                if i > 33:
                    i = 0
                    print(math.floor(keys_binded / 34), i)
                layer[math.floor(keys_binded / 34)][i] = findkey(end+1, r'cradio.txt')
            elif content[start:end] == 'bt':
                if i > 33:
                    i = 0
                    print(math.floor(keys_binded / 34), i)
                layer[math.floor(keys_binded / 34)][i] = findkey(end+1, r'cradio.txt')
            elif content[start:end] == 'sk':
                if i > 33:
                    i = 0
                    print(math.floor(keys_binded / 34), i)
                layer[math.floor(keys_binded / 34)][i] = findkey(end+1, r'cradio.txt')
            elif content[start:end] == 'hm':
                if i > 33:
                    i = 0
                    print(math.floor(keys_binded / 34), i)
                layer[math.floor(keys_binded / 34)][i] = findkey(end+1, r'cradio.txt')
            print('Found {0} in place {1} and located it in layer[{2}][{3}]'.format(content[start:end], start, math.floor(keys_binded / 34), i))
            keys_binded += 1
            i += 1
            #print(content[start:end])
            #print(index)



search_str(r'cradio.txt', '&')

print(kp_set)
print(kp_list)
print(len(kp_list))
print(layer)


for i in range(0, 5):
    print("\n")
    for n in range (0, 33):
        print(layer[i][n])

#For the button keys on the grid we should know on which layer we are
active_layer=0
def callback(text, active_layer):
    print(text.get())
    if text.get() == "1":
        active_layer = 1
        print(f'Layer set to:{active_layer}')
        switch_button_name(active_layer)
    elif text.get() == "2":
        active_layer = 2
        print(f'Layer set to:{active_layer}')
        switch_button_name(active_layer)
    elif text.get() == "3":
        active_layer = 3
        print(f'Layer set to:{active_layer}')
        switch_button_name(active_layer)
    elif text.get() == "4":
        active_layer = 4
        print(f'Layer set to:{active_layer}')
        switch_button_name(active_layer)
    elif text.get() == "0":
        active_layer = 0
        print(f'Layer set to:{active_layer}')
        switch_button_name(active_layer)

#Function to switch button names
b_text = []

for i in range(0, 34):
    b_text.append(tk.StringVar())

def switch_button_name(layer_number):
    for i in range(0, 34):
        b_text[i].set(layer[layer_number][i])
        print('Setting button {0} to {1} while layer {2} is active'.format('B%s' % i, b_text[i].get(), layer_number))
        globals()['B%s' % i].configure(text=b_text[i])
        print(b_text[i].get())

#Here grid of the Ferris Sweep keyboard grid is made

B0 = ttk.Button(root, textvariable=b_text[0], command=lambda: callback(b_text[0], active_layer))
B1 = ttk.Button(root, textvariable=b_text[1], command=lambda: callback(b_text[1], active_layer))
B2 = ttk.Button(root, textvariable=b_text[2], command=lambda: callback(b_text[2], active_layer))
B3 = ttk.Button(root, textvariable=b_text[3], command=lambda: callback(b_text[3], active_layer))
B4 = ttk.Button(root, textvariable=b_text[4], command=lambda: callback(b_text[4], active_layer))
B5 = ttk.Button(root, textvariable=b_text[5], command=lambda: callback(b_text[5], active_layer))
B6 = ttk.Button(root, textvariable=b_text[6], command=lambda: callback(b_text[6], active_layer))
B7 = ttk.Button(root, textvariable=b_text[7], command=lambda: callback(b_text[7], active_layer))
B8 = ttk.Button(root, textvariable=b_text[8], command=lambda: callback(b_text[8], active_layer))
B9 = ttk.Button(root, textvariable=b_text[9], command=lambda: callback(b_text[9], active_layer))
B10 = ttk.Button(root, textvariable=b_text[10], command=lambda: callback(b_text[10], active_layer))
B11 = ttk.Button(root, textvariable=b_text[11], command=lambda: callback(b_text[11], active_layer))
B12 = ttk.Button(root, textvariable=b_text[12], command=lambda: callback(b_text[12], active_layer))
B13 = ttk.Button(root, textvariable=b_text[13], command=lambda: callback(b_text[13], active_layer))
B14 = ttk.Button(root, textvariable=b_text[14], command=lambda: callback(b_text[14], active_layer))
B15 = ttk.Button(root, textvariable=b_text[15], command=lambda: callback(b_text[15], active_layer))
B16 = ttk.Button(root, textvariable=b_text[16], command=lambda: callback(b_text[16], active_layer))
B17 = ttk.Button(root, textvariable=b_text[17], command=lambda: callback(b_text[17], active_layer))
B18 = ttk.Button(root, textvariable=b_text[18], command=lambda: callback(b_text[18], active_layer))
B19 = ttk.Button(root, textvariable=b_text[19], command=lambda: callback(b_text[19], active_layer))
B20 = ttk.Button(root, textvariable=b_text[20], command=lambda: callback(b_text[20], active_layer))
B21 = ttk.Button(root, textvariable=b_text[21], command=lambda: callback(b_text[21], active_layer))
B22 = ttk.Button(root, textvariable=b_text[22], command=lambda: callback(b_text[22], active_layer))
B23 = ttk.Button(root, textvariable=b_text[23], command=lambda: callback(b_text[23], active_layer))
B24 = ttk.Button(root, textvariable=b_text[24], command=lambda: callback(b_text[24], active_layer))
B25 = ttk.Button(root, textvariable=b_text[25], command=lambda: callback(b_text[25], active_layer))
B26 = ttk.Button(root, textvariable=b_text[26], command=lambda: callback(b_text[26], active_layer))
B27 = ttk.Button(root, textvariable=b_text[27], command=lambda: callback(b_text[27], active_layer))
B28 = ttk.Button(root, textvariable=b_text[28], command=lambda: callback(b_text[28], active_layer))
B29 = ttk.Button(root, textvariable=b_text[29], command=lambda: callback(b_text[29], active_layer))
B30 = ttk.Button(root, textvariable=b_text[30], command=lambda: callback(b_text[30], active_layer))
B31 = ttk.Button(root, textvariable=b_text[31], command=lambda: callback(b_text[31], active_layer))
B32 = ttk.Button(root, textvariable=b_text[32], command=lambda: callback(b_text[32], active_layer))
B33 = ttk.Button(root, textvariable=b_text[33], command=lambda: callback(b_text[33], active_layer))
#11 columns

switch_button_name(active_layer)

empty_label1 = Label(root, text="                  ", bg="white")
empty_label2 = Label(root, text="                  ", bg="white")
empty_label3 = Label(root, text="                  ", bg="white")
empty_label4 = Label(root, text="                  ", bg="white")


title_bar.grid(column=0, row=0, columnspan=11, sticky=N+E+S+W)
title_label.grid(column=0, row=0, columnspan=11, sticky=N+E+S+W)
close_label.grid(column=10, row=0)

B0.grid(column=0, row = 1, padx=5, pady=5)
B1.grid(column=1, row = 1, padx=5, pady=5)
B2.grid(column=2, row = 1, padx=5, pady=5)
B3.grid(column=3, row = 1, padx=5, pady=5)
B4.grid(column=4, row = 1, padx=5, pady=5)
empty_label1.grid(column=5, row=1)
B5.grid(column=6, row = 1, padx=5, pady=5)
B6.grid(column=7, row = 1, padx=5, pady=5)
B7.grid(column=8, row = 1, padx=5, pady=5)
B8.grid(column=9, row = 1, padx=5, pady=5)
B9.grid(column=10, row = 1, padx=5, pady=5)
B10.grid(column=0, row = 2, padx=5, pady=5)
B11.grid(column=1, row = 2, padx=5, pady=5)
B12.grid(column=2, row = 2, padx=5, pady=5)
B13.grid(column=3, row = 2, padx=5, pady=5)
B14.grid(column=4, row = 2, padx=5, pady=5)
empty_label2.grid(column=5, row=2)
B15.grid(column=6, row = 2, padx=5, pady=5)
B16.grid(column=7, row = 2, padx=5, pady=5)
B17.grid(column=8, row = 2, padx=5, pady=5)
B18.grid(column=9, row = 2, padx=5, pady=5)
B19.grid(column=10, row = 2, padx=5, pady=5)
B20.grid(column=0, row = 3, padx=5, pady=5)
B21.grid(column=1, row = 3, padx=5, pady=5)
B22.grid(column=2, row = 3, padx=5, pady=5)
B23.grid(column=3, row = 3, padx=5, pady=5)
B24.grid(column=4, row = 3, padx=5, pady=5)
empty_label3.grid(column=5, row=3)
B25.grid(column=6, row = 3, padx=5, pady=5)
B26.grid(column=7, row = 3, padx=5, pady=5)
B27.grid(column=8, row = 3, padx=5, pady=5)
B28.grid(column=9, row = 3, padx=5, pady=5)
B29.grid(column=10, row = 3, padx=5, pady=5)
B30.grid(column=3, row = 4, padx=5, pady=5)
B31.grid(column=4, row = 4, padx=5, pady=5)
empty_label4.grid(column=5, row=4)
B32.grid(column=6, row = 4, padx=5, pady=5)
B33.grid(column=7, row = 4, padx=5, pady=5)
#-----------------------------------------------------------------------------


root.mainloop()
