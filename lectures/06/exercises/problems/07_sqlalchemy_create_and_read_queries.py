"""Problem 07: Create and read data with SQLAlchemy.

Task:
1. Open a SQLAlchemy Session on `school.db`.
2. Create one Assignment for an existing student.
3. Read all students.
4. Read students with age >= 22 sorted by age descending.
5. Read assignments with joined student names.

Starter:
- Reuse `Student` and `Assignment` from `db_models.py`.
- Use `select(...)` queries.
"""

from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from db_models import Assignment, Base, Student

import os

_db_path = os.path.join(os.path.dirname(__file__), "..", "..", "..", "..", "school.db")
DB_URL = f"sqlite:///{os.path.abspath(_db_path)}"


def main() -> None:
    engine = create_engine(DB_URL, echo=False)

    with Session(engine) as session:
        new_assignment = Assignment(title="SQL Basics", score=95, student_id=2)
        session.add(new_assignment)
        session.commit()
        print(f"Created assignment: {new_assignment.title} (id={new_assignment.id})")

        print("All Students:")
        students = session.execute(select(Student)).scalars().all()
        for s in students:
            print(f"  {s.id}: {s.name}, age={s.age}, email={s.email}, track={s.track}")

        print("Students with age >= 22 (sorted by age desc):")
        stmt = select(Student).where(Student.age >= 22).order_by(Student.age.desc())
        filtered = session.execute(stmt).scalars().all()
        for s in filtered:
            print(f"  {s.id}: {s.name}, age={s.age}")

        print("Assignments with Student Names:")
        stmt = select(Assignment, Student.name).join(Student)
        rows = session.execute(stmt).all()
        for assignment, student_name in rows:
            print(
                f"  {assignment.title} (score={assignment.score}) -> student: {student_name}"
            )


if __name__ == "__main__":
    main()
