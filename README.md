# Membership Application - No GUI Version

## Table of contents
* [General info](#general-info)
* [Motivation](#motivation)
* [Technologies](#technologies)
* [Setup](#setup)
* [Installation and Open](#installation-and-open)
* [Instruction](#instruction)


## General info
This is a mock design for a membership web application, I use python to create the framework and connected with SQLlite to create a database.


## Motivation
The membership web application will be one of the function for a product introduction website, this basic framework will continue to develop for the future usage. 

	
## Technologies
Project is created with:
* Python 3.9.8
* Pycharm Profession 2021.3.1
* SQLite 3.7.15
* DB Browser for SQLite

	
## Setup
To run this project, install it locally. run the python script with any IDE or throught the operating system command-line or termial


## Installation and Open 
1. Clone the repo https://github.com/JuneKTMan/Membership_app_noGUI.git
2. Before opening the project file, please confirm your python have a sqlite3 module, you can install the module by,
For Python version 3:
```
pip install pysqlite3

```
3. Open the project folder by IDE. 
4. Open the project from the Project folder > membership_app_noGUI

![file_structure](https://user-images.githubusercontent.com/97205265/152093044-847fca3b-6b40-4f9f-8e2e-f7accb50600d.PNG)



## Instruction
1. Run the SQL_membership.py.. You will see the below menu show in the console window, follow the instruction to select or add record into the database.

```
Please choose the function you want to do
[1] List all records
[2] In put a last name to list the record
[3] Add a record
[4] Exit
Please input the number of index [1-4] here:
```

2. Input a number to choose the menu, function 1: List all record in the database 
```
Please input the number of index [1-4] here:1
Browse Data:
cursor DICT=> (('ID', None, None, None, None, None, None), ('FIRST_NAME', None, None, None, None, None, None), ('LAST_NAME', None, None, None, None, None, None), ('ADDRESS', None, None, None, None, None, None), ('POSTAL_CODE', None, None, None, None, None, None), ('PHONE_NUM', None, None, None, None, None, None))
col=> ['ID', 'FIRST_NAME', 'LAST_NAME', 'ADDRESS', 'POSTAL_CODE', 'PHONE_NUM'] 6
success:  SELECT * from PERSON
SELECT results:  [['ID', 'FIRST_NAME', 'LAST_NAME', 'ADDRESS', 'POSTAL_CODE', 'PHONE_NUM'], [1, 'Paul', 'HaHa', 'California', 101, 9022221111], [2, 'Tom', 'House', 'Halifax', 102, 9023332222], [3, 'Allen', 'Muse', 'Calgary', 103, 1202221111], [4, 'Johnny', 'Walker', 'Edmonton', 104, 9952221111], [5, 'Ju', 'Luma', 'Halifax', 102230, 9022212109]]
Execute SQL => [['ID', 'FIRST_NAME', 'LAST_NAME', 'ADDRESS', 'POSTAL_CODE', 'PHONE_NUM'], [1, 'Paul', 'HaHa', 'California', 101, 9022221111], [2, 'Tom', 'House', 'Halifax', 102, 9023332222], [3, 'Allen', 'Muse', 'Calgary', 103, 1202221111], [4, 'Johnny', 'Walker', 'Edmonton', 104, 9952221111], [5, 'Ju', 'Luma', 'Halifax', 102230, 9022212109]]
Back to index?(Y/N):
```
Then press Y to return index or press N to close exit the menu
Function 2: Select a member record by input the last name
```
Please input the number of index [1-4] here:2
List the record by input the last name
Please enter one of this last name (case sensitivity):Luma
db_select_str=> SELECT * from PERSON where LAST_NAME ='Luma'
cursor DICT=> (('ID', None, None, None, None, None, None), ('FIRST_NAME', None, None, None, None, None, None), ('LAST_NAME', None, None, None, None, None, None), ('ADDRESS', None, None, None, None, None, None), ('POSTAL_CODE', None, None, None, None, None, None), ('PHONE_NUM', None, None, None, None, None, None))
col=> ['ID', 'FIRST_NAME', 'LAST_NAME', 'ADDRESS', 'POSTAL_CODE', 'PHONE_NUM'] 6
success:  SELECT * from PERSON where LAST_NAME ='Luma'
SELECT results:  [['ID', 'FIRST_NAME', 'LAST_NAME', 'ADDRESS', 'POSTAL_CODE', 'PHONE_NUM'], [5, 'Ju', 'Luma', 'Halifax', 102230, 9022212109]]
result match with lastname=> [['ID', 'FIRST_NAME', 'LAST_NAME', 'ADDRESS', 'POSTAL_CODE', 'PHONE_NUM'], [5, 'Ju', 'Luma', 'Halifax', 102230, 9022212109]]
Back to index?(Y/N):
```
Function 3: Add a new membership record into the database
```
Please input the number of index [1-4] here:3
Please input the below data
Please enter a ID (ID must be an integer):6
Please enter a first name:Jon
Please enter a last name:Gon
Please enter an address:Greenwood
Please enter a postal code:203130
Please enter a phone number:9022113456
cursor DICT=> (('ID', None, None, None, None, None, None), ('FIRST_NAME', None, None, None, None, None, None), ('LAST_NAME', None, None, None, None, None, None), ('ADDRESS', None, None, None, None, None, None), ('POSTAL_CODE', None, None, None, None, None, None), ('PHONE_NUM', None, None, None, None, None, None))
col=> ['ID', 'FIRST_NAME', 'LAST_NAME', 'ADDRESS', 'POSTAL_CODE', 'PHONE_NUM'] 6
success:  SELECT * from PERSON
SELECT results:  [['ID', 'FIRST_NAME', 'LAST_NAME', 'ADDRESS', 'POSTAL_CODE', 'PHONE_NUM'], [1, 'Paul', 'HaHa', 'California', 101, 9022221111], [2, 'Tom', 'House', 'Halifax', 102, 9023332222], [3, 'Allen', 'Muse', 'Calgary', 103, 1202221111], [4, 'Johnny', 'Walker', 'Edmonton', 104, 9952221111], [5, 'Ju', 'Luma', 'Halifax', 102230, 9022212109], [6, 'Jon', 'Gon', 'Greenwood', 203130, 9022113456]]
Data inserted successfully. [['ID', 'FIRST_NAME', 'LAST_NAME', 'ADDRESS', 'POSTAL_CODE', 'PHONE_NUM'], [1, 'Paul', 'HaHa', 'California', 101, 9022221111], [2, 'Tom', 'House', 'Halifax', 102, 9023332222], [3, 'Allen', 'Muse', 'Calgary', 103, 1202221111], [4, 'Johnny', 'Walker', 'Edmonton', 104, 9952221111], [5, 'Ju', 'Luma', 'Halifax', 102230, 9022212109], [6, 'Jon', 'Gon', 'Greenwood', 203130, 9022113456]]
Back to index?(Y/N):
```
Function 4: Exit the menu and close the database
```
Please input the number of index [1-4] here:4
Exit the Database
Datadase closed
```
