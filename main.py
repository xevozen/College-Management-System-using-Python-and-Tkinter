import tkinter
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk 
import os
import mysql.connector
root =Tk()
root.title("Home Page")
root.geometry("1080x650+100+20")
root.resizable(False, False) 
global root_window
is_admin = False
root_window = root
def on_closing():
    global is_on
    if is_admin:
        on_.config(image=off)
        is_on = False
    else:
        on_.config(image=on)
        is_on = True
    window.destroy()
def draw_login_page():
    global window
    newWindow = Toplevel(root_window)
    # newWindow.attributes('-alpha',0.9)
    newWindow.title("Admin Login")
    newWindow.geometry("400x400+500+200")
    newWindow.configure(bg="#fbb1bd")
    header=Frame(newWindow, bg="#e23946", bd=5)
    header.place(x=0,y=0,width=400,height=60)
    #heading label
    nsec=Label(header, text="Netaji Subhash Engineering College",font=("Helvetica",16,"bold"), bg = "#e23946",fg="#eae2b7")
    nsec.place(x=0, y=10, width=400)
    username = Label(newWindow, text ="Username", font=("Helvetica", 16), relief = FLAT, bg="#fbb1bd")
    username.place(x=20, y=100)
    username_input = Text(newWindow, height = 1,
                font = ("Helvetica", 16),
                width = 20,
                bg = "light yellow")
    username_input.place(x=120, y=100)
    password = Label(newWindow, text ="Password", font=("Helvetica", 16), relief = FLAT, bg="#fbb1bd")
    password.place(x=20, y=175)
    password_input = tkinter.Entry(newWindow,
                                   show = '*', 
                                   font = ("Helvetica", 16),
                                   width = 20,
                                   bg = "light yellow"
                                   )
    password_input.place(x=120, y=175)
    submit= Button(newWindow, text="LOGIN", command = login, font=("Helvetica", 16), bd =2, bg = "#e23946",fg="#eae2b7", relief=RAISED)
    submit.place(x=150, y=250, width = 100, height = 50)
    alert=Label(newWindow, text="Default Username: admin, password:admin",font=("Helvetica",8,), bg = "#e23946",fg="#eae2b7")
    alert.place(x=0, y=360, width=400)
    newWindow.protocol("WM_DELETE_WINDOW", on_closing)
    window = newWindow
def login():
    username = window.winfo_children()[2].get(1.0, "end-1c")
    password = window.winfo_children()[4].get()
    db = mysql.connector.connect(host="localhost", user="root", password="", database="nsec_db")
    mycursor = db.cursor()
    mycursor.execute("SELECT y FROM global_values WHERE x = 'admin'")
    rows = mycursor.fetchone()
    if rows == None:
        messagebox.showinfo("Failure",  "Oops! Something went wrong")
        return
    server_pwd = rows[0]
    db.commit()
    db.close()
    global is_on
    if username == "admin" and password == server_pwd:
        tkinter.messagebox.showinfo("Success",  "Access Granted")
        is_admin = True
        on_.config(image=off)
        is_on = False
        draw_admin()
    else:
        tkinter.messagebox.showinfo("Failure",  "Access Denied")
        is_admin = False
        on_.config(image=on)
        is_on = True
        draw_visitor()
    window.destroy()
def button_mode():
   global is_on
   #Determine it is on or off
   if is_on:
      on_.config(image=off)
      is_on = False
      draw_login_page()
   else:
      on_.config(image = on)
      is_on = True
      is_admin = False
      draw_visitor()
      
def draw_search_employee():
    # import search_employee
    os.system('python search_employee.py')
def draw_search_student():
    # import search_student
    os.system('python search_student.py')
def draw_company_list():
    os.system('python view_company_list.py')
def draw_visitor_fees():
    os.system('python visitor_fees_structure.py')
def draw_notice_board():
    os.system('python view_notice_board.py')
def draw_edit_student():
    os.system('python edit_student.py')
def draw_edit_employee():
    os.system('python edit_employee.py')
def draw_edit_notice_board():
    os.system('python edit_notice_board.py')
def draw_edit_company_list():
    os.system('python edit_company_list.py')
def draw_change_password():
    os.system('python change_password.py')
def draw_execute_dbms():
    os.system('python execute_dbms.py')

