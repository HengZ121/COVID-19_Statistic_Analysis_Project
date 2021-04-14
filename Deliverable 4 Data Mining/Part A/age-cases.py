import psycopg2
import matplotlib.pyplot as plt


#establishing the connection to database
conn = psycopg2.connect(
   database="CSI4142",
   user='CSI4142',
   password='uOttawa1234!',
   host='lileyao1998.synology.me',
   port= '15432'
)  
cursor = conn.cursor()

### Load dataset
### New cases and mobility status of the day.
cursor.execute('''
	SELECT p.age, count(f.case_number)
	FROM postivecase p, covid_fact_table f
	WHERE f.case_number = m.case_number
	GROUP BY (p.age)
''')

x = [] #### x-axis (# of cases)
y = [] #### y-axis (age)

for record in cursor:
	x.append(record[1])
	y.append(record[0])

plt.plot(bins, y, 'r--', linewidth=1)
plt.show()