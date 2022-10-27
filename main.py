# Import Module
import tkinter
from tkinter import *
from PIL import Image, ImageTk
from pynput import keyboard
import math
from tkinter import ttk
import tkinter as tk
from time import sleep

#-----------------------------------------------------------------------------
# Create Tkinter Object
root = Tk()
root.wm_attributes("-transparentcolor", "black")
root.wm_attributes("-topmost", True)
root.attributes("-alpha", 0.6)
root.overrideredirect(True)
root.configure(background='black')

# Create clpse button and titlebar
def quitter(e):
    root.quit()
def move_app(e):
    root.geometry(f'+{e.x_root}+{e.y_root}')

title_bar = Frame(root, bg="grey", relief='raised', bd=0)
title_label = Label(title_bar, text="Ferris Sweep GUI", bg="grey", fg="orange")
close_label = Label(root, text=" X ", bg="orange", fg="black")
close_label.bind("<Button-1>", quitter)
title_bar.bind("<B1-Motion>", move_app)

# Read the Image
image = Image.open("ferris_sweep_gui.png")

# Resize the image using resize() method
x = 4
resize_image = image.resize((250*x, 100*x))

img = ImageTk.PhotoImage(resize_image)

# create label and add resize image

label1 = Label(image=img, bg="black")
#label1.image = img
#label1.pack() - (delete # to show img)

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
#Key dictionary - FROM ZMK to label of the button or to listener key
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
    'V': ['V', 'v'],
    'Y': ['Y', 'y'],
    'Z': ['Z', 'z'],
    'LALT': ['ALT', 'Key.alt_l'],
    'RALT': ['RALT', 'Key.alt_r'],
    'MINUS': ['-', '-'],
    'BKSP': ['<--', 'Key.backspace'],
    'LGUI': ['LWIN', 'Key.cmd'],
    'RGUI': ['RWIN', 'Key.menu'],
    'UNDERSCORE': ['_', '_'],
    'EXCL': ['!', '!'],
    'LC(LS(LALT))': ['LC(LS(LALT))', ''],
    'LSHIFT': ['SHIFT', 'Key.shift'],
    'ESC': ['ESC', 'Key.esc'],
    'ATSN': ['@', '@'],
    'LC(LG(LS(N4)))': ['#', '#'],
    'DLLR': ['$', '$'],
    'PRCNT': ['%', '%'],
    'CARET': ['^', '^'],
    'LS(COMMA)': ['<', '<'],
    'LS(DOT)': ['>', '>'],
    'SEMI': [';', ';'],
    'SPC': ['˽ꟷ', 'Key.space'],
    'TAB': ['TAB', 'Key.tab'],
    'EQUAL': ['=', '='],
    'LA(RBKT)': ['LA(RBKT', ''], #??????????????????????????
    'LA(LS(RBKT))': ['LA(LS(RBKT))', ''], #??????????????????????????
    'SQT': ["'", "'"],
    'BSLH': ['\\', '\\'],
    'LBRC': ['{', '{'],
    'RBRC': ['}', '}'],
    'PIPE': ['|', '|'],
    'ENTER': ['ENTER', 'Key.enter'],
    'TILDE': ['~', '~'],
    'LA(N3)': ['LA(N3)', ''], #??????????????????????????
    'LA(LBKT)': ['LA(LBKT)', ''], #??????????????????????????
    'LA(LS(LBKT))': ['LA(LS(LBKT))', ''], #??????????????????????????
    'DQT': ['"', '"'],
    'LBKT': ['[', '['],
    'LPRN': ['(', '('],
    'RPRN': [')', ')'],
    'RBKT': [']', ']'],
    'C_PP': ['C_PP', ''], #??????????????????????????
    'C_PREV': ['CC_PREV', ''], #??????????????????????????
    'C_NEXT': ['CC_NEXT', ''], #??????????????????????????
    'LS(MINUS)': ['LS(MINUS)', ''], #??????????????????????????
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
    'SCROLL_LEFT': ['SCR_L', ''], #??????????????????????????
    'SCROLL_RIGHT': ['SCR_R', ''], #??????????????????????????
    'MOVE_UP': ['M_UP', ''], #??????????????????????????
    'NUM_5': ['NUM_5', ''], #??????????????????????????
    'LG(LBKT)': ['LG(LBKT)', ''], #??????????????????????????
    'LC(LS(TAB))': ['LC(LS(TAB))', ''], #??????????????????????????
    'RC(TAB)': ['RC(TAB)', ''], #??????????????????????????
    'LG(RBKT)': ['LG(RBKT)', ''], #??????????????????????????
    'F1': ['F1', 'Key.f1'],
    'MOVE_LEFT': ['M_L', ''], #??????????????????????????
    'MOVE_DOWN': ['M_D', ''], #??????????????????????????
    'MOVE_RIGHT': ['M_R', ''], #??????????????????????????
    'DEL': ['DEL', 'Key.delete'],
    'LEFT': ['LEFT', 'Key.left'],
    'DOWN': ['DOWN', 'Key.down'],
    'UP': ['UP', 'Key.up'],
    'RIGHT': ['RIGHT', 'Key.right'],
    'LG(GRAVE)': ['LG(GRAVE)', ''], #??????????????????????????
    'RCLK': ['RCLK', ''], #??????????????????????????
    'SCROLL_UP': ['SCR_UP', ''], #??????????????????????????
    'SCROLL_DOWN': ['SCR_DN', ''], #??????????????????????????
    'LCLK': ['LCLK', ''], #??????????????????????????
    'PG_DN': ['PAGE DN', 'Key.page_down'],
    'K_VOL_DN': ['', ''], #??????????????????????????
    'BT_PRV': ['BT_PRV', ''], #??????????????????????????
    'BT_NXT': ['BT_NXT', ''], #??????????????????????????
    'BT_CLR': ['BR_CLR', ''], #??????????????????????????
    'RCTRL': ['RCTRL', ''],  #??????????????????????????
    'DOT': ['DOT', ''],
    '0': ['L-0', ''],
    '1': ['L-1', ''],
    '2': ['L-2', ''],
    '3': ['L-3', ''],
    '4': ['L-4', ''],
    'Empty': ['', '']
}

