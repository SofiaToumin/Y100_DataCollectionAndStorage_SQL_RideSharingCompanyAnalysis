#1. Print the company_name field.
#Find the number of taxi rides for each taxi company for November 15-16, 2017,
#name the resulting field trips_amount, and print it, too.
#Sort the results by the trips_amount field in descending order.
select
    cabs.company_name as company_name,
    count(trips.trip_id) as trips_amount
from cabs
right join trips on trips.cab_id = cabs.cab_id
where
    start_ts :: date IN ('2017-11-15', '2017-11-16')
group by
    cabs.company_name
order by
    trips_amount DESC;

#2. Find the number of rides for every taxi company whose name contains the words
#"Yellow" or "Blue" for November 1-7, 2017.
#Name the resulting variable trips_amount. Group the results by the company_name field.
SELECT
    cabs.company_name as company_name,
    COUNT(trips.trip_id) AS trips_amount
FROM
    cabs
INNER JOIN
    trips
ON
    trips.cab_id = cabs.cab_id
WHERE
    CAST(trips.start_ts AS date) BETWEEN '2017-11-01' AND '2017-11-07'
    AND cabs.company_name LIKE '%%Yellow%%'
GROUP BY company_name
UNION ALL
SELECT
    cabs.company_name as company_name,
    COUNT(trips.trip_id) AS trips_amount
FROM
    cabs
INNER JOIN
    trips
ON
    trips.cab_id = cabs.cab_id
WHERE
    CAST(trips.start_ts AS date) BETWEEN '2017-11-01' AND '2017-11-07'
    AND cabs.company_name LIKE '%%Blue%%'
GROUP BY company_name;

#3.For November 1-7, 2017, the most popular taxi companies were Flash Cab and Taxi Affiliation Services.
#Find the number of rides for these two companies and name the resulting variable trips_amount.
#Join the rides for all other companies in the group "Other." Group the data by taxi company names.
#Name the field with taxi company names company. Sort the result in descending order by trips_amount.
SELECT
    CASE
        WHEN CABS.COMPANY_NAME != 'Flash Cab' AND
        CABS.COMPANY_NAME != 'Taxi Affiliation Services'
        THEN 'Other'
        ELSE CABS.COMPANY_NAME
        END AS COMPANY,
    COUNT(TRIPS.TRIP_ID) AS TRIPS_AMOUNT
FROM
    CABS
INNER JOIN TRIPS ON TRIPS.CAB_ID = CABS.CAB_ID
WHERE START_TS :: DATE BETWEEN '2017-11-01' AND '2017-11-07'
GROUP BY
    COMPANY
ORDER BY
    TRIPS_AMOUNT DESC;

#4.Retrieve the identifiers of the O'Hare and Loop neighborhoods from the neighborhoods table.
SELECT
    NEIGHBORHOOD_ID,
    NAME
FROM NEIGHBORHOODS
WHERE
    NAME LIKE '%Hare' OR
    NAME LIKE 'Loop';

#5.For each hour, retrieve the weather condition records from the weather_records table.
#Using the CASE operator, break all hours into two groups: Bad if the description field contains
#the words rain or storm, and Good for others. Name the resulting field weather_conditions.
#The final table must include two fields: date and hour (ts) and weather_conditions.
SELECT
    TS,
    CASE WHEN DESCRIPTION LIKE '%rain%' OR
              DESCRIPTION LIKE '%storm%'
              THEN 'Bad'
         ELSE 'Good'
         END AS WEATHER_CONDITIONS
FROM
    WEATHER_RECORDS;

#6.Retrieve from the trips table all the rides that started in the Loop (pickup_location_id: 50) on a Saturday
#and ended at O'Hare (dropoff_location_id: 63). Get the weather conditions for each ride.
#Use the method you applied in the previous task. Also, retrieve the duration of each ride.
#Ignore rides for which data on weather conditions is not available. Sort by trip_id.
SELECT
    TRIPS.START_TS AS START_TS,
    CASE WHEN WEATHER_RECORDS.DESCRIPTION LIKE '%rain%' OR
              WEATHER_RECORDS.DESCRIPTION LIKE '%storm%'
              THEN 'Bad'
         ELSE 'Good' END AS WEATHER_CONDITIONS,
    TRIPS.DURATION_SECONDS AS DURATION_SECONDS
FROM
    TRIPS
INNER JOIN WEATHER_RECORDS ON WEATHER_RECORDS.TS  = TRIPS.START_TS
WHERE
    TRIPS.PICKUP_LOCATION_ID = 50 AND
    TRIPS.DROPOFF_LOCATION_ID = 63 AND
    EXTRACT (ISODOW FROM TRIPS.START_TS) = 6
ORDER BY
    TRIPS.TRIP_ID;
