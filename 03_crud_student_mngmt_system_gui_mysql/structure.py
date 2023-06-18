from tkinter import font
from turtle import width
import pymysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk

master = Tk()
master.title('Student Registration System')
master.geometry('1280x720')
my_tree = ttk.Treeview(master)
#print(my_tree)

# placeholder for entry
ph1 = tk.StringVar()
ph2 = tk.StringVar()
ph3 = tk.StringVar()
ph4 = tk.StringVar()
ph5 = tk.StringVar()

def set_placeholder(word, num):
    if num == 1:
        ph1.set(word)
    if num == 2:
        ph2.set(word)
    if num == 3:
        ph3.set(word)
    if num == 4:
        ph4.set(word)
    if num == 5:
        ph5.set(word)

# connection to mysql
def connections():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        db='student_bd'
    )
    return conn

def refresh_table():
    for data in my_tree.get_children():
        #print(data)
        my_tree.delete(data)
        
    for array in read():
        my_tree.insert(parent='', index='end', iid=array, text='', values=(array), tag='orow')
        
    my_tree.tag_configure('orow', background='#EEEEEE', font='arial 12')
    my_tree.grid(row=8, column=0, rowspan=11, columnspan=5, padx=10, pady=20)
    
def read():
    conn = connections()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students')
    result = cursor.fetchall()
    conn.commit()
    conn.close()
    return result

def add():
    
    s_id = str(student_id_entry.get())
    f_name = str(first_name_entry.get())
    l_name = str(last_name_entry.get())
    add_address = str(address_entry.get())
    add_phone = str(phone_entry.get())
    
    if (s_id == '' or s_id == ' ') or (f_name == '' or f_name == ' ') or (l_name == '' or l_name == ' ') or (add_address == '' or add_address == ' ') or (add_phone == '' or add_phone == ' '):
        messagebox.showerror('Error', 'Please fill all the blank entry')
        return
    else:
        try:
            conn = connections()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO students VALUES ('"+s_id+"', '"+f_name+"', '"+l_name+"', '"+add_address+"', '"+add_phone+"')")
            conn.commit()
            conn.close()
            
        except:
            messagebox.showinfo('Error','Student id already exist')
            return
    refresh_table()
    
        
def update_but():
    select_st_id =''    
    try:
        select_item = my_tree.selection()[0]
        select_st_id = str(my_tree.item(select_item)['values'][0])
    except:
        messagebox.showinfo('Error', 'Please select a data row')
        return
    #print('line 98')
    update_id = str(student_id_entry.get())
    update_f_name = str(first_name_entry.get())
    update_l_name = str(last_name_entry.get())
    update_address = str(address_entry.get())
    update_phone = str(phone_entry.get())    
    
    if (update_id == '' or update_id == ' ') or (update_f_name == '' or update_f_name == ' ') or (update_l_name == '' or update_l_name == ' ') or (update_address == '' or update_address == ' ') or (update_phone == '' or update_phone == ' '):
        messagebox.showerror('Error', 'Please fill all the blank entry')
        return
    else:
        try:
            conn = connections()
            cursor = conn.cursor()
            cursor.execute("UPDATE students SET STUDENTID='"+
                           update_id+"', FIRSTNAME= '"+
                           update_f_name+"', LASTNAME= '"+
                           update_l_name+"', ADDRESS= '"+
                           update_address+"', PHONE= '"+
                           update_phone+"' WHERE STUDENTID='"+
                           select_st_id+"' ")
            conn.commit()
            conn.close()
        except:
            messagebox.showerror('Error', 'Student id already exist')
            return
            
    refresh_table()
    

# delete the selacted data
def delete():
    dicision = messagebox.askquestion('Warning!', 'Delete the selacted data?')
    
    if dicision != 'yes':
        return
    else:
        selected_item = my_tree.selection()[0]
        #print(selected_item)
        delete_data = str(my_tree.item(selected_item)['values'][0])
        #print(delete_data)
        try:
            conn = connections()
            cursor = conn.cursor()
            cursor.execute('DELETE FROM students WHERE STUDENTID= "'+str(delete_data)+'"')
            conn.commit()
            conn.close()
        except:
            messagebox.showerror('Error', 'Sorry an error ocured')
            return
        
    refresh_table()

def search():
    sr_st_id = (student_id_entry.get())
    sr_f_name = (first_name_entry.get())
    sr_l_name = (last_name_entry.get())
    sr_address = (address_entry.get())
    sr_phone = (phone_entry.get())
    
    conn = connections()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE STUDENTID='"+
                   sr_st_id+"' or FIRSTNAME= '"+
                   sr_f_name+"' or LASTNAME= '"+
                   sr_l_name+"' or ADDRESS= '"+
                   sr_address+"' or PHONE= '"+
                   sr_phone+"' ")
    
    try:
       result = cursor.fetchall()
       #print(result)
       for num in range(0,5):
           set_placeholder(result[0][num],(num+1))
           
       conn.commit()
       conn.close()
    except:
        messagebox.showerror('Error', 'No data found')
        return