kp_set = set()
kp_list = []
layer = list()

def findkey(start, file_path, type):
    with open(file_path, 'r') as file:
        #mh keys take two values. When pressed for ex. 200ms it switches to first value.
        if type == 'hm':
            hm = ['', '']
            i = len(hm) -1
            c_read = False
            for value in hm:
                if(c_read == False):
                    content = file.read()
                    c_read = True
                end1 = content.find(' ', start)
                end2 = content.find('\n', start)
                end3 = content.find('\t', start)
                print(end1)
                print(end1)
                print(end1)
                lowest = []
                if end1 > 0:
                    lowest.append(end1)
                if end2 > 0:
                    lowest.append(end2)
                if end3 > 0:
                    lowest.append(end3)
                end = min(lowest)
                hm[i] = content[start:end]
                start = end + 1
                print(start)
                i -= 1

            print('HM key found. Values assigned: {0}'.format(hm))
            return hm
            c_read = False
        else:
            content = file.read()
            end1 = content.find(' ', start)
            end2 = content.find('\n', start)
            end3 = content.find('\t', start)
            lowest = []
            if end1 > 0:
                lowest.append(end1)
            if end2 > 0:
                lowest.append(end2)
            if end3 > 0:
                lowest.append(end3)
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
                layer[math.floor(keys_binded / 34)][i] = findkey(end+1, r'cradio.txt', 'kp')
            elif content[start:end] == 'mt':
                if i > 33:
                    i = 0
                    print(math.floor(keys_binded / 34), i)
                layer[math.floor(keys_binded / 34)][i] = findkey(end+1, r'cradio.txt', 'mt')
            elif content[start:end] == 'to':
                if i > 33:
                    i = 0
                    print(math.floor(keys_binded / 34), i)
                layer[math.floor(keys_binded / 34)][i] = findkey(end+1, r'cradio.txt', 'to')
            elif content[start:end] == 'trans':
                if i > 33:
                    i = 0
                    print(math.floor(keys_binded / 34), i)
                layer[math.floor(keys_binded / 34)][i] = 'Empty'
            elif content[start:end] == 'mmv':
                if i > 33:
                    i = 0
                    print(math.floor(keys_binded / 34), i)
                layer[math.floor(keys_binded / 34)][i] = findkey(end+1, r'cradio.txt', 'mmw')
            elif content[start:end] == 'td':
                if i > 33:
                    i = 0
                    print(math.floor(keys_binded / 34), i)
                layer[math.floor(keys_binded / 34)][i] = findkey(end+1, r'cradio.txt', 'td')
            elif content[start:end] == 'mkp':
                if i > 33:
                    i = 0
                    print(math.floor(keys_binded / 34), i)
                layer[math.floor(keys_binded / 34)][i] = findkey(end + 1, r'cradio.txt', 'mkp')
            elif content[start:end] == 'mwh':
                if i > 33:
                    i = 0
                    print(math.floor(keys_binded / 34), i)
                layer[math.floor(keys_binded / 34)][i] = findkey(end+1, r'cradio.txt', 'mwh')
            elif content[start:end] == 'bt':
                if i > 33:
                    i = 0
                    print(math.floor(keys_binded / 34), i)
                layer[math.floor(keys_binded / 34)][i] = findkey(end+1, r'cradio.txt', 'bt')
            elif content[start:end] == 'sk':
                if i > 33:
                    i = 0
                    print(math.floor(keys_binded / 34), i)
                layer[math.floor(keys_binded / 34)][i] = findkey(end+1, r'cradio.txt', 'sk')
            elif content[start:end] == 'hm':
                if i > 33:
                    i = 0
                    print(math.floor(keys_binded / 34), i)
                layer[math.floor(keys_binded / 34)][i] = findkey(end+1, r'cradio.txt', 'hm')
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
    if text.get() == "L-1":
        active_layer = 1
        print(f'Layer set to:{active_layer}')
        switch_button_name(active_layer)
    elif text.get() == "L-2":
        active_layer = 2
        print(f'Layer set to:{active_layer}')
        switch_button_name(active_layer)
    elif text.get() == "L-3":
        active_layer = 3
        print(f'Layer set to:{active_layer}')
        switch_button_name(active_layer)
    elif text.get() == "L-4":
        active_layer = 4
        print(f'Layer set to:{active_layer}')
        switch_button_name(active_layer)
    elif text.get() == "L-0":
        active_layer = 0
        print(f'Layer set to:{active_layer}')
        switch_button_name(active_layer)

