from tkinter import *
from tkinter import messagebox,filedialog
from tkinter.ttk import Treeview
from tkinter import ttk
import pymysql
import pandas
import time
import random

master = Tk()
master.title('Student Registration System')
master.config(bg='gold3')
master.geometry('1174x700+200+50')
master.resizable(False, False)


############################# button command function ###############
def add_student():
    #print('add student')
    def submit_button():
        #print('add student submit button')
        add_i = id_val.get()
        add_n = name_val.get()
        add_m = mobile_val.get()
        add_e = email_val.get()
        add_a = address_val.get()
        add_g = gender_val.get()
        add_d = dob_val.get()
        #print(add_i,add_n,add_m,add_e,add_a,add_g,add_d)
        
        add_time = time.strftime('%H:%M:%S')
        add_date = time.strftime('%d-%m-%y')
        
        if (add_i == '' or add_i == ' ') or (add_n == '' or add_n == ' ') or (add_m == '' or add_m == ' ') or (add_e == '' or add_e == ' ') or (add_a == '' or add_a == ' ') or (add_g == '' or add_g == ' ') or (add_d == '' or add_d == ' '):
            messagebox.showinfo('Notification', 'All field are required*', parent= add_master)
            return
        else:
            try:
                insert_data = 'insert into student_table values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                cursor.execute(insert_data,(add_i,add_n,add_m,add_e,add_a,add_g,add_d,add_time, add_date))
                conn.commit()
                
                # After inser will clean the form
                res = messagebox.askyesnocancel('Notification', 'ID {} NAME {} added successfully.and want to clean the form'.format(add_i,add_n),parent=add_master)
                if res == True:
                    id_val.set('')
                    name_val.set('')
                    mobile_val.set('')
                    email_val.set('')
                    address_val.set('')
                    gender_val.set('')
                    dob_val.set('')
                    
            except:
                messagebox.showerror('Error','Id {} already exist.Try another one!'.format(add_i))
            
        # show all data into treeview screen from database    
        show_all = 'select * from student_table'
        cursor.execute(show_all)
        datas = cursor.fetchall()
        show_treeview.delete(* show_treeview.get_children()) # delete from the database first
        
        for i in datas:
            vv = (i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8])
            show_treeview.insert('',END,values=vv)
        
        
        
    
    add_master = Toplevel()
    add_master.title('Add Student')
    add_master.geometry('470x470+220+200')
    add_master.grab_set()
    add_master.resizable(False, False)
    add_master.config(bg='blue')
    #add_master.iconbitmap('mngmmt.png')
    
    #------------------ Add student label --------------
    id_label = Label(add_master, text='Enter ID: ', font=('times',20,'bold'), bg='gold2', relief=GROOVE, borderwidth=3, width=12, anchor='w')
    id_label.place(x=10, y=10)
    
    name_label = Label(add_master, text='Enter Name: ', font=('times',20,'bold'), bg='gold2', relief=GROOVE, borderwidth=3, width=12, anchor='w')
    name_label.place(x=10, y=70)
    
    mobile_label = Label(add_master, text='Enter Mobile: ', font=('times',20,'bold'), bg='gold2', relief=GROOVE, borderwidth=3, width=12, anchor='w')
    mobile_label.place(x=10, y=130)
    
    email_label = Label(add_master, text='Enter Email: ', font=('times',20,'bold'), bg='gold2', relief=GROOVE, borderwidth=3, width=12, anchor='w')
    email_label.place(x=10, y=190)
    
    address_label = Label(add_master, text='Enter Address: ', font=('times',20,'bold'), bg='gold2', relief=GROOVE, borderwidth=3, width=12, anchor='w')
    address_label.place(x=10, y=250)
    
    gender_label = Label(add_master, text='Enter Gender: ', font=('times',20,'bold'), bg='gold2', relief=GROOVE, borderwidth=3, width=12, anchor='w')
    gender_label.place(x=10, y=310)
    
    dob_label = Label(add_master, text='Enter D.O.B: ', font=('times',20,'bold'), bg='gold2', relief=GROOVE, borderwidth=3, width=12, anchor='w')
    dob_label.place(x=10, y=370)
    
    #------------------ Add student entries --------------
    id_val = StringVar()
    name_val = StringVar()
    mobile_val = StringVar()
    email_val = StringVar()
    address_val = StringVar()
    gender_val = StringVar()
    dob_val = StringVar()
    
    id_entry = Entry(add_master, textvariable= id_val, font=('roman',15,'bold'), bd=5)
    id_entry.place(x=240, y=10)
    
    name_entry = Entry(add_master, textvariable= name_val, font=('roman',15,'bold'), bd=5)
    name_entry.place(x=240, y=70)
    
    mobile_entry = Entry(add_master, textvariable= mobile_val, font=('roman',15,'bold'), bd=5)
    mobile_entry.place(x=240, y=130)
    
    email_entry = Entry(add_master, textvariable= email_val, font=('roman',15,'bold'), bd=5)
    email_entry.place(x=240, y=190)
    
    address_entry = Entry(add_master, textvariable= address_val, font=('roman',15,'bold'), bd=5)
    address_entry.place(x=240, y=250)
    
    gender_entry = Entry(add_master, textvariable= gender_val, font=('roman',15,'bold'), bd=5)
    gender_entry.place(x=240, y=310)
    
    dob_entry = Entry(add_master, textvariable= dob_val, font=('roman',15,'bold'), bd=5)
    dob_entry.place(x=240, y=370)
    
    #========== connect db button ===============
    add_button = Button(add_master, text='Submit', font=('roman',15,'bold'), width=20, 
                        bd=5, activebackground='green2', activeforeground='white',command= submit_button)
    add_button.place(x=140, y=415)
    
    

