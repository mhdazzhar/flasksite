from flask import Flask
app=Flask(__name__)

@app.route('/')
def home():
    return '<h1>Hello world</h1>'
app.run()

@app.route('/new')
def new():
    return '<h1> Welcome Homie'
app.run()
