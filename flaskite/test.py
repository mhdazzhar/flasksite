from flask import Flask
new=Flask(__name__)

@new.route('/profile/<username>')
def home(username):
    return '<h1>This is the profile for %s</h1>' %username
new.run()

