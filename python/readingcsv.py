import csv
from datetime import date
 
# csv file name
filename = "test.csv"
today = date.today() 
# initializing the titles and rows list
fields = []
rows = []
 

print("today : ", today)
# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
     
    # extracting field names through first row
    fields = next(csvreader)
 
    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)
     # get total number of rows
    print("Total no. of rows: %d"%(csvreader.line_num))
 
# printing the field names
print('Field names are:' + ', '.join(field for field in fields))
 
# printing first 5 rows
print('\nFirst 5 rows are:\n')
for row in rows:
    # parsing each column of a row
    for col in row:
        print("%10s"%col,end=" "),
    print('\n')