def search_student():
    #print('search student')
    def src_button():
        #print('done src')
        sr_i = id_val.get()
        sr_n = name_val.get()
        sr_m = mobile_val.get()
        sr_e = email_val.get()
        sr_a = address_val.get()
        sr_g = gender_val.get()
        sr_d = dob_val.get()
        sr_date = date_val.get()
        src_time = time.strftime('%H:%M:%S')
        
        if sr_i != '':
            select_id = 'select * from student_table where ID = %s'
            cursor.execute(select_id, (sr_i))
            datas = cursor.fetchall()
            show_treeview.delete(* show_treeview.get_children()) # delete from database first
            
            for i in datas:
                vv = (i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8])
                show_treeview.insert('',END,values=vv)
                
        elif sr_n != '':
            select_id = 'select * from student_table where NAME = %s'
            cursor.execute(select_id, (sr_n))
            datas = cursor.fetchall()
            show_treeview.delete(* show_treeview.get_children()) # delete from database first
            
            for i in datas:
                vv = (i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8])
                show_treeview.insert('',END,values=vv)
        elif sr_m != '':
            select_id = 'select * from student_table where MOBILE = %s'
            cursor.execute(select_id, (sr_i))
            datas = cursor.fetchall()
            show_treeview.delete(* show_treeview.get_children()) # delete from database first
            
            for i in datas:
                vv = (i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8])
                show_treeview.insert('',END,values=vv)
                
        elif sr_e != '':
            select_id = 'select * from student_table where EMAIL = %s'
            cursor.execute(select_id, (sr_e))
            datas = cursor.fetchall()
            show_treeview.delete(* show_treeview.get_children()) # delete from database first
            
            for i in datas:
                vv = (i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8])
                show_treeview.insert('',END,values=vv)
                
        elif sr_a != '':
            select_id = 'select * from student_table where ADDRESS = %s'
            cursor.execute(select_id, (sr_a))
            datas = cursor.fetchall()
            show_treeview.delete(* show_treeview.get_children()) # delete from database first
            
            for i in datas:
                vv = (i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8])
                show_treeview.insert('',END,values=vv)
                
        elif sr_g != '':
            select_id = 'select * from student_table where GENDER = %s'
            cursor.execute(select_id, (sr_g))
            datas = cursor.fetchall()
            show_treeview.delete(* show_treeview.get_children()) # delete from database first
            
            for i in datas:
                vv = (i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8])
                show_treeview.insert('',END,values=vv)
                
        elif sr_d != '':
            select_id = 'select * from student_table where D.O.B = %s'
            cursor.execute(select_id, (sr_d))
            datas = cursor.fetchall()
            show_treeview.delete(* show_treeview.get_children()) # delete from database first
            
            for i in datas:
                vv = (i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8])
                show_treeview.insert('',END,values=vv)
                
        elif sr_date != '':
            select_id = 'select * from student_table where DATE = %s'
            cursor.execute(select_id, (sr_date))
            datas = cursor.fetchall()
            show_treeview.delete(* show_treeview.get_children()) # delete from database first
            
            for i in datas:
                vv = (i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8])
                show_treeview.insert('',END,values=vv)
                
        elif src_time != '':
            select_id = 'select * from student_table where TIME = %s'
            cursor.execute(select_id, (src_time))
            datas = cursor.fetchall()
            show_treeview.delete(* show_treeview.get_children()) # delete from database first
            
            for i in datas:
                vv = (i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8])
                show_treeview.insert('',END,values=vv)
                
            #============= END ==========
            
        
        
    search_master = Toplevel()
    search_master.title('Search Student')
    search_master.geometry('470x530+220+200')
    search_master.grab_set()
    search_master.resizable(False, False)
    search_master.config(bg='red')
    search_master.iconbitmap('stu.ico')
    
    #------------------ Search student label --------------
    id_label = Label(search_master, text='Enter ID: ', font=('times',20,'bold'), bg='gold2', relief=GROOVE, borderwidth=3, width=12, anchor='w')
    id_label.place(x=10, y=10)
    
    name_label = Label(search_master, text='Enter Name: ', font=('times',20,'bold'), bg='gold2', relief=GROOVE, borderwidth=3, width=12, anchor='w')
    name_label.place(x=10, y=70)
    
    mobile_label = Label(search_master, text='Enter Mobile: ', font=('times',20,'bold'), bg='gold2', relief=GROOVE, borderwidth=3, width=12, anchor='w')
    mobile_label.place(x=10, y=130)
    
    email_label = Label(search_master, text='Enter Email: ', font=('times',20,'bold'), bg='gold2', relief=GROOVE, borderwidth=3, width=12, anchor='w')
    email_label.place(x=10, y=190)
    
    address_label = Label(search_master, text='Enter Address: ', font=('times',20,'bold'), bg='gold2', relief=GROOVE, borderwidth=3, width=12, anchor='w')
    address_label.place(x=10, y=250)
    
    gender_label = Label(search_master, text='Enter Gender: ', font=('times',20,'bold'), bg='gold2', relief=GROOVE, borderwidth=3, width=12, anchor='w')
    gender_label.place(x=10, y=310)
    
    dob_label = Label(search_master, text='Enter D.O.B: ', font=('times',20,'bold'), bg='gold2', relief=GROOVE, borderwidth=3, width=12, anchor='w')
    dob_label.place(x=10, y=370)
    
    date_label = Label(search_master, text='Enter Date : ', font=('times',20,'bold'), bg='gold2', relief=GROOVE, borderwidth=3, width=12, anchor='w')
    date_label.place(x=10, y=430)
    
    #------------------ Search student entries --------------
    id_val = StringVar()
    name_val = StringVar()
    mobile_val = StringVar()
    email_val = StringVar()
    address_val = StringVar()
    gender_val = StringVar()
    dob_val = StringVar()
    date_val = StringVar()
    
    id_entry = Entry(search_master, textvariable= id_val, font=('roman',15,'bold'), bd=5)
    id_entry.place(x=240, y=10)
    
    name_entry = Entry(search_master, textvariable= name_val, font=('roman',15,'bold'), bd=5)
    name_entry.place(x=240, y=70)
    
    mobile_entry = Entry(search_master, textvariable= mobile_val, font=('roman',15,'bold'), bd=5)
    mobile_entry.place(x=240, y=130)
    
    email_entry = Entry(search_master, textvariable= email_val, font=('roman',15,'bold'), bd=5)
    email_entry.place(x=240, y=190)
    
    address_entry = Entry(search_master, textvariable= address_val, font=('roman',15,'bold'), bd=5)
    address_entry.place(x=240, y=250)
    
    gender_entry = Entry(search_master, textvariable= gender_val, font=('roman',15,'bold'), bd=5)
    gender_entry.place(x=240, y=310)
    
    dob_entry = Entry(search_master, textvariable= dob_val, font=('roman',15,'bold'), bd=5)
    dob_entry.place(x=240, y=370)
    
    date_entry = Entry(search_master, textvariable= date_val, font=('roman',15,'bold'), bd=5)
    date_entry.place(x=240, y=430)
    
    #========== student search button ===============
    add_button = Button(search_master, text='Submit', font=('roman',15,'bold'), width=20,
                        bd=5, activebackground='green2', activeforeground='white', command= src_button)
    add_button.place(x=140, y=475)

