The weather station used:

Toronto City ONTARIO
TORONTO BUTTONVILLE A ONTARIO
TORONTO LESTER B. PEARSON INT'L A ONTARIO
Ottawa CDA RCS

Give each station a code:
Toronto City ONTARIO----1
TORONTO BUTTONVILLE A ONTARIO----2
TORONTO LESTER B. PEARSON INT'L A ONTARIO----3
Ottawa CDA RCS----6

The value of weather_key is concatenation of station code and date. For example, the weather_key for ottawa on 2020/01/17 is 620200117.
This is done in Excel via 'concatenate(COL1, COL2)'

For missing values， here is the solution:
- All missing 'snow_on_ground' and 'total_recipitation' are filled with 0.
- all missing temperature are filled with mean value of the day before and after of the missing date.
 

