"""
CREATE TABLE
DROP TABLE
INSERT INTO TABLE
SELECT FROM TABLE
DELETE FROM TABLE
"""

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, insert
engine = create_engine('sqlite:///census.sqlite', echo = True)
meta = MetaData()

students = Table(
   'students', meta, 
   Column('id', Integer, primary_key = True), 
   Column('name', String), 
   Column('lastname', String),
)
meta.create_all(engine)

students = Table('students', meta, autoload=True, autoload_with=engine)

# Print the column names
print(students.columns.keys())

# Print full table metadata
print(repr(meta.tables['students']))

# FROM HERE DOWN
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

# INSERT INTO TABLE


# SELECT FROM TABLE
for student in session.query(students).all():
    print(student)

