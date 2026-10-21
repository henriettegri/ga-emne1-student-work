-- sjekke at man bruker riktig database.
USE world;


-- Innebygde funksjoner - aggregatfunksjon

SELECT SUM(Population) AS total_population,
AVG(Population) AS avg_population,
MIN(Population) AS min_population,
MAX(Population) AS max_population
FROM city
WHERE CountryCode = 'NOR'

-- kan telle kolonne
SELECT COUNT(IndepYear)
FROM Country;
-- flere rader har NULL, teller ikke med dem.


SELECT AVG(Population)
FROM country;

-- lettere å lese, delt opp i millioner
SELECT Name, Population / 1000000 AS pop_millions
FROM country;

-- begrenser antall rader.
SELECT Name, Population / 1000000 AS pop_millions
FROM country
WHERE Population > 10000000
ORDER BY pop_millions DESC;

-- rekkefølge
SELECT Population
FROM country
-- WHERE
GROUP BY
-- ORDER BY
-- LIMIT;

SELECT Continent, SUM(Population)
FROM country
-- WHERE
GROUP BY Continent
-- ORDER BY
-- LIMIT;
;


SELECT Continent, SUM(Population), COUNT(*)
FROM country
-- WHERE
GROUP BY Continent
-- ORDER BY
-- LIMIT;
;

SELECT Continent, Region, SUM(Population), COUNT(*)
FROM country
-- WHERE
GROUP BY Continent, Region
-- ORDER BY
-- LIMIT;
;

-- bøtter, sorterer i bøtter og så summerer opp det som er i bøttene
SELECT Continent, Region, SUM(Population), COUNT(*)
FROM country
-- WHERE
GROUP BY Continent, Region
ORDER BY Continent ASC, Region ASC
-- LIMIT;
;



-- sortert alfabetisk på kontinent, så på summen av befolkning
SELECT Continent, Region, SUM(Population), COUNT(*)
FROM country
-- WHERE
GROUP BY Continent, Region
ORDER BY Continent ASC, SUM(Population) ASC
-- LIMIT;
;



-- Having
SELECT Continent, COUNT(*)
FROM country
-- WHERE
GROUP BY Continent
-- ORDER BY Continent ASC, SUM(Population) ASC
-- LIMIT;
;

-- de som er for små får ikke være med
SELECT Continent, COUNT(*)
FROM country
WHERE Population > 10000000
GROUP BY Continent
-- ORDER BY Continent ASC, SUM(Population) ASC
-- LIMIT;
;

-- having - bare kontinenter som har fem eller flere land. Where er en sjekk av rader, having er en sjekk på resultatene av group by,
SELECT Continent, COUNT(*)
FROM country
WHERE Population > 10000000
GROUP BY Continent
HAVING COUNT(*) >= 5
-- ORDER BY Continent ASC, SUM(Population) ASC
-- LIMIT;
;

SELECT Continent, COUNT(*) AS country_count
FROM country
WHERE Population > 10000000
GROUP BY Continent
HAVING COUNT(*) >= 5
-- ORDER BY Continent ASC, SUM(Population) ASC
-- LIMIT;
;

-- kan bruke alias, men ikke i where
SELECT Continent, COUNT(*) AS country_count
FROM country
WHERE Population > 10000000
GROUP BY Continent
HAVING country_count>= 5
-- ORDER BY Continent ASC, SUM(Population) ASC
-- LIMIT;
;

SELECT Continent, COUNT(*) AS country_count
FROM country
WHERE Population > 10000000
GROUP BY Continent
HAVING country_count>= 5
ORDER BY country_count
-- LIMIT;
;


SELECT Continent, COUNT(*) AS country_count
FROM country
WHERE Population > 10000000
GROUP BY Continent
HAVING country_count>= 5
ORDER BY country_count
-- LIMIT;
;