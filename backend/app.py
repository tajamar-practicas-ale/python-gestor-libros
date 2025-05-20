from flask import Flask
from flask_cors import CORS
from routes.auth import auth_bp  # Importamos el Blueprint para la autenticación
from routes.libros import libros_bp
from models import db, Usuario,  LibroModel  # Importamos db, Usuario y LibroModel desde models.py

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})  # Configuración CORS
# CORS(app, resources={r"/api/*": {"origins": "*"}}) 

# Configuración de la base de datos SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mi_basedatos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa db con la aplicación
db.init_app(app)

@app.route('/api/login', methods=['POST', 'GET'])
def index():
    if not db.session.query(Usuario).first():
        nuevo_usuario = Usuario(username='Juan', password='1234', role='usuario')
        db.session.add(nuevo_usuario)
        db.session.commit()

    if not db.session.query(LibroModel).first():
        # Crear libros de ejemplo
        libros = [
            LibroModel(titulo="Cien años de soledad", autor="Gabriel García Márquez", precio=19.99),
            LibroModel(titulo="1984", autor="George Orwell", precio=15.99),
            LibroModel(titulo="El principito", autor="Antoine de Saint-Exupéry", precio=9.99)
        ]
        db.session.add_all(libros)
        db.session.commit()

    usuarios = Usuario.query.all()
    return '<br>'.join([f'Usuario: {u.username}, {u.password}, {u.role}' for u in usuarios])

# Registra el Blueprint de autenticación
app.register_blueprint(auth_bp, url_prefix='/api')
app.register_blueprint(libros_bp, url_prefix='/api')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Crear las tablas en la base de datos si no existen
        print("Tablas creadas o ya existen.")
        
        # Llamar a la función para agregar libros si no existen
        if not db.session.query(LibroModel).first():
            # Crear libros de ejemplo
            libros_iniciales = [
                LibroModel(titulo="Cien años de soledad", autor="Gabriel García Márquez", precio=19.99),
                LibroModel(titulo="1984", autor="George Orwell", precio=15.99),
                LibroModel(titulo="El principito", autor="Antoine de Saint-Exupéry", precio=9.99)
            ]
            db.session.add_all(libros_iniciales)
            print("Libros creados")
            db.session.commit()
    
    app.run('0.0.0.0', debug=True)
