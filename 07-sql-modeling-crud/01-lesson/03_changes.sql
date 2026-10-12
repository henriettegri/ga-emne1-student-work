--En ny kolonne i rooms
Bruk gjerne fila 03_changes.sql til denne sliden.
ALTER TABLE rooms
ADD COLUMN capacity INT NOT NULL DEFAULT 1;
ALTER TABLE rooms
MODIFY COLUMN capacity INT NOT NULL DEFAULT 2;


--Fjerne struktur
ALTER TABLE rooms
DROP COLUMN capacity;
CREATE TABLE scratch_notes (
note VARCHAR(100)
);
DROP TABLE scratch_notes