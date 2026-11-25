import pandas as pd
import os

FILE = "staff.csv"


def read_data():
    if os.path.exists(FILE):
        return pd.read_csv(FILE)
    return pd.DataFrame(columns=["emp_id", "emp_name", "emp_salary"])


def write_data(df):
    df.to_csv(FILE, index=False)


def add_employee():
    df = read_data()
    eid = int(input("ID: "))
    name = input("Name: ")
    sal = int(input("Salary: "))
    row = pd.DataFrame([{"emp_id": eid, "emp_name": name, "emp_salary": sal}])
    df = pd.concat([df, row], ignore_index=True)
    write_data(df)
    print("Employee added.")


def list_employees():
    df = read_data()
    if df.empty:
        print("Nothing to show.")
    else:
        print(df.to_string(index=False))


def find_employee():
    df = read_data()
    term = input("Search name: ").lower()
    matches = df[df["emp_name"].str.lower().str.contains(term, na=False)]
    if matches.empty:
        print("No match found.")
    else:
        print(matches.to_string(index=False))


def change_salary():
    df = read_data()
    eid = int(input("ID: "))
    if eid not in df["emp_id"].values:
        print("ID doesn't exist.")
        return
    new_sal = int(input("New salary: "))
    df.loc[df["emp_id"] == eid, "emp_salary"] = new_sal
    write_data(df)
    print("Salary changed.")


def drop_employee():
    df = read_data()
    eid = int(input("ID to delete: "))
    if eid not in df["emp_id"].values:
        print("ID doesn't exist.")
        return
    df = df[df["emp_id"] != eid].reset_index(drop=True)
    write_data(df)
    print("Removed.")


while True:
    print("\n[1] Add  [2] List  [3] Search  [4] Update salary  [5] Delete  [6] Exit")
    opt = input("-> ")

    if opt == "1":
        add_employee()
    elif opt == "2":
        list_employees()
    elif opt == "3":
        find_employee()
    elif opt == "4":
        change_salary()
    elif opt == "5":
        drop_employee()
    elif opt == "6":
        print("Done.")
        break
    else:
        print("Invalid choice.")
