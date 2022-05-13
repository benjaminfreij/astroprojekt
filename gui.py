from cProfile import label
from hashlib import sha3_224
import tkinter as tk
from turtle import color
from PIL import ImageTk
from click import command
from matplotlib.pyplot import text
from tkinter import *
import sys
import os



def show_image(imagefile): #funktion för att visa bilderna. 
    image = ImageTk.PhotoImage(file=imagefile)
    imagebox.pack()
    imagebox.config(image=image)
    imagebox.image = image


def restart_program(): #funktion för att starta om programmet.
    python = sys.executable
    os.execl(python, python, * sys.argv)

def show_label(label_to_show): #funktion som går igenom alla labels, och tar bort alla, och sedan lägger till labeln som har blivit inputad. 
    for label in labels:
        if label.winfo_ismapped():
            label.pack_forget()
    label_to_show.pack(pady=20)

root = tk.Tk()


label0 = Label(root, text="KIC 11242721 \n 19.65036503650365 d", font="Calibri 15 bold")       
label1 = Label(root, text="KIC 11018648 \n, Seismology(ID: KIC 11018648) - computed values: \n * numax: 2355.00 uHz method: ACF2D \n * deltanu: 105.23 uHz method: ACF2D \n * mass: 1.15 solMass method: Uncorrected Scaling Relations \n * radius: 1.24 solRad method: Uncorrected Scaling Relations \n * logg: 4.31 dex method: Uncorrected Scaling Relations",
    font=('Calibri 15 bold'))

label2 = Label(root, text="19.65036503650365 d",
font=('Calibri 15 bold'))
label3= Label(root, text="KIC 12404086 \n 13.197319731973197 d \n 132.33393339333932 d", font=("Calibri 15 bold"))
label4 = Label(root,text="KIC 11754553 \n 11.973597359735972 d", font=("Calibri 15 bold"))
label5 = Label(root, text="KIC 11812062 \n  3.7286728672867286 d \n 93.22082208220822 d", font=("Calibri 15 bold"))
label6=Label(root, text="KIC 11818800 \n Seismology(ID: KIC 11818800) - computed values: \n * numax: 2265.00 uHz (method: ACF2D) \n * deltanu: 141.15 uHz (method: ACF2D) \n * mass: 0.30 solMass (method: Uncorrected Scaling Relations) \n * radius: 0.65 solRad (method: Uncorrected Scaling Relations) \n * logg: 4.29 dex (method: Uncorrected Scaling Relations) \n 11.831083108310832 d", font="Calibri 15 bold")
label7=Label(root,text="KIC 11853255 \n 4.486848684868487 d \n 177.24822482248226 d", font="Calibri 15 bold")
label8=Label(root, text="KIC 11909839 \n Seismology(ID: KIC 11909839) - computed values: \n * numax: 2265.00 uHz (method: ACF2D) \n * deltanu: 86.76 uHz (method: ACF2D) \n * mass: 2.30 solMass (method: Uncorrected Scaling Relations) \n * radius: 1.77 solRad (method: Uncorrected Scaling Relations) \n * logg: 4.30 dex (method: Uncorrected Scaling Relations) \n KIC 11909839 \n 10.405940594059407 d \n 167.6194619461946 d", font=("Calibri 15 bold"))
label9=Label(root,text="KIC 11918099  \n Seismology(ID: KIC 11918099) - computed values: \n * numax: 2565.00 uHz (method: ACF2D) \n * deltanu: 118.48 uHz (method: ACF2D) \n * mass: 0.78 solMass (method: Uncorrected Scaling Relations) \n * radius: 1.00 solRad (method: Uncorrected Scaling Relations) \n  * logg: 4.33 dex (method: Uncorrected Scaling Relations) \n 4.674967496749675 d \n 46.75157515751575 d", font="Calibri 15 bold")
label10=Label(root,text="KIC 11960862 \n 6.575157515751576 d \n 32.87658765876587 d", font="Calibri 15 bold")
label11=Label(root,text="KIC 12020329 \n Seismology(ID: KIC 12020329) - computed values: \n * numax: 2265.00 uHz (method: ACF2D) \n * deltanu: 91.10 uHz (method: ACF2D) \n * mass: 1.76 solMass (method: Uncorrected Scaling Relations) \n * radius: 1.57 solRad (method: Uncorrected Scaling Relations) \n * logg: 4.29 dex (method: Uncorrected Scaling Relations) \n 7.274427442744274 d \n 36.375237523752375 d", font=("Calibri 15 bold"))
label12=Label(root, text="KIC 12066335 \n 11.66006600660066 d", font = "Calibri 15 bold")
labelx=Label(root,text="Supernova Exempel", font="Calibri 15 bold")
labels = [label0, label1, label2, label3, label4, label5, label6, label7, label8, label9, label10,label11,label12,labelx]

