import psycopg2
import csv
import requests
import json

'''
DATABASE TABLE:
  date_key int PRIMARY KEY,
  day date,
  month varchar(3),
  day_of_week varchar(10),
  week_in_year int,
  weekend boolean,
  holiday boolean,
  season varchar(10)
'''
### 
insert_query = "INSERT INTO Mobility (date_key, day, month, day_of_week, week_in_year, weekend, holiday, season) VALUES "
days_code_dictionary = {
  '1': 'Monday',
  '2': 'Tuesday',
  '3': 'Wednesday',
  '4': 'Thursday',
  '5': 'Friday',
  '6': 'Saturday',
  '7': 'Sunday',
}
month_code_dictionary = {
  '01': 'JAN',
  '02': 'FEB',
  '03': 'MAR',
  '04': 'APR',
  '05': 'MAY',
  '06': 'JUN',
  '07': 'JUL',
  '08': 'AUG',
  '09': 'SEP',
  '10': 'OCT',
  '11': 'NOV',
  '12': 'DEC'
}

seasons_code_dictionary = {
  '01': 'Winter',
  '02': 'Winter',
  '03': 'Spring',
  '04': 'Spring',
  '05': 'Spring',
  '06': 'Summer',
  '07': 'Summer',
  '08': 'Summer',
  '09': 'Fall',
  '10': 'Fall',
  '11': 'Fall',
  '12': 'Winter'
}
holidays = []
print("Getting Holiday Info...")
holiday_api_url = "https://holidayapi.com/v1/holidays?pretty&key=7ebcf0af-6d7c-41a0-b3e3-28efe08d5fd7&country=CA&year=2020"
h_info = requests.get(holiday_api_url).json()["holidays"]
for holiday in h_info:
  holidays.append(holiday["date"])


class Instance:
    def __init__ (self, date_key, day, month, day_of_week, week_in_year, weekend, season):
        self.date_key = date_key
        self.day = day
        self.month = month
        self.day_of_week = day_of_week
        self.week_in_year = week_in_year
        self.weekend = weekend
        if self.day in holidays:
          self.holiday = 'true'
        else:
          self.holiday = 'false'
        self.season = season

    def insert_data_into_onset_d (self):
        insert_query = "INSERT INTO OnsetDate (onset_date_key, day, month, day_of_week, week_in_year, weekend, holiday, season) VALUES "
        values_string = "("+self.date_key+",'" +  self.day +"', '"+self.month + "','" + self.day_of_week +"'," +self.week_in_year +"," +self.weekend + ","+ self.holiday + ",'"+ self.season +"')"
        cursor.execute(insert_query + values_string)
    def insert_data_into_report_d (self):
        insert_query = "INSERT INTO ReportDate (reported_date_key, day, month, day_of_week, week_in_year, weekend, holiday, season) VALUES "
        values_string = "("+self.date_key+",'" +  self.day +"', '"+self.month + "','" + self.day_of_week +"'," +self.week_in_year +"," +self.weekend + ","+ self.holiday + ",'"+ self.season +"')"
        cursor.execute(insert_query + values_string)
    def insert_data_into_test_d (self):
        insert_query = "INSERT INTO TestDate (test_date_key, day, month, day_of_week, week_in_year, weekend, holiday, season) VALUES "
        values_string = "("+self.date_key+",'" +  self.day +"', '"+self.month + "','" + self.day_of_week +"'," +self.week_in_year +"," +self.weekend + ","+ self.holiday + ",'"+ self.season +"')"
        cursor.execute(insert_query + values_string)
    def insert_data_into_specimen_d (self):
        insert_query = "INSERT INTO SpecimenDate (specimen_date_key, day, month, day_of_week, week_in_year, weekend, holiday, season) VALUES "
        values_string = "("+self.date_key+",'" +  self.day +"', '"+self.month + "','" + self.day_of_week +"'," +self.week_in_year +"," +self.weekend + ","+ self.holiday + ",'"+ self.season +"')"
        cursor.execute(insert_query + values_string)

print("Loading Information...")
content=[]
with open('date.csv', encoding = 'utf-8-sig') as file:
    reader = csv.reader(file)
    for row in reader:
        content.append(row)

print("Information Loaded")

#establishing the connection to database
conn = psycopg2.connect(
   database="CSI4142",
   user='CSI4142',
   password='uOttawa1234!',
   host='lileyao1998.synology.me',
   port= '15432'
)  
cursor = conn.cursor()

print("Database Connected")

### load all mobility information

print("Data Staging in Progress")
for elem in content:
    date_key = elem[0].replace('-','')
    weekend = 'false'
    if (elem[1] == '6' or elem[1] == '7'): 
      weekend = 'true' 
    else: 
      weekend = 'false'
    ins = Instance( date_key,  elem[0], month_code_dictionary[elem[0][5:7]], days_code_dictionary[elem[1]], elem[2], weekend, seasons_code_dictionary[elem[0][5:7]])
    ins.insert_data_into_onset_d()
    ins.insert_data_into_specimen_d()
    ins.insert_data_into_test_d()
    ins.insert_data_into_report_d()


print("Datastaging Completed")


# Commit changes in the database
conn.commit()
conn.close()