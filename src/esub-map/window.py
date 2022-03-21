from tkinter import *
from tkinter import ttk
import json

TITLE = "esub-map"
GEOMETRY = "500x500"
COLORSCHEME = "assets/colorschemes/default.json"

root = Tk()
root.title(TITLE)
root.geometry(GEOMETRY)
root.resizable(True, True)
with open(COLORSCHEME, "r") as f:
    cs_data = f.read()
cs = json.loads(cs_data)
root.config(bg=cs["bg"])
root.mainloop()

