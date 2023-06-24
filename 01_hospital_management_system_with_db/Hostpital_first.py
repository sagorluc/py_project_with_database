from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import datetime
import pymysql

class Hospital:
    def __init__(self, master) -> None:
        self.master = master
        self.master.title('Hospital Management System')
        self.master.geometry('1540x800+0+0')
        
        #================== VARIABLE ====================
        # global tb_name_val,ref_val,dose_val,no_tb_val,lot_val,issue_val
        # global expired_val,daily_val,side_val,futher_val,blood_val,stroage_val
        # global medication_val,patient_id_val,nid_val,p_name_val,p_dob_val,p_address_val
        
        self.tb_name_val = StringVar()
        self.ref_val = StringVar()
        self.dose_val = StringVar()
        self.no_tb_val = StringVar()
        self.lot_val = StringVar()
        self.issue_val = StringVar()
        self.expired_val = StringVar()
        self.daily_val = StringVar()
        self.side_val = StringVar()
        self.futher_val = StringVar()
        self.blood_val = StringVar()
        self.stroage_val = StringVar()
        self.medication_val = StringVar()
        self.patient_id_val = StringVar()
        self.nid_val = StringVar()
        self.p_name_val = StringVar()
        self.p_dob_val = StringVar()
        self.p_address_val = StringVar()
        
        
        first_label = Label(self.master, bd=20, relief=RIDGE, text='Hospital Management System',
                            fg='red', bg='white',font=('times new roman',50,'bold'))
        first_label.pack(side=TOP, fill=X)
        
        #==================== DATA FRAME =================
        data_frame = Frame(self.master, bd=20, relief=RIDGE)
        data_frame.place(x=0,y=130,width=1530, height=400)
        
        data_frame_left = LabelFrame(data_frame, bd=10, relief=RIDGE, padx=10,
                                     font=('times new roman',15,'bold'),
                                     text='Patient Information')
        data_frame_left.place(x=0,y=5,width=980, height=350)
        
        data_frame_right = LabelFrame(data_frame, bd=10, relief=RIDGE, padx=10,
                                     font=('times new roman',15,'bold'),
                                     text='Prescription')
        data_frame_right.place(x=990,y=5,width=460, height=350)
        
        #==================== BUTTONS FRAME ================
        button_frame = Frame(self.master, bd=20, relief=RIDGE)
        button_frame.place(x=0,y=530,width=1530, height=70)
        
        #==================== DETAILS FRAME ================
        details_frame = Frame(self.master, bd=20, relief=RIDGE)
        details_frame.place(x=0,y=600,width=1530, height=190)
        
        #==================== DATA FRAME LEFT ================
        tablet_name_lable = Label(data_frame_left,text='Name Of Tablet: ',
                            font=('times new roman',12,'bold'),padx=2, pady=6)
        tablet_name_lable.grid(row=0,column=0)

        Refarence_label = Label(data_frame_left,text='Refarence No: ',
                            font=('times new roman',12,'bold'),padx=2, pady=6)
        Refarence_label.grid(row=1,column=0)
        
        dose_label = Label(data_frame_left,text='Dose: ',
                            font=('times new roman',12,'bold'),padx=2, pady=6)
        dose_label.grid(row=2,column=0)
        
        tablet_label = Label(data_frame_left,text='No of Tablets: ',
                            font=('times new roman',12,'bold'),padx=2, pady=6)
        tablet_label.grid(row=3,column=0)
        
        lot_label = Label(data_frame_left,text='Lot: ',
                            font=('times new roman',12,'bold'),padx=2, pady=6)
        lot_label.grid(row=4,column=0)
        
        issue_label = Label(data_frame_left,text='Issue Date: ',
                            font=('times new roman',12,'bold'),padx=2, pady=6)
        issue_label.grid(row=5,column=0)
        
        expired_label = Label(data_frame_left,text='Expired Date: ',
                            font=('times new roman',12,'bold'),padx=2, pady=6)
        expired_label.grid(row=6,column=0)
        
        daily_label = Label(data_frame_left,text='Daily Dose: ',
                            font=('times new roman',12,'bold'),padx=2, pady=6)
        daily_label.grid(row=7,column=0)
        
        side_label = Label(data_frame_left,text='Side Effect: ',
                            font=('times new roman',12,'bold'),padx=2, pady=6)
        side_label.grid(row=8,column=0)
        

        #==================== DATA FRAME LEFT ENTRY ===========
        combox_name_tablet_entry = ttk.Combobox(data_frame_left,textvariable= self.tb_name_val,font=('times new roman',12,'bold'), width=35)
        combox_name_tablet_entry['values'] = ('Coronavirus','Norovirus',
                                    'Epstein',
                                    'Influenza',
                                    'Hepatitis',
                                    'Herpes',
                                    'papill')
        combox_name_tablet_entry.grid(row=0, column=1)
        
        refarence_entry = Entry(data_frame_left,textvariable= self.ref_val,font=('arial',12,'bold'), width=34 )
        refarence_entry.grid(row=1, column=1)
        
        dose_entry = Entry(data_frame_left,textvariable= self.dose_val,font=('arial',12,'bold'), width=34 )
        dose_entry.grid(row=2, column=1)
        
        tablet_entry = Entry(data_frame_left,textvariable= self.no_tb_val,font=('arial',12,'bold'), width=34 )
        tablet_entry.grid(row=3, column=1)
        
        lot_entry = Entry(data_frame_left,textvariable= self.lot_val,font=('arial',12,'bold'), width=34 )
        lot_entry.grid(row=4, column=1)
        
        issue_entry = Entry(data_frame_left,textvariable=self.issue_val,font=('arial',12,'bold'), width=34 )
        issue_entry.grid(row=5, column=1)
        
        expired_entry = Entry(data_frame_left,textvariable=self.expired_val,font=('arial',12,'bold'), width=34 )
        expired_entry.grid(row=6, column=1)
        
        daily_entry = Entry(data_frame_left,textvariable= self.daily_val,font=('arial',12,'bold'), width=34 )
        daily_entry.grid(row=7, column=1)
        
        side_entry = Entry(data_frame_left,textvariable= self.side_val,font=('arial',12,'bold'), width=34 )
        side_entry.grid(row=8, column=1)
        
        
        #==================== DATA FRAME RIGHT ================
        further_label = Label(data_frame_left,text='Further Informaton: ',
                            font=('times new roman',12,'bold'),padx=10, pady=6)
        further_label.grid(row=0,column=2)
        
        pressure_label = Label(data_frame_left,text='Blood Pressure: ',
                            font=('times new roman',12,'bold'),padx=10, pady=6)
        pressure_label.grid(row=1,column=2)
        
        storage_label = Label(data_frame_left,text='Storage Advice: ',
                            font=('times new roman',12,'bold'),padx=10, pady=6)
        storage_label.grid(row=2,column=2)
        
        medication_label = Label(data_frame_left,text='Medication: ',
                            font=('times new roman',12,'bold'),padx=10, pady=6)
        medication_label.grid(row=3,column=2)
        
        patient_id_label = Label(data_frame_left,text='Patient Id: ',
                            font=('times new roman',12,'bold'),padx=10, pady=6)
        patient_id_label.grid(row=4,column=2)
        
        nid_number_label = Label(data_frame_left,text='Nid Number: ',
                            font=('times new roman',12,'bold'),padx=10, pady=6)
        nid_number_label.grid(row=5,column=2)
        
        patient_name_label = Label(data_frame_left,text='Patient Name: ',
                            font=('times new roman',12,'bold'),padx=10, pady=6)
        patient_name_label.grid(row=6,column=2)
        
        dob_label = Label(data_frame_left,text='Date Of Birth: ',
                            font=('times new roman',12,'bold'),padx=10, pady=6)
        dob_label.grid(row=7,column=2)
        
        address_label = Label(data_frame_left,text='Patient Address: ',
                            font=('times new roman',12,'bold'),padx=10, pady=6)
        address_label.grid(row=8,column=2)
        
        #==================== DATA FRAME RIGHT ENTRY ================
        further_entry = Entry(data_frame_left,textvariable= self.futher_val,font=('arial',12,'bold'), width=29 )
        further_entry.grid(row=0, column=3)
        
        pressure_entry = Entry(data_frame_left,textvariable= self.blood_val,font=('arial',12,'bold'), width=29 )
        pressure_entry.grid(row=1, column=3)
        
        storage_entry = Entry(data_frame_left,textvariable= self.stroage_val,font=('arial',12,'bold'), width=29 )
        storage_entry.grid(row=2, column=3)
        
        medication_entry = Entry(data_frame_left,textvariable= self.medication_val,font=('arial',12,'bold'), width=29 )
        medication_entry.grid(row=3, column=3)
        
        patient_id_entry = Entry(data_frame_left,textvariable= self.patient_id_val,font=('arial',12,'bold'), width=29 )
        patient_id_entry.grid(row=4, column=3)
        
        nid_entry = Entry(data_frame_left,textvariable= self.nid_val,font=('arial',12,'bold'), width=29 )
        nid_entry.grid(row=5, column=3)
        
        patient_name_entry = Entry(data_frame_left,textvariable= self.p_name_val,font=('arial',12,'bold'), width=29 )
        patient_name_entry.grid(row=6, column=3)
        
        dob_entry = Entry(data_frame_left,textvariable= self.p_dob_val,font=('arial',12,'bold'), width=29 )
        dob_entry.grid(row=7, column=3)
        
        address_entry = Entry(data_frame_left,textvariable=self.p_address_val,font=('arial',12,'bold'), width=29 )
        address_entry.grid(row=8, column=3)
        
        #================== TEXT FIELD =======================
        self.text_field = Text(data_frame_right, font=('arial',12,'bold'), width=46, height=16, padx=2, pady=6)
        self.text_field.grid(row=0, column=0)
        
        
        #================== All BUTTON =======================
        prsciption_button = Button(button_frame, text="Presciption", bg='green',fg='white',font=('arial',12,'bold'),
                                   width=23, padx=2, pady=6, command= self.presciption_show)
        prsciption_button.grid(row=0, column=0)
        
        prsciption_data_button = Button(button_frame, text="Presciption Data", bg='green',fg='white',font=('arial',12,'bold'),
                                   width=23, padx=2, pady=6, command= self.presciption_data)
        prsciption_data_button.grid(row=0, column=1)
        
        button_update = Button(button_frame, text="Update", bg='green', fg='white', font=('arial', 12, 'bold'),
                            width=23, padx=2, pady=6, command= self.Update_data)
        button_update.grid(row=0, column=2)

        
        button_delete = Button(button_frame, text="Delete", bg='green',fg='white',font=('arial',12,'bold'),
                                   width=23, padx=2, pady=6, command= self.Delete_data)
        button_delete.grid(row=0, column=3)
        
        button_clear = Button(button_frame, text="Clear", bg='green',fg='white',font=('arial',12,'bold'),
                                   width=23, padx=2, pady=6, command= self.Clear_data)
        button_clear.grid(row=0, column=4)
        
        button_exit = Button(button_frame, text="Exit", bg='green',fg='white',font=('arial',12,'bold'),
                                   width=23, padx=2, pady=6, command= self.exit)
        button_exit.grid(row=0, column=5)
        
        #======================= TABLE ======================
        #======================= SCROLL BAR =================
        scroll_x = ttk.Scrollbar(details_frame, orient= HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_frame, orient= VERTICAL)
        
        #======================== Treeview ===================
        self.my_tree = ttk.Treeview(details_frame, columns=('Name Of Tablet',
                                                       'Refarence No',
                                                       'Dose',
                                                       'No Of Tablet',
                                                       'Lot','Issue Date',
                                                       'Expired Date',
                                                       'Daily Dose','Side Effect',
                                                       'Further Information','Blood Pressure',
                                                       'Storage','Medication','Patient Id',
                                                       'Nid Number','Patient Name',
                                                       'Date Of Birth','Patient Address'),
                               xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill= X)
        scroll_y.pack(side=RIGHT, fill= Y)
        scroll_x.config(command= self.my_tree.xview)
        scroll_y.config(command= self.my_tree.yview)
        
        #======================= SET HEADING OF TREE ==============
        self.my_tree.heading('Name Of Tablet', text='Name Of Table')
        self.my_tree.heading('Refarence No', text='Refarence No')
        self.my_tree.heading('Dose', text='Dose')
        self.my_tree.heading('No Of Tablet', text='No Of Tablet')
        self.my_tree.heading('Lot', text='Lot')
        self.my_tree.heading('Issue Date', text='Issue Date')
        self.my_tree.heading('Expired Date', text='Expired Date')
        self.my_tree.heading('Daily Dose', text='Daily Dose')
        self.my_tree.heading('Side Effect', text='Side Effect')
        self.my_tree.heading('Further Information', text='Further Information')
        self.my_tree.heading('Blood Pressure', text='Blood Pressure')
        self.my_tree.heading('Storage', text='Storage')
        self.my_tree.heading('Medication', text='Medication')
        self.my_tree.heading('Patient Id', text='Patient Id')
        self.my_tree.heading('Nid Number', text='Nid Number')
        self.my_tree.heading('Patient Name', text='Patient Name')
        self.my_tree.heading('Date Of Birth', text='Date Of Birth')
        self.my_tree.heading('Patient Address', text='Patient Address')
        self.my_tree['show'] = 'headings'
        
        #======================= SET COLUMN WIDTH =================
        self.my_tree.column('Name Of Tablet',width=100)
        self.my_tree.column('Refarence No',width=100)
        self.my_tree.column('Dose',width=50)
        self.my_tree.column('No Of Tablet',width=100)
        self.my_tree.column('Lot',width=50)
        self.my_tree.column('Issue Date',width=100)
        self.my_tree.column('Expired Date',width=100)
        self.my_tree.column('Daily Dose',width=100)
        self.my_tree.column('Side Effect',width=100)
        self.my_tree.column('Further Information',width=112)
        self.my_tree.column('Blood Pressure',width=100)
        self.my_tree.column('Storage',width=70)
        self.my_tree.column('Medication',width=100)
        self.my_tree.column('Patient Id',width=100)
        self.my_tree.column('Nid Number',width=100)
        self.my_tree.column('Patient Name',width=100)
        self.my_tree.column('Date Of Birth',width=100)
        self.my_tree.column('Patient Address',width=100)
        
        self.my_tree.pack(fill=BOTH, expand=1)
        self.my_tree.bind('<ButtonRelease-1>', self.get_cursor) # get data into from
        self.show_data() # fetchall data to show on treeview table
        
        #============== END HERE ==================
        
