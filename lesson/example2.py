from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def homepage():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        return render_template('response.html',
               n=request.form['firstname'],
               s=request.form['sex'])

app.run(debug=True)
