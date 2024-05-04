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

def get_records_by_pattern(pattern):
    cur.execute(f"""SELECT * FROM phonebook WHERE name LIKE '{pattern}'
     OR last_name LIKE '{pattern}'
     OR phone LIKE '{pattern}'
                """)
    rows = cur.fetchall()
    for row in rows:
        print(row)

def insert_or_update_user(name, last_name, phone):
    cur.execute(f"""SELECT * FROM phonebook WHERE first_name = '{name}'
     AND last_name = '{last_name}';
                """)
    if cur.fetchone() is None:
        cur.execute(f"""INSERT INTO phonebook (first_name, last_name, phone) VALUES "
        ('{name}', '{last_name}', '{phone}')
                    """)
    else:
        cur.execute(f"""UPDATE phonebook SET phone = '{phone}' WHERE name = '{name}' AND last_name = '{last_name}'""")
    conn.commit()

def insert_many_users(user_list):
    for user in user_list:
        name, last_name, phone = user
        if len(phone) == 12:
            insert_or_update_user(name, last_name, phone)
        else:
            print(f"Incorrect data: {user}")

def query_data_with_pagination(limit, offset):
    cur.execute("SELECT * FROM phonebook LIMIT %s OFFSET %s", (limit, offset))
    rows = cur.fetchall()
    for row in rows:
        print(row)

def delete_data_by_username_or_phone(username=None, phone=None):
    if username:
        cur.execute(f"""DELETE FROM phonebook WHERE name = '{username}' OR last_name = '{username}' """)
    if phone:
        cur.execute(f"""DELETE FROM phonebook WHERE phone = '{phone}' """)
    conn.commit()