def delete_student():
    cc = show_treeview.focus() # tracking 
    c_item = show_treeview.item(cc) # get all the item of tracking object
    #print(c_item)
    v_id = c_item['values'][0] # get ID primary key 
    #print(v_id)
    query_del = 'delete from student_table where ID = %s'
    cursor.execute(query_del, (v_id))
    conn.commit()
    messagebox.showinfo('Notification', 'ID {} delete successfully'.format(v_id))
    
    # get all data from database
    select_i = 'select * from student_table'
    cursor.execute(select_i)
    datas = cursor.fetchall()
    show_treeview.delete(* show_treeview.get_children()) # delete from database first
            
    for i in datas:
        vv = (i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8])
        show_treeview.insert('',END,values=vv)
    

def update_student():
    #print('update student')
    def update():
        up_i = id_val.get()
        up_n = name_val.get()
        up_m = mobile_val.get()
        up_e = email_val.get()
        up_a = address_val.get()
        up_g = gender_val.get()
        up_d = dob_val.get()
        up_date = date_val.get()
        up_time = time_val.get()
        #print(up_i,up_n,up_m,up_e,up_a,up_g,up_d,up_date,up_time)
        
        if (up_i == '' or up_i == ' ') or (up_n == '' or up_n == ' ') or (up_m == '' or up_m == ' ') or (up_e == '' or up_e == ' ') or (up_a == '' or up_a == ' ') or (up_g == '' or up_g == ' ') or (up_d == '' or up_d == ' '):
            messagebox.showinfo('Notification', 'All field are required*', parent= update_master)
            return
        else:
            up_query = 'update student_table set NAME = %s, MOBILE = %s, EMAIL = %s, ADDRESS = %s, GENDER = %s, DOB = %s, TIME = %s, DATE = %s where ID = %s'
            cursor.execute(up_query, (up_n,up_m,up_e,up_a,up_g,up_d,up_date,up_time, up_i))
            conn.commit()
            messagebox.showinfo('Notification', 'ID {} data updated successfully'.format(up_i), parent= update_master)
            
            # get all data from database
            all_query = 'select * from student_table'
            cursor.execute(all_query)
            datas = cursor.fetchall()
            show_treeview.delete(* show_treeview.get_children()) # delete from database
            
            for i in datas:
                val = (i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8])
                show_treeview.insert('',END, values=val)
    
    update_master = Toplevel()
    update_master.title('Update Student')
    update_master.geometry('470x600+220+160')
    update_master.grab_set()
    update_master.resizable(False, False)
    update_master.config(bg='red')
    #update_master.iconbitmap('mngmmt.png')
    
    #------------------ Update student label --------------
    id_label = Label(update_master, text='Update ID: ', font=('times',20,'bold'), bg='gold2', relief=GROOVE, borderwidth=3, width=12, anchor='w')
    id_label.place(x=10, y=10)
    
    name_label = Label(update_master, text='Enter Name: ', font=('times',20,'bold'), bg='gold2', relief=GROOVE, borderwidth=3, width=12, anchor='w')
    name_label.place(x=10, y=70)
    
    mobile_label = Label(update_master, text='Update Mobile: ', font=('times',20,'bold'), bg='gold2', relief=GROOVE, borderwidth=3, width=12, anchor='w')
    mobile_label.place(x=10, y=130)
    
    email_label = Label(update_master, text='Update Email: ', font=('times',20,'bold'), bg='gold2', relief=GROOVE, borderwidth=3, width=12, anchor='w')
    email_label.place(x=10, y=190)
    
    address_label = Label(update_master, text='Update Address: ', font=('times',20,'bold'), bg='gold2', relief=GROOVE, borderwidth=3, width=12, anchor='w')
    address_label.place(x=10, y=250)
    
    gender_label = Label(update_master, text='Update Gender: ', font=('times',20,'bold'), bg='gold2', relief=GROOVE, borderwidth=3, width=12, anchor='w')
    gender_label.place(x=10, y=310)
    
    dob_label = Label(update_master, text='Update D.O.B: ', font=('times',20,'bold'), bg='gold2', relief=GROOVE, borderwidth=3, width=12, anchor='w')
    dob_label.place(x=10, y=370)
    
    date_label = Label(update_master, text='Update Date : ', font=('times',20,'bold'), bg='gold2', relief=GROOVE, borderwidth=3, width=12, anchor='w')
    date_label.place(x=10, y=430)
    
    time_label = Label(update_master, text='Update Time : ', font=('times',20,'bold'), bg='gold2', relief=GROOVE, borderwidth=3, width=12, anchor='w')
    time_label.place(x=10, y=490)
    
    
    #------------------ Update student entries --------------
    id_val = StringVar()
    name_val = StringVar()
    mobile_val = StringVar()
    email_val = StringVar()
    address_val = StringVar()
    gender_val = StringVar()
    dob_val = StringVar()
    date_val = StringVar()
    time_val = StringVar()
    
    id_entry = Entry(update_master, textvariable= id_val, font=('roman',15,'bold'), bd=5)
    id_entry.place(x=240, y=10)
    
    name_entry = Entry(update_master, textvariable= name_val, font=('roman',15,'bold'), bd=5)
    name_entry.place(x=240, y=70)
    
    mobile_entry = Entry(update_master, textvariable= mobile_val, font=('roman',15,'bold'), bd=5)
    mobile_entry.place(x=240, y=130)
    
    email_entry = Entry(update_master, textvariable= email_val, font=('roman',15,'bold'), bd=5)
    email_entry.place(x=240, y=190)
    
    address_entry = Entry(update_master, textvariable= address_val, font=('roman',15,'bold'), bd=5)
    address_entry.place(x=240, y=250)
    
    gender_entry = Entry(update_master, textvariable= gender_val, font=('roman',15,'bold'), bd=5)
    gender_entry.place(x=240, y=310)
    
    dob_entry = Entry(update_master, textvariable= dob_val, font=('roman',15,'bold'), bd=5)
    dob_entry.place(x=240, y=370)
    
    date_entry = Entry(update_master, textvariable= date_val, font=('roman',15,'bold'), bd=5)
    date_entry.place(x=240, y=430)
    
    time_entry = Entry(update_master, textvariable= time_val, font=('roman',15,'bold'), bd=5)
    time_entry.place(x=240, y=490)

    
    #========== student update button ===============
    update_button = Button(update_master, text='Update', font=('roman',15,'bold'), width=20,
                           bd=5, activebackground='green2', activeforeground='white', command= update)
    update_button.place(x=140, y=540)
    
    # target object
    cc = show_treeview.focus()
    all_item = show_treeview.item(cc)
    all_val = all_item['values']
    
    if all_val != 0:
        id_val.set(all_val[0])
        name_val.set(all_val[1])
        mobile_val.set(all_val[2])
        email_val.set(all_val[3])
        address_val.set(all_val[4])
        gender_val.set(all_val[5])
        dob_val.set(all_val[6])
        date_val.set(all_val[7])
        time_val.set(all_val[8])
    else:
        messagebox.showerror('Error','No values available!')
    

