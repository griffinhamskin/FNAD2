from tkinter import *
import tkinter as tk
import customtkinter
import pyglet
from config import *
import sys
pyglet.font.add_file('img\8bitoperator.ttf')

mainscreen = True
root = customtkinter.CTk()
newWindow = customtkinter.CTkToplevel(root)
newWindow.withdraw()
root.geometry('800x600')


bgimg= tk.PhotoImage(file="img/titleScreen1.ppm")
bgimg2= tk.PhotoImage(file="img\MiddleDark.png")

def end():
    root.destroy()
def delete():
    sys.exit()
def closeInfo():
    root.deiconify()
    newWindow.withdraw()
def controlsPage():
    root.withdraw()
    newWindow.deiconify()
    newWindow.title('Info')
    newWindow.geometry('362x567')
    limg2= customtkinter.CTkLabel(master=newWindow, image=bgimg2, text='')
    infoLabel= customtkinter.CTkLabel(master=newWindow, text=f'The goal is to survive four nights, you are a night guard \n working for FNAD Association, but be warned creatures\n come out at night. If you see something in your room the most \nyou can try to do is use your flashlight on it (Pressing F),\n the cameras are controlled by the number keys corralating\n to the camera name. Make sure to keep the boiler up!', bg_color='white', fg_color='transparent')
    quitbutton=customtkinter.CTkButton(master=newWindow,text='Back',fg_color='red', command=closeInfo,width=200,height=70, font=('font',50),bg_color='red',border_width=2,border_color='black')

    limg2.place(x=0,y=0)
    infoLabel.pack()
    quitbutton.place(x=90,y=450)


limg= customtkinter.CTkLabel(master=root, image=bgimg, text='')
startbutton=customtkinter.CTkButton(master=root,text='Start',fg_color='red', command=end,width=350,height=70, font=('font',50),bg_color='red',border_width=2,border_color='black')
infoButton=customtkinter.CTkButton(master=root,text='Controls',fg_color='red', command=controlsPage,width=350,height=70, font=('font',50),bg_color='red',border_width=2,border_color='black')
quitbutton=customtkinter.CTkButton(master=root,text='Quit',fg_color='red', command=delete,width=350,height=70, font=('font',50),bg_color='red',border_width=2,border_color='black')


limg.pack()
infoButton.place(x=250,y=400)
startbutton.place(x=250,y=300)
quitbutton.place(x=250,y=500)
root.mainloop()