from flask import Blueprint, request, jsonify
from models import db, Usuario  # Importa db y Usuario desde models.py

# Definir el Blueprint para la autenticación
auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login/', methods=['POST'])
def login_usuario():
    # Obtener los datos del cuerpo de la solicitud (JSON)
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Buscar al usuario en la base de datos
    usuario_db = Usuario.query.filter_by(username=username).first()

    if usuario_db and usuario_db.password == password:
        return jsonify({"token": "fake-jwt"}), 200
    else:
        return jsonify({"message": "Credenciales incorrectas"}), 401
