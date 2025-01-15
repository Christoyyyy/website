from flask import Flask,render_template,request,redirect,url_for
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

app = Flask(__name__)

# Path to your service account JSON file
SERVICE_ACCOUNT_FILE = 'service.json'

# Google Sheets ID (Replace with your Google Sheet ID)
SPREADSHEET_ID = '1EYelOw9oOb5cnsF2CIfFk56-PMWS79nPA5l7lpF6nyA'





SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# Authenticate with Google Sheets API
credentials = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('sheets', 'v4', credentials=credentials)
sheet = service.spreadsheets()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    phone = request.form.get('phone')
    email = request.form.get('email')
    journey = request.form.get('journey')
    destiny = request.form.get('destiny')
    gpay = request.form.get('gpay')
    paytm = request.form.get('paytm')
    male = request.form.get('male')
    female = request.form.get('female')

    # Append the data to Google Sheets
    values = [[name, email, phone,journey,destiny,gpay,paytm,male,female]]
    body = {'values': values}
    result = sheet.values().append(
        spreadsheetId=SPREADSHEET_ID,
        range="Sheet1!A1",
        valueInputOption="RAW",
        insertDataOption="INSERT_ROWS",
        body=body
    ).execute()

    print(f"{result.get('updates').get('updatedCells')} cells appended.")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)