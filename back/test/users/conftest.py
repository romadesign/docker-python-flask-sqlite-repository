# file: test/users/conftest.py

import pytest  # type: ignore

import sqlite3

from src.domain.model.user import hash_password


@pytest.fixture
def database():
    conn = sqlite3.connect(":memory:")
    sql = f"""
        DROP TABLE IF EXISTS users;
        CREATE TABLE users (
            id varchar primary key,
            username varchar,
            name varchar,
            password varchar,
            user_rol text,
            phone_number varchar,
            e_mail varchar,
            address varchar,
            destination_province_code varchar NOT NULL,
            destination_city_code varchar NOT NULL,
            FOREIGN KEY("destination_province_code", "destination_city_code") 
                 REFERENCES "cities"("province_code", "city_code")
        );
        INSERT INTO users ( id, username, name, password, user_rol, phone_number, e_mail, address, destination_province_code, destination_city_code) values
            ("user-1", "user-1@example.com", "User 1", '{hash_password("user-1-password")}', "admin", "223366895", "user-1@example.com", "bilbao", "48", "002"),
            ("user-2", "user-2@example.com", "User 2", '{hash_password("user-2-password")}', "user", "55689854", "user-2@example.com", "casco viejo", "48", "002"),
            ("user-3", "user-3@example.com", "User 3", '{hash_password("user-3-password")}', "user", "55568842", "user-3@example.com", "barakaldo", "48", "002"),
            ("user-4", "user-4@example.com", "User 4", '{hash_password("user-4-password")}', "user", "2662266558", "user-4@example.com", "muskiz", "48", "002");
    """
    conn.executescript(sql)
    return conn
