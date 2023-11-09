import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

# load the .env file variables
load_dotenv()


DB_USER = 'postgres'
DB_PASSWORD = 'postgres'
DB_PORT = 3306
DB_HOST = 'db'
DB_NAME = 'sample-db'


# 1) Connect to the database here using the SQLAlchemy's create_engine function

def connect():
    global engine
    connection_string = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}?autocommit=true"
    print("Starting the connection...")
    engine = create_engine(connection_string)
    engine.connect() 
    return engine

# 2) Execute the SQL sentences to create your tables using the SQLAlchemy's execute function


create_publishers_table = """ 
CREATE TABLE publishers(
    publisher_id INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    PRIMARY KEY(publisher_id)
);

"""

create_authors_table = """ 

CREATE TABLE authors(
    author_id INT NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    middle_name VARCHAR(50) NULL,
    last_name VARCHAR(100) NULL,
    PRIMARY KEY(author_id)
);
"""







# 3) Execute the SQL sentences to insert your data using the SQLAlchemy's execute function

# 4) Use pandas to print one of the tables as dataframes using read_sql function