def draw_visitor():
    for widget in dashboard.winfo_children():
        widget.destroy()
    welcome_text["text"] = "Welcome, Visitor"
    image1 = Image.open("media/nsec.jpg")
    test = ImageTk.PhotoImage(image1)
    label1 = Label(dashboard,image=test)
    label1.photo = test
    label1.place(x=0, y=0, height = 400, width = 1080)
    option= Button(dashboard, text ="Search Employee", command = draw_search_employee, bd =0, font=("Helvetica",16), bg = "#118ab2",fg="#eae2b7")
    option.place(x=150, y=75, width = 200, height = 50)
    option= Button(dashboard, text ="Search Student", command =  draw_search_student, bd =0, font=("Helvetica",16), bg = "#118ab2",fg="#eae2b7")
    option.place(x=730, y=75, width = 200, height = 50)
    option= Button(dashboard, text ="Fee Structure", command = draw_visitor_fees, bd =0, font=("Helvetica",16), bg = "#118ab2",fg="#eae2b7")
    option.place(x=150, y=275, width = 200, height = 50)
    option= Button(dashboard, text ="Notice Board", command = draw_notice_board,bd =0, font=("Helvetica",16), bg = "#118ab2",fg="#eae2b7")
    option.place(x=442, y=175, width = 200, height = 50)
    option= Button(dashboard, text ="Company List", command = draw_company_list,bd =0, font=("Helvetica",16), bg = "#118ab2",fg="#eae2b7")
    option.place(x=735, y=275, width = 200, height = 50)
def draw_admin():
    for widget in dashboard.winfo_children():
        widget.destroy()
    welcome_text["text"] = "Welcome, Admin"
    image1 = Image.open("media/nsec.jpg")
    test = ImageTk.PhotoImage(image1)
    label1 = Label(dashboard,image=test)
    label1.photo = test
    label1.place(x=0, y=0, height = 400, width = 1080)
    option= Button(dashboard, text ="View/Edit Employee", command = draw_edit_employee, bd =0, font=("Helvetica",16), bg = "#118ab2",fg="#eae2b7")
    option.place(x=100, y=75, width = 250, height = 50)
    option= Button(dashboard, text ="View/Edit Student", command =  draw_edit_student, bd =0, font=("Helvetica",16), bg = "#118ab2",fg="#eae2b7")
    option.place(x=735, y=75, width = 250, height = 50)
    option= Button(dashboard, text ="Change Password", command = draw_change_password, bd =0, font=("Helvetica",16), bg = "#118ab2",fg="#eae2b7")
    option.place(x=100, y=275, width = 250, height = 50)
    option= Button(dashboard, text ="View/Edit Notice Board", command = draw_edit_notice_board, bd =0, font=("Helvetica",16), bg = "#118ab2",fg="#eae2b7")
    option.place(x=420, y=75, width = 250, height = 50)
    option= Button(dashboard, text ="Execute DBMS Query", command = draw_execute_dbms, bd =0, font=("Helvetica",16), bg = "#118ab2",fg="#eae2b7")
    option.place(x=420, y=275, width = 250, height = 50)
    option= Button(dashboard, text ="View/Edit Company List", command = draw_edit_company_list,bd =0, font=("Helvetica",16), bg = "#118ab2",fg="#eae2b7")
    option.place(x=735, y=275, width = 250, height = 50)
    
#Header
header=Frame(root, bg="brown", bd=0)
header.place(x=0,y=0,width=1080,height=115)
#logo
image1 = Image.open("media/logo.jpg")
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(header,image=test)
label1.image = test
label1.place(x=0, y=0, height = 120)
#heading label
nsec=Label(header, text="Netaji Subhash Engineering College",font=("Helvetica",36,"bold"), bg = "brown",fg="#eae2b7")
nsec.place(x=105, y=20, width=950)

#Profile frame
frame=Frame(root, bg="#fbb1bd")
frame.place(x=0,y=115,width=1080,height=50)
welcome_text = Label(frame, text = "Welcome, Visitor", font=("Minion Pro Regular", 16), bg="#fbb1bd")
welcome_text.place(x=20, y=10)
is_on = True

# Define Our Images
on = PhotoImage(file ="media/on.png")
off = PhotoImage(file ="media/off.png")
# Create A Button
on_= Button(frame, image =on,bd =0, bg = "#fbb1bd", command = button_mode)
on_.place(x=950, y=0, width = 50, height = 50)
#visitor_text
visitor_text = Label(frame, text = "Visitor", font=("Minion Pro Regular", 16), bg="#fbb1bd")
visitor_text.place(x=880, y=10)
#admin_text
admin_text = Label(frame, text = "Admin", font=("Minion Pro Regular", 16), bg="#fbb1bd")
admin_text.place(x=1000, y=10)
#profile picture
image1 = Image.open("media/profile.png")
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(frame,image=test, bg = "#fbb1bd")
label1.place(x=820, y=0)

dashboard=Frame(root, bg="#bbb", bd=0)
dashboard.place(x=0,y=165,width=1080,height=400)
draw_visitor()
#Footer
footer=Frame(root, bg="brown", bd=0)
footer.place(x=0,y=565,width=1080,height=85)
root.mainloop()