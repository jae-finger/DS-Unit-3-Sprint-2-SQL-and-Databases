import pandas as pd
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()


# Credentials
DB_HOSTNAME = os.getenv("DB_HOSTNAME")
DB_NAME = os.getenv("DB_NAME")
DB_USER =  os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")


# Connect to PGDB
pg_conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                       password=DB_PASSWORD, host=DB_HOSTNAME)
pg_curs = pg_conn.cursor()


# Q1. How many survived?
query = """SELECT COUNT(id) FROM titanic
WHERE survived = 1;"""

# A1.
pg_curs.execute(query)
print('Survived:', pg_curs.fetchone()[0])


# Q2 How many didn't?
query = """SELECT COUNT(id) FROM titanic
WHERE survived = 0;"""

# A2. 
pg_curs.execute(query)
print("Didn't survive:", pg_curs.fetchone()[0])


# Q3. Count for each class
query = """SELECT class, COUNT(*) FROM titanic
GROUP BY class
ORDER BY class;"""

# A3. 
pg_curs.execute(query)
print('(Class, Count)')
print(pg_curs.fetchall())


# Q4. Average age of survived?
query = """SELECT AVG(age) FROM titanic
WHERE survived =1;"""

# A4.
pg_curs.execute(query)
print('Average age of surviving:')
print(pg_curs.fetchone()[0])


# Q5. Average age of those that didn't?
query = """SELECT AVG(age) FROM titanic
WHERE survived =0;"""

# A5. 
pg_curs.execute(query)
print("Average age of those who didn't survive:")
print(pg_curs.fetchone()[0])


# Q6. Average age by class
query = """SELECT class, AVG(age) FROM titanic
GROUP BY class
ORDER BY class;"""

# A6. 
pg_curs.execute(query)
print('(Class, Average age)')
print(pg_curs.fetchall())


# Q7. Average fare by class
query = """SELECT class, AVG(fare) FROM titanic
GROUP BY class
ORDER BY class;"""

# A7. 
pg_curs.execute(query)
print('(Class, Average Fare Price )')
print(pg_curs.fetchall())


# Q8. Average price of fare by survival status
query = """SELECT survived, AVG(fare) FROM titanic
GROUP BY survived
ORDER BY survived;"""

# A8. 
pg_curs.execute(query)
print('(Survival Status, Average Fare Price )')
print(pg_curs.fetchall())


# Q9. Average number of siblings & spouses by class
query = """SELECT class, AVG(sibling_spouse) FROM titanic
GROUP BY class
ORDER BY class;"""

# A10. 
pg_curs.execute(query)
print('(Class, Average Spouses & Siblings)')
print(pg_curs.fetchall())


# Q11. Average number siblings & spouses if survived
query = """SELECT survived, AVG(sibling_spouse) FROM titanic
GROUP BY survived
ORDER BY survived;"""

# A11. 
pg_curs.execute(query)
print('(Survival Status, Average Spouses & Siblings)')
print(pg_curs.fetchall())


# Q12. Average number parents & children by class
query = """SELECT class, AVG(parent_children) FROM titanic
GROUP BY class
ORDER BY class;"""

# A12. 
pg_curs.execute(query)
print('(Class, Average Parents & Children)')
print(pg_curs.fetchall())


# Q13. Average number parents & children by survival status
query = """SELECT survived, AVG(parent_children) FROM titanic
GROUP BY survived
ORDER BY survived;"""

# A14.
pg_curs.execute(query)
print('(Survival Status, Average Parents & Children)')
print(pg_curs.fetchall())


# Q15. Does anyone have the same name?
query = """SELECT name FROM
(SELECT name, COUNT(name) FROM titanic
GROUP BY name) AS name_counts
WHERE count > 1;"""

# A16.
pg_curs.execute(query)
print('Anybody with the same name?')
if pg_curs.fetchall() == []:
    print('There is nobody with the same name.')
else:
    print('There are people with the same name.')