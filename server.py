from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

def get_data_from_db():
    connection = sqlite3.connect('my_database.db')
    cursor = connection.cursor()

    cursor.execute("""
        SELECT students.id, students.name, students.age, contacts.truba, contacts.address
        FROM students
        LEFT JOIN contacts ON students.id = contacts.student_id
    """)
    
    rows = cursor.fetchall()  
    connection.close()

    students = []
    for row in rows:
        student = {
            "id": row[0],
            "name": row[1],
            "age": row[2],
            "truba": row[3],  
            "address": row[4]  
        }
        students.append(student)

    return students

@app.route('/students', methods=['GET'])
def students():
    data = get_data_from_db()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)