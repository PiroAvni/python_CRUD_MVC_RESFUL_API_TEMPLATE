class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    author = db.Column(db.String(100))

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author
        }


if __name__ == '__main__':
    app.run(debug=True)