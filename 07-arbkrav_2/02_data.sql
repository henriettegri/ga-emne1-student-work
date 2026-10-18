
INSERT INTO products (product_id, product_name, category, price, stock)
VALUES (1, 'Laptop Pro 15', 'Computers', '12999.00', 8),
        (2, 'Wireless mouse', 'Accessories', '399.00', 45),
        (3, 'Mechanical keyboard', 'Accessories', '899.00', 22),
        (4, '27-inch monitor', 'Monitors', 399.00, 45),
        (5, 'USB-C hub', 'Accessories', '699.00', 30),
        (6,  'HD webcam', 'Accessories', '799.00', 18),
        (7,  'Gaming headset', 'Audio', '1199.00', 16),
        (8,  'Bluetooth speaker', 'Audio', '1499.00', 12),
        (9,  'External SSD 1TB', 'Storage', '1099.00', 25),
        (10,  'Laptop stand', 'Accessories', '549.00', 35)
        ;

INSERT INTO customers (customer_id, first_name, last_name, email, city, registered_date)
VALUES (1, 'Ola', 'Nordmann', 'ola.nordmann@example.com', 'Oslo', '2025-01-15'),
        (2, 'Kari', 'Hansen', 'kari.hansen@example.com',   'Bergen', '2025-02-03'),
        (3, 'Per', 'Johansen', 'per.johansen@example.com', 'Trondheim', '2025-02-18'),
        (4,  'Anne', 'Larsen', 'anne.larsen@example.com', 'Oslo', '2025-03-01'),
        (5,  'Thomas', 'Andersen', 'thomas.andersen@example.com', 'Stavanger', '2025-03-12'),
        (6, 'Maria', 'Nilsen', 'maria.nilsen@example.com', 'Kristiansand', '2025-04-05'),
        (7, 'Erik', 'Olsen', 'erik.olsen@example.com', 'Bergen', '2025-04-21'),
        (8, 'Ingrid', 'Berg', 'ingrid.berg@example.com', 'Tromsø', '2025-05-10')
        ;


INSERT INTO orders (order_id, customer_id, product_id, quantity, order_date, status)
VALUES ( 1, 1, 1, 1, '2025-06-01', 'Delivered'),
        (2, 1, 2, 2, '2025-06-01', 'Delivered'),
        (3, 2, 4, 1, '2025-06-03', 'Delivered'),
        (4, 3, 3, 1, '2025-06-05', 'Delivered'),
        (5, 4, 5, 2, '2025-06-08', 'Delivered'),
        (6, 5, 7, 1, '2025-06-10', 'Delivered'),
        (7, 6, 8, 1, '2025-06-12', 'Delivered'),
        (8, 7, 9, 2, '2025-06-15', 'Delivered'),
        (9, 2, 2, 1, '2025-07-01', 'Delivered'),
        (10, 3, 5, 1, '2025-07-04', 'Delivered'),
        (11, 4, 4, 2, '2025-07-06', 'Delivered'),
        (12, 5, 9, 1, '2025-07-09', 'Delivered'),
        (13, 1, 9, 1, '2025-08-02', 'Shipped'),
        (14, 3, 2, 3, '2025-08-05', 'Shipped'),
        (15, 5, 4, 1, '2025-08-08', 'Processing'),
        (16, 7, 5, 2, '2025-08-10', 'Processing'),
        (17, 6, 3, 1, '2025-08-12', 'Shipped'),
        (18, 2, 6, 2, '2025-08-15', 'Processing')
        ;


-- 1. Produktoversikt: Finn produkter som koster mer enn 750 kr og har minst 10 enheter på lager. Vis
-- produktnavn, kategori, pris og lagerbeholdning. Sorter fra dyrest til billigst.SELECT product_name, category, price, stock
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
-- 3. Bestillinger i en periode: Finn alle bestillinger som ble registrert i juli 2025. Vis ordrenummer, dato, antall
-- og status.
SELECT order_id, order_date, quantity, status
FROM orders
WHERE order_date BETWEEN '2025-07-01' AND '2025-07-31';

-- 4. Full bestillingsoversikt: Lag en oversikt som henter informasjon fra alle tre tabellene. Vis ordrenummer,
-- kundens fornavn og etternavn, produktnavn, antall, pris per produkt, bestillingsdato og status.
SELECT orders.order_id, customers.first_name, customers.last_name, products.product_id, products.product_name, orders.quantity, orders.order_date, orders.status
FROM orders
JOIN products on products.product_id = orders.product_id
JOIN customers on customers.customer_id = orders.customer_id;

-- 5. Beregnet verdi: Utvid bestillingsoversikten slik at den også viser en beregnet verdi basert på price *
-- quantity. Gi den beregnede kolonnen et passende navn og sorter fra høyest til lavest verdi.

SELECT orders.order_id, customers.first_name, customers.last_name, products.product_id, products.product_name, orders.quantity, orders.order_date, orders.status,
       price * quantity AS beregnet_verdi
FROM orders
JOIN products on products.product_id = orders.product_id
JOIN customers on customers.customer_id = orders.customer_id
ORDER BY beregnet_verdi DESC;


-- 6. Bestillinger med høy verdi: Finn bestillinger med en beregnet verdi på mer enn 2000 kr. Vis kunden,
-- produktet, antall, pris og beregnet verdi.


7. Bestillinger per status: Finn ut hvor mange bestillinger som har hver status.
8. Gjennomsnittspris per kategori: Finn gjennomsnittsprisen for produktene i hver kategori. Sorter fra
høyest til lavest gjennomsnittspris.
9. Bestillinger per kunde: Finn ut hvor mange bestillinger hver kunde har gjort. Sorter kunden med flest
bestillinger først. Resultatet skal også inkludere kunder som har 0 bestillinger.
10. Antall solgte produkter: Finn ut hvor mange enheter som totalt er bestilt av hvert produkt. Produkter
som ikke forekommer i noen bestilling skal også være med i resultatet og vises med 0 bestilte enheter.
Husk at antall rader i orders og totalt antall bestilte enheter ikke nødvendigvis er det samme.
11. Beregnet verdi per produkt: Finn samlet beregnet verdi for hvert produkt basert på bestillingene. Vis
produktnavn, totalt antall bestilte enheter og samlet beregnet verdi. Produkter uten bestillinger skal også
være med og vises med 0 bestilte enheter og 0 i beregnet verdi. Sorter fra høyest til lavest verdi.
12. Kunder med flere bestillinger: Finn kunder som har mer enn én bestilling. Vis kunden og antall
bestillinger. Finn ut hvordan du kan filtrere grupperte resultater.
13. Kunder uten bestillinger: Finn kunden eller kundene som ikke har noen bestillinger. Oppgaven skal løses
ved hjelp av relasjonen mellom customers og orders.
14. Produkter uten bestillinger: Finn produktet eller produktene som ikke forekommer i noen bestilling.
Oppgaven skal løses ved hjelp av relasjonen mellom products og orders.
15. Utforskingsoppgave: Finn kunden som har høyest samlet beregnet verdi på bestillingene sine. Du får
ikke oppgitt hvilke SQL-elementer som skal brukes. Forklar kort hvordan du kom frem til løsningen.