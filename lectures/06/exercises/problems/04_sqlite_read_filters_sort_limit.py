"""Problem 04: Practice WHERE, ORDER BY, LIMIT.

Task:
1. Get students with age >= 22
2. Sort students by age DESC
3. Return only top 3 oldest students
4. Get backend students younger than 23

Use parameterized queries for filter values.
"""

import sqlite3

DB_PATH = "school.db"


def main() -> None:
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("SELECT * FROM students WHERE age >= ?", (22,))
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.execute(
        "SELECT * FROM students WHERE age >= ? ORDER BY age DESC LIMIT 3", (22,)
    )
    oldest_students = cur.fetchall()
    for row in oldest_students:
        print(row)

    cur.execute("SELECT * FROM students WHERE track = ? AND age < ?", ("backend", 23))
    backend_youngsters = cur.fetchall()
    for row in backend_youngsters:
        print(row)

    conn.close()


if __name__ == "__main__":
    main()
