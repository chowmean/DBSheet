# DBSheet
Using google spreadsheets as database. 

## This package helps you make use of google sheets as databases. What all it supports 

1. Creating Tables
2. Inserting Rows
3. Get all records
4. Search for One Row
5. Search for particular number of Rows 

## How to initialize
```python
from db_sheet.db_sheet import DbSheet
from db_sheet.sheet_table import WorkingTable, CreateTable, Table
db = DbSheet(db_name = "SHEETBACKEND", api_creds = "client_secret.json", scope = ['https://spreadsheets.google.com/feeds'])
sheet = db.get_db_conn()
```

Sheet is like database.


### Creating tables

```python
from db_sheet.db_sheet import DbSheet
from db_sheet.sheet_table import WorkingTable, CreateTable, Table
db = DbSheet(db_name = "SHEETBACKEND", api_creds = "client_secret.json", scope = ['https://spreadsheets.google.com/feeds'])
sheet = db.get_db_conn()
table = Table({"Col1","col2"},"name_of_table")
creator = CreateTable(table, sheet)
creator.create_table()
```

### Inserting Rows

```python
from db_sheet.sheet_table import WorkingTable, CreateTable, Table
working_table = WorkingTable("tablename",sheet)
working_table.insert({"value1","value2"}
```


### Get all records

```python
from db_sheet.sheet_table import WorkingTable, CreateTable, Table
working_table = WorkingTable("tablename",sheet)
working_table.get_all()
```

### Search for One Row

```python
from db_sheet.sheet_table import WorkingTable, CreateTable, Table
working_table = WorkingTable("tablename",sheet)
working_table.get_one("column_name",value)
```

### Search for particular number of Rows 

```python
from db_sheet.sheet_table import WorkingTable, CreateTable, Table
working_table = WorkingTable("tablename",sheet)
working_table.find("column_name",value,total_count_u_need)
```


## Contribution:

### You can contibute by following below simple steps.

1. Make sure your build is passing
2. Keep your code clean and proper commenting with pep8. 

Thats it for now. Will add more since its just a begginging.
Suggestions are welcome. Please create an issue if you think this is **** and you can make it better :D

@ Author: chowmean