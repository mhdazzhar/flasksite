from flask import Flask,render_template
app=Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')



@app.route('/profile/<username>')
def profile(username):
    return render_template('profile.html',username=username,isACTIVE=True)

@app.route('/books')
def books():
    books=[ {'name': 'Atomic Habits', 'author': 'James Clear', 'cover': 'https://upload.wikimedia.org/wikipedia/commons/0/06/Atomic_habits.jpg'},
        {'name': 'Aadujeevitham', 'author': 'Benyamin', 'cover': 'https://assets-in.bmscdn.com/iedb/movies/images/mobile/thumbnail/xlarge/aadujeevitham-et00038685-1664540041.jpg'},
        {'name': 'Harry Potter and the Philosophers Stone', 'author': 'J.K Rowling', 'cover': 'https://res.cloudinary.com/bloomsbury-atlas/image/upload/w_568,c_scale/jackets/9781408855652.jpg'}]
    return render_template('books.html',books=books)


app.run(debug=True)