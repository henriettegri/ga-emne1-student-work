-- SELECT DATABASE(); viser hvem som er aktiv

CREATE DATABASE IF NOT EXISTS music_school;

USE music_school;


CREATE TABLE rooms (
    id INT AUTO_INCREMENT,
    name VARCHAR(40) NOT NULL,
    PRIMARY KEY (id),
    UNIQUE(name)
);

--to ulike måte, over og under
CREATE TABLE rooms (
    id INT AUTO_INCREMENT,
    name VARCHAR(40) NOT NULL UNIQUE ,
    PRIMARY KEY (id)
);


 purchase_price DECIMAL(8,2)
-- (8,2) åtte siffer, to skal være desimaler


CREATE TABLE instruments
(
    id             INT AUTO_INCREMENT,
    name           VARCHAR(80) NOT NULL,
    purchase_price DECIMAL(8,2),
    acquired_on DATE,
    room_id INT NOT NULL,
    PRIMARY KEY  (id),
    FOREIGN KEY (room_id) REFERENCES rooms(id)
);


CREATE TABLE instruments
(
    id             INT AUTO_INCREMENT,
    name           VARCHAR(80) NOT NULL,
    purchase_price DECIMAL(8,2),
    acquired_on DATE,
    room_id INT NOT NULL,
    PRIMARY KEY  (id),
    FOREIGN KEY (room_id) REFERENCES rooms(id)
);


-- legge til kolonne
ALTER TABLE rooms
ADD COLUMN capacity INT NOT NULL DEFAULT 1;

-- endre kolonne
ALTER TABLE rooms
MODIFY COLUMN capacity INT NOT NULL DEFAULT 10;

ALTER TABLE rooms
DROP COLUMN capacity;


     CREATE TABLE scratch_notes (
    note VARCHAR(100)
);

DROP TABLE scratch_notes;