1.
# Import module
from tkinter import *
from tkinter import messagebox
import mysql.connector

# Create object
root = Tk()

# Adjust size
root.geometry("1280x800")
root.title('Login')

# Add image file
bg = PhotoImage(file = "D:\Amritha\currency\img.png")

def login():
    username = username_entry.get()
    password = password_entry.get()
    if username=='' or password=='':
        messagebox.showerror(title="Error", message="Invalid login.")              
    else:
         try:
          mydb=mysql.connector.connect(host='localhost',user='root',password='password',database='converter')
          mycursor =mydb.cursor()
          print("connected")
         
         except:
           messagebox.showerror("connection","Database connection not established")
           return
    command="use converter"
    mycursor.execute(command) 
    command="select * from login where username=%s and password=%s"
    mycursor.execute(command,(username,password))
    myresult= mycursor.fetchone()
    print(myresult)

    if myresult==None:
       
       messagebox.showinfo("invalid","Invalid username and password")

    else:
       
       messagebox.showinfo("Login","Successfully Login!!")
       root.destroy()
       import currency


13
         
        

# Create Canvas
canvas1 = Canvas( root, width = 1000,
				height = 400)

canvas1.pack(fill = "both", expand = True)

# Display image
canvas1.create_image( 0, 0, image = bg,
					anchor = "nw")

# Add Text
canvas1.create_text( 996, 220, text = "Login", font=("Times New Roman", 30))
canvas1.create_text( 930, 300, text = "Username", font=("Times New Roman", 20))
canvas1.create_text( 930, 400, text = "Password", font=("Times New Roman", 20))

#text bxes
username_entry = Entry(root, font=("Arial", 16))

password_entry = Entry(root, show="*", font=("Arial", 16))


# Create Buttons
button2 = Button( root, text = "Login" ,width = 10,
				height = 1, bg="#370466", fg="#FFFFFF", font=("Times New Roman", 16),command=login)

# Display Buttons
username_entry_canvas = canvas1.create_window( 875, 330, anchor = "nw",
									window = username_entry)
password_entry_canvas = canvas1.create_window( 875, 430, anchor = "nw",
									window = password_entry)

button2_canvas = canvas1.create_window( 925, 500,
									anchor = "nw",
									window = button2)

# Execute tkinter
root.mainloop()









14



2.
# Import module
import tkinter  as tk
from tkinter import Tk, ttk
from tkinter import *
from tkinter import messagebox

from PIL import Image, ImageTk

import requests
import json
import mysql.connector
#colors 
cor0 = "#FFFFFF"  # white
cor1 = "#333333"  # black
cor2 = "#EB5D51"  # red
btn = "#250071" #purple
mainc = "#EEF0FD"
subc = "#EDD399"
# Create object
root = Tk()


# Adjust size
root.geometry("1280x800")
root.title('Converter')

# Add image file
bg = PhotoImage(file = "D:\Amritha\currency\img1.png")

def history():
     root.destroy()
     import cnvrt


def convert():
    url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"

    currency_1 = combo1.get()
    currency_2 = combo2.get()
    amount = value.get()

    querystring = {"from":currency_1,"to":currency_2,"amount":amount}












