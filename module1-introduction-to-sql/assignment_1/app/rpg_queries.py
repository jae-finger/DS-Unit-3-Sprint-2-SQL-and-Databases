# assignment_1/app/assignment_1.py

import sqlite3
import os

FILEPATH = os.path.join(os.path.dirname(__file__), "..", "data", "rpg_db.sqlite3")

conn = sqlite3.connect(FILEPATH)

curs = conn.cursor()

print("----------------")
print("Question 1: How many total Characters are there?")
query_q1 = "SELECT COUNT(distinct character_id) FROM charactercreator_character"
results_q1 = curs.execute(query_q1).fetchall()
print("Q1 Answer:", results_q1)
print('There are 302 characters in this RPG.')

print("----------------")
print("Question 2: How many of each specific subclass?")

query_q2_mage = "SELECT COUNT(distinct character_ptr_id) FROM charactercreator_mage"
results_q2_mage = str((curs.execute(query_q2_mage).fetchall())).strip('[(').strip(',)]')

query_q2_necro = "SELECT COUNT(distinct mage_ptr_id) FROM charactercreator_necromancer"
results_q2_necro = str((curs.execute(query_q2_necro).fetchall())).strip('[(').strip(',)]')

query_q2_thief = "SELECT COUNT(distinct character_ptr_id) FROM charactercreator_thief"
results_q2_thief = str((curs.execute(query_q2_thief).fetchall())).strip('[(').strip(',)]')

query_q2_fighter = "SELECT COUNT(distinct character_ptr_id) FROM charactercreator_fighter"
results_q2_fighter = str((curs.execute(query_q2_fighter).fetchall())).strip('[(').strip(',)]')

query_q2_cleric = "SELECT COUNT(distinct character_ptr_id) FROM charactercreator_cleric"
results_q2_cleric = str((curs.execute(query_q2_cleric).fetchall())).strip('[(').strip(',)]')

print(f"Q2 Answer: There are...{results_q2_mage} mages (of which {results_q2_necro} are necros), {results_q2_thief} thieves, {results_q2_fighter} fighters, and {results_q2_cleric} clerics.")
# The subclass results total 302, which is the total number of characters. SANITY CHECK!

print("----------------")
print("Question 3: How many total Items?")
query_q3 = "SELECT COUNT(distinct item_id) FROM armory_item"
results_q3 = str((curs.execute(query_q3).fetchall())).strip('[(').strip(',)]')
print(f"There are {results_q3} items total.")

print("----------------")
print("Question 4: How many of the Items are weapons? How many are not?")
no_weapons = int(results_q3)
query_q4_weapons = "SELECT COUNT(distinct item_ptr_id) FROM armory_weapon"
results_q4 = int(str((curs.execute(query_q4_weapons).fetchall())).strip('[(').strip(',)]'))
not_weapons = no_weapons - results_q4
print(f"{results_q4} items are weapons and {not_weapons} are not weapons.")

print("----------------")
print("Question 5: How many Items does each character have? (Return first 20 rows)")
query_q5 = "SELECT character_id, COUNT(item_id) as number_of_items FROM charactercreator_character_inventory GROUP BY character_id LIMIT 20"
results_q5 = curs.execute(query_q5).fetchall()
print("(character id, number of items)")
for each in results_q5:
    print(each)

print("----------------")
print("Question 6: How many Weapons does each character have? (Return first 20 rows)")
print("(character id, number of weapons)")
query_q6 = "SELECT i.character_id, COUNT(w.item_ptr_id) as number_of_weapons FROM charactercreator_character_inventory i LEFT JOIN armory_weapon w ON i.item_id = w.item_ptr_id GROUP BY 1 LIMIT 20"
results_q6 = curs.execute(query_q6).fetchall()
for each in results_q6:
    print(each)

print("----------------")
print("Question 7: On average, how many Items does each Character have?")
query_q7 = "SELECT COUNT(item_id)/COUNT(distinct character_id) as average_item_per_char FROM charactercreator_character_inventory"
results_q7 = str((curs.execute(query_q7).fetchall())).strip('[(').strip(',)]')
print(f"On average, each character has {results_q7} items.")

print("----------------")
print("Question 8: On average, how many Weapons does each character have")
query_q8 = "SELECT COUNT(item_id)/COUNT(distinct character_id) as number_of_weaps_per_char FROM charactercreator_character_inventory WHERE item_id >= 138 AND item_id <=174"
results_q8 = str((curs.execute(query_q8).fetchall())).strip('[(').strip(',)]')
print(f'Each character has {results_q8} weapon on average.')
print("----------------")


# Mike's solution code
# -- On average, how many Items does each Character have?
# -- return a single number
# -- intermediate step:
# --     row per character (302)
# --     columns: character_id, name, item_count
# ​
# select avg(item_count) as avg_items
# from (
#     select
#       c.character_id
#       ,c."name" as character_name
#       ,count(distinct inv.item_id) as item_count
#     from charactercreator_character c
#     left join charactercreator_character_inventory inv ON c.character_id = inv.character_id
#     group by 1, 2
# ) subq


# -- are there any characters without items?
# -- no (we saw no counts > 1)
# select character_id, item_id, count(distinct id) as row_count
# from charactercreator_character_inventory
# group by character_id, item_id
# order by 3 desc

# --2.- How many of each specific subclass?
# -- How many of each specific subclass?
# -- Expecting cleric total = 75
# -- Expecting fighter total = 68
# -- Expecting mage total = 108
# -- Expecting necro total = 11
# -- Expecting thief total = 51
# SELECT 
#         ccc.character_id as character 
#         ,count(distinct c.character_ptr_id) as total_clerics
#         ,count(distinct f.character_ptr_id) as total_fighters
#         ,count(distinct m.character_ptr_id) as total_mages
#         ,count(distinct n.mage_ptr_id) as total_necromancers
#         ,count(distinct t.character_ptr_id) as total_thieves
# FROM charactercreator_character ccc 
# LEFT JOIN charactercreator_fighter f  
#     ON character = f.character_ptr_id
# LEFT JOIN charactercreator_cleric c 
#     ON character = c.character_ptr_id
# LEFT JOIN charactercreator_mage m 
#     ON character =  m.character_ptr_id
# LEFT JOIN charactercreator_necromancer n 
#     ON character = n.mage_ptr_id
# LEFT JOIN charactercreator_thief t 
#     ON character = t.character_ptr_id
# --GROUP BY character 