# reset or delete data from data bese
def reset():
    dicision = messagebox.askquestion('Warning!', 'Delete all data?')
    
    if dicision != 'yes':
        return
    else:
        try:
            conn = connections()
            cursor = conn.cursor()
            cursor.execute('DELETE FROM students')
            conn.commit()
            conn.close()
        except:
            messagebox.showerror('Error', 'Sorry an error ocured')
            return
        
    refresh_table()

def select():    
        try:
            selected_item = my_tree.selection()[0]
            select_st_id = str(my_tree.item(selected_item)['values'][0])
            select_f_name = str(my_tree.item(selected_item)['values'][1])
            select_l_name = str(my_tree.item(selected_item)['values'][2])
            select_address = str(my_tree.item(selected_item)['values'][3])
            select_phone = str(my_tree.item(selected_item)['values'][4])
            
            set_placeholder(select_st_id, 1)
            set_placeholder(select_f_name, 2)
            set_placeholder(select_l_name, 3)
            set_placeholder(select_address, 4)
            set_placeholder(select_phone, 5)
            
        except:
            messagebox.showerror('Error', 'Please select a data row')
            return

# gui
crud_label = Label(master, text='Student Registration System (CRUD MATRIX)', font=('arial bold',30))
crud_label.grid(row=0, column=0, rowspan=2, columnspan=8, padx=50, pady=40)

#======================= Label ===================================
student_id_label = Label(master, text='Student ID: ', font='arial 15')
first_name_label = Label(master, text='First Name: ', font='arial 15')
last_name_label = Label(master, text='Last Name: ', font='arial 15')
address_label = Label(master, text='Address: ', font='arial 15')
phone_label = Label(master, text='Phone number: ', font='arial 15')

student_id_label.grid(row=3, column=0, columnspan=1, padx=50, pady=5)
first_name_label.grid(row=4, column=0, columnspan=1, padx=50, pady=5)
last_name_label.grid(row=5, column=0, columnspan=1, padx=50, pady=5)
address_label.grid(row=6, column=0, columnspan=1, padx=50, pady=5)
phone_label.grid(row=7, column=0, columnspan=1, padx=50, pady=5)

#============================ Entry ===============================
student_id_entry = Entry(master, width=55, bd=5, font='arial 15', textvariable= ph1)
first_name_entry = Entry(master, width=55, bd=5, font='arial 15', textvariable= ph2)
last_name_entry = Entry(master, width=55, bd=5, font='arial 15', textvariable= ph3)
address_entry = Entry(master, width=55, bd=5, font='arial 15', textvariable= ph4)
phone_entry = Entry(master, width=55, bd=5, font='arial 15', textvariable= ph5)

student_id_entry.grid(row=3, column=1, columnspan=4, padx=5, pady=0)
first_name_entry.grid(row=4, column=1, columnspan=4, padx=5, pady=0)
last_name_entry.grid(row=5, column=1, columnspan=4, padx=5, pady=0)
address_entry.grid(row=6, column=1, columnspan=4, padx=5, pady=0)
phone_entry.grid(row=7, column=1, columnspan=4, padx=5, pady=0)

#============================= Button ============================
add_button = Button(
    master, text='Add', padx=65, pady=25, width=10, bd=5, font='arial 15', bg='#84f894' , command= add
)
update_button = Button(
    master, text='Update', padx=65, pady=25, width=10, bd=5, font='arial 15', bg='#84E8F8', command= update_but
)
delete_button = Button(
    master, text='Delete', padx=65, pady=25, width=10, bd=5, font='arial 15', bg='#FF9999', command= delete
)
search_button = Button(
    master, text='Search', padx=65, pady=25, width=10, bd=5, font='arial 15', bg='#F4FE82', command= search
)
reset_button = Button(
    master, text='Reset', padx=65, pady=25, width=10, bd=5, font='arial 15', bg='#F398FF', command= reset
)
select_button = Button(
    master, text='Select', padx=65, pady=25, width=10, bd=5, font='arial 15', bg='#84F894', command= select
)

add_button.grid(row=3, column=5,columnspan=1, rowspan=2)
update_button.grid(row=5, column=5, columnspan=1, rowspan=2)
delete_button.grid(row=7, column=5, columnspan=1, rowspan=2)
search_button.grid(row=9, column=5, columnspan=1, rowspan=2)
reset_button.grid(row=11, column=5, columnspan=1, rowspan=2)
select_button.grid(row=13, column=5, columnspan=1, rowspan=2)

# style of database 
style = ttk.Style()
style.configure('Treeview.Heading', font=('arial bold',15))

my_tree['columns'] = ('Student ID', 'First Name', 'Last Name', 'Address', 'Phone')

my_tree.column('#0', width=0, stretch= NO)
my_tree.column('Student ID', anchor=W, width=170)
my_tree.column('First Name', anchor=W, width=150)
my_tree.column('Last Name', anchor=W, width=150)
my_tree.column('Address', anchor=W, width=165)
my_tree.column('Phone', anchor=W, width=150)

my_tree.heading('Student ID', text='Student ID', anchor=W)
my_tree.heading('First Name', text='First Name', anchor=W)
my_tree.heading('Last Name', text='Last Name', anchor=W)
my_tree.heading('Address', text='Address', anchor=W)
my_tree.heading('Phone', text='Phone', anchor=W)

refresh_table()

master.mainloop()
