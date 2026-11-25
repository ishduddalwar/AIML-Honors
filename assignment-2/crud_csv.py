import csv
import os

DATA_FILE = "staff.csv"
HEADERS = ["EmpID", "EmpName", "EmpSalary"]


def init_file():
    with open(DATA_FILE, "w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=HEADERS)
        writer.writeheader()
    print("CSV file initialized.")


def insert():
    if not os.path.exists(DATA_FILE):
        print("Run option 1 first to create the file.")
        return

    emp_id = input("Employee ID: ")
    emp_name = input("Employee Name: ")
    emp_sal = input("Salary: ")

    with open(DATA_FILE, "a", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=HEADERS)
        writer.writerow({"EmpID": emp_id, "EmpName": emp_name, "EmpSalary": emp_sal})
    print("Record inserted.")


def display():
    if not os.path.exists(DATA_FILE):
        print("No file found.")
        return

    with open(DATA_FILE, "r") as fh:
        reader = csv.DictReader(fh)
        for entry in reader:
            print(f"  {entry['EmpID']}  |  {entry['EmpName']}  |  {entry['EmpSalary']}")


def search():
    if not os.path.exists(DATA_FILE):
        print("No file found.")
        return

    query = input("Search name: ").lower()
    with open(DATA_FILE, "r") as fh:
        reader = csv.DictReader(fh)
        found = [r for r in reader if query in r["EmpName"].lower()]

    if found:
        for entry in found:
            print(f"  {entry['EmpID']}  |  {entry['EmpName']}  |  {entry['EmpSalary']}")
    else:
        print("No match.")


def modify():
    if not os.path.exists(DATA_FILE):
        print("No file found.")
        return

    with open(DATA_FILE, "r") as fh:
        rows = list(csv.DictReader(fh))

    target_id = input("ID to update: ")
    hit = False
    for row in rows:
        if row["EmpID"] == target_id:
            row["EmpName"] = input("New name: ")
            row["EmpSalary"] = input("New salary: ")
            hit = True
            break

    if hit:
        with open(DATA_FILE, "w", newline="") as fh:
            writer = csv.DictWriter(fh, fieldnames=HEADERS)
            writer.writeheader()
            writer.writerows(rows)
        print("Record updated.")
    else:
        print("ID not found.")


def delete():
    if not os.path.exists(DATA_FILE):
        print("No file found.")
        return

    with open(DATA_FILE, "r") as fh:
        rows = list(csv.DictReader(fh))

    target_id = input("ID to remove: ")
    remaining = [r for r in rows if r["EmpID"] != target_id]

    if len(remaining) == len(rows):
        print("ID not found.")
    else:
        with open(DATA_FILE, "w", newline="") as fh:
            writer = csv.DictWriter(fh, fieldnames=HEADERS)
            writer.writeheader()
            writer.writerows(remaining)
        print("Record removed.")


while True:
    print("\nMenu: 1)Create  2)Insert  3)Display  4)Search  5)Modify  6)Delete  7)Quit")
    choice = input(">> ")

    if choice == "1":
        init_file()
    elif choice == "2":
        insert()
    elif choice == "3":
        display()
    elif choice == "4":
        search()
    elif choice == "5":
        modify()
    elif choice == "6":
        delete()
    elif choice == "7":
        print("Bye.")
        break
    else:
        print("Invalid option.")
