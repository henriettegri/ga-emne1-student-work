-- 10 Les og rett SQL
Koden nedenfor inneholder feil eller utrygge avgrensninger. Forklar problemene og skriv korrigerte versjoner.
Ikke kjør de feilaktige endringssetningene. Du trenger ikke kjøre rettelsene for å fullføre denne delen.


-- Oppgave 10.1 Komma og parenteser
--Finn to kommafeil i tabelldefinisjonen. Forklar hvor komma skal skille definisjoner, og hvor det ikke skal stå et
--komma.

CREATE TABLE scratch_tags (
id INT AUTO_INCREMENT,
label VARCHAR(30) NOT NULL
PRIMARY KEY (id),
);
-- mangler komma etter NOT NULL, må fjerne komma etter (id)
CREATE TABLE scratch_tags (
id INT AUTO_INCREMENT,
label VARCHAR(30) NOT NULL,
PRIMARY KEY (id)
);

-- Oppgave 10.2 Kolonner og verdier
--Hva mangler i innsettingen? Finn først en gyldig avdelings-ID med en kontrollspørring, og skriv en rettet
--INSERT-setning.
INSERT INTO animals (name, species, area_id)
VALUES ('Tyra', 'cat');

-- area_id kan ikke være NULL
 INSERT INTO animals (name, species, area_id)
VALUES ('Tyra', 'cat', 4);


-- Oppgave 10.3 Gyldig SQL med feil utvalg
--Målet er å oppdatere bare kaninen Luna. Hvorfor kan koden påvirke feil dyr selv om den kjører uten
--syntaksfeil? Skriv en kontrollspørring og en rettelse som bruker riktig id.
UPDATE animals
SET weight = 2.50
WHERE name = 'Luna';
-- fordi det er to dyr som heter Luna. Må ha med id eller dyr.

UPDATE animals
SET weight = 2.50
WHERE name = 'Luna' AND id = 6;

-- Oppgave 10.4 Sletting er ikke en SELECT
--Finn syntaksfeilen. Skriv deretter en versjon som avgrenser med Novas id, og en kontrollspørring som bør
--kjøres før slettingen.
DELETE * FROM animals
WHERE name = 'Nova';

SELECT *
FROM animals
WHERE name = 'Nova';

DELETE FROM animals
WHERE name = 'Nova';
