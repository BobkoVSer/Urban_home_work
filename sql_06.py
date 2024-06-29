import sqlite3


def create_tables_students():
    query = ("""
        CREATE TABLE IF NOT EXISTS students 
        (id          INTEGER       PRIMARY KEY AUTOINCREMENT ,
        name         TEXT,
        age          INTEGER);""")
    con.execute(query)


def create_tables_grades():
    con.execute("""
        CREATE TABLE IF NOT EXISTS grades 
        (id         INTEGER        PRIMARY KEY AUTOINCREMENT,
        student_id  INTEGER,
        subject     TEXT,
        grade       REAL,
        FOREIGN KEY (student_id) REFERENCES students(id));""")


class University:

    def __init__(self, name):
        self.name = name

    @staticmethod
    def add_student(name, age):
        with sqlite3.connect('students.db') as c:
            c.execute("PRAGMA foreign_key = ON")
            c.execute(""f"INSERT INTO students (name, age) VALUES ('{name}', '{age}');""")
            c.commit()

    @staticmethod
    def add_grade(student_id, subject, grade):
        with sqlite3.connect('students.db') as c:
            c.execute("PRAGMA foreign_key = ON")
            query = ""f"INSERT INTO grades (student_id, subject, grade) VALUES ('{student_id}', '{subject}', '{grade}');"""
            c.execute(query)
            c.commit()

    @staticmethod
    def get_students(subject=None):
        with sqlite3.connect('students.db') as c:
            if subject is None:
                cur = c.execute(""f"SELECT students.name, students.age, subject, grade FROM students JOIN grades ON students.id = grades.student_id;""")
            else:
                cur = c.execute(f"SELECT students.name, students.age, subject, grade FROM students JOIN grades ON students.id = grades.student_id WHERE subject = '{subject}'")
            c.commit()
            return cur.fetchall()


with sqlite3.connect('students.db') as con:
    con.cursor()
    create_tables_students()
    create_tables_grades()
    con.commit()

u1 = University('Urban')

u1.add_student('Ivan', 26)   #id - 1
u1.add_student('Ilya', 24)  # id - 2
u1.add_student('Alex', 38)  # id - 3
u1.add_student('Vika', 18)  # id - 4
#
u1.add_grade(1, 'Python', 4.8)
u1.add_grade(2, 'PHP', 4.3)
u1.add_grade(3, 'Python', 5)
u1.add_grade(4, 'Java', 4.1)
#
u1.add_grade(1, 'Python', 4.7)
u1.add_grade(2, 'PHP', 4.9)
u1.add_grade(3, 'Python', 5)
u1.add_grade(4, 'Java', 4.8)
#
u1.add_grade(1, 'Python', 4.9)
u1.add_grade(2, 'PHP', 4.1)
u1.add_grade(3, 'Python', 5)
u1.add_grade(4, 'Java', 4.2)

print(u1.get_students())
print(u1.get_students('Python'))
print(u1.get_students('PHP'))