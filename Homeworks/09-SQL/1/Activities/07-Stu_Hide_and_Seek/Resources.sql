-- drop table if exists wordassociation; 
-- create table wordassociation(
--     author int,
--     word1 varchar,
--     word2 varchar,
--     source varchar(5)
-- );
-- select * from wordassociation where word1='stone'; 
-- select * from wordassociation where author between 0 and 10; 
-- select * from wordassociation where word1='pie' or word2='pie';
select * from wordassociation where source ='BC'and author between 333 and 335; 