from DbSheet import DbSheet
from SheetTable import WorkingTable
db = DbSheet("SHEETBACKEND")
sheet = db.get_db_conn()

# Extract and print all of the values
#list_of_hashes = sheet.get_all_records()
#print(list_of_hashes)
# creator = CreateTable(table, sheet)
# creator.create_table()

working_table = WorkingTable("Testtable2",sheet)
# print (working_table.insert({1,2,3}))
# print (working_table.insert({3,2,3}))
# print (working_table.insert({4,2,3}))
# print (working_table.insert({5,2,3}))
# print (working_table.insert({6,2,3}))
# print (working_table.insert({7,2,3}))

data = working_table.get_all()
print (data)
print working_table.get_attr("id",2)
print ("\n")
print working_table.get_one("data1",2)
print ("\n")
print working_table.find("data1",2,3)
#sheet.add_worksheet("table_name",4, 12)