#List of button textvariable
b_text = []
#List of Listener key added to button
b_listener_key = []

for i in range(0, 34):
    b_text.append(tk.StringVar())
    b_listener_key.append('')
#Function to switch button names
def switch_button_name(layer_number):
    for i in range(0, 34):
        #need to check if button is double value, ex. "hm" or "mt". If it is than we should search the dictionary by the values of the list
        if isinstance(layer[layer_number][i],  list):
            count = len(layer[layer_number][i])
            key_name = ''

            for j in range(0, count):
                key_name = key_name + ' ' + key_dict[f'{layer[layer_number][i][j]}'][0]

            b_text[i].set(key_name)

            print('Setting button {0} to {1} while layer {2} is active'.format('B%s' % i, b_text[i].get(), layer_number))
            globals()['B%s' % i].configure(text=b_text[i])
            print(b_text[i].get())
            b_listener_key[i] = key_dict[f'{layer[layer_number][i][0]}'][1]
            print(b_listener_key[i])
        else:
            b_text[i].set(key_dict[f'{layer[layer_number][i]}'][0])
            print('Setting button {0} to {1} while layer {2} is active'.format('B%s' % i, b_text[i].get(), layer_number))
            globals()['B%s' % i].configure(text=b_text[i])
            print(b_text[i].get())
            b_listener_key[i] = key_dict[f'{layer[layer_number][i]}'][1]
            print(b_listener_key[i])

