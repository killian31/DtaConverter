# Converter .dta to .csv
### Copyright : Killian Steunou

import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory
import tkinter as tk 
from tkmacosx import Button

filename = ''
directory=''


def ask_dta_file():
    global filename, lbl_file
    Tk().withdraw() 
    filename = askopenfilename()
    lbl_file['text'] = filename

def ask_directory():
    global directory, lbl_folder
    directory = askdirectory() 
    lbl_folder['text'] = directory

def convert():
    global filename, directory
    if filename!="":
        data = pd.io.stata.read_stata(filename)
        data.to_csv(f"{directory}/Data_converted.csv")
    else:
        pass

# Window
app = tk.Tk()
app.title("Converter")
app.geometry("1404x936")
app.minsize(1080,720)
app.maxsize(1920,1080)
app.config(background='#00bbf9')

# Labels
lbl_title = tk.Label(app, text="Dta Converter", font=("Times", 80), bg='#00bbf9', fg='white')
lbl_file = tk.Label(app, text=" "*100, font=("Times", 10), bg='sky blue', fg='white')
lbl_folder = tk.Label(app, text=" "*100, font=("Times", 10), bg='sky blue', fg='white')
# Buttons
btn_select_file = Button(app, text='Select file', font=('Times',20), height=60, width=250, 
overrelief='solid', relief='solid',highlightthickness=4,
focuscolor='gray', bg='#00bbf9', fg='white', 
overbackground='blue', overforeground='white', command=ask_dta_file)

btn_select_folder = Button(app, text='Select destination folder', font=('Times',20), height=60, width=250, 
overrelief='solid', relief='solid',highlightthickness=4,
focuscolor='gray', bg='#00bbf9', fg='white', 
overbackground='blue', overforeground='white', command=ask_directory)

btn_convert = Button(app, text='Convert', font=('Times',20), height=120, width=500, 
overrelief='solid', relief='solid',highlightthickness=4,
focuscolor='gray', bg='#00bbf9', fg='white', 
overbackground='blue', overforeground='white', command=convert)

lbl_title.pack(side="top")
lbl_file.place(relx=0.25, rely = 0.40, anchor='center')
lbl_folder.place(relx=0.75, rely=0.40, anchor='center')
btn_select_file.place(relx=0.25, rely=0.32, anchor='center')
btn_select_folder.place(relx=0.75, rely=0.32, anchor='center')
btn_convert.place(relx=0.5, rely=0.55, anchor='center')
app.mainloop()