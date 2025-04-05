select 
    origin_city as origin_city_o
    ,origin_country
    ,destiny_city as destiny_city_o
    ,destiny_country
    ,travel_date::date as travel_date
    ,origin_city || '- Date: ' || travel_date as origin_city
    ,destiny_city || '- Date: ' || travel_date as destiny_city
    ,min(price * 0.85) as price
    ,count(companies) as companies
from 
    flightsearcher.summary_view
WHERE 1=1
    --and org in ('GRU','BCN','LIS','MAD','CDG')
    --and dest in ('GRU','BCN','LIS','MAD','CDG')
    and travel_date between date'{START_DATE}' AND date'{END_DATE}'
    and destiny_city is not null and origin_city is not null
group by
    1,2,3,4,5;

