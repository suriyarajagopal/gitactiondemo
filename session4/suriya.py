from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Have a Pleasent Day!!'

if __name__ == '__main__':
    app.run(debug=True, port=5000)