def show_student():
        all_query = 'select * from student_table'
        cursor.execute(all_query)
        datas = cursor.fetchall()
        show_treeview.delete(* show_treeview.get_children()) # delete form database
        
        for i in datas:
            val = (i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8])
            show_treeview.insert('',END, values=val)

def export_student():
    save_path = filedialog.asksaveasfilename() # get the path for file to save
    print(save_path)
    
    get_child = show_treeview.get_children() # get all the child data from treeview screen
    
    ex_i, ex_n, ex_m, ex_e, ex_a, ex_g, ex_d, ex_date, ex_time = [],[],[],[],[],[],[],[],[]
    for i in get_child:
        content = show_treeview.item(i)
        get_v = content['values']
        ex_i.append(get_v[0])
        ex_n.append(get_v[1])
        ex_m.append(get_v[2])
        ex_e.append(get_v[3])
        ex_a.append(get_v[4])
        ex_g.append(get_v[5])
        ex_d.append(get_v[6])
        ex_date.append(get_v[7])
        ex_time.append(get_v[8])
        
    # all the data save in csv file xl formet
    xl_header = ['ID', 'NAME', 'MOBILE', 'EMAIL', 'ADDRESS', 'GENDER', 'D.O.B', 'ADDED TIME', 'ADDED DATE']
    p_df = pandas.DataFrame(list(zip(ex_i, ex_n, ex_m, ex_e, ex_a, ex_g, ex_d, ex_date, ex_time)), columns= xl_header)
    paths = r'{}.csv'.format(save_path) 
    p_df.to_csv(paths, index= False)
    messagebox.showinfo('Notification', 'Student data saved {}'.format(paths))    

