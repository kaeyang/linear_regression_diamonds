import psycopg2
from user_definition import *

# Create local postgreSQL connection
connection = psycopg2.connect(database="postgres",
                        user=postgres_user, password=postgres_password, 
                        host=postgres_host, port=postgres_port
)

connection.autocommit = True

# Create cursor object
cursor = connection.cursor()

# Drop table if it already exists to create new table
sql1 = '''DROP TABLE IF EXISTS diamonds'''
cursor.execute(sql1)

# Create table schema
create_data_schema = '''
CREATE TABLE diamonds (
diamond_id TEXT PRIMARY KEY,
carat FLOAT NOT NULL,
cut TEXT NOT NULL,
color TEXT NOT NULL,
clarity TEXT NOT NULL,
depth FLOAT NOT NULL,
table_val FLOAT NOT NULL,
price INT NOT NULL,
x FLOAT NOT NULL,
y FLOAT NOT NULL,
z FLOAT NOT NULL
)
'''
cursor.execute(create_data_schema)

# Lastly, import data from csv file into postgreSQL table
with open('diamonds.csv') as csvFile:
   next(csvFile) # Skip header
   cursor.copy_from(csvFile, "diamonds", sep=",")

# Save changes and close connection to PostgreSQL server
connection.commit()
connection.close()