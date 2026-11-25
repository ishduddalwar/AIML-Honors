import sqlite3

DB = "staff.db"


def connect():
    return sqlite3.connect(DB)


def create_table():
    with connect() as conn:
        conn.execute(
            "CREATE TABLE IF NOT EXISTS staff "
            "(emp_id INTEGER PRIMARY KEY, emp_name TEXT, emp_salary REAL)"
        )


def add():
    eid = int(input("ID: "))
    name = input("Name: ")
    sal = float(input("Salary: "))
    with connect() as conn:
        conn.execute("INSERT INTO staff VALUES (?, ?, ?)", (eid, name, sal))
    print("Record added.")


def show():
    with connect() as conn:
        rows = conn.execute("SELECT * FROM staff").fetchall()
    if rows:
        for eid, name, sal in rows:
            print(f"  {eid}  |  {name}  |  {sal}")
    else:
        print("Table is empty.")


def find():
    term = input("Name to search: ").lower()
    with connect() as conn:
        rows = conn.execute("SELECT * FROM staff").fetchall()
    hits = [r for r in rows if term in r[1].lower()]
    if hits:
        for eid, name, sal in hits:
            print(f"  {eid}  |  {name}  |  {sal}")
    else:
        print("Nothing found.")


def change_salary():
    eid = int(input("ID: "))
    new_sal = float(input("New salary: "))
    with connect() as conn:
        cur = conn.execute("UPDATE staff SET emp_salary=? WHERE emp_id=?", (new_sal, eid))
    if cur.rowcount:
        print("Salary updated.")
    else:
        print("ID not found.")


def remove():
    eid = int(input("ID: "))
    with connect() as conn:
        cur = conn.execute("DELETE FROM staff WHERE emp_id=?", (eid,))
    if cur.rowcount:
        print("Deleted.")
    else:
        print("ID not found.")


create_table()

while True:
    print("\n1-Add  2-Show all  3-Search  4-Update salary  5-Delete  6-Exit")
    opt = input("Pick: ")

    if opt == "1":
        add()
    elif opt == "2":
        show()
    elif opt == "3":
        find()
    elif opt == "4":
        change_salary()
    elif opt == "5":
        remove()
    elif opt == "6":
        break
    else:
        print("Try again.")
