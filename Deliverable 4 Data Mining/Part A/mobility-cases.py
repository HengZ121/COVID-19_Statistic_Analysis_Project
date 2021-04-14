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
	SELECT m.grocery_pharmacy, m.parks, m.transit_stations, m.retail_recreation, m.residential, m.workplaces,
		count(f.case_number)
	FROM mobility m, covid_fact_table f
	WHERE f.mobility_key = m.mobility_key
	GROUP BY (m.grocery_pharmacy, m.parks, m.transit_stations, m.retail_recreation, m.residential, m.workplaces)
''')

x = [] #### x-axis (# of cases)
parks = [] #### y-axis (age)
workplaces = []
residential = []
transit_stations = []
grocery_pharmacy = []
retail_recreation = []

for record in cursor:
	grocery_pharmacy.append(record[0])
	parks.append(record[1])
	transit_stations.append(record[2])
	retail_recreation.append(record[3])
	residential.append(record[4])
	workplaces.append(record[5])
	x.append(record[6])

fig, ax = plt.subplots(3, figsize=(15, 10))
ax[0].scatter(x, parks, s = 3)
ax[0].set_title("Parks Mobiity versus Cases")
ax[1].scatter(x, workplaces, s = 3)
ax[1].set_title("Workplaces Mobiity versus Cases")
ax[2].scatter(x, residential, s = 3)
ax[2].set_title("Residential Mobiity versus Cases")
plt.show()

fig, ax = plt.subplots(3, figsize=(15, 10))
ax[0].scatter(x, transit_stations, s = 3)
ax[0].set_title("Transit Mobiity versus Cases")
ax[1].scatter(x, grocery_pharmacy, s = 3)
ax[1].set_title("Grocery and Phamacy Mobiity versus Cases")
ax[2].scatter(x, retail_recreation, s = 3)
ax[2].set_title("Recreational Retail Mobiity versus Cases")
plt.show()