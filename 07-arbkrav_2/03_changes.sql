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

3. Registrer nye bestillinger: Henrik Solberg kjøper 1 Docking station,
2 enheter av USB-C cable og 1
External SSD 2TB. Du får ikke oppgitt customer_id eller product_id.
Finn først de nødvendige
verdiene i databasen og registrer bestillingene. Kontroller resultatet med
en spørring som viser kundens navn og produktnavn i stedet for bare ID-er.


4. Prisendring: Øk prisen på alle produkter i kategorien Accessories med 8 %. Finn først produktene som
blir påvirket og kontroller dagens priser. Utfør deretter oppdateringen og kontroller resultatet.
5. Lagerpåfylling: Produkter med færre enn 15 enheter på lager får levert 20 nye enheter. Finn først
produktene som blir påvirket, og oppdater deretter lagerbeholdningen.
6. Endre flere verdier: Produktet Gaming headset skal få 15 % høyere pris og 10 nye enheter på lager.
Begge endringene skal utføres med samme UPDATE.
7. Oppdater ordrestatus: Alle bestillinger med status Shipped som er registrert før 10. august 2025, skal
endres til Delivered. Kontroller radene før og etter oppdateringen.
8. Opprett og slett testdata: Opprett en testkunde, et testprodukt og en bestilling hvor testkunden kjøper
testproduktet. Kontroller at dataene finnes, og slett deretter alle testdataene igjen. Du må selv finne riktig
rekkefølge for slettingen og forklare hvorfor rekkefølgen er viktig.
9. Bruk en transaksjon: Registrer en ny bestilling og reduser samtidig lagerbeholdningen for produktet
som bestilles. Begge endringene skal utføres som én transaksjon. Kontroller resultatet før transaksjonen
avsluttes. Avslutt transaksjonen med COMMIT. Forklar også hva ROLLBACK ville gjort dersom en av
operasjonene skulle angres, og hvorfor transaksjoner er nyttige når flere endringer hører sammen.

