import tkinter
from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector

root =Tk()
root.title("Execute DBMS Query")
root.geometry("900x500+200+100")
root.resizable(False, False) 
global root_window
root_window = root
def on_closing():
    root_window.destroy()
    
def execute_query():
    query_input = queryInput.get(1.0, "end-1c")
    db = mysql.connector.connect(host="localhost", user="root", password="", database="nsec_db")
    mycursor = db.cursor(buffered = True)
    try:
        mycursor.execute(query_input)
        db.commit()
    except:
        messagebox.showerror("Alert", "An error occured, check your query")
        db.rollback()
        db.close()
        return
    rows = mycursor.fetchall()
    for widget in bottom_panel.winfo_children():
        widget.destroy()
    label1 = Label(bottom_panel, text =">>> "+ str(mycursor.rowcount)+" Rows Affected / Selected", bg = "#333", fg = "#00FF00", font = ("Lucida Console", 12))
    label1.place(x=10, y=0, height = 40, width = 300)
    if rows == None:
        return
    for widget in top_panel.winfo_children():
        widget.destroy()
    num_fields = len(mycursor.description)
    field_names = [i[0] for i in mycursor.description]
    a = list(field_names)
    scrollx=Scrollbar(top_panel,orient=HORIZONTAL)
    data_table=ttk.Treeview(top_panel, columns=a, show="headings", xscrollcommand=scrollx.set)
    scrollx.place(x=10, y=180, width = 880)
    scrollx.config(command=data_table.xview)
    data_table.place(x=10, y=0, width = 880, height = 180)
    for i in a:
        data_table.heading(column = i, text = i.upper())
        data_table.column(column = i, width = 200)
    for row in rows:
        data_table.insert('', END, values=row)

#Header
header=Frame(root, bg="brown", bd=0)
header.place(x=0,y=0,width=900,height=75)
#heading label
nsec=Label(header, text="Netaji Subhash Engineering College",font=("Helvetica", 28,"bold"), bg = "brown",fg="#eae2b7")
nsec.place(x=0, y=10, width=900)
#Profile frame
frame2=Frame(root, bg="#fbb1bd")
frame2.place(x=0,y=75,width=900,height=50)
welcome_text = Label(frame2, text = "Execute Custom DBMS Query", font=("Helvetica", 16), bg="#fbb1bd")
welcome_text.place(x=20, y=10)
close = Button(frame2, text = "Close", bd = 0, command = on_closing, font=("Minion Pro Regular", 16), bg="#fff", fg = "#000")
close.place(x=830, y=0, height = 50, width = 70)
#panel
panel=Frame(root, bg="#bbb", bd=0)
panel.place(x=0,y=125,width=900,height=375)
#panel_elements
searchBy=Label(panel,text="Enter Query",font=("Helvetica",12, "bold"),bg="#bbb",fg="#222")
searchBy.place(x=10, y=10)
scrollx=Scrollbar(panel,orient=HORIZONTAL)
queryInput=Text(panel, wrap=NONE, font=("Lucida Console", 15),bd=0, xscrollcommand=scrollx.set)
scrollx.config(command=queryInput.xview)
scrollx.place(x=10, y=70, width = 880, height = 12)
queryInput.place(x=10, y=40, height = 30, width = 880)
queryBtn=Button(panel,text="Execute", command = execute_query, font=("Helvetica",16,"bold"), bd = 0)
queryBtn.place(x=790, y=5, height = 30)

top_panel=Frame(panel, bg="#ddd", bd=0)
top_panel.place(x=0,y=85,width=900,height=200)
bottom_panel=Frame(panel, bg="#333", bd=0)
bottom_panel.place(x=0,y=285,width=900,height=90)

root.mainloop()
