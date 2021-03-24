/*Iceberg: Top 5 days that have the most cases (by onset_date) from all 6 phu units*/
SELECT d.day, count(*)
FROM date d, covid_fact_table f
WHERE f.onset_date_key = d.date_key AND d.day < ('2021-03-01'::Date)
GROUP BY (d.day)
ORDER BY count(*) DESC LIMIT 5

/*Windowing: Rank all phu_units in terms of number of cases (reported date) per month 
from 2020-11-01 to 2021-02-28*/
SELECT p.phu_name, d.month, count(*) as resolved_case_total,
RANK() OVER (PARTITION BY d.month ORDER BY count(*)DESC)
FROM phu_location p, date d, covid_fact_table f
WHERE p.phu_location_key = f.phu_location_key
AND f.reported_date_key = d.date_key AND d.day < ('2021-03-01'::Date)
GROUP BY (p.phu_location_key, d.month)

/*Window Clause: Compare the quantity of resolved cases in Ottawa for every month between
Nov. 2020 to Feb.2021 with the average of quantities of resolved cases in Ottawa among those
four months, onset date is used to analyze since we found the outbreak happened at the end of
Dec., and many people did show symptoms in Dec. but reported in JAN thus it is better to count
cases based on the date they had corona virus */
SELECT p.phu_name, d.month, count(*) AS resolved_case_total, 
ROUND((count(*) - (AVG(count(*)) OVER W)),2) AS comparsion
FROM phu_location p, date d, covid_fact_table f
WHERE p.phu_location_key = f.phu_location_key AND f.phu_location_key =2251 
AND f.onset_date_key = d.date_key AND f.resolved = true AND d.day < ('2021-03-01'::Date)
GROUP BY (p.phu_location_key, d.month)
WINDOW W AS (PARTITION BY p.phu_name )
ORDER BY CASE d.month
	WHEN 'NOV' THEN 00
	WHEN 'DEC' THEN 01
	WHEN 'JAN' THEN 02
	WHEN 'FEB' THEN 03
	END