import DB_helper
import sqlite3

print("####### Starting Sequence ######")
######  Open the DB Connection
my_conn = DB_helper.open_DB()  #### returns connection
cursor = my_conn.cursor()

######  Create the DB Table, if not yet created
create_table_str = '''CREATE TABLE PERSON
         (ID INT PRIMARY KEY     NOT NULL,
         FIRST_NAME           TEXT    NOT NULL,
         LAST_NAME            TEXT     NOT NULL,
         ADDRESS        CHAR(150),
         POSTAL_CODE    INT,
         PHONE_NUM      INT);'''
DB_helper.execute_stmt(my_conn, create_table_str)

###### Insert rows into the DB Table
DB_helper.execute_stmt_with_commit(my_conn, "INSERT INTO PERSON (ID,FIRST_NAME,LAST_NAME,ADDRESS,POSTAL_CODE,PHONE_NUM) \
          VALUES (1, 'Paul', 'HaHa', 'California',101, 9022221111 )");

DB_helper.execute_stmt_with_commit(my_conn, "INSERT INTO PERSON (ID,FIRST_NAME,LAST_NAME,ADDRESS,POSTAL_CODE,PHONE_NUM) \
          VALUES (2, 'Tom', 'House', 'Halifax',102, 9023332222 )");

DB_helper.execute_stmt_with_commit(my_conn, "INSERT INTO PERSON (ID,FIRST_NAME,LAST_NAME,ADDRESS,POSTAL_CODE,PHONE_NUM) \
          VALUES (3, 'Allen', 'Muse', 'Calgary',103, 1202221111 )");

DB_helper.execute_stmt_with_commit(my_conn, "INSERT INTO PERSON (ID,FIRST_NAME,LAST_NAME,ADDRESS,POSTAL_CODE,PHONE_NUM) \
          VALUES (4, 'Johnny', 'Walker', 'Edmonton',104, 9952221111 )");

##### User Can choose the function by input the index num #######
backIndex = "Y"
while (backIndex != "N"):
    print("Please choose the function you want to do")
    print("[1] List all records")
    print("[2] In put a last name to list the record")
    print("[3] Add a record")
    print("[4] Exit")

    chose = input("Please input the number of index [1-4] here:")
    dbIndex = ["1", "2", "3", "4"]

    #### Dump the table ####
    if chose == "1":
        print("Browse Data:")
        results = DB_helper.execute_select(my_conn, "SELECT * from PERSON")
        print("Execute SQL =>", results)
        backIndex = input("Back to index?(Y/N):")

    ##### Match last name ####
    elif chose == "2":
        print("List the record by input the last name")
        lastName = input("Please enter one of this last name (case sensitivity):")
        quote = "'"

        db_select_str = "SELECT * from PERSON where LAST_NAME =" + quote + lastName + quote
        print("db_select_str=>", db_select_str)
        results = DB_helper.execute_select(my_conn, db_select_str)
        print("result match with lastname=>", results)

        backIndex = input("Back to index?(Y/N):")

    ##### user in put Data by themself #######
    elif chose == "3":
        print("Please input the below data")
        p_id = input("Please enter a ID (ID must be an integer):")
        p_firstname = input("Please enter a first name:")
        p_lastname = input("Please enter a last name:")
        p_address = input("Please enter an address:")
        p_postalcode = input("Please enter a postal code:")
        p_phonenum = input("Please enter a phone number:")

        cursor.execute("INSERT INTO PERSON (ID,FIRST_NAME,LAST_NAME,ADDRESS,POSTAL_CODE,PHONE_NUM) \
                           VALUES (?, ?, ?, ?, ?, ?)",
                       (p_id, p_firstname, p_lastname, p_address, p_postalcode, p_phonenum))
        my_conn.commit()

        results = DB_helper.execute_select(my_conn, "SELECT * from PERSON")
        print("Data inserted successfully.", results)

        backIndex = input("Back to index?(Y/N):")

    ##### User exit the DB #####
    elif chose == "4":
        print("Exit the Database")
        break

print("Datadase closed")
DB_helper.close_DB(my_conn)
