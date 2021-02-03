CREATE TABLE Covid_Fact_Table (
	case_number int,
	area_number int,
	date_confirmed date,
	PRIMARY KEY (case_number, area_number, date_confirmed)
)

CREATE TABLE PositiveCase(
	case_number int PRIMARY KEY,
	age int NOT NULL,
	gender varchar(1) NOT NULL,
	source_of_infection varchar(20),
	test_date date NOT NULL,
	area_number int
)

CREATE TABLE CityDailyInfo(
	area_number int,
	updated_date date,
	testing_facilities_type varchar(20),
	availability_of_facilities int,
	total_cases int NOT NULL,
	weather varchar(20),
	gathering_area_type varchar(20),
	mobility_info varchar(20),
	average_stay_duration int,
	PRIMARY KEY (area_number, updated_date)
)