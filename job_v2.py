# Hands-On Demo 4 - Data Extraction, Cleansing, Transformation and Enrichment Pipeline Creation
# Version 2
# Business rule: Load only records with a production quantity greater than 10.

# Imports
import csv
import sqlite3

# Opens the CSV file with the food production data
with open('food_production', 'r') as file:
    
    # Creates a CSV reader to read the file
    reader = csv.reader(file)

    # Skips the first row, which contains the column headers
    next(reader)

    # Connects to the database
    conn = sqlite3.connect('nidb.db')

    # Deletes the existing table, if any
    conn.execute('DROP TABLE IF EXISTS producao')

    # Creates a new table to store the food production data
    conn.execute('''CREATE TABLE producao (
                    produto TEXT,
                    quantidade INTEGER,
                    preco_medio REAL,
                    receita_total REAL
                )''')

    # Inserts each row of the file with a quantity greater than 10 into the database table
    for row in reader:
        if int(row[1]) > 10:
            conn.execute('INSERT INTO producao (produto, quantidade, preco_medio, receita_total) VALUES (?, ?, ?, ?)', row)

    conn.commit()
    conn.close()

print("Job Sucess!")
