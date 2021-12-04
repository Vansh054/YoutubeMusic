import pywhatkit 
from PIL import Image,ImageTk
from tkinter import *


def play():
    song = music.get()
    pywhatkit.playonyt(song)

root = Tk()
root.title('YoutubeMusic')
root.geometry('600x450')
bg = ImageTk.PhotoImage(file="bg.jpg")
bgimage = Label(root,image=bg).place(x=0,y=0,relwidth=1,relheight=1)
music = StringVar()
music_inp = Entry(root,textvariable=music,bd=5)
music_inp.place(x=225,y=300)
btn = Button(root, text='', font='Times 20 bold', bg='white',
                 fg='white', height=1, width=4, command=lambda: play())
btn.place(x=250,y=350)
root.mainloop()

