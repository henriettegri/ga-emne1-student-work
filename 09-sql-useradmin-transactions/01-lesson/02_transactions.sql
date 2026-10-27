-- starter denne, da vet systemet at ingenting kan sees av andre brukere før commit eller rollback.
START TRANSACTION;

UPDATE city
SET Population = Population - 100000
WHERE CountryCode ='NOR'
    AND Name ='Oslo'

UPDATE city
SET Population = Population + 100000
WHERE CountryCode ='NOR'
    AND Name ='Bergen'

-- angrer:
ROLLBACK;


-- starter denne, da vet systemet at ingenting kan sees av andre brukere før commit eller rollback.
START TRANSACTION;

UPDATE city
SET Population = Population - 100000
WHERE CountryCode ='NOR'
    AND Name ='Oslo';

UPDATE city
SET Population = Population + 100000
WHERE CountryCode ='NOR'
    AND Name ='Bergen';

-- permanent endring hvis commit gjennomføres:
COMMIT;