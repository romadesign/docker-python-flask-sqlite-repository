# file: test/users/conftest.py

import pytest  # type: ignore

import sqlite3

from src.domain.model.user import hash_password


@pytest.fixture
def database():
    conn = sqlite3.connect(":memory:")
    sql = f"""
        DROP TABLE IF EXISTS blogs;
        CREATE TABLE blogs (
            id  TEXT PRIMARY KEY,
            blogtype VARCHAR ,
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
        INSERT INTO blogs (id, blogtype, title, image, price, user_id, start_time, end_time ) VALUES
                ('blog-id-1', 'blog-service-type-1', 'blog-title-1', 'blog-image-1', 'blog-price-1', 'blog-user-id-1', 'blog-start-time-1', 'blog-end-time-1' ),
                ('blog-id-2', 'blog-service-type-2', 'blog-title-2', 'blog-image-2', 'blog-price-2', 'blog-user-id-2', 'blog-start-time-2', 'blog-end-time-2');
        INSERT INTO users ( id, username, name, password, user_rol, phone_number, e_mail, address) values
                ("blog-user-id-1", "user-1@example.com", "User 1", '{hash_password("user-1-password")}', "admin", "223366895", "user-1@example.com", "bilbao"),
                 ("user_1", "user-1@example.com", "xxxxx", '{hash_password("user-1-password")}', "admin", "223366895", "user-1@example.com", "deustu"),
                ("blog-user-id-2", "user-2@example.com", "User 2", '{hash_password("user-2-password")}', "user", "55689854", "user-2@example.com", "casco viejo");
    """
    conn.executescript(sql)

    return conn
