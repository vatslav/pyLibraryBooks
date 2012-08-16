import sqlalchemy
import re
a=[]
a.append(2)
re.
from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:', echo=True)
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
metadata = MetaData()
users_table = Table('users', metadata,
Column('id', Integer, primary_key=True),
Column('name', String),
Column('fullname', String),
Column('password', String) )
