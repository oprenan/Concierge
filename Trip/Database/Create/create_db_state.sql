CREATE DATABASE main;
USE main;

CREATE SCHEMA FLIGHTSEARCHER;

CREATE user dealer_ddl;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA flightsearcher TO dealer_ddl;

CREATE user dealer_ro;
GRANT SELECT ON ALL TABLES IN SCHEMA flightsearcher TO dealer_ro;

