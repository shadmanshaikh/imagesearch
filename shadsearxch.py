from importlib.metadata import entry_points
import tkinter as tk
from turtle import bgcolor, color
from typing import Text
from typing_extensions import IntVar
from matplotlib.pyplot import text
from selenium import webdriver
from setuptools import Command
import webbrowser
from PIL import ImageTk , Image
# driver = webdriver.Chrome(executable_path=r'C:\Users\XAN\Desktop\py\tkinter\chromedriver.exe')

main = tk.Tk()
# t = tk.Text(main, height=2,width=20)
# t.pack()

# Myin = input()    
# h = print(t)
# print(Myin)

img = ImageTk.PhotoImage(Image.open(r"C:\Users\XAN\Desktop\py\tkinter\shadsearch.png"))
label_img = tk.Label(main, image=img)
label_img.pack()


# t = Text(main , height=5,width=4)
myl =  tk.Label(main, text="Made with \u2764\ufe0fby SHADMAN" , font='bold' )
# lab_btn.pack()


# def Startext():
#     # print('You can Start the Process')
#     lab = tk.Label(main,text="You just clicked start Button" , font='bold')
#     # webbrowser.open('https://www.google.com')
#     lab.pack()
#     # print(t)
#     # t.pack()
# def Stoptext():
#     # print("Now you can stop the text")
#     lab2 = tk.Label(main,text="You just clicked stop Button" , font='bold')
#     lab2.pack()

# search_string = input()

def display_text():
    global entry
    string = entry.get()
    dislabel.configure(text=string)

def takemetosite():
    webbrowser.open('https://www.google.com/search?tbm=isch&q='+entry.get())



dislabel = tk.Label(main, text='')
dislabel.pack()
entry = tk.Entry(main, width=40)
entry.focus_set()
entry.pack()

dis_btn = tk.Button(main, text='search',width=8,height=3 ,command=takemetosite,padx=2)
dis_btn.pack(pady=3)
# main.bind('<Return>',Startext)
main.title('+-------+SHADSEARXCH+-------+')
# btn = tk.Button(main, text='START',font='bold',width='10',height='5' , bg='green', activebackground='white',command=Startext)
# btn.pack(side=tk.RIGHT,padx=140,pady=200)
# btn1 = tk.Button(main, text='STOP',font='bold',width='10',height='5' , bg='red', activebackground='black',command=Stoptext)
# btn1.pack(side=tk.RIGHT,padx=140,pady=200)
# myl.pack(side=tk.BOTTOM )

# text = Text(main)
# text.insert(tk.INSERT, "1")
# btn1.pack()
# btn.pack()
myl.pack(fill='both')
main.mainloop()


# other = tk.Tk()
# menubtn = tk.Menubutton(other, text="MyChoice", relief=tk.FLAT)
# menubtn.menu = tk.Menu(menubtn)
# menubtn["menu"]=menubtn.menu
# menubtn.menu.add_checkbutton(label='hindi')
# menubtn.menu.add_checkbutton(label='kannada')
# menubtn.menu.add_checkbutton(label='english')
# menubtn.grid()
# other.mainloop()

