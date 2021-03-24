a.
/*explore the total number of positive cases in your data mart; drill down to a month (December 2020)
SELECT count(*), d.month
FROM date d, covid_fact_table f
WHERE f.reported_date_key = d.date_key AND d.month = 'DEC'
group by d.month

/*drill down to a specific day: 2020-12-19
SELECT count(*), d.day
FROM date d, covid_fact_table f
WHERE f.reported_date_key = d.date_key AND d.day = '2020-12-19'
group by d.day


/*consider all the unresolved cases in Toronto City
SELECT count(*), f.unresolved
FROM covid_fact_table f, phu_location p
WHERE f.phu_location_key=p.phu_location_key AND p.phu_name='Toronto Public Health'
group by f.unresolved

/*roll up to all data in data mart
SELECT count(*), f.unresolved,p.city
FROM covid_fact_table f, phu_location p
WHERE f.phu_location_key=p.phu_location_key 
group by f.unresolved, rollup (p.city,p.province)
order by p.city


b.
/*the number of cases in a specific PHU(resolved, unresolved and fatal)
SELECT count(*), f.resolved,f.unresolved,f.fatal
FROM phu_location p, covid_fact_table f
WHERE f.phu_location_key=p.phu_location_key AND p.phu_name='Toronto Public Health'
GROUP by f.resolved,f.unresolved,f.fatal

/*the number cases across the PHUs when a specific special measure was in place
SELECT count(*), s.description
FROM covid_fact_table f,specialmeasures s
WHERE f.special_measures_key=s.special_measures_key AND s.keyward1='Stay-at-home'
group by s.description

c.
/*provide the number of fatal cases during DEC and JAN, in Oakville and Ottawa
SELECT count(*), f.fatal,p.city
FROM covid_fact_table f, phu_location p, date d
WHERE d.month in ('DEC', 'JAN') AND p.city in ('Oakville','Ottawa') AND f.phu_location_key=p.phu_location_key AND f.reported_date_key = d.date_key
group by f.fatal,p.city

/*provide the number of unresolved cases when contrasting two mobility locations, e.g.,parks and transit, in Peel and Ottawa.
SELECT count(*), f.unresolved,m.parks,m.transit_stations,m.metro_area
FROM covid_fact_table f, mobility m
WHERE m.metro_area in ('Regional Municipality of Peel','Ottawa Division') AND f.mobility_key=m.mobility_key
group by f.unresolved,m.parks,m.transit_stations,m.metro_area
order by m.metro_area

d.

/* during different month
SELECT count(*), d.month
FROM date d, covid_fact_table f
WHERE f.reported_date_key = d.date_key 
group by d.month
ORDER BY count(*) DESC

/*when certain types of measures are in place
SELECT count(*), s.keyward1
FROM covid_fact_table f,specialmeasures s
WHERE f.special_measures_key=s.special_measures_key 
group by s.keyward1
ORDER BY count(*) DESC


/*contrasting mobility levels in Ottawa and Peel
SELECT count(*),m.metro_area,m.grocery_pharmacy,m.parks,m.transit_stations,m.retail_recreation,m.residential,m.workplaces
FROM covid_fact_table f, mobility m
WHERE m.metro_area in ('Regional Municipality of Peel','Ottawa Division') AND f.mobility_key=m.mobility_key
group by m.metro_area,m.grocery_pharmacy,m.parks,m.transit_stations,m.retail_recreation,m.residential,m.workplaces








