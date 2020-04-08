CREATE TABLE dict
(
  id serial PRIMARY KEY,
  word_eng text NOT NULL,
  word_translation text NOT NULL,
  user_id integer NOT NULL
);