import sqlite3
from tkinter import *
from tkinter import ttk

master = Tk()
master.title('Inventory System')
master.geometry('1030x380')
my_tree = ttk.Treeview(master)

def reverse(tuples):
    new_tup = tuples[:: -1]
    return new_tup

#=========================== insert ==============================
def insertt(id , name, price, quantity):
    conn = sqlite3.connect('data_db')
    cursor = conn.cursor()
    cursor.execute(""" CREATE TABLE IF NOT EXISTS
    inventory(itemId TEXT, itemName TEXT, itemPrice TEXT, itemQuantity TEXT)""")
    
    cursor.execute("INSERT INTO inventory VALUES('"+
                   str(id)+"','"+
                   str(name)+"', '"+
                   str(price)+"', '"+
                   str(quantity)+"' )")
    conn.commit()
    
def delete(data):
    conn = sqlite3.connect('data_db')
    cursor = conn.cursor()
    cursor.execute(""" CREATE TABLE IF NOT EXISTS
    inventory(itemId TEXT, itemName TEXT, itemPrice TEXT, itemQuantity TEXT)""")
    
    cursor.execute("DELETE FROM inventory WHERE itemId= '"+str(data)+"' ")
    conn.commit()
    
#============================ update =============================   
def update(id, name, price, quantity, idname):
    conn = sqlite3.connect('data_db')
    cursor = conn.cursor()
    cursor.execute(""" CREATE TABLE IF NOT EXISTS
    inventory(itemId TEXT, itemName TEXT, itemPrice TEXT, itemQuantity TEXT)""")
    
    cursor.execute("UPDATE inventory SET itemId= '"+
                   str(id)+"', itemName= '"+
                   str(name)+"', itemPrice= '"+
                   str(price)+"', itemQuantity= '"+
                   str(quantity)+"' WHERE itemId='"+
                   str(idname)+"' ")
    

    conn.commit()
    
#============================ read =============================    
def read():
    conn = sqlite3.connect('data_db')
    cursor = conn.cursor()
    cursor.execute(""" CREATE TABLE IF NOT EXISTS
    inventory(itemId TEXT, itemName TEXT, itemPrice TEXT, itemQuantity TEXT)""")
    
    cursor.execute("SELECT * FROM inventory")
    result = cursor.fetchall()
    conn.commit()
    return result

#========================== insert data =========================
def insert_data():
    
    item_id = str(id_entry.get())
    item_name = str(name_entry.get())
    item_price = str(price_entry.get())
    item_quantity = str(quantity_entry.get())
    
    if item_id == '' or item_id == ' ':
        print('Error inserting Id!')
    if item_name == '' or item_name == ' ':
        print('Error inserting Name!')
    if item_price == '' or item_price == ' ':
        print('Error inserting Price!')
    if item_quantity == '' or item_quantity == ' ':
        print('Error inserting Quantity!')
    
    else:
        insertt(str(item_id), str(item_name), str(item_price), str(item_quantity))
    
    
    for data in my_tree.get_children():
        my_tree.delete(data)
    
       
    for res in reverse(read()):
        item_idd = len(my_tree.get_children())
        my_tree.insert(parent='' , index='end', iid=item_idd, text='', values=(res), tag='orow')   
     
    my_tree.tag_configure('orow', background='#EEEEEE', font=('arial bold',15))
    my_tree.grid(row=1, column=5, columnspan=4, rowspan=5, padx=10, pady=10)
    
#======================== delete data ============================
def delete_data():
    select_item = my_tree.selection()[0]
    delete_d = str(my_tree.item(select_item)['values'][0])
    delete(delete_d)
    
    for data in my_tree.get_children():
        my_tree.delete(data)
        
    for result in reverse(read()):
        item_id = len(my_tree.get_children())
        my_tree.insert(parent='' , index='end', iid=item_id, text='', values=(result), tag='orow')   
     
    my_tree.tag_configure('orow', background='#EEEEEE', font=('arial bold',15))
    my_tree.grid(row=1, column=5, columnspan=4, rowspan=5, padx=10, pady=10)
    
