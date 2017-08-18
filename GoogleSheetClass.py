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

    def get_rows(self):
        pass


