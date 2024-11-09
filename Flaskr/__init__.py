from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuración base de datos
USER_DB = 'root'
PASS_DB = ''  # Si hay una contraseña, colócala aquí
URL_DB = 'localhost'
NAME_DB = '' # Poner el nombre de la base de datos de wordbench
FULL_URL_DB = f'mysql+pymysql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'

app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Configuración de la migración
migrate = Migrate()
migrate.init_app(app, db)
