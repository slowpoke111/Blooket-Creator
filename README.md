# Blooket-Creator
Speed up Blooket creation by having a program automate most of the work.

Steps to use:
1. Create a Blooket account https://www.blooket.com/
2. Create a Blooket (Add title and description, set creation method to manual, scroll down, and click create)
3. Once editing the Blooket, select the green button labeled "Spreadsheet import"
4. A box should pop up, select copy. You will be redirected and prompted to make a copy.
5. After making a copy, share it with your Google service account.
  5a. To create a google service account:
    1. Go to the Google APIs Console (https://console.developers.google.com/).
    2. Create a new project.
    3. Click Enable API. Search for and enable the Google Drive API.
    4. Search for and enable the Google Sheets API.
    5. Create credentials for a Web Server to access Application Data.
    6. Name the service account and grant it a Project Role of Editor.
    7. Download the JSON file.
    8. Rename it to `service_account.json`(Do not share this file with anyone)
6. Install gspread (pip install gspread)
7. Download blooketsheet.py and questions.txt.
8. On line 5 change `filename` to the path of the service_account.
9. On line 6, `sa.open("filename")`, change `filename` to the name of the Google Sheet you copied earlier (The Google Sheet must be shared with the service worker. The service worker also needs to have permission to edit.).
10. Edit `questions.txt` (Use the same format as the example)
11. Run the program.
12. Open the Google Sheet.
13. Go to file and download as CSV.
14. Go back to Blooket.
15. Click upload as CSV (If you do not see the button, make sure you are editing the Blooket, then click "Spreadsheet Import").


Todo
- [x] Blooket Creator Framework
- [ ] Custom tkinkter interface/web app
- [ ] True False support (adding True when the answer is False instead of randomly picking)
