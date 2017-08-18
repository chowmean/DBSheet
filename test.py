from DbSheet import DbSheet
from SheetTable import WorkingTable, CreateTable, Table
db = DbSheet("SHEETBACKEND")
sheet = db.get_db_conn()

# Extract and print all of the values
#list_of_hashes = sheet.get_all_records()
#print(list_of_hashes)
table = Table({"data1","data2"},"Testtable2")
# creator = CreateTable(table, sheet)
# creator.create_table()

working_table = WorkingTable("Testtable2",sheet)

# print (working_table.insert({"ad2",1}))
# print (working_table.insert({"asdsad",1}))
# print (working_table.insert({"adasdasdasd2",1}))
# print (working_table.insert({"asd",1}))
# print (working_table.insert({"aasdasdd2",1}))
# print (working_table.insert({"aasdasdd2",1}))
#
# data = working_table.get_all()
# print (data)
# print working_table.get_attr("data1",2)
# print ("\n")
# print working_table.get_one("data1",2)
# print ("\n")
# print working_table.find("data1",2,3)
#sheet.add_worksheet("table_name",4, 12)
print working_table.delete("data2",'aasdasdd2')