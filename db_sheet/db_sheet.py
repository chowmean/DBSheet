import gspread
from oauth2client.service_account import ServiceAccountCredentials
class DbSheet:
    def __init__(self, db_name, api_creds, scope):
        self.db_name = db_name
        self.api_creds = api_creds
        self.scope = scope

    def get_db_conn(self):
        db_scope = self.scope
        creds = ServiceAccountCredentials.from_json_keyfile_name(self.api_creds, db_scope)
        client = gspread.authorize(creds)
        db_conn = client.open(self.db_name)
        return db_conn