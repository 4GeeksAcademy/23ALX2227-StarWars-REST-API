"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Character, Planet, Films, Favorites
from json 
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def get_all_users():
    users = User.query.all()
    if len(users) < 1:
        return jsonify({"msg": "not found"}), 404
    serialized_users = [x.serialize() for x in users]
    return serialized_users, 200

@app.route('/user/<int:user_id>', methods=['GET'])
def get_one_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        return jsonify({"msg": f"user with id {user_id} not found"}), 404
    serialized_user = user.serialize()
    return serialized_user, 200

@app.route('/user', methods=['POST'])
def create_one_user():
    body = json.loads(request.data)
    new_user = User(
        name = body["name"],
        email = body["email"],
        password = body["password"],
        is_active = True
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"msg": "user created succesfull", "user_added": new_user }), 200


@app.route('/character', methods=['GET'])
def get_all_character():
    character = Character.query.all()
    if len(character) < 1:
        return jsonify({"msg": "not found"}), 404
    serialized_character = list(map(lambda x: x.serialize(), character))
    return serialized_character, 200

@app.route('/character/<int:character_id>', methods=['GET'])
def get_one_character(character_id):
    character = Character.query.get(character_id)
    if character is None:
        return jsonify({"msg": f"Character with id {character_id} not found"}), 404
    serialized_character = character.serialize()
    return serialized_character, 200

@app.route('/planet', methods=['GET'])
def get_all_planet():
    planet = Planet.query.all()
    if len(planet) < 1:
        return jsonify({"msg": "not found"}), 404
    serialized_planet = list(map(lambda x: x.serialize(), planet))    
    return serialized_planet, 200

@app.route('/planet/<int:planet_id>', methods=['GET'])
def get_one_planet(planet_id):
    planet = Planet.query.get(planet_id)
    if planet is None:
        return jsonify({"msg": f"Planet with id {planet_id} not found"}), 404
    serialized_planet = planet.serialize()
    return serialized_planet, 200

@app.route('/films', methods=['GET'])
def get_all_films():
    films = Films.query.all()
    if len(films) < 1:
        return jsonify({"msg": "not found"}), 404
    serialized_films = list(map(lambda x: x.serialize(), films))
    return serialized_films, 200

@app.route('/films/<int:films_id>', methods=['GET'])
def get_one_films(films_id):
    films = Films.query.get(films_id)
    if films is None:
        return jsonify({"msg": f"Films with id {films_id} not found"}), 404
    serialized_films = films.serialize()
    return serialized_films, 200

@app.route('/user/<int:user_id>/favorites', methods=['GET'])
def get_favorites(user_id):
    favorites = Favorites.query.filter_by(user_id = user_id).all()
    if len(favorites) < 1:
        return jsonify({"msg": "not found"}), 404
    serialized_favorites = list(map(lambda x: x.serialize(), favorites))
    return serialized_favorites, 200

@app.route('/user', methods=['POST'])
def add_favorites():
    body = request.json
    new_favorites = Favorites(
        user_id = body["user_id"],
        planet_id = body["planet_id"],
        character_id = body["character_id"],
        films_id = body["film_id"]
    )
    if new_favorites.planet_id is None and new_favorites.character_id is None and new_favorites.films_id is None:
        return jsonify({"msg": "Sos un boludo"}), 400
    db.session.add(new_favorites)
    db.session.commit()
    return jsonify({"msg": "Sos un capo", "add_favorite": new_favorites}), 200


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
