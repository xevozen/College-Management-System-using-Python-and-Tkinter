import tkinter
from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector

root =Tk()
root.title("Change Password")
root.geometry("900x500+200+100")
root.resizable(False, False) 
global root_window
root_window = root
def on_closing():
    # root_window.destroy()
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root_window.destroy() 
def change_pwd():
    db = mysql.connector.connect(host="localhost", user="root", password="", database="nsec_db")
    mycursor = db.cursor()
    mycursor.execute("SELECT y FROM global_values WHERE x = 'admin'")
    rows = mycursor.fetchone()
    if rows == None:
        messagebox.showerror("Failure",  "Oops! Something went wrong")
        return
    server_pwd = rows[0]
    db.commit()
    if CurrentPwd.get() == server_pwd:
        if NewPwd.get() == NewPwd2.get():
            try:
                mycursor.execute("UPDATE global_values SET y = '"+str(NewPwd.get())+"' WHERE x = 'admin'")
                db.commit()
                messagebox.showinfo("Success",  "Password changed")
            except EXCEPTION as e:
                messagebox.showerror("Failure",  e)
                db.rollback()
                db.close()
        else:
            messagebox.showerror("Failure",  "New Passwords didn't match")

    else:
        messagebox.showerror("Failure",  "Oops! Something went wrong")
    CurrentPwd.delete(0, END)
    NewPwd.delete(0, END)
    NewPwd2.delete(0, END)
    root_window.destroy()
    

root_window.protocol("WM_DELETE_WINDOW", on_closing)
#Header
header=Frame(root, bg="brown", bd=0)
header.place(x=0,y=0,width=900,height=75)

#heading label
nsec=Label(header, text="Netaji Subhash Engineering College",font=("Helvetica", 28,"bold"), bg = "brown",fg="#eae2b7")
nsec.place(x=0, y=10, width=900)

#Profile frame
frame2=Frame(root, bg="#fbb1bd")
frame2.place(x=0,y=75,width=900,height=50)
welcome_text = Label(frame2, text = "Change Password", font=("Helvetica", 16), bg="#fbb1bd")
welcome_text.place(x=20, y=10)

close = Button(frame2, text = "Close", bd = 0, command = on_closing, font=("Helvetica", 16), bg="#fff", fg = "#000")
close.place(x=830, y=0, height = 50, width = 70)

#panel
panel=Frame(root, bg="#bbb", bd=0)
panel.place(x=0,y=125,width=900,height=375)
#panel_elements
searchBy=Label(panel,text="Current Password",font=("Helvetica",16),bg="#bbb",fg="#222")
searchBy.place(x=200, y=20)
CurrentPwd=Entry(panel,font=("Helvetica",12), show='*', bd = 0)
CurrentPwd.place(x=450, y=20, height = 30, width = 220)
searchBy=Label(panel,text="New Password",font=("Helvetica",16),bg="#bbb",fg="#222")
searchBy.place(x=200, y=100)
NewPwd=Entry(panel,font=("Helvetica",12), show='*', bd = 0)
NewPwd.place(x=450, y=100, height = 30, width = 220)
searchBy=Label(panel,text="Retype New Password",font=("Helvetica",16),bg="#bbb",fg="#222")
searchBy.place(x=200, y=180)
NewPwd2=Entry(panel,font=("Helvetica",12), show='*', bd = 0)
NewPwd2.place(x=450, y=180, height = 30, width = 220)
searchBtn=Button(panel,text="Change Password", command = change_pwd, font=("Helvetica",16,"bold"), bd = 0)
searchBtn.place(x=300, y=260, height = 50, width = 250)

root.mainloop()