def exit_program():
    res = messagebox.askyesnocancel('Notification', 'Do you want to exit?')
    
    if res == True:
        master.destroy()
    else:
        return

#========================= Entery frame =============================
data_entry_frame = Frame(master, bg='gold2', relief=GROOVE, borderwidth=5)
data_entry_frame.place(x=10, y=80, width=500, height=600)

#------------------------ Data frame label ------------------------
tx = f"{'-'*20} Welcome {'-'*20}"
add_label = Label(data_entry_frame, text= tx, font=('arial',20,'italic bold'), width=30, bg='gold2')
add_label.pack(side=TOP,expand = True)

#------------------------ Data frame button ----------------------
add_button = Button(data_entry_frame, text='1. Add Student', font=('chiller',20, 'bold'), width=25, bd=6, 
                    bg='skyblue',relief=RIDGE, activebackground='blue', activeforeground='white', command= add_student)
add_button.pack(side=TOP, expand= True)

search_button = Button(data_entry_frame, text='2. Search Student', font=('chiller',20, 'bold'), width=25, bd=6, 
                    bg='skyblue',relief=RIDGE, activebackground='blue', activeforeground='white', command= search_student)
search_button.pack(side=TOP, expand= True)

delete_button = Button(data_entry_frame, text='3. Delete Student', font=('chiller',20, 'bold'), width=25, bd=6, 
                    bg='skyblue',relief=RIDGE, activebackground='blue', activeforeground='white', command= delete_student)