root.geometry("1920x1080+300+150")
root.configure(bg="black")

frame = tk.Frame(root)
frame.pack()

avslutknapp = tk.Button(frame, text="Avsluta", fg="red", bg="black", command=quit)
avslutknapp.pack(side=tk.LEFT)

s1 = tk.Button(frame, text="KIC 11018648",bg="black",fg="white", command=lambda: [show_image("newdir/astrobild1.png"), show_label(label1)])
s1.pack(side=tk.LEFT)

s2 = tk.Button(frame, text="KIC 11242721" ,bg="black", fg="white", command=lambda: [show_image("newdir/astrobild2.png"), show_label(label2)])
s2.pack(side=tk.LEFT)

s3 = tk.Button(frame, text="KIC 12404086",bg="black", fg="white", command=lambda: [show_image("newdir/astrobild3.png"), show_label(label3)])
s3.pack(side=tk.LEFT)

s4 = tk.Button(frame, text="KIC 11754553",bg="black", fg="white", command=lambda: [show_image("newdir/astrobild4.png"), show_label(label4)])
s4.pack(side=tk.LEFT)

s5 = tk.Button(frame, text="KIC 11812062",bg="black", fg="white", command=lambda: [show_image("newdir/astrobild5.png"), show_label(label5)])
s5.pack(side=tk.LEFT)

s6 = tk.Button(frame, text="KIC 11818800",bg="black", fg="white", command=lambda: [show_image("newdir/astrobild6.png"), show_label(label6)])
s6.pack(side=tk.LEFT)

s7 = tk.Button(frame, text="KIC 11853255",bg="black", fg="white", command=lambda: [show_image("newdir/astrobild7.png"), show_label(label7)])
s7.pack(side=tk.LEFT)

s8 = tk.Button(frame, text="KIC 11853255",bg="black", fg="white", command=lambda: [show_image("newdir/astrobild8.png"), show_label(label8)])
s8.pack(side=tk.LEFT)

s9 = tk.Button(frame, text="KIC 11918099",bg="black", fg="white", command=lambda: [show_image("newdir/astrobild9.png"), show_label(label9)])
s9.pack(side=tk.LEFT)

s10 = tk.Button(frame, text="KIC 11960862",bg="black", fg="white", command=lambda: [show_image("newdir/astrobild10.png"), show_label(label10)])
s10.pack(side=tk.LEFT)

s11 = tk.Button(frame, text="KIC 12020329",bg="black", fg="white", command=lambda: [show_image("newdir/astrobild11.png"), show_label(label11)])
s11.pack(side=tk.LEFT)

s12 = tk.Button(frame, text="KIC 12066335",bg="black", fg="white", command=lambda: [show_image("newdir/astrobild12.png"), show_label(label12)])
s12.pack(side=tk.LEFT)

sx = tk.Button(frame, text="Supernova",bg="black", fg="white", command=lambda: [show_image("newdir/supernova'.png"), show_label(labelx)])
sx.pack(side=tk.LEFT)

refresh = tk.Button(frame, text="Restart", fg = "white", bg = "black", command=restart_program)
refresh.pack(side=tk.LEFT)

imagebox = tk.Label(root)

root.mainloop()















