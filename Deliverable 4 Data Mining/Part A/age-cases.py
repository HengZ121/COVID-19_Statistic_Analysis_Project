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
	FROM positivecase p, covid_fact_table f
	WHERE f.case_number = p.case_number
	GROUP BY (p.age)
''')

y = [] #### y-axis (# of cases)
x = [] #### x-axis (age)

for record in cursor:
	y.append(record[1])
	x.append(record[0])

plt.plot(x, y, 'r--', linewidth=1)
plt.title("# of cases among different age group")
plt.show()