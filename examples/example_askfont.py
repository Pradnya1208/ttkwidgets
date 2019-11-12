# -*- coding: utf-8 -*-

# Copyright (c) Juliette Monsel 2018
# For license see LICENSE

from ttkwidgets.font import askfont
try:
    import Tkinter as tk
    import ttk
except ImportError:
    import tkinter as tk
    from tkinter import ttk

res = (None, None)

def font():
    global res
    res = askfont(font=res[0])
    if res[0] is not None:
        label.configure(font=res[0])
    print(res)

window = tk.Tk()
label = ttk.Label(window, text='Sample text rendered in the chosen font.')
label.pack(padx=10, pady=10)
ttk.Button(window, text="Pick a font", command=font).pack()
window.mainloop()