delete_button.pack(side=TOP, expand= True)

update_button = Button(data_entry_frame, text='4. Update Student', font=('chiller',20, 'bold'), width=25, bd=6, 
                    bg='skyblue',relief=RIDGE, activebackground='blue', activeforeground='white', command= update_student)
update_button.pack(side=TOP, expand= True)

show_button = Button(data_entry_frame, text='5. Show All', font=('chiller',20, 'bold'), width=25, bd=6, 
                    bg='skyblue',relief=RIDGE, activebackground='blue', activeforeground='white', command= show_student)
show_button.pack(side=TOP, expand= True)

export_button = Button(data_entry_frame, text='6. Export Data', font=('chiller',20, 'bold'), width=25, bd=6, 
                    bg='skyblue',relief=RIDGE, activebackground='blue', activeforeground='white', command= export_student)
export_button.pack(side=TOP, expand= True)

exit_button = Button(data_entry_frame, text='7. exit', font=('chiller',20, 'bold'), width=25, bd=6, 
                    bg='skyblue',relief=RIDGE, activebackground='blue', activeforeground='white', command= exit_program)
exit_button.pack(side=TOP, expand= True)


#======================== Show data frame =========================
show_data_frame = Frame(master, bg='white', relief=GROOVE, borderwidth=5)
show_data_frame.place(x=550, y=80, width=500, height=600)

