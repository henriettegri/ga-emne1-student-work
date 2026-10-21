-- det ligger ikke noe navn på land i city, derfor brukes join.

SELECT country.Name AS country_name, city.Name AS city_name
FROM city
INNER JOIN country ON city.CountryCode = country.Code
WHERE country.Continent = 'Europe'
ORDER BY country.Name;


-- on er viktig for at det skal bli riktig.
SELECT CountryCode, Code, country.Name as country_name, city.Name AS city_name
FROM city
JOIN country ON CountryCode = Code;

-- kan bestsemme rekkefølge, her kan man sjekke at countrycode og code samsvarer.
SELECT country.Name as country_name, CountryCode, Code, city.Name AS city_name
FROM city
JOIN country ON CountryCode = Code;



SELECT country.Name AS country_name,
       city.Name AS capital_name,
    countrylanguage.Language
FROM country
JOIN city ON country.Capital = city.ID
JOIN countrylanguage ON country.Code = countrylanguage.CountryCode
WHERE country.Continent = 'Europe'
    AND countrylanguage.IsOfficial = 'T'
ORDER BY country_name ASC;

-- flere kolonner
SELECT country.Name AS country_name,
        city.Id,
        country.Capital,
       city.Name AS capital_name,
    countrylanguage.Language
FROM country
JOIN city ON country.Capital = city.ID
JOIN countrylanguage ON country.Code = countrylanguage.CountryCode
WHERE country.Continent = 'Europe'
    AND countrylanguage.IsOfficial = 'T'
ORDER BY country_name ASC;


SELECT country.Name,
       city.Name
FROM country
JOIN city ON city.CountryCode = country.Code;
-- left join, alt til venstre blir med.
-- FROM country LEFT JOIN city - alt til venstre, altså country blir med.


SELECT country.Name,
       city.Name
FROM country
LEFT JOIN city ON city.CountryCode = country.Code
ORDER BY country.Name;
-- left join, alt til venstre blir med.
-- FROM country LEFT JOIN city - alt til venstre, altså country blir med.
-- her blir landet med selv om det ikke har noen byer.

-- sorterer i den ene kolonna
SELECT country.Name,
       city.Name
FROM country
LEFT JOIN city ON city.CountryCode = country.Code
WHERE city.Name IS NULL
ORDER BY country.Name;

SELECT country.Name,
       city.Name
FROM country
LEFT JOIN city ON city.CountryCode = country.Code
WHERE city.CountryCode IS NULL
ORDER BY country.Name;