#Here grid of the Ferris Sweep keyboard grid is made
button_bg = "black"
button_fg = "orange"
button_font = 'sans 10 bold'
button_w = 8
button_h = 4


B0 = tk.Button(root, textvariable=b_text[0], bg=button_bg, width=button_w, height=button_h, fg=button_fg,  font=button_font, command=lambda: [callback(b_text[0], active_layer), print('Button 0 is p')])
B1 = tk.Button(root, textvariable=b_text[1], bg=button_bg, width=button_w, height=button_h, fg=button_fg,  font=button_font, command=lambda: callback(b_text[1], active_layer))
B2 = tk.Button(root, textvariable=b_text[2], bg=button_bg, width=button_w, height=button_h, fg=button_fg,  font=button_font, command=lambda: callback(b_text[2], active_layer))
B3 = tk.Button(root, textvariable=b_text[3], bg=button_bg, width=button_w, height=button_h, fg=button_fg,  font=button_font, command=lambda: callback(b_text[3], active_layer))
B4 = tk.Button(root, textvariable=b_text[4], bg=button_bg, width=button_w, height=button_h, fg=button_fg,  font=button_font, command=lambda: callback(b_text[4], active_layer))
B5 = tk.Button(root, textvariable=b_text[5], bg=button_bg, width=button_w, height=button_h, fg=button_fg,  font=button_font, command=lambda: callback(b_text[5], active_layer))
B6 = tk.Button(root, textvariable=b_text[6], bg=button_bg, width=button_w, height=button_h, fg=button_fg,  font=button_font, command=lambda: callback(b_text[6], active_layer))
B7 = tk.Button(root, textvariable=b_text[7], bg=button_bg, width=button_w, height=button_h, fg=button_fg,  font=button_font, command=lambda: callback(b_text[7], active_layer))
B8 = tk.Button(root, textvariable=b_text[8], bg=button_bg, width=button_w, height=button_h, fg=button_fg,  font=button_font, command=lambda: callback(b_text[8], active_layer))
B9 = tk.Button(root, textvariable=b_text[9], bg=button_bg, width=button_w, height=button_h, fg=button_fg,  font=button_font, command=lambda: callback(b_text[9], active_layer))
B10 = tk.Button(root, textvariable=b_text[10], bg=button_bg, width=button_w, height=button_h, fg=button_fg,  font=button_font, command=lambda: callback(b_text[10], active_layer))
B11 = tk.Button(root, textvariable=b_text[11], bg=button_bg, width=button_w, height=button_h, fg=button_fg,  font=button_font, command=lambda: callback(b_text[11], active_layer))
B12 = tk.Button(root, textvariable=b_text[12], bg=button_bg, width=button_w, height=button_h, fg=button_fg,  font=button_font, command=lambda: callback(b_text[12], active_layer))
B13 = tk.Button(root, textvariable=b_text[13], bg=button_bg, width=button_w, height=button_h, fg=button_fg,  font=button_font, command=lambda: callback(b_text[13], active_layer))
B14 = tk.Button(root, textvariable=b_text[14], bg=button_bg, width=button_w, height=button_h, fg=button_fg,  font=button_font, command=lambda: callback(b_text[14], active_layer))
B15 = tk.Button(root, textvariable=b_text[15], bg=button_bg, width=button_w, height=button_h, fg=button_fg,  font=button_font, command=lambda: callback(b_text[15], active_layer))
B16 = tk.Button(root, textvariable=b_text[16], bg=button_bg, width=button_w, height=button_h, fg=button_fg,  font=button_font, command=lambda: callback(b_text[16], active_layer))
B17 = tk.Button(root, textvariable=b_text[17], bg=button_bg, width=button_w, height=button_h, fg=button_fg,  font=button_font, command=lambda: callback(b_text[17], active_layer))
B18 = tk.Button(root, textvariable=b_text[18], bg=button_bg, width=button_w, height=button_h, fg=button_fg,  font=button_font, command=lambda: callback(b_text[18], active_layer))
B19 = tk.Button(root, textvariable=b_text[19], bg=button_bg, width=button_w, height=button_h, fg=button_fg,  font=button_font, command=lambda: callback(b_text[19], active_layer))
B20 = tk.Button(root, textvariable=b_text[20], bg=button_bg, width=button_w, height=button_h, fg=button_fg,  font=button_font, command=lambda: callback(b_text[20], active_layer))
B21 = tk.Button(root, textvariable=b_text[21], bg=button_bg, width=button_w, height=button_h, fg=button_fg,  font=button_font, command=lambda: callback(b_text[21], active_layer))
B22 = tk.Button(root, textvariable=b_text[22], bg=button_bg, width=button_w, height=button_h, fg=button_fg,  font=button_font, command=lambda: callback(b_text[22], active_layer))
B23 = tk.Button(root, textvariable=b_text[23], bg=button_bg, width=button_w, height=button_h, fg=button_fg,  font=button_font, command=lambda: callback(b_text[23], active_layer))
B24 = tk.Button(root, textvariable=b_text[24], bg=button_bg, width=button_w, height=button_h, fg=button_fg,  font=button_font, command=lambda: callback(b_text[24], active_layer))
B25 = tk.Button(root, textvariable=b_text[25], bg=button_bg, width=button_w, height=button_h, fg=button_fg,  font=button_font, command=lambda: callback(b_text[25], active_layer))
B26 = tk.Button(root, textvariable=b_text[26], bg=button_bg, width=button_w, height=button_h, fg=button_fg,  font=button_font, command=lambda: callback(b_text[26], active_layer))
B27 = tk.Button(root, textvariable=b_text[27], bg=button_bg, width=button_w, height=button_h, fg=button_fg,  font=button_font, command=lambda: callback(b_text[27], active_layer))
B28 = tk.Button(root, textvariable=b_text[28], bg=button_bg, width=button_w, height=button_h, fg=button_fg,  font=button_font, command=lambda: callback(b_text[28], active_layer))
B29 = tk.Button(root, textvariable=b_text[29], bg=button_bg, width=button_w, height=button_h, fg=button_fg,  font=button_font, command=lambda: callback(b_text[29], active_layer))
B30 = tk.Button(root, textvariable=b_text[30], bg=button_bg, width=button_w, height=button_h, fg=button_fg,  font=button_font, command=lambda: callback(b_text[30], active_layer))
B31 = tk.Button(root, textvariable=b_text[31], bg=button_bg, width=button_w, height=button_h, fg=button_fg,  font=button_font, command=lambda: callback(b_text[31], active_layer))
B32 = tk.Button(root, textvariable=b_text[32], bg=button_bg, width=button_w, height=button_h, fg=button_fg,  font=button_font, command=lambda: callback(b_text[32], active_layer))
B33 = tk.Button(root, textvariable=b_text[33], bg=button_bg, width=button_w, height=button_h, fg=button_fg,  font=button_font, command=lambda: callback(b_text[33], active_layer))
#11 columns

