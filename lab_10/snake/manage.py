import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="snake",
    user="postgres",
    password="dosik13094664"
)
cur = conn.cursor()

def get_all_data():
    cur.execute("SELECT * FROM snakegame ORDER BY user_score DESC")
    rows = cur.fetchall()
    for row in rows:
        print(f"Username = {row[0]} Score = {row[1]} Level = {row[2]}")

get_all_data()