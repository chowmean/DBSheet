class Table:
    def __init__(self, columns, name):
        self.columns = columns
        self.name = name


class CreateTable:
    def __init__(self, table_obj, sheet_obj):
        self.table = table_obj
        self.sheet = sheet_obj

    def create_table(self):
        cols = len(self.table.columns)
        name = self.table.name
        rows = 1
        wk_sheet = self.sheet.add_worksheet(name, rows, cols)
        return self.addRows(wk_sheet)

    def addRows(self,worksheet):
        worksheet.append_row(self.table.columns)
        worksheet.delete_row(1)
        return True


class WorkingTable:
    def __init__(self, name, sheet_obj):
        for i in range(0,100):
            self.wk_sheet = sheet_obj.get_worksheet(i)
            if self.wk_sheet.title == name:
                break
            elif self.wk_sheet.title == "":
                return "No sheet with this name found"

    def get_all(self):
        return self.wk_sheet.get_all_records()

    def insert(self, row):
        if len(row) != self.wk_sheet.col_count:
            return "Column count doest match"
        return self.wk_sheet.append_row(row)

    def get_one(self,key, value):
        return self.find(key, value, 1)

    def get_attr(self, key, value):
        return self.find(key,value)

    def find(self,key, value, count=-1):
        all_data = self.get_all()
        matched_rows = []
        matched_count = 0
        for each_d in all_data:
            if each_d[key] == value:
                matched_rows.append(each_d)
                matched_count = matched_count +1
                if matched_count == count:
                    break;
        return matched_rows

    def get_index(self,key, value):
        all_data = self.get_all()
        matched_rows = []
        index = 1
        for each_d in all_data:
            if each_d[key] == value:
                return index + 1
            index = index + 1
        return -1

    def delete(self,key, value):
        index = self.get_index(key, value)
        print index
        while index != -1:
            self.wk_sheet.delete_row(index)
            index = self.get_index(key, value)