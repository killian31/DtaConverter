# Converter .dta to .csv
### Copyright : Killian Steunou

import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory

def convert():
    Tk().withdraw() 
    filename = askopenfilename() 
    if filename!="":
        directory = askdirectory() 
    else:
        pass
    data = pd.io.stata.read_stata(filename)
    data.to_csv(f"{directory}/Data_converted.csv")

try:
    convert()
except:
    print("Canceled or wrong file type.")