#======================== update data ===========================
def update_data():
     
    selet_data = my_tree.selection()[0]
    update_d = str(my_tree.item(selet_data)['values'][0])
    update(id_entry.get(), name_entry.get(), price_entry.get(), quantity_entry.get(), update_d)

    
    for data in my_tree.get_children():
        my_tree.delete(data)
        
    for result in reverse(read()):
        item_id = len(my_tree.get_children())
        my_tree.insert(parent='' , index='end', iid=item_id, text='', values=(result), tag='orow')   
     
    my_tree.tag_configure('orow', background='#EEEEEE', font=('arial bold',15))
    my_tree.grid(row=1, column=5, columnspan=4, rowspan=5, padx=10, pady=10)
    
    
#====================== All label ======================
title_label = Label(master, text='Store Name', font=('arial bold',30), bd=2 )
title_label.grid(row=0, column=0, columnspan=8, padx=20, pady=20)


id_label = Label(master, text='ID', font=('arial bold', 15))
name_label = Label(master, text='Name', font=('arial bold', 15))
price_label = Label(master, text='Price', font=('arial bold', 15))
quantity_label = Label(master, text='Quantity', font=('arial bold', 15))

id_label.grid(row=1, column=1,padx=10, pady=10)
name_label.grid(row=2, column=1,padx=10, pady=10)
price_label.grid(row=3, column=1,padx=10, pady=10)
quantity_label.grid(row=4, column=1,padx=10, pady=10)

#========================= All entries ===================
# id = IntVar()
# name = StringVar()
# price = StringVar()
# quantity = IntVar()

id_entry = Entry(master, width=25, bd=5, font=('arial bold',15))
name_entry = Entry(master, width=25, bd=5, font=('arial bold',15))
price_entry = Entry(master, width=25, bd=5, font=('arial bold',15))
quantity_entry = Entry(master, width=25, bd=5, font=('arial bold',15))

id_entry.grid(row=1, column=2, columnspan=3, padx=5, pady=5 )
name_entry.grid(row=2, column=2, columnspan=3, padx=5, pady=5 )
price_entry.grid(row=3, column=2, columnspan=3, padx=5, pady=5 )
quantity_entry.grid(row=4, column=2, columnspan=3, padx=5, pady=5 )

#========================= All button ======================
button_enter = Button(master, text='Enter', padx=5, pady=5, bd=3, font=('arial bold',15), bg='#0099ff', command= insert_data)
button_update = Button(master, text='Update', padx=5, pady=5, bd=3, font=('arial bold',15), bg='#ffff00', command= update_data)
button_delete = Button(master, text='Delete', padx=5, pady=5, bd=3, font=('arial bold',15), bg='#e62e00', command= delete_data)

button_enter.grid(row=5, column=2, columnspan=1)
button_update.grid(row=5, column=3, columnspan=1)
button_delete.grid(row=5, column=4, columnspan=1)

#======================== style ============================

style = ttk.Style()
style.configure('Treeview.Heading', font=('arial bold',15))

my_tree['columns'] = ('ID', 'NAME', 'PRICE', 'QUANTITY')

my_tree.column('#0', width=0, stretch= NO)
my_tree.column('ID', anchor= W, width= 150)
my_tree.column('NAME', anchor= W, width= 150)
my_tree.column('PRICE', anchor= W, width= 150)
my_tree.column('QUANTITY', anchor= W, width= 150)

my_tree.heading('ID', text='ID', anchor= W)
my_tree.heading('NAME', text='NAME', anchor= W)
my_tree.heading('PRICE', text='PRICE', anchor= W)
my_tree.heading('QUANTITY', text='QUANTITY', anchor= W)

my_tree.tag_configure('orow', background='#EEEEEE', font=('arial bold',15))
my_tree.grid(row=1, column=5, columnspan=4, rowspan=5, padx=10, pady=10)



master.mainloop()