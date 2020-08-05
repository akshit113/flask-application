from flask import Flask
from pandas import DataFrame

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def hello():
    # df = DataFrame([[1, 2], [3, 4], [5, 6]])
    return '<h1>Home Page</h1>'
    # return df.to_html()


@app.route('/about')
def about():
    return '<h1>About Page</h1>'


if __name__ == '__main__':
    app.run(debug=True)
