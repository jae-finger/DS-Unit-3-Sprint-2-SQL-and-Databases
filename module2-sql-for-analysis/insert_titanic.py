'''
Title: LS DS Unit3 Sprint2 -- insert_titanic.py
Author: Jonathan Finger
'''

# 0. Import Packages
import os
import pandas
import psycopg2
from psycopg2.extras import execute_values
import numpy as np
psycopg2.extensions.register_adapter(np.int64, psycopg2._psycopg.AsIs)

# 1. Import titanic.csv (loads if titanic.csv is in "data" directory)
CSV_FILEPATH = os.path.join(os.path.dirname(__file__), "data", "titanic.csv")
df = pandas.read_csv(CSV_FILEPATH)
df.index += 1

# 2. Connect to PG DataBase
DB_HOSTNAME = os.getenv("DB_HOSTNAME")
DB_NAME = os.getenv("DB_NAME")
DB_USER =  os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

conn = psycopg2.connect(host=DB_HOSTNAME, database=DB_NAME, user=DB_USER, password=DB_PASSWORD)
curs = conn.cursor()

# 3. Create a table on the server
create_table = """
CREATE TABLE IF NOT EXISTS titanic (
    id SERIAL PRIMARY KEY,
    surv int,
    p_class int,
    name varchar,
    sex varchar,
    age int,
    num_sibling_spouse int,
    num_parent_child int,
    fare float
);
"""
curs.execute(create_table)

# 4. Insert titanic.csv data into titanic table
titanic_tuple = list(df.to_records())
insert_data = "INSERT INTO titanic (id, surv, p_class, name, sex, age, num_sibling_spouse, num_parent_child, fare) VALUES %s"
execute_values(curs, insert_data, titanic_tuple)


# 5. Commit results and close connection
conn.commit()
curs.close()
conn.close()
exit()