#----------------------- show treeviwe frame ----------------------
style = ttk.Style()
style.configure('Treeview.Heading', font=('chiller',20,'bold'), foreground='blue')
style.configure('Treeview', font= ('times',15, 'bold'), background='cyan', foreground='black')

#----------------------- Set the scroll bar -----------------------
scroll_x = Scrollbar(show_data_frame, orient= HORIZONTAL)
scroll_y = Scrollbar(show_data_frame, orient= VERTICAL)

show_treeview = Treeview(show_data_frame, columns=('ID', 'NAME', 'MOBILE NO',
                                                   'EMAIL', 'ADRESS', 'GENDER',
                                                   'D.O.B', 'ADDED DATE', 'ADDED TIME'),
                         xscrollcommand= scroll_x.set, yscrollcommand= scroll_y.set)

scroll_x.pack(side=BOTTOM, fill= X)
scroll_y.pack(side=RIGHT, fill= Y)

scroll_x.config(command= show_treeview.xview)
scroll_y.config(command= show_treeview.yview)

#------------------Set the heading of treeview -------------------
show_treeview.heading('ID', text='ID')
show_treeview.heading('NAME', text='NAME')
show_treeview.heading('MOBILE NO', text='MOBILE NO')
show_treeview.heading('EMAIL', text='EMAIL')
show_treeview.heading('ADRESS', text='ADDRESS')
show_treeview.heading('GENDER', text='GENDER')
show_treeview.heading('D.O.B', text='D.O.B')
show_treeview.heading('ADDED DATE', text='ADDED TIME')
show_treeview.heading('ADDED TIME', text='ADDED DATE')
show_treeview['show'] = 'headings'

#----------------- Set the column width of treeview -----------
show_treeview.column('ID', width= 100)
show_treeview.column('NAME', width= 200)
show_treeview.column('MOBILE NO', width= 200)
show_treeview.column('EMAIL', width= 300)
show_treeview.column('ADRESS', width= 200)
show_treeview.column('GENDER', width= 100)
show_treeview.column('D.O.B', width= 150)
show_treeview.column('ADDED DATE', width= 150)
show_treeview.column('ADDED TIME', width= 150)

show_treeview.pack(fill=BOTH, expand= 1)

#========================= Slider =================================
def slider_trick():
    global cnt, txt, ss
    if cnt >= len(ss):
        cnt = 0
        txt = ''
        slider_label.config(text= txt)
    else:
        txt = txt + ss[cnt]
        slider_label.config(text= txt)
        cnt += 1
    
    slider_label.after(200, slider_trick)
    
color = ['red', 'green', 'blue', 'pink', 'gold2', 'gold3']
def change_color():
    fg = random.choice(color)
    slider_label.config(fg= fg)
    slider_label.after(200, change_color)
    
cnt = 0
txt = ''
ss = 'Welcome To Student Management System'
slider_label = Label(master, text= ss, font=('chiller', 30, 'italic bold'), relief=RIDGE, borderwidth=5, width=35, bg='cyan')
slider_label.place(x=260, y=0)
slider_trick()
change_color()

    
#========================= Clock =================================
def make_clock():
    time_set = time.strftime('%H:%M:%S')
    date_set = time.strftime('%d-%m-%y')
    clock_label.config(text='Time: '+time_set+'\n'+'Date: '+date_set)
    clock_label.after(200, make_clock)
    
    
clock_label = Label(master, font=('time',14,'bold'),relief=RIDGE, borderwidth=5, bg='lawn green')
clock_label.place(x=0, y=0)
make_clock()

