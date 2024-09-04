import psycopg2

conn = psycopg2.connect(
    dbname="goit",
    user="lead_proxy",
    password="cd3f3ns3",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    fullname VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS status (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL
);
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    status_id INTEGER NOT NULL REFERENCES status(id),
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE
);
""")

conn.commit()

cur.close()
conn.close()

print("Таблиці створені успішно.")
