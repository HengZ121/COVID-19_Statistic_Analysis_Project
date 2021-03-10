import psycopg2


### 
targeted_regions = ["Toronto Division", "Regional Municipality of Durham", "Regional Municipality of Halton", "Regional Municipality of Peel", "Regional Municipality of York", "Ottawa Division"]
region_code = ["1","2","3","4","5","6"]
insert_query = "INSERT INTO Mobility (mobility_key, metro_area, province, grocery_pharmacy, parks, transit_stations, retail_recreation, residential, workplaces) VALUES "
province_abbrev = {
  'Alberta': 'AB',
  'British Columbia': 'BC',
  'Manitoba': 'MB',
  'New Brunswick': 'NB',
  'Newfoundland and Labrador': 'NL',
  'Northwest Territories': 'NT',
  'Nova Scotia': 'NS',
  'Nunavut': 'NU',
  'Ontario': 'ON',
  'Prince Edward Island': 'PE',
  'Quebec': 'QC',
  'Saskatchewan': 'SK',
  'Yukon': 'YT'
}
class Instance:
    def __init__ (self, mobility_key, metro_area, province, grocery_pharmacy,
                  parks, transit_stations, retail_recreation, residential, workplaces):
        self.mobility_key = mobility_key
        self.metro_area = metro_area
        self.province = province
        self.grocery_pharmacy = grocery_pharmacy
        self.parks = parks
        self.transit_stations = transit_stations
        self.retail_recreation = retail_recreation
        self.residential =residential
        self.workplaces = workplaces

        if self.grocery_pharmacy == "":
            self.grocery_pharmacy = "NULL"
        if self.parks == "":
            self.parks = "NULL"
        if self.transit_stations == "":
            self.transit_stations = "NULL"
        if self.retail_recreation == "":
            self.retail_recreation = "NULL"
        if self.residential == "":
            self.residential = "NULL"
        if self.workplaces == "":
            self.workplaces = "NULL"
        
    def insert_data (self):
        values_string = "("+self.mobility_key+",'" +  self.metro_area +"', '"+self.province + "'," + self.grocery_pharmacy +"," +self.parks + ","+ self.transit_stations + ","+ self.retail_recreation + ","+ self.residential + "," + self.workplaces+")"
        cursor.execute(insert_query + values_string)


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
file = open("mobility_info.txt", encoding = "utf8")
content = file.readlines()
print("Information Loaded")

print("Data Staging in Progress")
for elem in content:
    fragment = elem.split(",")
    for count in range (len(targeted_regions)):
        # check whether the info fragment is in city we want
        if targeted_regions[count] == fragment[3]:
            mobility_key = region_code[count]+fragment[8].replace('-','')
            Instance(mobility_key, fragment[3], province_abbrev[fragment[2]],fragment[10],fragment[11],fragment[12],fragment[9],fragment[14],fragment[13]).insert_data()
            break

#Getting query
cursor.close()
print("Data Staging Finished")

# Commit changes in the database
conn.commit()
conn.close()
