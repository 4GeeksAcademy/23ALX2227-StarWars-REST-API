from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)       
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    favorites = db.relationship("Favorites", backref= "user")

    def __repr__(self):
        return '<User %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,                        
            "email": self.email,
            "password": self.password,            
            "is_active": self.is_active            
            # do not serialize the password, its a security breach
        }
    
class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    eye_color = db.Column(db.String(80), unique=False, nullable=False)
    hair_color = db.Column(db.String(80), unique=False, nullable=False)
    favorites = db.relationship("Favorites", backref= "character")

    def __repr__(self):
        return '<Character %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "eye_color": self.eye_color,
            "hair_color": self.hair_color
            # do not serialize the password, its a security breach
        }
    
class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    gravity = db.Column(db.String(80), unique=False, nullable=False)
    clima = db.Column(db.String(80), unique=False, nullable=False)
    poblation = db.Column(db.String(80), unique=False, nullable=False)
    rotation_period = db.Column(db.String(80), unique=False, nullable=False)
    favorites = db.relationship("Favorites", backref= "planet")

    def __repr__(self):
        return '<Planet %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gravity": self.gravity,
            "clima": self.clima,
            "poblation": self.poblation,
            "rotation_period": self.rotation_period
            # do not serialize the password, its a security breach
        }

class Films(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    created = db.Column(db.String(80), unique=False, nullable=False)
    edited = db.Column(db.String(80), unique=False, nullable=False)
    producer = db.Column(db.String(80), unique=False, nullable=False)
    title = db.Column(db.String(80), unique=False, nullable=False)
    director = db.Column(db.String(80), unique=False, nullable=False)
    favorites = db.relationship("Favorites", backref= "films")

    def __repr__(self):
        return '<Films %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "created": self.created,
            "edited": self.edited,
            "producer": self.producer,
            "title": self.title,
            "director": self.director,
            # do not serialize the password, its a security breach
        }

class Favorites(db.Model):
    id= db.Column(db.Integer, primary_key="true")
    user_id= db.Column(db.Integer, db.ForeignKey("user.id"))
    planet_id= db.Column(db.Integer, db.ForeignKey("planet.id"), nullable=False)
    character_id= db.Column(db.Integer, db.ForeignKey("character.id"), nullable=False)
    films_id= db.Column(db.Integer, db.ForeignKey("films.id"), nullable=False)

    def __repr__(self):
        return '<Favorites %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet_id": self.planet_id,
            "character_id": self.character_id,
            "films_id": self.films_id            
            # do not serialize the password, its a security breach
        }