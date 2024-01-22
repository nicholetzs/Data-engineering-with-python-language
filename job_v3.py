# Hands-On Demo 4 - Data Extraction, Cleansing, Transformation and Enrichment Pipeline Creation
# Version 3
# Business rule: Remove the "period" character in the last column of the file to prevent the number from being truncated 

# Imports
import csv
import sqlite3

# Function to remove the dot in the data from the last column
def remove_ponto(valor):
    return int(valor.replace('.', ''))

# Opens the CSV file with the food production data
with open('food_production.csv', 'r') as file:
    
    # Creates a CSV reader to read the file
    reader = csv.reader(file)

    # Skips the first row, which contains the column headers
    next(reader)

    # Connects to the database
    conn = sqlite3.connect('dsadb.db')

    # Deletes the existing table, if any
    conn.execute('DROP TABLE IF EXISTS producao')

    # Creates a new table to store the food production data
    conn.execute('''CREATE TABLE producao (
                    produto TEXT,
                    quantidade INTEGER,
                    preco_medio REAL,
                    receita_total INTEGER
                )''')

    # Inserts each row of the file with a quantity greater than 10 into the database table
    for row in reader:
        if int(row[1]) > 10:
            
            # Removes the point from the value of the last column and converts it to an integer
            row[3] = remove_ponto(row[3])

            # Inserts the record into the database
            conn.execute('INSERT INTO producao (produto, quantidade, preco_medio, receita_total) VALUES (?, ?, ?, ?)', row)

    conn.commit()
    conn.close()

print("Job Sucess!")
