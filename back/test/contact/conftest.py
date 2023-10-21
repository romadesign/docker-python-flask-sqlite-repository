
import pytest  # type: ignore

import sqlite3


@pytest.fixture
def database():
    conn = sqlite3.connect(":memory:")
    sql = f"""
        DROP TABLE IF EXISTS contact;
        CREATE TABLE contact (
            id  varchar PRIMARY KEY,
            name VARCHAR ,
            e_mail varchar,
            observation varchar

           
        );
       
        INSERT INTO contact (id, name, e_mail, observation ) VALUES
                ('contact-id-1', 'contact-name-1', 'contact-e-mail-1', 'contact-observation-1'),
                ('contact-id-2', 'contact-name-2', 'contact-e-mail-2', 'contact-observation-2');
       
    """
    conn.executescript(sql)


    return conn
