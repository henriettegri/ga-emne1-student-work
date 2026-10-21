5 Prøv reglene i databasen
Disse forsøkene skal avvises av databasen. Kjør dem enkeltvis, les feilmeldingen og skriv kort hvilken regel som
stoppet forsøket. Ikke fjern reglene for å få ugyldige data inn.


--Oppgave 5.1 Et avdelingsnavn som finnes fra før
--Forsøk å legge inn en ny avdeling med navnet Cat Wing. Utelat ID-en. Hvilken regel blir brutt? Kontroller at
--et fortsatt bare finnes én avdeling med dette navnet.

FEILMELDING: Duplicate entery 'Cat wing' for key 'areas.name'. Regelen kommer pga 'UNIQUE'

--Oppgave 5.2 En obligatorisk verdi mangler
--Forsøk å legge inn et dyr med NULL som navn. Bruk en gyldig art og en eksisterende avdeling.
--Forsøk deretter å registrere dyret Kira med art cat, men med NULL i area_id. Forklar hvorfor begge
--forsøkene skal feile, selv om de berører forskjellige kolonner.

INSERT INTO animals (name, species, area_id)
VALUES(NULL, 'cat', 1);
Name kan ikke være null.

INSERT INTO animals (name, species, area_id)
VALUES(NULL, 'cat', 1);
area_id kan ikke være null.


--Oppgave 5.3 En avdeling som ikke finnes
--Finn et positivt heltall som ikke finnes i areas.id, og kontroller det med SELECT. Forsøk å registrere Kira
--med dette tallet som area_id.
--Hvilken regel stopper innsettingen nå? Hvorfor er NOT NULL alene utilstrekkelig til å kontrollere at en avdeling
--finnes?

SELECT area_id
FROM animals
WHERE area_id = 5;

Finner ingen rader

INSERT INTO animals (name, species, area_id)
VALUES('Kira', 'cat', 5);
FEILMELDING: Cannot add or update a child rpw: a foreign key constraint fails.
Kan ikke legge til eller oppdatere denne raden fordi den refererer til en rad i en annen tabell som ikke finnes.



--Oppgave 5.4 En ID som allerede er brukt
--Finn ID-en til et eksisterende dyr. Forsøk å sette inn et nytt dyr med akkurat denne ID-en, men ellers gyldige
--verdier.
--Kontroller til slutt at tabellene fortsatt har fire avdelinger og seks dyr. Forklar hvorfor et dyr med samme navn
--kan være gyldig, mens et dyr med samme primærnøkkel ikke er det.

INSERT INTO animals (id, name, species, weight, admitted_on,  area_id)
VALUES ('1 ', 'Charlie', 'dog', 10.3 ,'2010-03-26' , 2);
FEILMELDING: Duplicate entry '1' for key 'animals.PRIMARY'

Et dyr kan ha samme navn som et annet dyr fordi navn ikke trenger å være unike. Primærnøkkelen må derimot
være unik for hver rad i tabellen. Hvis to dyr hadde samme primærnøkkel, ville databasen ikke kunne skille
dem fra hverandre. Derfor tillates like navn, men ikke like primærnøkler.

--Om automatiske ID-er
--Ikke regn med at neste ID blir nøyaktig én høyere enn den siste du så. Mislykkede innsettinger og sletting kan
--gi hull i nummerserien. Hent derfor ID-ene fra databasen når du trenger dem.