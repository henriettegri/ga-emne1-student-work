USE world;

SELECT *
FROM country

SELECT DATABASE();


CREATE USER 'city_reader'@'%'
IDENTIFIED BY 'ReadOnly_09!';
-- % er wildcard

-- gi rettigheter, skal få lov til å gjøre select-spørringer, på world.city-schema
-- ikke lov til insert, update osv.
GRANT SELECT ON world.city
TO 'city_reader'@'%';

-- sjekke at brukeren finnes og hvilke rettigheter den har
SHOW GRANTS
FOR 'city_reader'@'%';


SELECT CURRENT_USER();

-- mySQL har den siste biten
SELECT CURRENT_USER(), CONNECTION_ID();

-- får ikke lov til å hente fra country, eller update, får feilmelding
SELECT *
FROM country;

UPDATE city
SET Population = 100
WHERE CountryCode = 'NOR'
AND Name = 'Oslo';

SELECT Name, Population
FROM city
WHERE CountryCode = 'NOR'
    AND Name IN ('Oslo', 'Bergen');


