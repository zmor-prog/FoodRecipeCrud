from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipes.db'
db = SQLAlchemy(app)
class Recipe_Picture(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column('Created', db.DateTime, default=datetime.datetime.now)
    url = db.Column('URL', db.String())
    alt = db.Column('alt', db.String())
    recipe_id=db.Column(db.Integer)

    def __repr__(self):
        return f'''<Picture (
               URL: {self.url}
               Alt: {self.alt}
               recipe_id:{self.recipe_id}
               )'''
class Recipe_Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column('Created', db.DateTime, default=datetime.datetime.now)
    name = db.Column('Name', db.String())
    
    def __repr__(self):
        return f'''<Recipe_Ingredient (Name: {self.name}
               )'''
class Recipe_Ingredient_amount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column('Created', db.DateTime, default=datetime.datetime.now)
    name = db.Column('Amount', db.String())
    
    def __repr__(self):
        return f'''<Recipe_Ingredient_amount (Name: {self.name}
               )'''
class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column('Created', db.DateTime, default=datetime.datetime.now)
    review = db.Column('Content', db.String())
    
    def __repr__(self):
        return f'''<Reviews (Name: {self.review}
               )'''
class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column('Created', db.DateTime, default=datetime.datetime.now)
    user_id = db.Column('User', db.Integer)
    recipe_id = db.Column('Recipe', db.Integer)
    
    def __repr__(self):
        return f'''<Favorites (Name: {self.user_id}
               )'''
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column('Created', db.DateTime, default=datetime.datetime.now)
    name = db.Column('Username', db.String())
    password = db.Column('Password', db.String())
    email = db.Column('Email', db.String())
    fname = db.Column('First', db.String())
    lname = db.Column('Last', db.String())
    def __repr__(self):
        return f'''<User (Username: {self.name}
               Password: {self.password}
               Email: {self.email}
               First: {self.fname}
               Last: {self.lname}
               )'''

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column('Created', db.DateTime, default=datetime.datetime.now)
    name = db.Column('Name', db.String())
    age = db.Column('Age', db.String())
    breed = db.Column('Breed', db.String())
    color = db.Column('Color', db.String())
    size = db.Column('Size', db.String())
    weight = db.Column('Weight', db.String())
    url = db.Column('URL', db.String())
    url_tag = db.Column('Alt Tag', db.String())
    pet_type = db.Column('Pet Type', db.String())
    gender = db.Column('Gender', db.String())
    spay = db.Column('Spay', db.String())
    house_trained = db.Column('House Trained', db.String())
    description = db.Column('Description', db.Text())

    def __repr__(self):
        return f'''<Pet (Name: {self.name}
               Age: {self.age}
               Breed: {self.breed}
               Color: {self.color}
               Size: {self.size}
               Weight: {self.weight}
               URL: {self.url}
               Tag: {self.url_tag}
               Gender: {self.gender}
               Spay: {self.spay}
               House Trained: {self.house_trained}
               Description: {self.description}
               )'''