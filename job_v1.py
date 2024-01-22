# Hands-On Demo 4 - Data Extraction, Cleansing, Transformation and Enrichment Pipeline Creation
# Version 1

# Imports
import csv
import sqlite3

# Create a new data base
conn = sqlite3.connect('nidb.db')

# Create a table to store food production data
conn.execute('''CREATE TABLE producao (
                produto TEXT,
                quantidade INTEGER,
                preco_medio REAL,
                receita_total REAL
            )''')

# Records and closes the connection
conn.commit()
conn.close()

# Opens the CSV file with the food production data
with open('food_production.csv', 'r') as file:
    
    # Creates a CSV reader to read the file
    reader = csv.reader(file)

    # Skips the first row, which contains the column headers
    next(reader)

    # Connects to the database
    conn = sqlite3.connect('nidb.db')

    # Inserts each row of the file into the database table
    for row in reader:
        conn.execute('INSERT INTO producao (produto, quantidade, preco_medio, receita_total) VALUES (?, ?, ?, ?)', row)

    conn.commit()
    conn.close()

print("Job Sucess!")

