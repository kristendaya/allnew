CREATE TABLE movieTBL (
	movie_id        number(4),
    movie_title     nvarchar2(30),
    movie_director  nvarchar2(30),
    movie_star      nvarchar2(30),
    movie_script    clob,
    movie_film      blob
);

SELECT * FROM movieTBL
