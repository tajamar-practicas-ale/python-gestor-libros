from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
    role = db.Column(db.String(80), nullable=False)

    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

class LibroModel(db.Model):
    __tablename__ = 'libros'  # Nombre de la tabla en la base de datos

    id = db.Column(db.Integer, primary_key=True)  # Campo id como clave primaria
    titulo = db.Column(db.String(255), nullable=False)
    autor = db.Column(db.String(255), nullable=False)
    precio = db.Column(db.Float, nullable=False)

    def __init__(self, titulo, autor, precio):
        self.titulo = titulo
        self.autor = autor
        self.precio = precio
