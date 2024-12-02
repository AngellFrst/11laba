import sqlite3  # Импостер

connection = sqlite3.connect("my_database.db") 
cursor = connection.cursor()


cursor.execute("DROP TABLE IF EXISTS students")
cursor.execute("DROP TABLE IF EXISTS contacts")

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER
)
""")


cursor.execute("""
CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    phone INTEGER,
    address TEXT,
    FOREIGN KEY(student_id) REFERENCES students(id)
)
""")


cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", ("Ангелина", 18))
cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", ("Семен", 18))
cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", ("Катя", 17))
cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", ("Женя", 15))

cursor.execute("INSERT INTO contacts (student_id, phone, address) VALUES (?, ?, ?)", (1, 89020056737, "Хо Ши Мина"))
cursor.execute("INSERT INTO contacts (student_id, phone, address) VALUES (?, ?, ?)", (2, 8073373125, "Кольцевая"))
cursor.execute("INSERT INTO contacts (student_id, phone, address) VALUES (?, ?, ?)", (3, 89091235435, "Городская"))
cursor.execute("INSERT INTO contacts (student_id, phone, address) VALUES (?, ?, ?)", (4, 89057892321, "Варейкиса"))


cursor.execute("""
SELECT students.name, contacts.phone, contacts.address
FROM students
JOIN contacts ON students.id = contacts.student_id
""")

rows = cursor.fetchall()
for row in rows:
    print(f"Имя: {row[0]}, Номер телефона: {row[1]}, Адрес: {row[2]}")




connection.close()



