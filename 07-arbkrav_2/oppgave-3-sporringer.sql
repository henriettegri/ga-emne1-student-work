-- OPPGAVE 3 - SELECT og utforsking av data

-- 1. Produktoversikt: Finn produkter som koster mer enn 750 kr og har minst 10 enheter på lager. Vis
-- produktnavn, kategori, pris og lagerbeholdning. Sorter fra dyrest til billigst.
SELECT product_name, category, price, stock
FROM products
WHERE price > 750 AND stock >= 10
ORDER BY price DESC;


-- 2. Kunder i utvalgte byer: Finn kunder som bor i Oslo, Bergen eller Trondheim. Sorter først etter by og
-- deretter etter etternavn.
SELECT city, last_name
FROM customers
WHERE (city = 'Oslo'
    OR city = 'Bergen'
    OR city = 'Trondheim')
ORDER BY city, last_name;


-- 3. Bestillinger i en periode: Finn alle bestillinger som ble registrert i juli 2025. Vis ordrenummer,
-- dato, antall og status.
SELECT order_id, order_date, quantity, status
FROM orders
WHERE order_date BETWEEN '2025-07-01' AND '2025-07-31';


-- 4. Full bestillingsoversikt: Lag en oversikt som henter informasjon fra alle tre tabellene. Vis ordrenummer,
-- kundens fornavn og etternavn, produktnavn, antall, pris per produkt, bestillingsdato og status.
SELECT orders.order_id, customers.first_name, customers.last_name, products.product_id, products.product_name, orders.quantity, orders.order_date, orders.status
FROM orders
JOIN products on products.product_id = orders.product_id
JOIN customers on customers.customer_id = orders.customer_id
ORDER BY order_id ASC;
-- Kommentar: for å ha oversikten underveis bruker jeg tabellnavnet først i SELECT-setningen.


-- 5. Beregnet verdi: Utvid bestillingsoversikten slik at den også viser en beregnet verdi basert på
-- price * quantity. Gi den beregnede kolonnen et passende navn og sorter fra høyest til lavest verdi.
SELECT orders.order_id, customers.first_name, customers.last_name, products.product_id,
       products.product_name, orders.quantity, orders.order_date, orders.status,
       price * quantity AS beregnet_verdi
FROM orders
JOIN products on products.product_id = orders.product_id
JOIN customers on customers.customer_id = orders.customer_id
ORDER BY beregnet_verdi DESC;


-- 6. Bestillinger med høy verdi: Finn bestillinger med en beregnet verdi på mer enn 2000 kr. Vis kunden,
-- produktet, antall, pris og beregnet verdi.
SELECT customers.customer_id, products.product_name, orders.quantity,
       products.price, products.price * orders.quantity AS beregnet_verdi
FROM orders
JOIN products ON products.product_id = orders.product_id
JOIN customers ON customers.customer_id = orders.customer_id
WHERE products.price * orders.quantity > 2000
ORDER BY beregnet_verdi DESC;


-- 7. Bestillinger per status: Finn ut hvor mange bestillinger som har hver status.
SELECT status, COUNT(*)
FROM orders
-- WHERE status = 'Delivered' OR status ='Shipped' OR status = 'Processing'
GROUP BY status;
-- Kommentar: Jeg trodde jeg måtte ha med en where clause, men da jeg kommenterte den ut, så jeg at det ikke
-- var nødvendig. Dette hjalp meg å forstå aggregatfunksjonen COUNT.


-- 8. Gjennomsnittspris per kategori: Finn gjennomsnittsprisen for produktene i hver kategori. Sorter fra
-- høyest til lavest gjennomsnittspris.
SELECT category, AVG(price) AS average
FROM products
GROUP BY category
ORDER BY average DESC;


-- 9. Bestillinger per kunde: Finn ut hvor mange bestillinger hver kunde har gjort. Sorter kunden med flest
-- bestillinger først. Resultatet skal også inkludere kunder som har 0 bestillinger.
SELECT customers.customer_id, customers.last_name, COUNT(orders.order_id) AS antall_bestillinger
FROM customers
LEFT JOIN orders ON customers.customer_id = orders.customer_id
GROUP BY customers.customer_id, customers.last_name;


-- 10. Antall solgte produkter: Finn ut hvor mange enheter som totalt er bestilt av hvert
-- produkt. Produkter som ikke forekommer i noen bestilling skal også være med i
-- resultatet og vises med 0 bestilte enheter. Husk at antall rader i orders og totalt
-- antall bestilte enheter ikke nødvendigvis er det samme.
SELECT products.product_id, products.product_name, COALESCE(SUM(quantity),0) AS total_of_product
FROM products
LEFT JOIN orders ON orders.product_id = products.product_id
GROUP BY products.product_id, products.product_name
ORDER BY product_id ASC;


