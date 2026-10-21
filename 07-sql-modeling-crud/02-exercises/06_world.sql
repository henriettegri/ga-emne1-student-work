-- 9 Les en modell som allerede finnes

-- oppgave 9.1
Country
- primærnøkkel: code

City
- primærnøkkel:

Country language
- primærnøkkel:


Fordi samme språk kan finnes i mange land, eller et land kan ha mange språk.

-- oppgave 9.2

SELECT CountryCode, Language, Percentage
FROM countrylanguage
WHERE countrycode = 'NOR';
