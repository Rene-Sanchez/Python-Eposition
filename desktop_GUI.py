""""
a program that stores horse ranch info for my desi bear

"""
from tkinter import *
import desktop_backend



window = Tk()#opens window
window.wm_title("Desiree's Ranch Finder")
window.configure(background='#ccccff')

def view_command():
    listbox.delete(0,END)
    for row in desktop_backend.view():
        listbox.insert(END,row)

def search_command():
    listbox.delete(0,END)
    for row in desktop_backend.search(name.get(),address.get(),Rating.get()):
        listbox.insert(END,row)

def add_command():
    desktop_backend.insert(name.get(),address.get(),Rating.get(),phone.get(),website.get(),notes.get())
    listbox.delete(0,END)
    listbox.insert(END,(name.get(),address.get(),Rating.get(),phone.get(),website.get(),notes.get()))

def get_selected_row(event):
    global selected_row #makes a global variable that can be called outside of funtion
    index=listbox.curselection()[0]
    selected_row=listbox.get(index)
    entry.delete(0,END)
    entry.insert(END,selected_row[1])
    Entry1.delete(0,END)
    Entry1.insert(END,selected_row[2])
    Entry3.delete(0,END)
    Entry3.insert(END,selected_row[3])
    Entry4.delete(0,END)
    Entry4.insert(END,selected_row[4])
    Entry5.delete(0,END)
    Entry5.insert(END,selected_row[5])
    Entry6.delete(0,END)
    Entry6.insert(END,selected_row[6])

def delete_command():
    desktop_backend.delete(selected_row[0])

def update_command():
    desktop_backend.update(selected_row[0],name.get(),address.get(),Rating.get(),phone.get(),website.get(),notes.get())

import webbrowser
import os
def map_command():
    desktop_backend.mapping(selected_row[2])
    webbrowser.open('file://'+ os.path.realpath('map.html'))

def clear_command():
    entry.delete(0,END)
    Entry1.delete(0,END)
    Entry3.delete(0,END)
    Entry4.delete(0,END)
    Entry5.delete(0,END)
    Entry6.delete(0,END)
    listbox.delete(0,END)

label1=Label(window,text="Name")
label1.grid(row=0,column=0)

label2=Label(window,text="Address")
label2.grid(row=2,column=0)

label4=Label(window,text="Rating")
label4.grid(row=1,column=2)

label5=Label(window,text="Phone")
label5.grid(row=0,column=2)

label6=Label(window,text="Website")
label6.grid(row=1,column=0)

label7=Label(window,text="Enter Notes")
label7.grid(row=19,column=0)

name = StringVar()
entry = Entry(window,textvariable=name)
entry.grid(row=0,column=1)

address = StringVar()
Entry1 = Entry(window,textvariable=address,width=48)
Entry1.grid(row=2,column=1,columnspan=4)

Rating = StringVar()
Entry3 = Entry(window,textvariable=Rating)
Entry3.grid(row=1,column=3)

phone = StringVar()
Entry4 = Entry(window,textvariable=phone)
Entry4.grid(row=0,column=3)

website = StringVar()
Entry5 = Entry(window,textvariable=website)
Entry5.grid(row=1,column=1)

notes = StringVar()
Entry6 = Entry(window,textvariable=notes)
Entry6.configure(width=50)
Entry6.grid(row=19,column=1, columnspan=4)

add_button = Button(window, text="Add",width=10,command=add_command, relief='raised')
add_button.grid(row=3,column=3,rowspan=3)

delete_button = Button(window, text="Delete",width=10,command=delete_command,relief='raised')
delete_button.grid(row=4,column=3,rowspan=3)

search_button = Button(window, text="Search",width=10,command=search_command,relief='raised')
search_button.grid(row=5,column=3,rowspan=3)

map_button = Button(window, text="Map",width=10,command=map_command, relief='raised')
map_button.grid(row=6,column=3,rowspan=3)

view_button = Button(window, text="View all",width=10,command=view_command,relief='raised')
view_button.grid(row=8,column=3,rowspan=3)

update_button = Button(window, text="Update",width=10,command=update_command,relief='raised')
update_button.grid(row=9,column=3,rowspan=3)

clear_button = Button(window, text="Clear",width=10,command=clear_command,relief='raised')
clear_button.grid(row=11,column=3,rowspan=3)

listbox=Listbox(window,height=20,width=25)
listbox.grid(row=3,column=1,rowspan=10,columnspan=1)

scroll=Scrollbar(window,width=10)
scroll.grid(row=4,column=2,rowspan=8,sticky="N"+"S")

listbox.configure(yscrollcommand=scroll.set)
scroll.configure(command=listbox.yview)

listbox.bind('<<ListboxSelect>>', get_selected_row)

window.mainloop() #closer that keeps window open
