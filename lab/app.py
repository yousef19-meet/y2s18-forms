from databases import *
from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', students=query_all())

@app.route('/student/<int:student_id>')
def display_student(student_id):
    return render_template('student.html', student=query_by_id(student_id))

@app.route('/add', methods=['GET', 'POST'])
def add_student_route():
	if request.method == 'GET':
		return render_template('add.html')
	else:
		add_student(request.form['student_name'],
			request.form['student_year'], False)
		return render_template('add.html')

@app.route('/delete/<int:student_id>', methods= ['POST'])
def delete(student_id):
	deleted_student=query_by_id(student_id)
	session.delete(deleted_student)
	session.commit()
	return redirect(url_for('home'))
app.run(debug=True)
