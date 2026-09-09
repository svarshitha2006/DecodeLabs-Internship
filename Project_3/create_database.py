import pandas as pd
import sqlite3

# Load the cleaned Excel dataset
df = pd.read_excel("cleaned_dataset.xlsx")

# Connect to SQLite database
connection = sqlite3.connect("ecommerce.db")

# Create the orders table
df.to_sql("orders", connection, if_exists="replace", index=False)

# Close the connection
connection.close()

print("SQL DATABASE CREATED SUCCESSFULLY!")
print("Database: ecommerce.db")
print("Table: orders")
print(f"Records inserted: {len(df)}")