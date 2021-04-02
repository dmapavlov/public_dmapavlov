"""Trow 2 bricks and show random result"""

import tkinter as tk
import random


def throw_bricks():
    value1 = random.randrange(1, 7, 1)
    value2 = random.randrange(1, 7, 1)
    label1["text"] = f"{value1}"
    label2["text"] = f"{value2}"
    label_sum["text"] = f"Сумма: {value1 + value2}"


window = tk.Tk()

window.rowconfigure(0, minsize=70, weight=1)
window.columnconfigure([0], minsize=70, weight=1)

button = tk.Button(text='Throw bricks', command=throw_bricks)
button.pack(fill=tk.X)

label1 = tk.Label()
label1.pack(fill=tk.X)

label2 = tk.Label()
label2.pack(fill=tk.X)

label_sum = tk.Label()
label_sum.pack(fill=tk.X)

window.mainloop()
