import os
import pandas
import sqlite3

# assignment_1/app/buddymove_holidayiq.py
FILEPATH = os.path.join(os.path.dirname(__file__), "..", "data", "buddymove_holidayiq.csv")

df = pandas.read_csv(FILEPATH)
#Check with provided parameters.
print(f"The dataframe should have 249 rows and 7 columns. It has a shape of {df.shape}.")

DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "data", "buddymove_holidayiq.sqlite3")
conn = sqlite3.connect("DB_FILEPATH")
curs = conn.cursor()

df.to_sql('Review', conn, if_exists='replace')

print('--- DATABASE CREATED ---')

print("Test 1: Count how many rows you have - it should be 249!")
query1 = "SELECT COUNT(*) FROM Review"
results1 = str((curs.execute(query1).fetchall())).strip('[(').strip(',)]')
print("Number of rows:", results1)

print("---------")
print("Test 2: How many users who reviewed at least 100 Nature in the category also reviewed at least 100 in the Shopping category?")
query2 = "SELECT COUNT(*) FROM Review WHERE Nature >= 100 AND Shopping > 100"
results2 = str((curs.execute(query2).fetchall())).strip('[(').strip(',)]')
print("Number of users with >= 100 shopping and nature reviews:", results2)
