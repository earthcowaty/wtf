from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET' , 'POST'])
def hello():
    if request.method == "POST":
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        sum = num1 + num2
        return render_template('index.html', num1=num1, num2=num2, sum=sum)
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)