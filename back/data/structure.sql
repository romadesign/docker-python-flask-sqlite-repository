BEGIN TRANSACTION;
DROP TABLE IF EXISTS users;
CREATE TABLE IF NOT EXISTS users (
    id varchar,
    username varchar,
    name varchar,
    password varchar,
    user_rol title,
    phone_number varchar,
    e_mail varchar,
    address varchar,
    PRIMARY KEY(id)
);

