
from googleapiclient.discovery import build
from google.oauth2 import service_account


SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'keys.json'

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)


# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1ErdS3uL89Nh8_Z-wqC8xnhHiyqkqOkuCPlZVI4LBgfQ'


service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
# result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
#                             range="Sheet1!A1:C5").execute()

# values = result.get('values', [])

# i = ["0"]
# Weather	Morning	Night	Humidity	Pattern

data = [["Sunny", "5", "1", "43", "Cloudy"]]

# res = sheet.values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID,
#                         range ="Sheet2!A1:G1", valueInputOption="USER_ENTERED",
#                         insertDataOption="INSERT_ROWS", body={"values": data}).execute()


# print(res)

def write_data():

        res = sheet.values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                        range ="Sheet2!A1:G1", valueInputOption="USER_ENTERED",
                        insertDataOption="INSERT_ROWS", body={"values": data}).execute()
        return res

write_data()