-- 11. Beregnet verdi per produkt: Finn samlet beregnet verdi for hvert produkt basert på
-- bestillingene. Vis produktnavn, totalt antall bestilte enheter og samlet beregnet verdi.
-- Produkter uten bestillinger skal også være med og vises med 0 bestilte enheter og 0 i
-- beregnet verdi. Sorter fra høyest til lavest verdi.
SELECT products.product_id, product_name, (COALESCE(SUM(orders.quantity),0)* price) AS beregnet_verdi
FROM products
LEFT JOIN orders ON products.product_id = orders.product_id
GROUP BY products.product_id, product_name, price
ORDER BY beregnet_verdi DESC;


-- 12. Kunder med flere bestillinger: Finn kunder som har mer enn én bestilling. Vis
-- kunden og antall bestillinger. Finn ut hvordan du kan filtrere grupperte resultater.
SELECT  customers.customer_id, last_name, COUNT(orders.customer_id) AS antall_bestillinger
FROM customers
LEFT JOIN orders ON orders.customer_id = customers.customer_id
GROUP BY customers.customer_id, last_name
HAVING antall_bestillinger > 1;


-- 13. Kunder uten bestillinger: Finn kunden eller kundene som ikke har noen bestillinger. Oppgaven skal løses
-- ved hjelp av relasjonen mellom customers og orders.
SELECT  customers.customer_id, last_name, orders.customer_id
FROM customers
LEFT JOIN orders ON orders.customer_id = customers.customer_id
WHERE orders.customer_id IS NULL;


-- 14. Produkter uten bestillinger: Finn produktet eller produktene som ikke forekommer i noen bestilling.
-- Oppgaven skal løses ved hjelp av relasjonen mellom products og orders.
SELECT products.product_id, product_name, orders.product_id
FROM products
LEFT JOIN orders ON orders.product_id = products.product_id
WHERE orders.product_id IS NULL;


-- 15. Utforskingsoppgave: Finn kunden som har høyest samlet beregnet verdi på
-- bestillingene sine. Du får ikke oppgitt hvilke SQL-elementer som skal brukes.
-- Forklar kort hvordan du kom frem til løsningen.
SELECT customers.last_name, SUM(orders.quantity*products.price) AS beregnet_verdi
FROM orders
JOIN products on products.product_id = orders.product_id
JOIN customers on customers.customer_id = orders.customer_id
GROUP BY customers.last_name
ORDER BY beregnet_verdi DESC;
-- Kommentar: Jeg tok utgangspunktet i tidligere oppgaver der tabellene orders, customers og products ble
-- koblet sammen med join. Jeg fant samlet beregnet verdi på samme måte som i deloppgave 11; jeg multipliserte
-- antall (quantity) med pris (price) og summerte verdien per kunde med aggregatfunksjonen SUM(). Dette ble
-- gruppert med GROUP BY og sortert synkende med ORDER BY DESC for å finne kunden med høyest samlet
-- beregnet verdi.


-- OPPGAVE 4 - INSERT, UPDATE, DELETE og transaksjoner

-- 1. Registrer en ny kunde: Registrer Henrik Solberg med e-post henrik.solberg@example.com,
-- bosted Lillehammer og dagens dato som registreringsdato. Kontroller at kunden ble registrert. I
-- kontrollspørringen skal du ikke bruke customer_id.

INSERT INTO customers (customer_id, first_name, last_name, email, city, registered_date)
VALUES (9, 'Henrik', 'Solberg', 'henrik.solberg@example.com', 'Lillehammer', '2026-10-22');

SELECT *
FROM customers;

-- 2. Registrer flere produkter: Registrer produktene i tabellen under med én INSERT-kommando. Kontroller
-- resultatet uten å være avhengig av hvilke product_id produktene fikk.

INSERT INTO products (product_id, product_name, category, price, stock)
VALUES (11, 'USB-C cable', 'Accessories', '199.00', 50),
        (12, 'Docking station', 'Accessories', '1899.00', 12),
        (13, 'External SSD 2TB', 'Storage', '1999.00', 8);

SELECT *
FROM products;

-- 3. Registrer nye bestillinger: Henrik Solberg kjøper 1 Docking station, 2 enheter av USB-C cable og 1
-- External SSD 2TB. Du får ikke oppgitt customer_id eller product_id. Finn først de nødvendige verdiene i
-- databasen og registrer bestillingene. Kontroller resultatet med en spørring som viser kundens navn og
-- produktnavn i stedet for bare ID-er.

