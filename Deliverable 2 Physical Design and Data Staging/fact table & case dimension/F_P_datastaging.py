import psycopg2
import csv

### 
phu_dic = {"Toronto Public Health": '001', 
"Durham Region Health Department":  '002', 
"Halton Region Health Department" :'003', 
"Peel Public Health" : '004', 
"York Region Public Health Services" :'005', 
"Ottawa Public Health" : '006'}

weather_dic = {
"Toronto Public Health": '1', 
"Durham Region Health Department":  '5', 
"Halton Region Health Department" :'4', 
"Peel Public Health" : '2', 
"York Region Public Health Services" :'3', 
"Ottawa Public Health" : '6'
}




class Instance:
    def __init__ (self, onset_date_key, reported_date_key, test_date_key, specimen_date_key, case_number, 
      phu_location_key, mobility_key, special_measures_key, weather_key, resolved, unresolved, fatal,
      age, gender, source_of_infection):
        self.onset_date_key = onset_date_key
        self.reported_date_key = reported_date_key
        self.test_date_key = test_date_key
        self.specimen_date_key = specimen_date_key
        self.case_number = case_number
        self.phu_location_key = phu_location_key
        self.mobility_key = mobility_key
        self.special_measures_key =special_measures_key #### Complex Value
        self.weather_key = weather_key
        self.resolved = resolved
        self.unresolved = unresolved
        self.fatal = fatal
        self.age = age
        self.gender = gender
        self.source_of_infection = source_of_infection
        
    def insert_data (self):
        query_un = "INSERT INTO PositiveCase (case_number, age, gender, source_of_infection) VALUES (%s, %s, '%s', '%s')" %(self.case_number, self.age, self.gender, self.source_of_infection)
        query_deux = ("INSERT INTO Covid_Fact_Table (onset_date_key, reported_date_key, test_date_key, "
          "specimen_date_key, case_number, phu_location_key, mobility_key, special_measures_key, weather_key"
          ", resolved, unresolved, fatal) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,'%s','%s','%s')" 
          %(self.onset_date_key, self.reported_date_key, self.test_date_key, self.specimen_date_key, self.case_number, 
            self.phu_location_key, self.mobility_key,self.special_measures_key, self.weather_key
          , self.resolved, self.unresolved, self.fatal))
        cursor.execute(query_un)
        cursor.execute(query_deux)

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

print("Data Staging in Progress")
for elem in content:
	phu = elem[11]
	if phu in phu_dic:
		case_number = elem[0]
		onset_date_key = elem[1].replace('-','')
		reported_date_key = elem[2].replace('-','')
		test_date_key = elem[3].replace('-','')
		if(test_date_key == ''):
			test_date_key = reported_date_key
		specimen_date_key = elem[4].replace('-','')
		if(specimen_date_key == ''):
			specimen_date_key = reported_date_key
		phu_location_key = elem[10]
		mobility_key = phu_dic[phu]+elem[1].replace('-','')
		cursor.execute("SELECT special_measures_key FROM specialmeasures WHERE start_date <= '%s' AND end_date > '%s' AND description = '%s'" 
        	%(elem[1],elem[1],phu) )
		special_measures_key = '0'
		m_k = cursor.fetchone()
		if type(m_k) is tuple:
			special_measures_key = m_k[0]
		weather_key = weather_dic[phu] + elem[1].replace('-','')
		age = elem[5].strip('s').strip('+')
		if (age == '<20'):
			age = '10'
		elif (age == 'UNKNOWN'):
			age = '0'
		gender = elem[6][0]
		source_of_infection = elem[7]

		resolved = 'false'
		unresolved = 'false'
		fatal = 'false'
		if (elem[8] == 'Resolved'):
			resolved = 'true'
		elif (elem[8] == 'Fatal'):
			fatal = 'true'
		else:
			unresolved = 'true'

		Instance(onset_date_key, reported_date_key, test_date_key, specimen_date_key, case_number, 
          phu_location_key, mobility_key, special_measures_key, weather_key, resolved, unresolved, fatal,
          age, gender, source_of_infection).insert_data()
        
    

#Getting query
cursor.close()
print("Data Staging Finished")

# Commit changes in the database
conn.commit()
conn.close()
