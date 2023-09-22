import sqlite3
from sqlite3 import Error

import illness

class IllnessHandler:
    def __init__(self):
        

        self.db_name = "illnesses.db"
        t_illness = illness.Illness()
        t_illness.settype("Depression")

        print(f"Illness Handler: {t_illness.gettype()}")

        self.create_conn_sqllite(self.db_name)
        self.create_table()


    def addIllness(self, t_illness: illness.Illness):

        sqliteConnection = sqlite3.connect(self.db_name)
        cursor = sqliteConnection.cursor()
        sqlite_insert_query = f"""INSERT INTO illnesses
                            (type, symptoms, treatment, medicine, support, financialaid)
                            VALUES
                            ('{t_illness.type}', '{t_illness.symptoms}', '{t_illness.treatment}' '{t_illness.medicine}', '{t_illness.support}', '{t_illness.financialaid}') """
        
        
        
        count = cursor.execute(sqlite_insert_query)
        sqliteConnection.commit()
        print("Record inserted successfully into SqliteDb_developers table", cursor.rowcount)
        cursor.close()


    def deleteIllness(self, t_id):
        try:
            sqliteConnection = sqlite3.connect(self.db)
            cursor = sqliteConnection.cursor()


            sql_delete_query = f"""DELETE from illnesses where id = {int(t_id)}"""
            cursor.execute(sql_delete_query)
            sqliteConnection.commit()
            print(f"\tIllness with id {t_id} removed! ")
            cursor.close()

        except sqlite3.Error as error:
            print("\tFailed to delete record from sqlite table", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("the sqlite connection is closed")
    

    def create_conn_sqllite(self, db_file):
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print(sqlite3.version)
        except Error as e:
            print(e)
        finally:
            if conn:
                conn.close()
        
        return conn
    


    def readSqliteTable(self):

        list_illnesses = []

        try:
            sqliteConnection = sqlite3.connect(self.db_name)
            cursor = sqliteConnection.cursor()

            sqlite_select_query = """SELECT * from illnesses ORDER BY type"""
            cursor.execute(sqlite_select_query)
            records = cursor.fetchall()
            print("Number of rows: ", len(records), "\n")

            '''for now in records:
                print("Id: ", row[0])
                print("Type: ", row[1])
                print("Symptoms: ", row[2])
                print("Treatment: ", row[3])
                print("Medicine: ", row[4])
                print("Support: ", row[5])
                print("Financial aid: ", row[6])
            '''

            for row in records:
                one_illness = illness.Illness(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                list_illnesses.append(one_illness)

            cursor.close

        except sqlite3.Error as error:
            print("Failed to read data from sqlite table", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("The SQLite connection is closed")
            
        return list_illnesses
    
    def create_table(self):
        try:
            sqliteConnection = sqlite3.connect(self.db_name)
            sqlite_create_table_query = '''CREATE TABLE IF NOT EXISTS Illnesses(
                                id INTEGER PRIMARY KEY,
                                type TEXT NOT NULL,
                                symptoms TEXT,
                                treatment INTEGER,
                                Medicine INTEGER,
                                support INTEGER,
                                financial aid INTEGER,);'''
            
            cursor = sqliteConnection.cursor()
            print("Successfully Connected to SqLite")
            cursor.execute(sqlite_create_table_query)
            sqliteConnection.commit()
            print("Table created")

            cursor.close()

        except sqlite3.Error as error:
            print("Error while creating a sqlite table", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("connection is closed")