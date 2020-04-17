'''
Title: LS DS Unit3 Sprint2 -- insert_titanic.py
Author: Jonathan Finger
'''

# 0. Import Packages
import pymongo
import os
import sqlite3
from dotenv import load_dotenv

load_dotenv()

# 1. Load rpg database (loads if in "data" directory)
DBFILEPATH = os.path.join(os.path.dirname(__file__), "data", "rpg_db.sqlite3")

slite_conn = sqlite3.connect(DBFILEPATH)
slite_conn.row_factory = sqlite3.Row
slite_curs = slite_conn.cursor()

get_characters = 'SELECT * FROM charactercreator_character'
characters_table = slite_curs.execute(get_characters).fetchall()

# 2. Connect to Atlas/Mongo
client = pymongo.MongoClient("mongodb+srv://Najf6XsR:<password>@cluster0-airxa.mongodb.net/test?retryWrites=true&w=majority")
db = client.test

DB_USER = os.getenv("MONGO_USER", default="OOPS")
DB_PASSWORD = os.getenv("MONGO_PASSWORD", default="OOPS")
CLUSTER_NAME = os.getenv("MONGO_CLUSTER_NAME", default="OOPS")

connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority"
print("----------------")
print("URI:", connection_uri)

client = pymongo.MongoClient(connection_uri)
print("----------------")
print("CLIENT:", type(client), client)

db = client.rpg_database 
print("----------------")
print("DB:", type(db), db)

collection = db.charactercreator_character
print("----------------")
print("COLLECTION:", type(collection), collection)

print("----------------")
print("COLLECTIONS:")
print(db.list_collection_names())

for row in characters_table:
    collection.insert_one({
        "character_id": characters_table[0][0],
        "name": characters_table[0][1],
        "level": characters_table[0][2],
        "exp": characters_table[0][3],
        "hp": characters_table[0][4],
        "strength": characters_table[0][5],
        "intelligence": characters_table[0][6],
        "dexterity": characters_table[0][7],
        "wisdom": characters_table[0][8],
    })

print("DOCS:", collection.count_documents({}))

# Succesfully copied the 302 row file!
#
# Assignment question: How was working with MongoDB different
# from working with PostgreSQL? What was easier, and what was harder?"
#
# I feel that working with MongoDB was easier than I thought. I figured
# that since I just started learning SQL, learning something similar yet
# different might be challenging. Instead, it was similar enough to provide
# some good context.
# 
# I found it easier to translate the SQL line of thinking even though at
# first I thought MongoDB looked very different with it's data format.
# However, what was harder than I thought was the terms. It was funny to see
# even Mike struggle to say database and table instead of the NoSQL collection
# and documents. :) 