""" Run program, opens menu window with options """
import tkinter as tk
import matplotlib.pyplot as plt

import classes

def print_result(text=""):
    """ open new window with text """
    root = tk.Tk()
    S = tk.Scrollbar(root)
    T = tk.Text(root, height=30, width=60)
    S.pack(side=tk.RIGHT, fill=tk.Y)
    T.pack(side=tk.LEFT, fill=tk.Y)
    S.config(command=T.yview)
    T.config(yscrollcommand=S.set)
    T.insert(tk.END, text)
    tk.mainloop()


""" create menu window """
root= tk.Tk()

canvas1 = tk.Canvas(root, width = 800, height = 600)
canvas1.pack()

label1 = tk.Label(root, text='Wpisz tekst by uzyksać rezultat, L-liczba:\n\nWL - by zobaczyć wykres miesiąca\n np. L0 -aktualny, L-1 - poprzedni\n\nTL by zobaczyć podsumowanie tekstowe miesiąca\n np. T-2 - przedostatni miesiąc \n\n 3T by zobaczyć podsumowanie tekstowe 3 ostatnich miesięcy')
label1.config(font=('helvetica', 11))
canvas1.create_window(400, 200, window=label1)

entry1 = tk.Entry (root) 
canvas1.create_window(400, 380, window=entry1)

def getResult ():
    """ open window with text or open plot window """ 
    x1 = entry1.get()
    if x1[0]=="T":
        try:
            print_result(classes.Month_text_or_plot_sum_up(int(x1[1:])).return_text_for_month())
        except Exception:
            pass
    elif x1[0] == "W":
        try:
            classes.Draw_plot_one_month(int(x1[1:])).draw()
        except Exception:
            pass
    if x1 == "3T":
        print_result(classes.Month_text_sum_up().return_text_for_3_last_months())

button1 = tk.Button(text='Potwierdź', command=getResult)
canvas1.create_window(400, 460, window=button1)

root.mainloop()