15

    if currency_2 == 'USD':
        symbol = '$'
    elif currency_2 == 'INR':
        symbol = '₹'
    elif currency_2 == 'EUR':
        symbol = '€'
    elif currency_2 == 'BRL':
        symbol = 'R$'
    elif currency_2 == 'CAD':
        symbol = 'CA $'
        

    headers = {
        'x-rapidapi-host': "currency-converter18.p.rapidapi.com",
        'x-rapidapi-key': "90c59d6c9fmsh4599f814e2ffc92p17fc6djsndeaa0265ac61"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    data = json.loads(response.text)
    converted_amount = data["result"]["convertedAmount"]
    formatted = symbol + " {:,.2f}".format(converted_amount)

    result['text'] = formatted

    print(converted_amount, formatted)
    
    mydb=mysql.connector.connect(host='localhost',user='root',password='password',database='converter')
    mycursor =mydb.cursor()
    command="use converter"
    mycursor.execute(command) 
    query = "INSERT INTO  history (cfrom ,cto ,input ,output) VALUES(%s,%s,%s,%s)"
    id = mycursor.execute(query, (currency_1, currency_2, amount, formatted))
    
    mydb.commit()

# Create Canvas
canvas1 = Canvas( root, width = 1000,
		height = 400)

canvas1.pack(fill = "both", expand = True)

# Display image
canvas1.create_image( 0, 0, image = bg,
		anchor = "nw")







16


#main frame
app_name = Label(root, text = "Currency Converter", font=('Arial 20 bold'),fg=cor1,bg=mainc)
app_name.place(x=500, y=150)


c_name = Label(root, text = "Convert Here !", font=('Arial 20 bold underline'),bg=subc)
c_name.place(x=300, y=250)

H_name = Label(root, text = "History", font=('Arial 20 bold underline'), bg=subc)
H_name.place(x=800, y=360)

result = Label(root, text = " ",width=17, height=2, pady=2, relief="flat", anchor=CENTER, font=('Arial 15 bold'), bg=cor0, fg=cor1)                  
result.place(x=280, y=500) 

currency = ['CAD', 'BRL', 'EUR', 'INR', 'USD']

from_label = Label(root, text = "Convert From", width=11, height=1, pady=0, padx=0, anchor=NW, font=('Arial 10 bold'), bg=subc, fg=cor1)
from_label.place(x=280, y=320)
combo1 = ttk.Combobox(root, width=8, justify=CENTER, font=("Ivy 12 bold"))
combo1['values'] = (currency)
combo1.place(x=280, y=345)

to_label = Label(root, text = "Convert To", width=11, height=1, pady=0, padx=0, relief="flat", anchor=NW, font=('Arial 10 bold'), bg=subc, fg=cor1)
to_label.place(x=398, y=320)

combo2 = ttk.Combobox(root, width=8, justify=CENTER, font=("Ivy 12 bold"))
combo2['values'] = (currency)
combo2.place(x=400, y=345)

in_label = Label(root, text = "Enter Amount", width=11, height=1, pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=subc, fg=cor1)
in_label.place(x=280, y=380)

value = Entry(root, width=22, justify=CENTER, font=("Ivy 12 bold"), relief=SOLID)
value.place(x=280, y=410)

button = Button(root, text="Convert", width=18, padx=5, height=1, bg=btn, fg=cor0,font=("Ivy 12 bold"), command=convert)
button.place(x=280, y=440)

res_label = Label(root, text = "Result", width=11, height=1, pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=subc, fg=cor1)
res_label.place(x=350, y=480)






17


button = Button(root, text="Click here to view History", width=18, padx=5, height=1, bg=btn, fg=cor0,font=("Ivy 12 bold"), command=history)
button.place(x=750, y=450)
    
# Execute tkinter
root.mainloop()









































18




3. 
import mysql.connector
import tkinter  as tk 
from tkinter import * 
my_w = tk.Tk()
my_w.geometry("400x250") 
my_w.title('history')
mydb=mysql.connector.connect(host='localhost',user='root',password='password',database='converter')


my_conn = mydb.cursor()
####### end of connection ####
my_conn.execute("SELECT * FROM history limit 0,10")
e=Label(my_w,width=10,text='From',borderwidth=3, relief='ridge',anchor='w',bg='beige')
e.grid(row=0,column=0)
e=Label(my_w,width=10,text='To',borderwidth=3, relief='ridge',anchor='w',bg='beige')
e.grid(row=0,column=1)
e=Label(my_w,width=10,text='Amount',borderwidth=3, relief='ridge',anchor='w',bg='beige')
e.grid(row=0,column=2)
e=Label(my_w,width=10,text='Result',borderwidth=3, relief='ridge',anchor='w',bg='beige')
e.grid(row=0,column=3)
i=1
for student in my_conn: 
    for j in range(len(student)):
        e=Label(my_w,width=10, text=student[j],borderwidth=3,relief='ridge', anchor="w") 
        e.grid(row=i, column=j) 
    i=i+1
my_w.mainloop()

# currencyconverter