import psycopg2

HOST     = "hostname",
DB       = "events_uploader",
USER     = "events_uploader",
PASSWORD = "events_uploader",
PORT     = "5432"

connection = psycopg2.connect(
    host     = HOST,
    db       = DB,
    user     = USER,
    password = PASSWORD,
    port     = PORT
)

cursor = connection.cursor()

cursor.execute("CREATE TABLE events_upload(id SERIAL PRIMARY KEY, subject VARCHAR, offset_start INTEGER, offset_end INTEGER, partition INTEGER, topic VARCHAR, created_at TIMESTAMP);")
cursor.execute("INSERT INTO events_upload (subject, offset_start, offset_end, partition, topic, created_at) "\+
               " values (%s, %s, %s, %s, %s, %s)", (subject, offset_start, offset_end, partition, topic, TIMESTAMP))
conn.commit()

cursor.close()

connection.close()