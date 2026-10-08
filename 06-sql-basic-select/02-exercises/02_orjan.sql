drop database if exists human_body;
create database if not exists human_body;



       auto_increment
       -- legger til tall, teller seg selv
       --uten auto_increment må man legge inn info på id


       --varchar - bruker bare bokstavene
       --char - 12 karakterer, vil uansett bruke et visst antall karakterer, fylle ut med blanke

drop database if exists human_body;
create database if not exists human_body;

use human_body;
create table hand (
    id int not null auto_increment,
    finger varchar(12)

);


insert into hand (finger)
values
    ('Tommel'),
    ('Pekefinger'),
    ('Langfinger'),
    ('ringfinger'),
    ('Lillefinger');




drop database if exists human_body;
create database if not exists human_body;

use human_body;
create table hand (
    id int not null primary key,
    finger varchar(12) not null

);


insert into hand (id, finger)
values
    (1, 'Tommel'),
    (2, 'Pekefinger'),
    (3, 'Langfinger'),
    (4, 'Ringfinger'),
    (5, 'Lillefinger');


SELECT finger
FROM hand
WHERE id = 3;

select *
from foot;





---- 7drop database if exists human_body;
create database if not exists human_body;

use human_body;
create table hand (
    id int auto_increment primary key,
    finger varchar(12) not null,
    what_hand enum('høyre', 'venstre') not null

);


insert into hand (finger, what_hand)
values
    ('Tommel', 'høyre'),
    ('Pekefinger', 'høyre'),
    ('Langfinger', 'høyre'),
    ('Ringfinger', 'høyre'),
    ('Lillefinger', 'høyre');


create table foot (
    id int auto_increment primary key,
    toes varchar(12) not null

);


insert into foot (toes)
values
    ('Storetå');
