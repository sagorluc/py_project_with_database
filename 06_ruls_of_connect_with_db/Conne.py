import mysql.connector as conn

class Conneciton:
    def __init__(self, localhost, username, password, db) -> None:
        try:
          self.con = conn.connect(host=localhost, 
                            user=username, 
                            password=password, 
                            database=db)
        
        #if self.con.is_connected():
          print('connection successfully')
        except Exception as e:
            print(e) 
            
            
    def table_create(self, tablename, schema):
        try:
            #query_create = "CREATE TABLE IF NOT EXISTS STUDENT(ID INT, NAME varchar(30))"
            query_create = "CREATE TABLE IF NOT EXISTS {0}({1})".format(tablename, schema)
            cursor = self.con.cursor()
            cursor.execute(query_create)
            self.con.commit()
            print('Table is created')
        except Exception as e:
            print(e)
            
        
    def insert_into_table(self, tablename, schema, value):
        try:
            # passing schema
            st = schema.split(',')
            #print(st)
            st1 =''
            for i in st:
                b = i.split(' ')
                st1 = st1 + b[0] + ','
            schema = st1[:len(st1)-1]
            #print(schema)
            #query_insert = "INSERT INTO STUDENT(ID,NAME) VALUES(1,'sagor')"    
            query_insert = "INSERT INTO {0}(ID, NAME) VALUES ({2})".format(tablename, schema, value)
            cursor = self.con.cursor()
            cursor.execute(query_insert)
            self.con.commit()
            print('data is inserted')
        except Exception as e:
            print(e)
        
    def select(self, tablename, select_column):
        try:
            #query_select = "SELECT STUDENT FROM select_column"
            query_select = "SELECT {1} FROM {0}".format(tablename, select_column)
            cursor = self.con.cursor()
            cursor.execute(query_select)
            
            row = cursor.fetchall()
            for i in row:
                print(i)
            #self.con.commit()
            print('data selected successfully')
        except Exception as e:
            print(e)
        
    def update_table(self, tablename, set_condition, filter_condition):
        try:
            #query_update = "UPDATE STUDENT SET ID=4 WHERE ID=1"
            query_update = "UPDATE {0} SET {1} WHERE {2}".format(tablename, set_condition, filter_condition)
            cursor = self.con.cursor()
            cursor.execute(query_update)
            self.con.commit()
            print('data updated')
        except Exception as e:
            print(e)
        
    def delete_table(self, tablename, delete_condition):
        try:
            #query_delete = "DELETE FROM student WHERE delete_condition" # without formet is not dynamic
            query_delete = "DELETE FROM {0} WHERE {1}".format(tablename, delete_condition)
            cursor = self.con.cursor()
            cursor.execute(query_delete)
            self.con.commit()
            print('delete successfully')
        except Exception as e:
            print(e)
    
    
c = Conneciton('localhost', 'root','102030','pratice_db')
tablename =  'student_four' # database name
schema = 'ID int, name varchar(30)' # id and name 
value = "2,'jakir'"
select = 'ID, name'
set_condition = 'ID=4'
filter_condition = 'ID=1'
delete_condition = 'ID=2'
c.table_create(tablename,schema)
c.insert_into_table(tablename, schema, value)
c.select(tablename, select)
c.update_table(tablename, set_condition, filter_condition)
c.delete_table(tablename, delete_condition)


