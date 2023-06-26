import pymysql
from tkinter import messagebox

class Connection:
    
    def __init__(self, hst, usr , passw, db) -> None:
        try:
            global conn
            conn = pymysql.connect(host=hst, user=usr, password=passw, database=db)
            cursor = conn.cursor()
            conn.commit()
            messagebox.showinfo('Notification', 'Database Connected')
        except:
            messagebox.showerror('Error', 'Failed Connected')
    #=================== OPEN ACCOUNT ========================        
    def open_account(self, name, accno, dob, addr, cont, op_val):
        data1 = (name, accno, dob, addr, cont, op_val)
        data2 = (name, accno, op_val)
        try:                   
            sql_insert_account = 'INSERT INTO account_table(Name, AccountNo, DateOfBirth, Address, ContactNo, OpeningBalance) values(%s,%s,%s,%s,%s,%s)'
            sql_insert_amount = 'INSERT INTO amount_table(Name, AccountNo, Balance) values(%s,%s,%s)'
            cursor = conn.cursor()
            cursor.execute(sql_insert_account,data1)
            cursor.execute(sql_insert_amount,data2)
            conn.commit()
            
            messagebox.showinfo('Notification','Data inserted successfully')
        except:
            messagebox.showerror('Error','Data insert failed')
        
    #================ DEPOSIT AMOUNT ======================    
    def deposit_amount(self,amount, ac_no):
        sql_query = 'SELECT Balance FROM amount_table WHERE AccountNo = %s'
        #data = (ac_no,)
        cursor = conn.cursor()
        cursor.execute(sql_query, ac_no)
        db_amount = cursor.fetchone()
        total_amount = db_amount[0] + amount 
        print(total_amount)
        
        #============= update balance in database ============
        sql_update = 'UPDATE amount_table SET Balance = %s WHERE AccountNo = %s'
        data1 = (total_amount,ac_no)
        cursor.execute(sql_update, data1)
        conn.commit()
        
        
        
    #=============== WITHDRAWAL AMOUNT =================
    def withdrawal_amount(self,withdraw_amount, ac_no):
        sql_query = 'SELECT Balance FROM amount_table WHERE AccountNo = %s'
        data = (ac_no,)
        cursor = conn.cursor()
        cursor.execute(sql_query, data)
        db_amount = cursor.fetchone()
        total_amount = db_amount[0] - withdraw_amount 
        #print(total_amount)
        
        #============= update balance in database ============
        sql_update = 'UPDATE amount_table SET Balance = %s WHERE AccountNo = %s'
        data1 = (total_amount,ac_no)
        cursor.execute(sql_update, data1)
        conn.commit()
    #====================== BALANCE ENQUIRE =================
    def balance_enquire(self, account_no):
        enq_bal = 'SELECT Balance FROM amount_table WHERE AccountNo = %s'.format(account_no)
        cursor = conn.cursor()
        cursor.execute(enq_bal, account_no)
        balance = cursor.fetchone()
        bal = balance[0]
        print(f'Id: {account_no}\nTotal balance is {bal}')
            
    
    #====================== CUSTOMER DETAILES ================
    def customer_details(self, account_no):
        show_all = 'SELECT * FROM account_table WHERE AccountNo = %s'
        cursor = conn.cursor()
        cursor.execute(show_all, account_no)
        row = cursor.fetchall()
        
        for i in row:
            print(f'\nName: {i[0]}')
            print(f'Account No: {i[1]}')
            print(f'Date Of Birth: {i[2]}')
            print(f'Address: {i[3]}')
            print(f'Contact No: {i[4]}')
            print(f'Balance: {i[5]}')
    
    #================= CLOSE ACCOUNT =====================
    def close_account(self, ac_no):
        ac_delete = 'DELETE FROM account_table WHERE AccountNo = %s'
        cursor = conn.cursor()
        cursor.execute(ac_delete, ac_no)
        conn.commit()
        print(f'ID: {ac_no}\nThis account has been delete successfully')
    
    #================== EXIT THE PROGRAME ===================
    def exit_program(self):
            exit()
    
    #================= CREATE ACCOUNT =======================      
    def create_account(self):
        lst = ['1. Open New Account',
               '2. Deposit Amount',
               '3. Withdraw Amount',
               '4. Balance Enquiry',
               '5. Display Customer Details',
               '6. Close An Account',
               '7. Exit']
        
        for i in lst:
            print(i)
            
        choice = int(input('Enter your choice: '))
        if choice == 7:
            self.exit_program()
        elif choice == 1:
            name = input('Enter your name: ')
            accno = int(input('Enter your accno: '))
            dob = input('Enter your date of birth: ')
            addr = input('Enter your address: ')
            cont = input('Enter your conctact no: ')
            op_bal = int(input('Enter your opening balance: '))
            self.open_account(name, accno, dob, addr, cont, op_bal)
        
        elif choice == 2:
            dep_amount = int(input('Enter your amount: '))
            dep_ac = int(input('Enter your account number: '))
            self.deposit_amount(dep_amount, dep_ac)
            
        elif choice == 3:
            withdraw_amount = int(input('Enter your withdraw amount: '))
            ac_no = int(input('Enter your account number: '))
            
            self.withdrawal_amount(withdraw_amount,ac_no)
            
        elif choice ==  4:
            bal_enq = int(input('Enter your account number: '))
            self.balance_enquire(bal_enq)
            
        elif choice == 5:
            acc_no = int(input('Enter your account number: '))
            self.customer_details(acc_no)
            
        elif choice == 6:
            ac_no = input('Enter account number: ')
            self.close_account(ac_no)
            
            
c = Connection('localhost','root','102030','bank_management')
c.create_account()