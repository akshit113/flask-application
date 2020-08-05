from flask import Flask

# how to set up flask
# 1. pip install flask
# 2. create app.py
# 3. set up FLASK_APP environment variable using set FLASK_APP = app.py or using os.environ['FLASK_APP'] = 'app.py'
# 4. navigate to the project folder in the terminal
# 5. run the flask app from command line using (1) python app.py  or using (2) flask run


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
