DROP table cities;

CREATE TABLE cities(
	city varchar(30) not NULL,
    state varchar(30) not NULL,
	population INT
); 
 

insert into cities (city, state, population)
values('Alameda', 'CA',79177),
	   ('Mesa','AZ',496401),
	   ('Boerne','TX',16056),
	   ('Anaheim','CA',352497),
	   ('Tuscon','AZ',535677),
	   ('Garland','TX',238002); 
select * from cities; 