SELECT customer_id, last_name
FROM customers
WHERE last_name = 'Solberg';

SELECT product_id, product_name
FROM products
WHERE (product_name = 'Docking station' OR
      product_name = 'USB-C cable' OR
       product_name = 'External SSD 2TB')
ORDER BY product_id;

-- Kommentar: Da det ikke står noe om "status" i oppgaven, velger jeg å endre tabellen "Orders" slik at default i
-- kolonnen status blir 'Processing' hvis ikke noe annet legges inn.
ALTER TABLE orders
MODUFY COLUMN status VARCHAR(20) NOT NULL DEFAULT 'Processing';

INSERT INTO orders (customer_id, product_id, quantity, order_date)
VALUES(9, 11, 2, '2026-10-25'),
      (9, 12, 1, '2026-10-25'),
      (9, 13, 1, '2026-10-25');

-- 4. Prisendring: Øk prisen på alle produkter i kategorien Accessories med 8 %. Finn først
-- produktene som blir påvirket og kontroller dagens priser. Utfør deretter oppdateringen og
-- kontroller resultatet.

SELECT product_name, price
FROM products;

UPDATE products
SET price = price * 1.08;


-- 5. Lagerpåfylling: Produkter med færre enn 15 enheter på lager får levert 20 nye enheter. Finn først
-- produktene som blir påvirket, og oppdater deretter lagerbeholdningen.

SELECT product_name, stock
FROM products
WHERE stock < 15;

UPDATE products
SET stock = stock + 20
WHERE stock < 15;

SELECT product_name, stock
FROM products;


-- 6. Endre flere verdier: Produktet Gaming headset skal få 15 % høyere pris og 10 nye enheter på lager.
-- Begge endringene skal utføres med samme UPDATE.

SELECT product_name, price, stock
FROM products
WHERE product_name = 'Gaming headset';

UPDATE products
SET price = price * 1.15, stock = stock + 10
WHERE product_name = 'Gaming headset';

-- 7. Oppdater ordrestatus: Alle bestillinger med status Shipped som er registrert før 10. august 2025, skal
-- endres til Delivered. Kontroller radene før og etter oppdateringen.

SELECT order_date, status
FROM orders;

SELECT order_date, status
FROM orders
WHERE status = 'Shipped' AND order_date < '2025-08-10';

UPDATE orders
SET status = 'Delivered'
WHERE status = 'Shipped' AND order_date < '2025-08-10';


-- 8. Opprett og slett testdata: Opprett en testkunde, et testprodukt og en bestilling hvor testkunden kjøper
-- testproduktet. Kontroller at dataene finnes, og slett deretter alle testdataene igjen. Du må selv finne
-- riktig rekkefølge for slettingen og forklare hvorfor rekkefølgen er viktig.

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

-- Kommentar: customers og products er parent-tabeller, mens orders er child-tabellen. orders er koblet til customers
-- og products med fremmednøkler. Av denne grunnen må bestillinger i orders slettes før kunder eller
-- bestillinger kan slettes.


-- 9. Bruk en transaksjon: Registrer en ny bestilling og reduser samtidig lagerbeholdningen for produktet
-- som bestilles. Begge endringene skal utføres som én transaksjon. Kontroller resultatet før transaksjonen
-- avsluttes. Avslutt transaksjonen med COMMIT. Forklar også hva ROLLBACK ville gjort dersom en av
-- operasjonene skulle angres, og hvorfor transaksjoner er nyttige når flere endringer hører sammen.

START TRANSACTION;

INSERT INTO orders (customer_id, product_id, quantity, order_date)
VALUES(8, 4, 1, '2026-10-27');

UPDATE products
SET stock = stock - 1
WHERE product_name = '27-inch monitor';

COMMIT;

-- Kontroll av resultat før commit gjennomføres. Jeg kunne spesifisert kolonner som skal vises, men siden
-- tabellen ikke er så stor, viser jeg alt.
-- Sjekke at ordren er lagt inn.
SELECT *
FROM ordres;

-- Sjekke at stock endres:
SELECT *
FROM products;

-- Kommentar: Fordelen med transaksjoner er at flere endringer kan behandles som en samlet operasjon.
-- Andre brukere vil først se endringene når COMMIT kjøres.
-- Hvis noe går galt før COMMIT, kan ROLLBACK angre alle endringene i transaksjonen.