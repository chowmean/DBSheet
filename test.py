import gspread
from oauth2client.service_account import ServiceAccountCredentials
from GoogleSheetClass import Table, CreateTable


table = Table( {"data1", "data2", "data2"}, "Testtable2")

#use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)


sheet = client.open("SHEETBACKEND")

# Extract and print all of the values
#list_of_hashes = sheet.get_all_records()
#print(list_of_hashes)
creator = CreateTable(table, sheet)
creator.create_table()
#sheet.add_worksheet("table_name",4, 12)