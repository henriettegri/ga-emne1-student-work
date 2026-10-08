-- Enkel spørring for å hente alle kolonner og rader i oppgitt tabell (city).

SELECT *
FROM city
WHERE countrycode = 'NOR';

-- Hente ut spesifikke kolonner
SELECT Name, Population
FROM city;

--Hente ut fra primærnøkkel
SELECT Name, Population
FROM city
WHERE CountryCode = 'SWE';

SELECT Name, Population, ID
FROM city
WHERE Population > 1000000;

-- enkle fnutter på tekststrenger
SELECT Name, Population
FROM country
WHERE Continent = 'Europe';

-- kan kombinere
SELECT Name, Population
FROM city
WHERE CountryCode = 'NOR'
    AND Population > 200000;

-- Bruk parentes slik at den prioriterer riktig
SELECT Name, Population
FROM city
WHERE (CountryCode = 'NOR'
        OR CountryCode = 'SWE')
    AND Population > 200000;

-- Sorterer resultat, asc - stigende
SELECT Name, Population
FROM city
WHERE (CountryCode = 'NOR'
        OR CountryCode = 'SWE')
    AND Population > 200000
ORDER BY Name ASC;


SELECT Name, Population
FROM city
WHERE Population > 1000000
ORDER BY Population DESC;

-- limit = bare vise et visst antall
SELECT Name, Population
FROM city
ORDER BY Population DESC
LIMIT 5;


-- Bruk city.
-- Hent navn og folketall for svenske byer med mer enn
-- 100 000 innbyggere.
-- Vis byen med størst folketall først.
SELECT Name, Population
FROM city
WHERE CountryCode = 'SWE'
    AND Population > 100000
ORDER BY Population DESC;



--Wildcard, søker etter byer som starter og slutter på O
-- % betyr null eller flere tegn
-- må ha LIKE og ikke =
SELECT Name
FROM city
WHERE Name LIKE 'O%o';

--Wildcard,
-- _ betyr nøyaktig ett tegn
SELECT Name
FROM city
WHERE Name LIKE 'O__o';

-- NULL betyr ingenting
SELECT *
FROM country
WHERE IndepYear IS NULL;

SELECT *
FROM country
WHERE IndepYear IS NOT NULL;


-- innebygd funksjon, telle rader
SELECT COUNT(*)
FROM country
WHERE IndepYear IS NULL;

SELECT COUNT(*)
FROM city
WHERE CountryCode = 'NOR';

--Alias, penere navn - AS:
SELECT COUNT(*) AS NumberOfNorwegianCities
FROM city
WHERE CountryCode = 'NOR';

SELECT Name AS CityName
FROM city
WHERE CountryCode = 'NOR';


-- slår sammen tabeller:
SELECT city.Name, city.Population, country.name
FROM city
JOIN country on city.CountryCode = country.code
WHERE CountryCode = 'NOR';

SELECT city.Name, city.Population, country.name
FROM city
JOIN country on city.CountryCode = country.code
WHERE CountryCode = 'NOR';

-- tips! kommenter ut join for å se hvordan det fungerer
SELECT city.Name as 'By', city.Population as 'Folketall', country.name as 'Land' , country.Continent as 'Kontinent'
FROM city
JOIN country on city.CountryCode = country.code
WHERE CountryCode = 'ITA';
