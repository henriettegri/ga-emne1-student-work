SELECT country.Code,
        country.Name,
        COUNT(city.ID) AS city_count
FROM country
LEFT JOIN city ON city.CountryCode = country.Code
GROUP BY country.Code, country.Name
ORDER BY city_count DESC;