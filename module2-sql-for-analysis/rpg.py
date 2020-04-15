'''
Title: LS DS Unit3 Sprint2 -- insert_titanic.py
Author: Jonathan Finger
'''

# 0. Import Packages
import os
import pandas
import psycopg2
from psycopg2.extras import execute_values
import sqlite3

# 1. Load rpg database (loads if in "data" directory)
DBFILEPATH = os.path.join(os.path.dirname(__file__), "data", "rpg_db.sqlite3")

slite_conn = sqlite3.connect(DBFILEPATH)
slite_curs = slite_conn.cursor()

get_characters = 'SELECT * FROM charactercreator_character'
characters_table = slite_curs.execute(get_characters).fetchall()

# 2. Connect to PG DataBase
DB_HOSTNAME = os.getenv("DB_HOSTNAME")
DB_NAME = os.getenv("DB_NAME")
DB_USER =  os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

conn = psycopg2.connect(host=DB_HOSTNAME, database=DB_NAME, user=DB_USER, password=DB_PASSWORD)
curs = conn.cursor()

# 3. Create a table on the server
create_table = """
CREATE TABLE charactercreator_character (character_id integer NOT NULL PRIMARY KEY, 
name varchar(30) NOT NULL, level integer NOT NULL, exp integer NOT NULL, hp integer NOT NULL, 
strength integer NOT NULL, intelligence integer NOT NULL, dexterity integer NOT NULL, wisdom integer NOT NULL);
"""
curs.execute(create_table)

# 4. Create insert table statement
for character in characters_table:
    insert_data = "INSERT INTO charactercreator_character (character_id, name, level, exp, hp, strength, intelligence, dexterity, wisdom) VALUES %s"
    curs.execute(insert_data)

# 5. Commit results and close connection
conn.commit()
curs.close()
conn.close()
exit()