import tkinter
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector
root =Tk()
root.title("Fees Structure")
root.geometry("900x500+200+100")
root.resizable(False, False) 
global root_window
root_window = root
def on_closing():
    root_window.destroy()
    
#Header
header=Frame(root, bg="#e23946", bd=0)
header.place(x=0,y=0,width=900,height=75)

#heading label
nsec=Label(header, text="Netaji Subhash Engineering College",font=("Helvetica", 28,"bold"), bg = "#e23946",fg="#eae2b7")
nsec.place(x=0, y=10, width=900)

#Profile frame
frame2=Frame(root, bg="#fbb1bd")
frame2.place(x=0,y=75,width=900,height=50)
welcome_text = Label(frame2, text = "Fees Structure", font=("Minion Pro Regular", 16), bg="#fbb1bd")
welcome_text.place(x=20, y=10)

close = Button(frame2, text = "Close", bd = 0, command = on_closing, font=("Minion Pro Regular", 16), bg="#fff", fg = "#000")
close.place(x=830, y=0, height = 50, width = 70)

result=Frame(root, bg = "#777", bd=0)
result.place(x=200,y=130,width=512,height=353)
image1 = Image.open("media/fees.jpg")
test = ImageTk.PhotoImage(image1)
label1 = Label(result,image=test)
label1.photo = test
label1.place(x=0, y=0)
# draw_panel()
root.mainloop()