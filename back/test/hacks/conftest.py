# file: test/users/conftest.py

import pytest  # type: ignore

import sqlite3

from src.domain.model.user import hash_password


@pytest.fixture
def database():
    conn = sqlite3.connect(":memory:")
    sql = f"""
        DROP TABLE IF EXISTS hacks;
        CREATE TABLE hacks (
            id  TEXT PRIMARY KEY,
            categoryhack VARCHAR,
            title TEXT NOT NULL,
            image BLOB NOT NULL UNIQUE,
            price TEXT ,
            user_id	TEXT,
            start_time TEXT,
            end_time TEXT

        );
        DROP TABLE IF EXISTS users;
        CREATE TABLE users (
            id varchar primary key,
            username varchar,
            name varchar,
            password varchar,
            user_rol title,
            phone_number varchar,
            e_mail varchar,
            address varchar
        );
        DROP TABLE IF EXISTS provinces;
        CREATE TABLE provinces (
            province_code varchar PRIMARY KEY,
            province_name varchar NOT NULL
        );

        DROP TABLE IF EXISTS cities;
        CREATE TABLE cities (
            province_code varchar,
            city_code varchar,
            city_name varchar NOT NULL,
            price varchar,
            PRIMARY KEY("province_code", "city_code"),
            FOREIGN KEY("province_code") REFERENCES "provinces"("province_code")
        );
        INSERT INTO hacks (id, categoryhack, title, image, price, user_id, start_time, end_time) VALUES
                ('hack-id-1', 'hack-service-type-1',  'hack-title-1', 'hack-image-1', 'hack-price-1', 'hack-user-id-1', 'hack-start-time-1', 'hack-end-time-1' ),
                ('hack-id-2', 'hack-service-type-2', 'hack-title-2', 'hack-image-2', 'hack-price-2', 'hack-user-id-2', 'hack-start-time-2', 'hack-end-time-2');
        INSERT INTO users ( id, username, name, password, user_rol, phone_number, e_mail, address) values
                ("hack-user-id-1", "user-1@example.com", "User 1", '{hash_password("user-1-password")}', "admin", "223366895", "user-1@example.com", "bilbao"),
                ("user_1", "user-1@example.com", "xxxxx", '{hash_password("user-1-password")}', "admin", "223366895", "user-1@example.com", "deustu"),
                ("hack-user-id-2", "user-2@example.com", "User 2", '{hash_password("user-2-password")}', "user", "55689854", "user-2@example.com", "casco viejo");
    """
    conn.executescript(sql)

    return conn
