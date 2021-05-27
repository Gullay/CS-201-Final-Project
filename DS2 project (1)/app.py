from  tkinter import *
import tkinter as tk
from tkinter.constants import LEFT
from PIL import Image, ImageTk
from bloom import Book_details

def searchBook(query): 
    if not query:temp = ["Type book's title in search box to search it.",""]
    else:temp = Book_details(query)  #returns a list after searching books title in data set.
    outputBox(temp)
    bookEntered.delete(0, END) #reomves the content written in search after hiting search book button.
    
main = tk.Tk()
# main.configure(bg='#666C59') 
main.title("BookReads")
main.iconbitmap("images\icon.ico") #icon

canvas = tk.Canvas(main, width= 800, height= 550)
canvas.grid(columnspan = 4, rowspan=4)

#background image
bg = ImageTk.PhotoImage(Image.open("images/bg3.jpg")) 
canvas.create_image(0, 0, anchor= NW, image = bg)
canvas.grid()

#logo
logo = ImageTk.PhotoImage(Image.open("images\logo.png"))
canvas.create_image(200, 150, anchor= CENTER, image = logo)
canvas.grid()

#entry box
bookEntered = tk.Entry(main, width = 60, background="light gray")
bookEntered.grid(column = 1, row = 2, ipady= 10)

#search button
button = tk.Button(main,text="Search Book",bg="#ea672a", fg="white",height = 2, width = 15, command=lambda: searchBook(bookEntered.get()))
button.grid(column= 1, row = 2, sticky="E")

#output
def outputBox(text):
    output = Text(main, width=40, height = 7, background="light grey")
    output.grid(row = 3, column = 1, sticky = 'W')
    output.insert(END, text[0])
    
    output1 = Text(main, width=40, height = 7, background="light grey")
    output1.grid(row = 3, column = 2, sticky = 'E')
    output1.insert(END, text[1])

#empty label
emptyLabel = Text(main, width=40, height = 7, background="light grey")
emptyLabel.grid(row = 3, column = 1, sticky = 'W')

#empty label
emptyLabel1 = Text(main, width=40, height = 7, background="light grey")
emptyLabel1.grid(row = 3, column = 2, sticky = 'E')
main.mainloop()
