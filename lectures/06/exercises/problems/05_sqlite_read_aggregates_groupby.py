"""Problem 05: Basic aggregates and GROUP BY.

Task:
1. Count all students
2. Compute average age
3. Compute min and max age
4. Count students per track (GROUP BY track)

Print each result.
"""

import sqlite3

DB_PATH = "school.db"


def main() -> None:
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM students")
    total_students = cur.fetchone()[0]
    print(f"Total students: {total_students}")

    cur.execute("SELECT AVG(age) FROM students")
    average_age = cur.fetchone()[0]
    print(f"Average age: {average_age}")

    cur.execute("SELECT MIN(age), MAX(age) FROM students")
    min_max_age = cur.fetchone()
    print(f"Min age: {min_max_age[0]}, Max age: {min_max_age[1]}")

    cur.execute("SELECT track, COUNT(*) FROM students GROUP BY track")
    students_per_track = cur.fetchall()
    for track, count in students_per_track:
        print(f"Track: {track}, Count: {count}")

    conn.close()


if __name__ == "__main__":
    main()
