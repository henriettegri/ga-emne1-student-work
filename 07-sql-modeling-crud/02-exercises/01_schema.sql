-- kolonner

CREATE DATABASE IF NOT EXISTS animal_shelter_practice;

USE animal_shelter_practice;

SELECT DATABASE()


CREATE TABLE areas (
    id INT AUTO_INCREMENT,
    name VARCHAR(40) NOT NULL,
    PRIMARY KEY (id),
    UNIQUE (name)
);

CREATE TABLE animals (
    id INT AUTO_INCREMENT,
    name VARCHAR(40) NOT NULL,
    species VARCHAR(20) NOT NULL,
    weight DECIMAL(5,2),
    admitted_on DATE,
    area_id INT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (area_id) REFERENCES areas(id)
);

