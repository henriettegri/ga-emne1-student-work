-- innehold

-- INSERT INTO legger til rader. Dette er del av
--Data Manipulation Language – DML.

INSERT INTO rooms (name)
VALUES ('Studio A');

INSERT INTO rooms (name)
VALUES ('Studio B'),
('Practice Room');


-- sjekke

SELECT *
FROM rooms;



INSERT INTO instruments (name, purchase_price, acquired_on, room_id)
VALUES ('Piano', 18000.00, '2026-09-01', 1);

UPDATE instruments
SET purchase_price = purchase_price * 1.10, name =  'Grand piano'
WHERE  id = 1;
-- id er et spesifikk

UPDATE instruments
SET purchase_price = purchase_price * 1.10, name =  'Grand piano'
WHERE  name = 'Piano';
-- id er et spesifikk

SELECT *
FROM instruments;

-- blir slettet
DELETE FROM instruments
WHERE id = 1;