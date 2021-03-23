import psycopg2
import csv

### 


#establishing the connection to database
conn = psycopg2.connect(
   database="CSI4142",
   user='CSI4142',
   password='uOttawa1234!',
   host='lileyao1998.synology.me',
   port= '15432'
)  
cursor = conn.cursor()

### load all mobility information
print("Loading Dataset...")
content=[]
with open('cases.csv', encoding = 'utf-8-sig') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        content.append(row)

print("Dataset Loaded")

print("Deleting Irrelavant Records from database")
for elem in content:
    case_number = elem[0]
    onset_date_key = elem[1].replace('-','')
    if (int(onset_date_key) < 20201101):
        cursor.execute("DELETE FROM positivecase WHERE case_number = "+ case_number)
    

#Getting query
cursor.close()
print("Data Staging Finished")

# Commit changes in the database
conn.commit()
conn.close()
