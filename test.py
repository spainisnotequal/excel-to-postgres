import pandas
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

# read file
FILE = "foo.xlsx"
df = pandas.read_excel(FILE)
print(df)

# connect to PostgreSQL
load_dotenv()
POSTGRES_ENGINE = os.getenv("POSTGRES_ENGINE")
engine = create_engine(POSTGRES_ENGINE)

# data fame to PostgreSQL
table_name = "foo"
df.to_sql(table_name, engine)