#======================== Connect to database button =============
def connectdb():
    def button_db():
        global conn, cursor
        hostt = host_val.get()
        userr = user_val.get()
        passwordd = password_val.get()
        db = db_val.get()
        # hostt = 'localhost'
        # userr = 'root'
        # passwordd = '102030'
        # db = 'student_management_system'
        
        if (hostt == '' or hostt == ' ') or (userr == '' or userr == ' ') or (passwordd == '' or passwordd == ' ') or (db ==  '' or db == ' '):
            messagebox.showerror('Error', 'All field are required*', parent = db_master)
            
        else:
            #print(hostt,userr,passwordd,db)
            try:
                conn = pymysql.connect(host= hostt, user= userr, 
                                        password= passwordd, 
                                        database= db)
                cursor = conn.cursor()
                print('Database Connceted')
            
            except:
                messagebox.showerror('Error','Database error connection!',parent= db_master)
                return
        
        #-------------- creating database -----------------
        try:
            
            creat_db = 'create database student_management_system'
            cursor.execute(creat_db)
            
            use_db = 'use student_management_system'
            cursor.execute(use_db)
            
            creat_table = 'create table student_table(ID int, NAME varchar(20), MOBILE varchar(20), EMAIL varchar(30), ADDRESS varchar(100), GENDER varchar(20), dob varchar(15), time varchar(20), date varchar(20) )'
            cursor.execute(creat_table)
            
            not_null = 'alter table student_table modify column ID int not null'
            cursor.execute(not_null)
            
            primary_key = 'alter table student_table modify column ID int primary key'
            cursor.execute(primary_key)
            messagebox.showinfo('Notification','Database careted',parent= db_master)
            
        except:
            st = 'use student_management_system'
            cursor.execute(st)           
            messagebox.showinfo('Notification', 'You are connected to the database',parent= db_master)
        
        
        
    db_master = Toplevel()
    db_master.title('Connect Database')
    db_master.geometry('470x300+800+230')
    db_master.grab_set() # stick the window
    db_master.resizable(False, False)
    db_master.config(bg='blue')
    
    #============= label of database window ===============
    host_label = Label(db_master, text='Enter Host: ', bg='gold2', font=('times',20,'bold'), relief=GROOVE, borderwidth=3, width=13, anchor='w')
    host_label.place(x=10, y=10)
    user_label = Label(db_master, text='Enter User: ', bg='gold2', font=('times',20,'bold'), relief=GROOVE, borderwidth=3, width=13, anchor='w')
    user_label.place(x=10, y=70)
    password_label = Label(db_master, text='Enter Password: ', bg='gold2', font=('times',20,'bold'), relief=GROOVE, borderwidth=3, width=13, anchor='w')
    password_label.place(x=10, y=130)
    db_label = Label(db_master, text='Database Name: ', bg='gold2', font=('times',20,'bold'), relief=GROOVE, borderwidth=3, width=13, anchor='w')
    db_label.place(x=10, y=200)
    
    #============ Enties of database window ================
    host_val = StringVar()
    user_val = StringVar()
    password_val = StringVar()
    db_val = StringVar()
    
    host_entry = Entry(db_master, font=('roman',15, 'bold'),bd=5 , textvariable= host_val)
    host_entry.place(x=250, y=10)
    user_entry = Entry(db_master, font=('roman',15, 'bold'),bd=5 , textvariable= user_val)
    user_entry.place(x=250, y=70)
    password_entry = Entry(db_master,show='*', font=('roman',15, 'bold'),bd=5 , textvariable= password_val)
    password_entry.place(x=250, y=130)
    db_entry = Entry(db_master, font=('roman',15, 'bold'),bd=5 , textvariable= db_val)
    db_entry.place(x=250, y=200)
    
    #========== connect db button ===============
    connect_button = Button(db_master, text='Connect', font=('roman',15,'bold'), width=20,
                            bd=5, activebackground='green2', activeforeground='white', command= button_db)
    connect_button.place(x=150, y=250)
    
cn = 'Connect To Database'
connect_to_db = Button(master, text= cn, width=23, font=('chiller',19, 'italic bold'), 
                       relief=RIDGE, borderwidth=4, bg='green2',
                       activebackground='blue', activeforeground='white', command=connectdb)
connect_to_db.place(x=930, y=0)

master.mainloop()