import psycopg2
from psycopg2 import sql

# Database connection parameters
dbname = 'book'
user = 'postgres'
password = '1234'
host = 'localhost'
port = '5432'

# Connect to the database
conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
cur = conn.cursor()

def store_data_from_file():
    file_path = input("Enter file path: ")
    with open(file_path, 'r') as file:
        for line in file:
            name, number = line.strip().split(',')
            cur.execute("INSERT INTO phonebooks (name, phone) VALUES (%s, %s)", (name, number))
    conn.commit()

def store_data_from_console():
    name = input("Enter name: ")
    number = input("Enter number: ")
    cur.execute("INSERT INTO phonebooks (name, phone) VALUES (%s, %s)", (name, number))
    conn.commit()

def query_data():
    name = input("Enter name: ")
    number = input("Enter number: ")
    if name:
        cur.execute("SELECT * FROM phonebooks WHERE name = %s", (name,))
    elif number:
        cur.execute("SELECT * FROM phonebooks WHERE phone = %s", (number,))
    else:
        cur.execute("SELECT * FROM phonebooks")
    return cur.fetchall()

def delete_data():
    name = input("Enter name: ")
    number = input("Enter number: ")
    if name:
        cur.execute("DELETE FROM phonebooks WHERE name = %s", (name,))
    elif number:
        cur.execute("DELETE FROM phonebooks WHERE phone = %s", (number,))
    conn.commit()

def update_data(name, new_number):
    name = input("Enter name: ")
    new_number = input("Enter new number: ")
    cur.execute("UPDATE phonebooks SET phone = %s WHERE name = %s", (new_number, name))
    conn.commit()

def main():
    while True:
        print("1. Store data from file")
        print("2. Store data from console")
        print("3. Query data")
        print("4. Delete data")
        print("5. Update data")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            store_data_from_file()
        elif choice == '2':
            store_data_from_console()
        elif choice == '3':
            print(query_data())
        elif choice == '4':
            delete_data()
        elif choice == '5':
            update_data()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

    # Close the cursor and connection
    cur.close()
    conn.close()

if __name__ == "__main__":
    main()