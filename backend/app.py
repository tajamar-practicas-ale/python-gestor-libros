from flask import Flask
from flask_cors import CORS
from routes.auth import auth_bp  # Importamos el Blueprint para la autenticación
from models import db, Usuario  # Importamos db y Usuario desde models.py

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
    usuarios = Usuario.query.all()
    return '<br>'.join([f'Usuario: {u.username}, {u.password}, {u.role}' for u in usuarios])

# Registra el Blueprint de autenticación
app.register_blueprint(auth_bp, url_prefix='/api')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Crear las tablas en la base de datos si no existen
    app.run('0.0.0.0', debug=True)
