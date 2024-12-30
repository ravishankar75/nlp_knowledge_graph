from flask import Flask, render_template

app = Flask(__name__)
print("Hello World")

@app.route('/')
def hello():
    return render_template('base.html', content="Hello, Flask!")

if __name__ == '__main__':
    app.run(debug=True)