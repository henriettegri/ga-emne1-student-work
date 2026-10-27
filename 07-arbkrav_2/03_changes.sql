UPDATE products
SET price = 3299
WHERE product_name = '27-inch monitor';

1. Registrer en ny kunde: Registrer Henrik Solberg med
e-post henrik.solberg@example.com, bosted Lillehammer og dagens
dato som registreringsdato. Kontroller at kunden ble registrert. I
kontrollspørringen skal du ikke bruke customer_id.

INSERT INTO customers (customer_id, first_name, last_name, email, city, registered_date)
VALUES (9, 'Henrik', 'Solberg', 'henrik.solberg@example.com', 'Lillehammer', '2026-10-22');

SELECT *
FROM customers;

2. Registrer flere produkter: Registrer produktene i tabellen under
med én INSERT-kommando. Kontroller
resultatet uten å være avhengig av hvilke product_id produktene fikk.

INSERT INTO products (product_id, product_name, category, price, stock)
VALUES (11, 'USB-C cable', 'Accessories', '199.00', 50),
        (12, 'Docking station', 'Accessories', '1899.00', 12),
        (13, 'External SSD 2TB', 'Storage', '1999.00', 8);

SELECT *
FROM products;

3. Registrer nye bestillinger: Henrik Solberg kjøper 1 Docking station, 2 enheter av USB-C cable og 1
External SSD 2TB. Du får ikke oppgitt customer_id eller product_id.
Finn først de nødvendige
verdiene i databasen og registrer bestillingene. Kontroller resultatet med
en spørring som viser kundens navn og produktnavn i stedet for bare ID-er.

SELECT customer_id, last_name
FROM customers
WHERE last_name = 'Solberg';

SELECT product_id, product_name
FROM products
WHERE (product_name = 'Docking station' OR
      product_name = 'USB-C cable' OR
       product_name = 'External SSD 2TB')
ORDER BY product_id;

-- LEGGER TIL DENNE
ALTER TABLE orders
MODUFY COLUMN status VARCHAR(20) NOT NULL DEFAULT 'Processing';

INSERT INTO orders (customer_id, product_id, quantity, order_date)
VALUES(9, 11, 2, '2026-10-25'),
      (9, 12, 1, '2026-10-25'),
      (9, 13, 1, '2026-10-25');

4. Prisendring: Øk prisen på alle produkter i kategorien Accessories med 8 %. Finn først
produktene som blir påvirket og kontroller dagens priser. Utfør deretter oppdateringen og
kontroller resultatet.

SELECT product_name, price
FROM products;

UPDATE products
SET price = price * 1.08;


5. Lagerpåfylling: Produkter med færre enn 15 enheter på lager får levert 20 nye enheter. Finn først
produktene som blir påvirket, og oppdater deretter lagerbeholdningen.

SELECT product_name, stock
FROM products
WHERE stock < 15;

UPDATE products
SET stock = stock + 20
WHERE stock < 15;

SELECT product_name, stock
FROM products;


6. Endre flere verdier: Produktet Gaming headset skal få 15 % høyere pris og 10 nye enheter på lager.
Begge endringene skal utføres med samme UPDATE.

SELECT product_name, price, stock
FROM products
WHERE product_name = 'Gaming headset';

UPDATE products
SET price = price * 1.15, stock = stock + 10
WHERE product_name = 'Gaming headset';

7. Oppdater ordrestatus: Alle bestillinger med status Shipped som er registrert før 10. august 2025, skal
endres til Delivered. Kontroller radene før og etter oppdateringen.

SELECT order_date, status
FROM orders;

SELECT order_date, status
FROM orders
WHERE status = 'Shipped' AND order_date < '2025-08-10';

UPDATE orders
SET status = 'Delivered'
WHERE status = 'Shipped' AND order_date < '2025-08-10';


8. Opprett og slett testdata: Opprett en testkunde, et testprodukt og en bestilling hvor testkunden kjøper
testproduktet. Kontroller at dataene finnes, og slett deretter alle testdataene igjen. Du må selv finne riktig
rekkefølge for slettingen og forklare hvorfor rekkefølgen er viktig.

INSERT INTO customers (customer_id, first_name, last_name, email, city, registered_date)
VALUES (10, 'Test', 'Testen', 'test.testen@example.com', 'Test', '2026-10-25');

INSERT INTO products (product_id, product_name, category, price, stock)
VALUES (14, 'Test', 'Test', '99.00', 10);

INSERT INTO orders (customer_id, product_id, quantity, order_date)
VALUES(10, 14, 1, '2026-10-25');

DELETE FROM orders
WHERE customer_id = 10;

DELETE FROM products
WHERE product_id = 14;

DELETE FROM customers
WHERE customer_id = 10;

-- customers og products er parent table, orders er child table. Ordre har fremmednøkler til
-- customers og products, derfor må ordre slettes før product og customer

9. Bruk en transaksjon: Registrer en ny bestilling og reduser samtidig lagerbeholdningen
for produktet som bestilles. Begge endringene skal utføres som én transaksjon. Kontroller
resultatet før transaksjonen avsluttes. Avslutt transaksjonen med COMMIT. Forklar også
hva ROLLBACK ville gjort dersom en av operasjonene skulle angres, og hvorfor transaksjoner
er nyttige når flere endringer hører sammen.

START TRANSACTION;

INSERT INTO orders (customer_id, product_id, quantity, order_date)
VALUES(8, 4, 1, '2026-10-27');

UPDATE products
SET stock = stock - 1
WHERE product_name = '27-inch monitor';


-- permanent endring hvis commit gjennomføres:
COMMIT;

