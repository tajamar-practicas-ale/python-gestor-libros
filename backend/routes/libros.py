from flask import Blueprint, request, jsonify
from models.libro import LibroModel
from app import db

libros_bp = Blueprint('libros', __name__)

# Obtener todos los libros
@libros_bp.route('/api/libros/', methods=['GET'])
def get_libros():
    libros = LibroModel.query.all()
    return jsonify([{'id': libro.id, 'titulo': libro.titulo, 'autor': libro.autor, 'precio': libro.precio} for libro in libros])

# Crear un nuevo libro
@libros_bp.route('/api/libros/', methods=['POST'])
def create_libro():
    data = request.get_json()
    titulo = data.get('titulo')
    autor = data.get('autor')
    precio = data.get('precio')

    if precio < 0:
        return jsonify({"message": "El precio debe ser mayor o igual a 0"}), 400

    nuevo_libro = LibroModel(titulo=titulo, autor=autor, precio=precio)
    db.session.add(nuevo_libro)
    db.session.commit()
    return jsonify({"message": "Libro creado exitosamente", "id": nuevo_libro.id}), 201

# Obtener un libro por su id
@libros_bp.route('/api/libros/<int:id>', methods=['GET'])
def get_libro(id):
    libro = LibroModel.query.get_or_404(id)
    return jsonify({'id': libro.id, 'titulo': libro.titulo, 'autor': libro.autor, 'precio': libro.precio})

# Actualizar el precio de un libro
@libros_bp.route('/api/libros/<int:id>', methods=['PUT'])
def update_libro(id):
    data = request.get_json()
    libro = LibroModel.query.get_or_404(id)
    
    nuevo_precio = data.get('precio')
    if nuevo_precio < 0:
        return jsonify({"message": "El precio debe ser mayor o igual a 0"}), 400

    libro.precio = nuevo_precio
    db.session.commit()
    return jsonify({"message": "Libro actualizado exitosamente"})

# Eliminar un libro
@libros_bp.route('/api/libros/<int:id>', methods=['DELETE'])
def delete_libro(id):
    libro = LibroModel.query.get_or_404(id)
    db.session.delete(libro)
    db.session.commit()
    return jsonify({"message": "Libro eliminado exitosamente"})