from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def homepage():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        print(request.form)
        return 'You just made a POST request!'

app.run(debug=True)