#=============== FUNCTIONALITY DECLEARTION ===================
    def presciption_data(self):

        self.p_n = self.tb_name_val.get()
        self.p_r = self.ref_val.get()
        self.p_dose = self.dose_val.get()
        self.p_tb_no = self.no_tb_val.get()
        self.p_lot = self.lot_val.get()
        self.p_issue = self.issue_val.get()
        self.p_ex = self.expired_val.get()
        self.p_daily = self.daily_val.get()
        self.p_side = self.side_val.get()
        self.p_fur = self.futher_val.get()
        self.p_blood = self.blood_val.get()
        self.p_stor = self.stroage_val.get()
        self.p_medi = self.medication_val.get()
        self.p_id = self.patient_id_val.get()
        self.p_nid = self.nid_val.get()
        self.p_name = self.p_name_val.get()
        self.p_dob = self.p_dob_val.get()
        self.p_address = self.p_address_val.get()
        
        if self.p_n == '' or self.p_r == '':
            messagebox.showerror('Error', 'All fields are required')
        else:
            try:
                conn = pymysql.connect(host='localhost',
                                    user='root',
                                    password='102030',
                                    database='hospital')
                cursor = conn.cursor()
                query_insert = 'insert into hospital_table values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
                cursor.execute(query_insert,(self.p_n,self.p_r,self.p_dose,self.p_tb_no,
                                            self.p_lot,self.p_issue,self.p_ex,self.p_daily,
                                            self.p_side,self.p_fur,self.p_blood,self.p_stor,
                                            self.p_medi,self.p_id,self.p_nid,self.p_name,self.p_dob,self.p_address))
                conn.commit()
                self.show_data() # fetchall data to show on treeview table
                conn.close()
                messagebox.showinfo('Notification', 'Data Inserted')
            except:
                messagebox.showerror('Error','Connection Failed')
                return
            
    # fetchall data into treeview        
    def show_data(self):
        conn = pymysql.connect(host='localhost', user='root',password='102030', database='hospital')
        cursor = conn.cursor()
        query_show = 'select * from hospital_table'
        cursor.execute(query_show)
        
        datas = cursor.fetchall()
        if len(datas) != 0:
            self.my_tree.delete(* self.my_tree.get_children())
            for i in datas:
                self.my_tree.insert('',END,values=i)
            conn.commit()
        conn.close()
        
    # target object and get value    
    def get_cursor(self,event=""): 
        # get data into form 
        target = self.my_tree.focus()
        content = self.my_tree.item(target)
        row = content['values']
        
        self.tb_name_val.set(row[0])
        self.ref_val.set(row[1])
        self.dose_val.set(row[2])
        self.no_tb_val.set(row[3])
        self.lot_val.set(row[4])
        self.issue_val.set(row[5])
        self.expired_val.set(row[6])
        self.daily_val.set(row[7])
        self.side_val.set(row[8])
        self.futher_val.set(row[9])
        self.blood_val.set(row[10])
        self.stroage_val.set(row[11])
        self.medication_val.set(row[12])
        self.patient_id_val.set(row[13])
        self.nid_val.set(row[14])
        self.p_name_val.set(row[15])
        self.p_dob_val.set(row[16])
        self.p_address_val.set(row[17])
        
    #=================== UPDATE DATA ======================
    def Update_data(self):
        self.u_n = self.tb_name_val.get()
        self.u_r = self.ref_val.get()
        self.u_dose = self.dose_val.get()
        self.u_tb_no = self.no_tb_val.get()
        self.u_lot = self.lot_val.get()
        self.u_issue = self.issue_val.get()
        self.u_ex = self.expired_val.get()
        self.u_daily = self.daily_val.get()
        self.u_side = self.side_val.get()
        self.u_fur = self.futher_val.get()
        self.u_blood = self.blood_val.get()
        self.u_stor = self.stroage_val.get()
        self.u_medi = self.medication_val.get()
        self.u_id = self.patient_id_val.get()
        self.u_nid = self.nid_val.get()
        self.u_name = self.p_name_val.get()
        self.u_dob = self.p_dob_val.get()
        self.u_address = self.p_address_val.get()
        try: 
            conn = pymysql.connect(host='localhost', user='root',password='102030', database='hospital')
            cursor = conn.cursor()
            query_update = 'update hospital_table set NameOfTablet = %s, Dose = %s, NoOfTablet = %s, Lot = %s, IssueDate = %s, ExpiredDate = %s, DailyDose = %s, SideEffect = %s, FurtherInformation = %s, BloodPressure = %s, Storagee = %s, Medication = %s, PatientId = %s, NidNumber = %s, PatientName = %s, DateOfBirth = %s, PatientAddress = %s where RefarenceNo = %s'
            cursor.execute(query_update,(self.u_n,self.u_dose,self.u_tb_no,
                                self.u_lot,self.u_issue,self.u_ex,self.u_daily,
                                self.u_side,self.u_fur,self.u_blood,self.u_stor,
                                self.u_medi,self.u_id,self.u_nid,self.u_name,self.u_dob,self.u_address,self.u_r))
            conn.commit()
            self.show_data()
            conn.close()
            messagebox.showinfo('Notification','Data Updated')
        except:
            messagebox.showerror('Error','Failed update')
            
    #==================== Presciption show ====================
    def presciption_show(self):
        self.t_n = self.tb_name_val.get()
        self.t_r = self.ref_val.get()
        self.t_dose = self.dose_val.get()
        self.t_tb_no = self.no_tb_val.get()
        self.t_lot = self.lot_val.get()
        self.t_issue = self.issue_val.get()
        self.t_ex = self.expired_val.get()
        self.t_daily = self.daily_val.get()
        self.t_side = self.side_val.get()
        self.t_fur = self.futher_val.get()
        self.t_blood = self.blood_val.get()
        self.t_stor = self.stroage_val.get()
        self.t_medi = self.medication_val.get()
        self.t_id = self.patient_id_val.get()
        self.t_nid = self.nid_val.get()
        self.t_name = self.p_name_val.get()
        self.t_dob = self.p_dob_val.get()
        self.t_address = self.p_address_val.get()
        
        self.text_field.insert(END, f'Name of Teblet: \t\t\t' + self.t_n + '\n')
        self.text_field.insert(END, f'Refarency No: \t\t\t' + self.t_r + '\n')
        self.text_field.insert(END, f'Dose: \t\t\t' + self.t_dose + '\n')
        self.text_field.insert(END, f'No Of Tablets: \t\t\t' + self.t_tb_no + '\n')
        self.text_field.insert(END, f'Lot: \t\t\t' + self.t_lot + '\n')
        self.text_field.insert(END, f'Issue Date: \t\t\t' + self.t_issue + '\n')
        self.text_field.insert(END, f'Expired Date: \t\t\t' + self.t_ex + '\n')
        self.text_field.insert(END, f'Daily Dose: \t\t\t' + self.t_daily + '\n')
        self.text_field.insert(END, f'Side Effect: \t\t\t' + self.t_side + '\n')
        self.text_field.insert(END, f'Further Informetion: \t\t\t' + self.t_fur + '\n')
        self.text_field.insert(END, f'Blood Pressure: \t\t\t' + self.t_blood + '\n')
        self.text_field.insert(END, f'Storage Advice: \t\t\t' + self.t_stor + '\n')
        self.text_field.insert(END, f'Medication: \t\t\t' + self.t_medi + '\n')
        self.text_field.insert(END, f'Patient Id: \t\t\t' + self.t_id + '\n')
        self.text_field.insert(END, f'Nid Number: \t\t\t' + self.t_nid + '\n')
        self.text_field.insert(END, f'Patient Name: \t\t\t' + self.t_name + '\n')
        self.text_field.insert(END, f'Date Of Birth: \t\t\t' + self.t_dob + '\n')
        self.text_field.insert(END, f'Patient Address: \t\t\t' + self.t_address + '\n')
    
    
    #=========================== DELETE DATA ======================    
    def Delete_data(self):
        self.d_r = self.ref_val.get()
        
        conn = pymysql.connect(host='localhost',user='root',password='102030',database='hospital')
        cursor = conn.cursor()
        value = self.d_r
        query_delet = 'delete from hospital_table where RefarenceNo = %s'
        cursor.execute(query_delet, value)
        conn.commit()
        conn.close()
        self.show_data() # fetchall 
        messagebox.showinfo('Notification', 'Delete successfully')
    #=========================== CLEAR DATA FORM =================    
    def Clear_data(self):
        self.tb_name_val.set('')
        self.ref_val.set('')
        self.dose_val.set('')
        self.no_tb_val.set('')
        self.lot_val.set('')
        self.issue_val.set('')
        self.expired_val.set('')
        self.daily_val.set('')
        self.side_val.set('')
        self.futher_val.set('')
        self.blood_val.set('')
        self.stroage_val.set('')
        self.medication_val.set('')
        self.patient_id_val.set('')
        self.nid_val.set('')
        self.p_name_val.set('')
        self.p_dob_val.set('')
        self.p_address_val.set('')
        self.text_field.delete('1.0',END)
    #=========================== EXIT WHOLE PROGRAM ===============    
    def exit(self):
        res = messagebox.askyesno('Notification','Are you sure!\nDo you want to exit?')
        if res == True:
            master.destroy()
        else:
            return    
        

#==================== CALL CLASS AND OBJECT =====================        
master = Tk()
h = Hospital(master)
#h.presciption_data()
master.mainloop()