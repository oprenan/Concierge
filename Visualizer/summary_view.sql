create or replace view flightsearcher.summary_view as
	select
		INITCAP(org_airport_city) as origin_city
		,INITCAP(org_airport_country) as origin_country
		,INITCAP(dest_airport_city) as destiny_city
		,INITCAP(dest_airport_country) as destiny_country
		,travel_date
		,price
		,companies
		,duration
		,stops
		,layovers
		,rn as price_rank
	from (
		select 
			org
			,org_airport.name as org_airport_name
			,org_airport.city as org_airport_city
			,org_airport.country as org_airport_country
			,dest
			,dest_airport.name as dest_airport_name
			,dest_airport.city as dest_airport_city
			,dest_airport.country as dest_airport_country
			,travel_date
			,price
			,companies
			,duration
			,stops
			,layovers
			,row_number() over (partition by org,dest,travel_date order by price asc) as rn
		from 
			flightsearcher.flight f
			left join flightsearcher.airports org_airport on f.org = org_airport.iata_code
			left join flightsearcher.airports dest_airport on f.org = dest_airport.iata_code
		where 1=1
			and stops is not null
	) dev
	order by org,dest,travel_date
;	
