import psycopg2
import csv
conn = psycopg2.connect(
    host="localhost",
    database="phonebook",
    user="postgres",
    password="dosik13094664"
)
cur = conn.cursor()

cur.execute("""DROP TABLE phonebook;
""")
conn.commit()

cur.execute("""
    CREATE TABLE Phonebook (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50),
        last_name VARCHAR(50),
        phone VARCHAR(50)
    );
""")
conn.commit()

def insert_data(name, last_name, phone):
    cur.execute(f"""INSERT INTO phonebook (name, last_name, phone) VALUES 
        ('{name}', '{last_name}', '{phone}');
                """)
    conn.commit()

def enter_data():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    phone = input("Enter phone: ")
    insert_data(first_name, last_name, phone)

def upload_csv(file_path):
    with open(file_path, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            name, last_name, phone = row
            insert_data(name, last_name, phone)

def update_data(id, name=None, phone=None):
    if name:
        cur.execute(f"""UPDATE phonebook SET name = '{name}' WHERE id = {id}""")
    if phone:
        cur.execute(f"""UPDATE phonebook SET phone = '{phone}' WHERE id = {id}""")
    conn.commit()

def query_data():
    cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()
    for row in rows:
        print(row)

def delete_data(name=None, phone=None):
    if name:
        cur.execute(f"""DELETE FROM phonebook WHERE name = '{name}' """)
    if phone:
        cur.execute(f"""DELETE FROM phonebook WHERE phone = '{phone}' """)
    conn.commit()


