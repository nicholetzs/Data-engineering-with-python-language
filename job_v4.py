# Hands-On Demo 4 - Data Extraction, Cleansing, Transformation and Enrichment Pipeline Creation
# Version 4
# Business rule: Enrich the data by adding a column with the profit margin of each product to the destination

# Imports
import csv
import sqlite3

# Function to remove the point from the last column
def remove_ponto(valor):
    return int(valor.replace('.', ''))

# Opens the CSV file with the food production data
with open('food_production.csv', 'r') as file:
    
    # Creates a CSV reader to read the file
    reader = csv.reader(file)

    # Skips the first row, which contains the column headers
    next(reader)

    # Connects to the database
    conn = sqlite3.connect('nidb.db')

    # Deletes the existing table, if any
    conn.execute('DROP TABLE IF EXISTS producao')

    # Creates a new table to store the food production data with the new column 'margem_lucro'
    conn.execute('''CREATE TABLE producao (
                    produto TEXT,
                    quantidade INTEGER,
                    preco_medio REAL,
                    receita_total INTEGER,
                    margem_lucro REAL
                )''')

    # Inserts each row of the file with a quantity greater than 10 into the database table
    for row in reader:
        if int(row[1]) > 10:
            
            # Removes the point from the value of the last column and converts it to an integer
            row[3] = remove_ponto(row[3])

            # Calculates gross profit margin based on average sales value and total revenue (token calculation)
            margem_lucro = (row[3] / float(row[1])) - float(row[2])

            # Inserts the row with the new column 'margem_lucro' into the database table
            conn.execute('INSERT INTO producao (produto, quantidade, preco_medio, receita_total, margem_lucro) VALUES (?, ?, ?, ?, ?)', (row[0], row[1], row[2], row[3], margem_lucro))

    conn.commit()
    conn.close()

print("Job Sucess!")
