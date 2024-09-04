import psycopg2
from faker import Faker

conn = psycopg2.connect(
    dbname="goit",
    user="lead_proxy",
    password="cd3f3ns3",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

fake = Faker()

statuses = [('new',), ('in progress',), ('completed',)]
cur.executemany("INSERT INTO status (name) VALUES (%s) ON CONFLICT (name) DO NOTHING", statuses)

for _ in range(10):
    fullname = fake.name()
    email = fake.email()
    cur.execute("INSERT INTO users (fullname, email) VALUES (%s, %s) ON CONFLICT (email) DO NOTHING", (fullname, email))

cur.execute("SELECT id FROM status")
status_ids = [row[0] for row in cur.fetchall()]

cur.execute("SELECT id FROM users")
user_ids = [row[0] for row in cur.fetchall()]

for _ in range(20):
    title = fake.sentence(nb_words=4)
    description = fake.text()
    status_id = fake.random.choice(status_ids)
    user_id = fake.random.choice(user_ids)
    cur.execute("INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)", 
                (title, description, status_id, user_id))

conn.commit()

cur.close()
conn.close()

print("Таблиці заповнені даними.")
