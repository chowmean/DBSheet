import gspread
from oauth2client.service_account import ServiceAccountCredentials
from settings import api_creds, scope
class DbSheet:
    def __init__(self, db_name):
        self.db_name = db_name
        self.scope = scope

    def get_db_conn(self):
        db_scope = self.scope
        creds = ServiceAccountCredentials.from_json_keyfile_name(api_creds, db_scope)
        client = gspread.authorize(creds)
        db_conn = client.open(self.db_name)
        return db_conn