switch_button_name(active_layer)

empty_label1 = Label(root, text="                  ", bg="black")
empty_label2 = Label(root, text="                  ", bg="black")
empty_label3 = Label(root, text="                  ", bg="black")
empty_label4 = Label(root, text="                  ", bg="black")


title_bar.grid(column=0, row=0, columnspan=13, sticky=N+E+S+W)
title_label.grid(column=0, row=0, columnspan=13, sticky=N+E+S+W)
close_label.grid(column=12, row=0, sticky=E)

B0.grid(column=0, row = 1, padx=5, pady=5)
B1.grid(column=1, row = 1, padx=5, pady=5)
B2.grid(column=2, row = 1, padx=5, pady=5)
B3.grid(column=3, row = 1, padx=5, pady=5)
B4.grid(column=4, row = 1, padx=5, pady=5)
empty_label1.grid(column=6, row=1)
B5.grid(column=8, row = 1, padx=5, pady=5)
B6.grid(column=9, row = 1, padx=5, pady=5)
B7.grid(column=10, row = 1, padx=5, pady=5)
B8.grid(column=11, row = 1, padx=5, pady=5)
B9.grid(column=12, row = 1, padx=5, pady=5)
B10.grid(column=0, row = 2, padx=5, pady=5)
B11.grid(column=1, row = 2, padx=5, pady=5)
B12.grid(column=2, row = 2, padx=5, pady=5)
B13.grid(column=3, row = 2, padx=5, pady=5)
B14.grid(column=4, row = 2, padx=5, pady=5)
empty_label2.grid(column=6, row=2)
B15.grid(column=8, row = 2, padx=5, pady=5)
B16.grid(column=9, row = 2, padx=5, pady=5)
B17.grid(column=10, row = 2, padx=5, pady=5)
B18.grid(column=11, row = 2, padx=5, pady=5)
B19.grid(column=12, row = 2, padx=5, pady=5)
B20.grid(column=0, row = 3, padx=5, pady=5)
B21.grid(column=1, row = 3, padx=5, pady=5)
B22.grid(column=2, row = 3, padx=5, pady=5)
B23.grid(column=3, row = 3, padx=5, pady=5)
B24.grid(column=4, row = 3, padx=5, pady=5)
empty_label3.grid(column=6, row=3)
B25.grid(column=8, row = 3, padx=5, pady=5)
B26.grid(column=9, row = 3, padx=5, pady=5)
B27.grid(column=10, row = 3, padx=5, pady=5)
B28.grid(column=11, row = 3, padx=5, pady=5)
B29.grid(column=12, row = 3, padx=5, pady=5)
B30.grid(column=4, row = 4, padx=5, pady=5)
B31.grid(column=5, row = 4, padx=5, pady=5)
empty_label4.grid(column=6, row=4)
B32.grid(column=7, row = 4, padx=5, pady=5)
B33.grid(column=8, row = 4, padx=5, pady=5)

