from flask import Flask, jsonify, request
import psycopg2
from flask_cors import CORS

app = Flask(name)
CORS(app)

# Database configuration
DB_HOST = 'db-asila.ct6ei6agkus4.ap-south-1.rds.amazonaws.com'  # Replace with your RDS endpoint
DB_NAME = 'postgres'
DB_USER = 'postgres'    # Replace with your RDS username
DB_PASS = 'postgres'  # Replace with your RDS password
DB_PORT = '5432'

def get_db_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        port=DB_PORT
    )
    return conn

@app.route('/students', methods=['GET'])
def get_students():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT student_id, full_name, gender, age, department, gpa, enrollment_year FROM tbl_asila_students")
    students = cur.fetchall()
    cur.close()
    conn.close()

    students_list = [{'student_id': student[0], 'full_name': student[1], 'gender': student[2],
                      'age': student[3], 'department': student[4], 'gpa': float(student[5]),
                      'enrollment_year': student[6]} for student in students]
    return jsonify(students_list)

@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()
    full_name = data.get('full_name')
    gender = data.get('gender')
    age = data.get('age')
    department = data.get('department')
    gpa = data.get('gpa')
    enrollment_year = data.get('enrollment_year')

    if not all([full_name, gender, age, department, gpa, enrollment_year]):
        return jsonify({'message': 'Missing required fields'}), 400

    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO tbl_asila_students (full_name, gender, age, department, gpa, enrollment_year) VALUES (%s, %s, %s, %s, %s, %s)",
                    (full_name, gender, age, department, gpa, enrollment_year))
        conn.commit()
        return jsonify({'message': 'Student added successfully'}), 201
    except Exception as e:
        conn.rollback()
        return jsonify({'message': f'Error adding student: {str(e)}'}), 500
    finally:
        cur.close()
        conn.close()

@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute("DELETE FROM tbl_asila_students WHERE student_id = %s", (student_id,))
        if cur.rowcount > 0:
            conn.commit()
            return jsonify({'message': f'Student with ID {student_id} deleted successfully'}), 200
        else:
            return jsonify({'message': f'Student with ID {student_id} not found'}), 404
    except Exception as e:
        conn.rollback()
        return jsonify({'message': f'Error deleting student: {str(e)}'}), 500
    finally:
        cur.close()
        conn.close()

if name == 'main':
    app.run(host='0.0.0.0', port=8000, debug=True)