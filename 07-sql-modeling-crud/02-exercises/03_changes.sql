ALTER TABLE animals
ADD COLUMN status VARCHAR(20) NOT NULL DEFAULT 'new';


INSERT INTO animals (name, species, area_id)
VALUES('Nova', 'cat', 1);


ALTER TABLE animals
MODIFY COLUMN status VARCHAR(20) NOT NULL DEFAULT 'available';


INSERT INTO animals (name, species, area_id)
VALUES('Orea', 'cat', 1);


ALTER TABLE animals
MODIFY COLUMN name VARCHAR(60) NOT NULL;

CREATE TABLE scratch_labels (
    id INT AUTO_INCREMENT NOT NULL,
    label VARCHAR(40),
    PRIMARY KEY(id)
);


INSERT INTO scratch_labels (label)
values('Temporary label');

SELECT *
FROM scratch_labels;

-- fjerne kolonne
ALTER TABLE scratch_labels
DROP COLUMN label;

DROP TABLE scratch_labels;

INSERT INTO scratch_labels (label)
values('Temporary label');

ALTER TABLE scratch_labels
DROP COLUMN label;

SELECT *
FROM scratch_labels;

DROP TABLE scratch_labels;



-- oppgave 7.1 - oppdaterer vekt
UPDATE animals
SET weight = 3.90
WHERE id = 1;

-- oppgave 7.2 - to endringer i samme setning
UPDATE animals
SET weight = 19.20,
    name = 'Rex Jr'
WHERE id = 3;

-- oppgave 7.3 - Flytte et dyr
SELECT name, area_id
FROM animals
WHERE name = 'Luna' AND area_id = 3;

SELECT id, name
FROM areas
WHERE name =  'Quiet Zone';

UPDATE animals
SET area_id = 4
WHERE name = 'Luna' AND species = 'Rabbit';

SELECT *
FROM animals
WHERE name = 'Luna' AND area_id = 4;

SELECT *
FROM animals
WHERE name = 'Pip';

-- Oppgave 7.4
SELECT *
FROM animals
WHERE name = 'Nala';

UPDATE animals
SET weight = 14.60
WHERE name = 'Nala';

UPDATE animals
SET weight = NULL
WHERE name = 'Nala';

SELECT name, weight
FROM animals
WHERE weight IS NULL;


En UPDATE uten WHERE kan endre alle radene i tabellen fordi databasen ikke får beskjed om hvilke rader
som skal oppdateres. Dette kan føre til at data blir overskrevet ved en feil. Safe update mode beskytter
mot slike feil og krever ofte at WHERE bruker primærnøkkelen id, slik at bare den riktige raden blir endret.



-- 8 Slett data i riktig rekkefølge
-- oppgave 8.1 - slett dyr
DELETE FROM animals
WHERE id = 8;

SELECT *
FROM animals;

-- oppgave 8.2 - slett avdeling

SELECT *
FROM areas;

DELETE FROM areas
WHERE id = 3;
FEILMELDING: Cannot delete or update a parent row: a foreign key constraint
            fails (`animal_shelter_practice`.`animals`, CONSTRAINT `animals_ibfk_1`
            FOREIGN KEY (`area_id`) REFERENCES `areas` (`id`)

UPDATE animals
SET area_id = 4
WHERE id = 5;

DELETE FROM areas
WHERE id = 3;

-- oppgave 8.3
SELECT COUNT(*)
FROM animals;

SELECT COUNT(*)
FROM areas;

DELETE - sletter rader
DROP TABLE sletter alt!