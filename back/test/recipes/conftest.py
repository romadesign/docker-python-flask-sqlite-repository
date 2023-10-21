# file: test/users/conftest.py

import pytest  # type: ignore

import sqlite3

from src.domain.model.user import hash_password


@pytest.fixture
def database():
    conn = sqlite3.connect(":memory:")
    sql = f"""
        DROP TABLE IF EXISTS recipes;
        CREATE TABLE recipes (
            id  TEXT PRIMARY KEY,
            categoryrecipe VARCHAR ,
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
        INSERT INTO recipes (id, categoryrecipe, title, image, price, user_id, start_time, end_time ) VALUES
                ('recipe-id-1', 'recipe-service-type-1', 'recipe-title-1', 'recipe-image-1', 'recipe-price-1', 'recipe-user-id-1', 'recipe-start-time-1', 'recipe-end-time-1' ),
                ('recipe-id-2', 'recipe-service-type-2', 'recipe-title-2', 'recipe-image-2', 'recipe-price-2', 'recipe-user-id-2', 'recipe-start-time-2', 'recipe-end-time-2');
        INSERT INTO users ( id, username, name, password, user_rol, phone_number, e_mail, address) values
                ("recipe-user-id-1", "user-1@example.com", "User 1", '{hash_password("user-1-password")}', "admin", "223366895", "user-1@example.com", "bilbao"),
                 ("user_1", "user-1@example.com", "xxxxx", '{hash_password("user-1-password")}', "admin", "223366895", "user-1@example.com", "deustu"),
                ("recipe-user-id-2", "user-2@example.com", "User 2", '{hash_password("user-2-password")}', "user", "55689854", "user-2@example.com", "casco viejo");
    """
    conn.executescript(sql)

    return conn
