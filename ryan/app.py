import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
import pandas as pd

# load the .env file variables
load_dotenv()

# 1) Connect to the database here using the SQLAlchemy's create_engine function

connection_string = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
engine = create_engine(connection_string).execution_options(autocommit=True)
connection = engine.connect()
print("Connected to database!")


# 2) Execute the SQL sentences to create your tables using the SQLAlchemy's execute function

with open("/workspaces/connecting-to-a-sql-database-project-tutorial-ds-2023/src/sql/drop.sql", "r") as f:
    sql_commands_1 = f.read().strip()

result_1 = engine.execute(sql_commands_1)

with open("/workspaces/connecting-to-a-sql-database-project-tutorial-ds-2023/src/sql/create.sql", "r") as f:
    sql_commands_2 = f.read().strip()
result_2 = engine.execute(sql_commands_2)

# 3) Execute the SQL sentences to insert your data using the SQLAlchemy's execute function

with open("/workspaces/connecting-to-a-sql-database-project-tutorial-ds-2023/src/sql/insert.sql", "r") as f:
    sql_commands_3 = f.read().strip()
result_3 = engine.execute(sql_commands_3)

# 4) Use pandas to print one of the tables as dataframes using read_sql function
result_dataFrame = pd.read_sql("Select * from publishers;", engine)
print(result_dataFrame)
connection.close()
