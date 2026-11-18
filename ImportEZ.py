import ezsheets  # Import the ezsheets library to interact with Google Sheets

s = ezsheets.Spreadsheet('https://docs.google.com/spreadsheets/d/1R1uPDoGjJWe_WqTuGDexomOO9ah-1vrCB5Mc43g1pII/edit?gid=0#gid=0')  # Create a Spreadsheet object using the provided Google Sheets URL

print(s.title)  # Print the title of the spreadsheet