-- Vis alle bynavn + befolkning der byen har flere innbyggere
-- enn gjennomsnittet av innbyggere for byer i hele verden

-- start med indre spørring
SELECT AVG(Population)
FROM city;
-- 350468.2236

-- se den andre select, kan bruke utregnet gjennomsnitt
SELECT Name, Population
FROM city
WHERE Population > 350468.2236
ORDER BY Population ASC;

-- hele
SELECT Name, Population
FROM city
WHERE Population > (
    SELECT AVG(Population)
    FROM city
)
ORDER BY Population ASC;

-- fra slide
SELECT Name, Population
FROM city
WHERE Population > (
    SELECT AVG(Population)
    FROM city
)
ORDER BY Population DESC;
