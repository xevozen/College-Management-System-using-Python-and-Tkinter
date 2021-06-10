from tkinter import*
import mysql.connector
from tkinter import ttk
root =Tk()
root.title("Company List")
root.geometry("900x500+200+100")
root.resizable(False, False) 
global root_window
root_window = root
def on_closing():
    root_window.destroy()
def search():
    option = dropdown.get()
    search_input = searchInput.get()
    db = mysql.connector.connect(host="localhost", user="root", password="", database="nsec_db")
    mycursor = db.cursor()
    if search_input == "":
        mycursor.execute("SELECT * FROM company_list")
    elif option == "Name":
        mycursor.execute("SELECT * FROM company_list WHERE name = '" + str(search_input).upper() + "'")
    elif option == "Year":
        mycursor.execute("SELECT * FROM company_list WHERE year LIKE '%" + str(search_input).upper() + "%'")
    elif option == "Department":
        mycursor.execute("SELECT * FROM company_list WHERE dept lIKE '%" + str(search_input).upper() + "%'")
    else:
        return
    rows = mycursor.fetchall()
    data_table.delete(*data_table.get_children())
    if rows == None:
        note_text['text'] = "Data: 0 Rows"
        return 
    note_text['text'] = "Data: "+str(len(rows))+" Rows"
    for row in rows:
        data_table.insert('', END, values=row)
    db.commit()
    db.close()

# IT WILL GET DATA IN LEFTBOX (getdata made events there and fecth value there also)
def getdata(event):
    currow = data_table.focus()
    contents = data_table.item(currow)
    row = contents['values']
    NameEntry.configure(state='normal')
    YearEntry.configure(state = 'normal')
    DepartmentEntry.configure(state = 'normal')
    NameEntry.delete(0, END)
    YearEntry.delete("1.0", "end")
    DepartmentEntry.delete("1.0", "end")
    NameEntry.insert(0, row[0])
    YearEntry.insert(END, row[2])
    DepartmentEntry.insert(END, row[1])
    NameEntry.configure(state='readonly')
    YearEntry.configure(state = 'disabled')
    DepartmentEntry.configure(state = 'disabled')

#Header
header=Frame(root, bg="brown", bd=0)
header.place(x=0,y=0,width=900,height=75)

#heading label
nsec=Label(header, text="Netaji Subhash Engineering College",font=("Helvetica", 28,"bold"), bg = "brown",fg="#eae2b7")
nsec.place(x=0, y=10, width=900)
#Profile frame
frame2=Frame(root, bg="#fbb1bd")
frame2.place(x=0,y=75,width=900,height=50)
welcome_text = Label(frame2, text = "Notice Board", font=("Minion Pro Regular", 16), bg="#fbb1bd")
welcome_text.place(x=20, y=10)
close = Button(frame2, text = "Close", command = on_closing, bd = 0, font=("Minion Pro Regular", 16), bg="#fff", fg = "#000")
close.place(x=830, y=0, height = 50, width = 70)
# LEFT BOX
leftbox=Frame(root,bd=0,bg="brown")
leftbox.place(x=10,y=140,width=500,height=350)

# INSIDE LEFT BOX
leftbox_title=Label(leftbox,text="Company List",font=("Helvetica",20,"bold"),fg="#eae2b7",bg="brown")
leftbox_title.place(x=10, y=30, width=  500)
NameLabel=Label(leftbox,text="Company Name",font=("Helvetica",15),fg="#eae2b7",bg="brown")
NameLabel.place(x=10, y =90)
NameEntry=Entry(leftbox,font=("Helvetica",15),bd=0)
NameEntry.place(x=160, y =90, width = 317)
YearLabel=Label(leftbox,text="Year",font=("Helvetica", 15),fg="#eae2b7",bg="brown")
YearLabel.place(x=10, y=140)
scrolly=Scrollbar(leftbox,orient=VERTICAL)
YearEntry=Text(leftbox, font=("Helvetica", 15),bd=0, yscrollcommand=scrolly.set)
scrolly.config(command=YearEntry.yview)
YearEntry.place(x=160, y=140, width = 300, height = 70)
scrolly.place(x=460, y=140, height = 70)
DepartmentLabel=Label(leftbox,text="Department",font=("Helvetica", 15),fg="#eae2b7",bg="brown")
DepartmentLabel.place(x=10, y=230)
scrolly=Scrollbar(leftbox,orient=VERTICAL)
DepartmentEntry=Text(leftbox, font=("Helvetica", 15),bd=0, yscrollcommand=scrolly.set)
scrolly.config(command=DepartmentEntry.yview)
DepartmentEntry.place(x=160, y=235, width = 300, height = 70)
scrolly.place(x=460, y=235, height = 70)

# RIGHT BOX
rightbox=Frame(root,bd=0,bg="indianred")
rightbox.place(x=500,y=140,width=390,height=350)

# RIGHT BOX HEADING
searchInput=Entry(rightbox,font=("Helvetica", 12),bd=0,width=17)
searchInput.place(x=10, y=10, height = 30)
dropdown=ttk.Combobox(rightbox,font=("Helvetica",10),state='readonly', width = 10)
dropdown['values']=("--Search By--", "Name", "Year", "Department")
dropdown.current(0)
dropdown.place(x=180, y=10, height = 30)
searchBtn=Button(rightbox,text="Search",command=search,font=("Helvetica", 12),width=10, bd = 0)
searchBtn.place(x=280, y=10, height = 30)

# BOX INSIDE RIGHT BOX
tabfrm=Frame(rightbox,bd=4,relief=RIDGE,bg="lightblue")
tabfrm.place(x=10,y=50,width=370,height=270)
scrolly=Scrollbar(tabfrm,orient=VERTICAL)
data_table=ttk.Treeview(tabfrm,columns=("name","department", "year"),yscrollcommand=scrolly.set)
scrolly.pack(side=RIGHT,fill=Y)
scrolly.config(command=data_table.yview)

note_text=Label(rightbox,font=("Helvetica", 10),bg="indianred",fg="white")
note_text.place(x=10, y=325)

# INSIDE RIGHT BOX
data_table.heading("name",text="Name")
data_table.heading("year",text="Year")
data_table.heading("department",text="Department")
data_table['show']="headings"
data_table.column("name",width = 10)
data_table.column("year",width=50)
data_table.column("department",width=30)
data_table.pack(fill=BOTH,expand=1)
data_table.bind("<ButtonRelease-1>",getdata)

search()

root.mainloop()