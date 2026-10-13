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