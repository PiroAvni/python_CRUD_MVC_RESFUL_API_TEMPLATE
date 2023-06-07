# app.py
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres+psycopg2://yabqzbvt:yefwOe3qoKVaVup0eNmlNCPecRbTP8l-@lucky.db.elephantsql.com/yabqzbvt'

db = SQLAlchemy(app)

# Import and register the book_routes Blueprint
from routes.book_routes import book_routes
app.register_blueprint(book_routes)

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == '__main__':
    app.run(debug=True, port=8000)
