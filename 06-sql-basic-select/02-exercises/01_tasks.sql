-- 4. Where
-- 4.1
SELECT city.CountryCode, name, District, population
FROM city
WHERE CountryCode = 'JPN';

-- 4.2
SELECT name, population
FROM country
WHERE Continent = 'South America';

--4.3
SELECT name, SurfaceArea
FROM country
WHERE SurfaceArea <= 1000;
-- < mindre enn, <= nøyaktig eller mind
-- re enn

--4.4
SELECT name, CountryCode, District
FROM city
WHERE District <> 'California';

-- 5. Kombinere betingelser
--5.1
SELECT name, Population
FROM city
WHERE CountryCode = 'BRA'
    AND Population >= 500000;

--5.2
SELECT name, Population
FROM city
WHERE Population >= 2000000
    AND Population <= 8000000;


-- 5.3
SELECT name, CountryCode, Population
FROM city
WHERE (CountryCode = 'AUS'
    OR CountryCode = 'NZL')
    AND Population > 200000;
-- Velg byer som ligger i Australia
-- eller New Zealand, og som har mer
-- enn 200 000 innbyggere.

-- 6. Sortering og avgrensning
-- 6.1
SELECT name, Region
FROM country
WHERE Continent = 'Asia'
ORDER BY Name ASC;

-- 6.2
SELECT name, SurfaceArea
FROM country
ORDER BY SurfaceArea DESC, Code ASC
LIMIT 8;
-- jeg kan bruke code i sorteringen selv om det
-- ikke vises i resultatet
-- DESC - synkende rekkefølge
-- ASC - stigende rekkefølge

-- 6.3
SELECT name, District, Population
FROM city
WHERE CountryCode = 'CAN'
ORDER BY District ASC, Population DESC, ID ASC;

-- 6.4
SELECT Code, Name
FROM country
ORDER BY name ASC
LIMIT 5;
-- uten sortering velger den landekoder på A

-- 7.Tekstsøk med LIKE
--7.1
SELECT Name
FROM country
WHERE Name LIKE 'Br%'
ORDER BY Name ASC;
-- B = 20 treff, BR = 3

--7.2
SELECT Name
FROM country
WHERE Name LIKE '%stan'
ORDER BY Name ASC;

SELECT Name
FROM country
WHERE Name LIKE '%is%'
ORDER BY Name ASC;

--7.3
SELECT Name
FROM country
WHERE Name LIKE '_a%';
-- a som 2.bokstav

SELECT Name
FROM country
WHERE Name LIKE '____';
-- nøyaktig fire tegn

-- 8. Lister og manglende verdier
-- 8.1
SELECT Name, CountryCode, Population
FROM city
WHERE CountryCode IN ('FRA', 'ESP', 'PRT')
ORDER BY CountryCode ASC , Name ASC ;

--8.2
SELECT Name, CountryCode, Population
FROM city
WHERE (CountryCode = 'FRA'
    OR CountryCode = 'ESP'
    OR CountryCode = 'PRT')
    AND Population >= 300000
ORDER BY CountryCode ASC , Name ASC;

SELECT Name, CountryCode, Population
FROM city
WHERE CountryCode IN ('FRA', 'ESP', 'PRT')
        AND Population >= 300000
ORDER BY CountryCode ASC , Name ASC ;

--8.3
SELECT Name, LifeExpectancy
FROM country
WHERE LifeExpectancy IS NULL;
-- Null betyr ingenting, ikke registert noe feks

--8.4
SELECT Name, LifeExpectancy
FROM country
WHERE LifeExpectancy IS NOT NULL
ORDER BY LifeExpectancy DESC, Code ASC
LIMIT 10;

--9. Tell rader med count
--9.1
SELECT COUNT(*) AS ContryCount
FROM country;
-- 239

SELECT COUNT(*) AS CityCount
FROM city;
-- 4079
--Innebygd funksjon

--9.2
SELECT COUNT(*) AS LargeCityCount
FROM city
WHERE Population > 500000;
-- 27

SELECT CountryCode, Population
FROM city
WHERE CountryCode = 'Mex' AND Population > 500000;
-- 27 rader

--9.3
SELECT Name, LifeExpectancy
FROM country
WHERE LifeExpectancy IS NULL;
--17
SELECT count(*) AS LifeExpectancy
FROM country
WHERE LifeExpectancy IS NULL;

SELECT count(*)
FROM country
WHERE LifeExpectancy IS NOT NULL;
--222
---17+222=239

-- 10. Les og rett spørringer
--10.1
SELECT Name Population
FROM city
WHERE CountryCode = 'ITA';
-- mangler komma
SELECT Name, Population
FROM city
WHERE CountryCode = 'ITA';

--10.2
SELECT Name, Population
FROM city
WHERE CountryCode = ITA;
-- mangler fnutter ''
SELECT Name, Population
FROM city
WHERE CountryCode = 'ITA';

--10.3
SELECT Name, CountryCode, Population
FROM city
WHERE CountryCode = 'EGY'
OR CountryCode = 'MAR' AND Population > 1000000;
-- mangler parenteser
SELECT Name, CountryCode, Population
FROM city
WHERE (CountryCode = 'EGY'
OR CountryCode = 'MAR') AND Population > 1000000;

--10.4
SELECT Name, HeadOfState
FROM country
WHERE HeadOfState = NULL;
-- det heter IS NULL
SELECT Name, HeadOfState
FROM country
WHERE HeadOfState IS NULL;



-- Ekstra:
SELECT CountryCode, Language, Percentage
FROM countrylanguage
WHERE CountryCode = 'IND'
ORDER BY  Percentage DESC, Language ASC;

SELECT CountryCode, Language, Percentage
FROM countrylanguage
WHERE Language = 'Spanish' AND IsOfficial = 'T'
ORDER BY  Percentage DESC, Language ASC;

-- Viser navn, lettere å forstå
SELECT countrylanguage.CountryCode, countrylanguage.Language, countrylanguage.Percentage, country.name
FROM countrylanguage
JOIN country on countrylanguage.CountryCode = country.code
WHERE Language = 'Spanish' AND IsOfficial = 'T'
ORDER BY  Percentage DESC, Language ASC;

