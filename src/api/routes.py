from flask import Blueprint, request, jsonify
from api.models import db, Planeta, Personaje, Favorito

api = Blueprint('api', __name__)

@api.route('/planetas', methods=['GET'])
def listar_planetas():
    planetas = Planeta.query.all()
    return jsonify([planeta.nombre for planeta in planetas])

@api.route('/personajes', methods=['GET'])
def listar_personajes():
    personajes = Personaje.query.all()
    return jsonify([personaje.nombre for personaje in personajes])

@api.route('/favoritos', methods=['POST'])
def agregar_favorito():
    data = request.json
    favorito = Favorito(user_id=data['user_id'], planeta_id=data.get('planeta_id'), personaje_id=data.get('personaje_id'))
    db.session.add(favorito)
    db.session.commit()
    return jsonify({"message": "Favorito agregado exitosamente"}), 201

@api.route('/favoritos/<int:favorito_id>', methods=['DELETE'])
def eliminar_favorito(favorito_id):
    favorito = Favorito.query.get_or_404(favorito_id)
    db.session.delete(favorito)
    db.session.commit()
    return jsonify({"message": "Favorito eliminado exitosamente"})
