1. Choose weather station from Weather data: https://climate.weather.gc.ca/historical_data/search_historic_data_e.html

The weather station we used are:
1)Toronto City ONTARIO                             in Toronto downtown
2) TORONTO LESTER B. PEARSON INT'L A ONTARIO       in Peel Region
3) TORONTO BUTTONVILLE A ONTARIO                   in York Region
4) BURLINGTON PIERS ONTARIO                        in Halton Region
5) OSHAWA ONTARIO                                  in Durham Region
6) Ottawa CDA RCS                                  in Ottawa

2. The value of weather_key is concatenation of station code and date. For example, the weather_key for ottawa on 2020/01/17 is 620200117.
This is done in Excel via 'concatenate(COL1, COL2)'

3. For missing values， here is the solution:
- All missing 'snow_on_ground' and 'total_recipitation' are filled with 0.
- all missing temperature are filled with mean value of the day before and after of the missing date.
 
4. import data use the menu in pgAdmin4 page: 
   - right click and choose 'import'
   - in the pop-up box select the csv file that are data staged.
   - delimit using comma ","
   


