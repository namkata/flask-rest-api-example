from db import db  # Import db instance from main


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    # Define any other fields you need for the User model
    # ...

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


class Book(db.Model):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    published_date = db.Column(db.Date)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))  # Use 'users.id' for the ForeignKey

    # Define a relationship with the User model
    user = db.relationship('User', backref=db.backref('books', lazy=True))  # Use 'User' instead of 'users'

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', '{self.published_date}')"
