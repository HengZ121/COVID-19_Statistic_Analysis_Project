CREATE TABLE Covid_Fact_Table (
	onset_date_key int,
	reported_date_key int,
	test_date_key int,
	specimen_date_key int,
	case_number int,
	phu_location_key int,
	mobility_key int,
	special_measures_key int,
	weather_key int,
	resolved Boolean,
	unresolved Boolean,
	Fatal Boolean,
	PRIMARY KEY (onset_date_key, reported_date_key, test_date_key,
		specimen_date_key, case_number, phu_location_key, mobility_key,
		special_measures_key, weather_key)
);

CREATE TABLE PositiveCase(
	case_number int PRIMARY KEY,
	age int NOT NULL,
	gender varchar(1) NOT NULL,
	source_of_infection varchar(20)
);

CREATE TABLE PHU_Location(
	phu_location_key int PRIMARY KEY,
	phu_name varchar(20),
	phu_address varchar(20),
	city varchar(20),
	postal_code varchar(20),
	province varchar(2),
	URL varchar(50),
	latitude int,
	longitude int
);

CREATE TABLE Weather(
	weather_key int PRIMARY KEY,
	daily_high_temperature int,
	daily_low_temperature int,
	snow_on_ground int,
	total_precipitation int
);

CREATE TABLE OnsetDate(
	onset_date_key int PRIMARY KEY,
	day date,
	month varchar(3),
	day_of_week varchar(10),
	week_in_year int,
	weekend boolean,
	holiday boolean,
	season varchar(10)
);

CREATE TABLE ReportDate(
	reported_date_key int PRIMARY KEY,
	day date,
	month varchar(3),
	day_of_week varchar(10),
	week_in_year int,
	weekend boolean,
	holiday boolean,
	season varchar(10)
);

CREATE TABLE TestDate(
	test_date_key int PRIMARY KEY,
	day date,
	month varchar(3),
	day_of_week varchar(10),
	week_in_year int,
	weekend boolean,
	holiday boolean,
	season varchar(10)
);

CREATE TABLE SpecimenDate(
	specimen_date_key int PRIMARY KEY,
	day date,
	month varchar(3),
	day_of_week varchar(10),
	week_in_year int,
	weekend boolean,
	holiday boolean,
	season varchar(10)
);

CREATE TABLE  Mobility(
	mobility_key int PRIMARY KEY,
	metro_area varchar(80),
	province varchar(2),
	grocery_pharmacy int,
	parks int,
	transit_stations int,
	retail_recreation int,
	residential int,
	workplaces int
);

CREATE TABLE SpecialMeasures(
	special_measures_key int PRIMARY KEY,
	title varchar(80),
	description varchar(80),
	keyward1 varchar(20),
	keyward2 varchar(20),
	start_date date,
	end_date date
)
