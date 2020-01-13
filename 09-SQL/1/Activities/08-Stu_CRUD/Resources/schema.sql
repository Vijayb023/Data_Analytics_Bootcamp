drop table if exists players;
drop table if exists matches;

create table players(
    player_id int,
	first_name varchar,
	last_name varchar,
	hand varchar,
    country_code varchar
);
