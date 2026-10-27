import sqlite3

def main():
    connection = sqlite3.connect("teachers.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM teachers")
    teachers = cursor.fetchall()

    print("List of teachers:")

    for teacher in teachers:
        print(teacher)

    connection.close()

if __name__ == "__main__":
    main()
