import psycopg2
from psycopg2 import sql
import config

conn = psycopg2.connect(
    host=config.host,
    database='postgres',
    user=config.user,
    password=config.password)

conn.autocommit = True
cursor = conn.cursor()
cursor.execute(sql.SQL(open(config.createdb, "r").read()).format(
        sql.Identifier(config.database)))