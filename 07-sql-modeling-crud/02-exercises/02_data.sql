INSERT INTO areas (name)
VALUES ('Cat Wing'),
       ('Dog Wing'),
       ('Small Animals'),
       ('Quiet Zone');

SELECT *
FROM areas;

1,Cat Wing
2,Dog Wing
4,Quiet Zone
3,Small Animals

    id INT AUTO_INCREMENT,
    name VARCHAR(40) NOT NULL,
    species VARCHAR(20) NOT NULL,
    weight DECIMAL(5,2),
    admitted_on DATE,
    area_id INT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (area_id) REFERENCES areas(id)

INSERT INTO animals (name, species, weight, admitted_on,  area_id)
VALUES ('Luna', 'cat', 3.80, '2026-09-12', 1),
        ('Milo', 'cat', 4.20, NULL, 1),
        ('Rex', 'dog', 18.50, '2026-09-15', 2),
        ('Nala', 'dog', NULL, '2026-09-07', 2),
        ('Pip', 'rabbit', 1.60, '2026-09-20', 3),
        ('Luna', 'rabbit', 2.10, NULL, 3);

SELECT id, name, species, area_id
FROM animals
ORDER BY species, id;

SELECT id, name, species, area_id
FROM animals
WHERE name = 'Luna'
ORDER BY species, id;

SELECT id, name, weight, admitted_on
FROM animals
WHERE weight IS NULL OR admitted_on IS NULL;

SELECT COUNT(*)
FROM animals;

SELECT COUNT(*)
FROM areas;

-- quiet_zone
SELECT name, area_id
FROM animals
WHERE area_id = 4;

-- small animals
SELECT name, area_id
FROM animals
WHERE area_id = 3;