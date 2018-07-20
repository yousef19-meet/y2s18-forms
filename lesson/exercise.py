from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def homepage():
    if request.method == 'GET':
        return render_template('sum_form.html')
    else:
        num1 = ???
        num2 = ???
        return render_template('sum_response.html',
               n1=num1, n2=num2, sum=num1+num2)

app.run(debug=True)
