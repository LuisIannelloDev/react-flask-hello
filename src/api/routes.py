from flask import Blueprint, request, jsonify
from api.models import db, User, Planeta, Personaje, Favorito

api = Blueprint('api', __name__)

# Endpoints para listar registros de people y planets
@api.route('/people', methods=['GET'])
def listar_personajes():
    personajes = Personaje.query.all()
    return jsonify([personaje.serialize() for personaje in personajes])

@api.route('/people/<int:people_id>', methods=['GET'])
def obtener_personaje(people_id):
    personaje = Personaje.query.get_or_404(people_id)
    return jsonify(personaje.serialize())

@api.route('/planets', methods=['GET'])
def listar_planetas():
    planetas = Planeta.query.all()
    return jsonify([planeta.serialize() for planeta in planetas])

@api.route('/planets/<int:planet_id>', methods=['GET'])
def obtener_planeta(planet_id):
    planeta = Planeta.query.get_or_404(planet_id)
    return jsonify(planeta.serialize())

# Endpoints para usuarios
@api.route('/users', methods=['GET'])
def listar_usuarios():
    usuarios = User.query.all()
    return jsonify([usuario.serialize() for usuario in usuarios])

@api.route('/users/favorites', methods=['GET'])
def listar_favoritos_usuario_actual():
    user_id = 1  # Esto debería obtenerse del contexto de la sesión o autenticación
    favoritos = Favorito.query.filter_by(user_id=user_id).all()
    return jsonify([favorito.serialize() for favorito in favoritos])

# Endpoints para agregar y eliminar favoritos
@api.route('/favorite/planet/<int:planet_id>', methods=['POST'])
def agregar_favorito_planeta(planet_id):
    user_id = 1  # Esto debería obtenerse del contexto de la sesión o autenticación
    favorito = Favorito(user_id=user_id, planeta_id=planet_id)
    db.session.add(favorito)
    db.session.commit()
    return jsonify({"message": "Planeta favorito agregado exitosamente"}), 201

@api.route('/favorite/people/<int:people_id>', methods=['POST'])
def agregar_favorito_personaje(people_id):
    user_id = 1  # Esto debería obtenerse del contexto de la sesión o autenticación
    favorito = Favorito(user_id=user_id, personaje_id=people_id)
    db.session.add(favorito)
    db.session.commit()
    return jsonify({"message": "Personaje favorito agregado exitosamente"}), 201

@api.route('/favorite/planet/<int:planet_id>', methods=['DELETE'])
def eliminar_favorito_planeta(planet_id):
    user_id = 1  # Esto debería obtenerse del contexto de la sesión o autenticación
    favorito = Favorito.query.filter_by(user_id=user_id, planeta_id=planet_id).first_or_404()
    db.session.delete(favorito)
    db.session.commit()
    return jsonify({"message": "Planeta favorito eliminado exitosamente"})

@api.route('/favorite/people/<int:people_id>', methods=['DELETE'])
def eliminar_favorito_personaje(people_id):
    user_id = 1  # Esto debería obtenerse del contexto de la sesión o autenticación
    favorito = Favorito.query.filter_by(user_id=user_id, personaje_id=people_id).first_or_404()
    db.session.delete(favorito)
    db.session.commit()
    return jsonify({"message": "Personaje favorito eliminado exitosamente"})

# Endpoints para agregar, modificar y eliminar planetas y personajes
@api.route('/planets', methods=['POST'])
def agregar_planeta():
    data = request.get_json()
    planeta = Planeta(
        nombre=data.get('nombre'),
        descripcion=data.get('descripcion')
    )
    db.session.add(planeta)
    db.session.commit()
    return jsonify(planeta.serialize()), 201

@api.route('/planets/<int:planet_id>', methods=['PUT'])
def modificar_planeta(planet_id):
    planeta = Planeta.query.get_or_404(planet_id)
    data = request.get_json()
    planeta.nombre = data.get('nombre', planeta.nombre)
    planeta.descripcion = data.get('descripcion', planeta.descripcion)
    db.session.commit()
    return jsonify(planeta.serialize())

@api.route('/planets/<int:planet_id>', methods=['DELETE'])
def eliminar_planeta(planet_id):
    planeta = Planeta.query.get_or_404(planet_id)
    db.session.delete(planeta)
    db.session.commit()
    return jsonify({"message": "Planeta eliminado exitosamente"})

@api.route('/people', methods=['POST'])
def agregar_personaje():
    data = request.get_json()
    personaje = Personaje(
        nombre=data.get('nombre'),
        descripcion=data.get('descripcion')
    )
    db.session.add(personaje)
    db.session.commit()
    return jsonify(personaje.serialize()), 201

@api.route('/people/<int:people_id>', methods=['PUT'])
def modificar_personaje(people_id):
    personaje = Personaje.query.get_or_404(people_id)
    data = request.get_json()
    personaje.nombre = data.get('nombre', personaje.nombre)
    personaje.descripcion = data.get('descripcion', personaje.descripcion)
    db.session.commit()
    return jsonify(personaje.serialize())

@api.route('/people/<int:people_id>', methods=['DELETE'])
def eliminar_personaje(people_id):
    personaje = Personaje.query.get_or_404(people_id)
    db.session.delete(personaje)
    db.session.commit()
    return jsonify({"message": "Personaje eliminado exitosamente"})