#-----------------------------------------------------------------------------

key_char = False
def on_press(key):
    global key_char
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
        i = b_listener_key.index(key.char)
        print(globals()['B%s' % i])
        print(B0)
        button_inv = globals()['B%s' % i]
        button_inv.invoke()
        print(f'Found {b_listener_key.index(key.char)}')
        widget = globals()['B%s' % i]
        widget.configure(relief="sunken", bg="orange")
        widget.invoke()
        key_char = True

    except AttributeError:
        print('special key {0} pressed'.format(
            key))
        i = b_listener_key.index(key)
        print(globals()['B%s' % i])
        button_inv = globals()['B%s' % i]
        button_inv.invoke()
        print(f'Found {b_listener_key.index(key)}')
        widget = globals()['B%s' % i]
        widget.configure(relief="sunken", bg="orange")
        widget.invoke()
def on_release(key):
    global key_char
    if key_char == True:
        print('{0} released'.format(
        key.char))
        i = b_listener_key.index(key.char)
        widget = globals()['B%s' % i]
        widget.configure(relief="raised", bg="black")
        key_char = False

    else:
        print('{0} released'.format(
        key))
        i = b_listener_key.index(key)
        widget = globals()['B%s' % i]
        widget.configure(relief="raised", bg="black")


        # if key == keyboard.Key.esc:
        # Stop listener
        # $    return False


listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()




#-----------------------------------------------------------------------------
root.mainloop()
