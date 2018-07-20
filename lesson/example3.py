from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def homepage():
    if request.method == 'GET':
        return render_template('form_with_birthday.html')
    else:
        return render_template('response_with_birthday.html',
               n=request.form['firstname'],
               s=request.form['sex'],
               is_birthday=request.form['birthday'])

app.run(debug=True)
