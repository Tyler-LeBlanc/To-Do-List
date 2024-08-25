from flask import Flask, render_template, request, redirect, url_for, jsonify
import mysql.connector

app = Flask(__name__)

# MySQL connection

conn = mysql.connector.connect(
    host="localhost",
    username="root",
    password="W0c2w401",
    database="toDo_db",
)

cursor = conn.cursor()

@app.route('/')
def index():
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    title = request.form['title']
    description = request.form['description']
    cursor.execute("INSERT INTO tasks (title, description) VALUES (%s, %s)", (title, description))
    conn.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    cursor.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
    conn.commit()
    return redirect(url_for('index'))

@app.route('/complete/<int:task_id>', methods=['POST'])
def complete_task(task_id):
    cursor.execute("UPDATE tasks SET completed = TRUE WHERE id = %s", (task_id,))
    conn.commit()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)

