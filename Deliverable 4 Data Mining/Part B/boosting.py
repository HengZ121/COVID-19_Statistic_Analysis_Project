import psycopg2
import time
from sklearn.ensemble import GradientBoostingClassifier

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
cursor.execute(
'''SELECT m.grocery_pharmacy, m.parks, m.transit_stations, m.retail_recreation, m.residential, m.workplaces,
		CASE s.keyword1
			WHEN 'Protect' THEN 25
			WHEN 'Restrict' THEN 5
			WHEN 'Control' THEN 75
			WHEN 'Stay-at-home' THEN 100
			ELSE 0
			END,
	w.daily_high_temperature, w.daily_low_temperature, 
		CASE c.gender
			WHEN 'M' THEN 1
			ELSE 0
			END, 
	c.age as label
	FROM covid_fact_table f, mobility m, 
		specialmeasures s, weather w, positivecase c
	WHERE f.mobility_key = m.mobility_key AND
		f.special_measures_key = s.special_measures_key AND
		f.weather_key = w.weather_key AND f.case_number = c.case_number''')

### Divide instances into training and testing
training = []
label_of_training = []
testing = []
label_of_testing = []
counter = 0
age_of20 = 0
age_of10 = 0
age_of30 = 0
age_of40 = 0
age_of50 = 0
age_of60 = 0


for record in cursor:
	if record[10] == 20:
		age_of20 = age_of20 + 1
	if record[10] == 10:
		age_of10 = age_of10 + 1
	if record[10] == 30:
		age_of30 = age_of30 + 1
	if record[10] == 40:
		age_of40 = age_of40 + 1
	if record[10] == 50:
		age_of50 = age_of50 + 1
	if record[10] == 60:
		age_of60 = age_of60 + 1

	if (counter % 3 == 0):
		if record[10] >= 60:
			training.append(list(record[0:10]))
			label_of_training.append(record[10])
		else:
			testing.append(list(record[0:10]))
			label_of_testing.append(record[10])
	else:
		### age distributing in training class without controlling imbalance: 10s - 21874, 20s - 32157, 30s - 25066, 40s - 22550, 50s - 22945, 60s - 14257
		if record[10] != 20 or age_of20 < 25000:
			training.append(list(record[0:10]))
			label_of_training.append(record[10])
	counter = counter + 1

starttime = time.time()
clf = GradientBoostingClassifier(n_estimators=100, learning_rate=1.0, max_depth=1, random_state=0)
clf = clf.fit(training, label_of_training)
endtime = time.time()
TP = 0 ### correctly predicted cases whose age are below 40
FN = 0 ### cases mis-predicted age > 40
FP = 0 ### cases mis-predicted age < 40
TN = 0 ### correctly predicted cases whose age > 40

count = 0
for elem in clf.predict(testing):
	if label_of_testing[count] <= 40 and elem <= 40:
		TP = TP + 1
	elif label_of_testing[count] <= 40 and elem > 40:
		FN = FN + 1
	elif label_of_testing[count] > 40 and elem <= 40:
		FP = FP + 1
	else:
		TN = TN + 1
	count = count + 1

print("Accuracy Rate: ", (TN + TP)/len(testing))
print("Precision Rate: ", TP/(TP + FP))
print("Recall Rate: ", TP/(TP + FN))
print("Model Construction Time: ", (endtime - starttime), " sec")