import snowflake.connector
import pandas as pd
from snowflake.sqlalchemy import URL
from sqlalchemy import create_engine

# create the connection string
url=URL(
    user='',
    password='',
    account='',
    warehouse='',
    database='',
    schema='',
    role=''
)

engine=create_engine(url)

connection=engine.connect()

query = '''
select * from myiristable
'''
 
df = pd.read_sql(query, connection)
 
df