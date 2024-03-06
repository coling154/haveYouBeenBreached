DROP DATABASE users;
CREATE DATABASE users;
use users;
CREATE TABLE users(
  	username VARCHAR(70),
   	password VARCHAR(80),
   	PRIMARY KEY (username)
);