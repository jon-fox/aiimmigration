from pgvector.psycopg2 import register_vector
import numpy as np
import psycopg2 as psy
import os

# local stuff for now
conn = psy.connect(database="postgres", user="postgres", password=os.getenv('DB_PSWD'), host="localhost", port=5432)

cur = conn.cursor()
cur.execute('CREATE EXTENSION IF NOT EXISTS vector')

register_vector(conn)

cur.execute('CREATE SCHEMA IF NOT EXISTS metainfo')
cur.execute('CREATE TABLE IF NOT EXISTS metainfo.threads (user text PRIMARY KEY NOT NULL, embedding vector(3))')

embedding = np.array([1, 2, 3])
cur.execute('INSERT INTO metainfo.threads (embedding) VALUES (%s)', (embedding,))

cur.execute('SELECT * FROM metainfo.threads ORDER BY embedding <-> %s LIMIT 5', (embedding,))
print(cur.fetchall())

cur.execute('CREATE INDEX ON metainfo.threads USING hnsw (embedding vector_l2_ops)')
# or
cur.execute('CREATE INDEX ON metainfo.threads USING ivfflat (embedding vector_l2_ops) WITH (lists = 100)')

conn.commit()
conn.close()
