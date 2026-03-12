from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Favorite(db.Model):
    # todos los valores de nuestra tabla de favoritos
    id = db.Column(db.Integer, primary_key=True) # la columna de identidad (unica)
    api_id = db.Column(db.Integer, unique=True) # ID interno, no se repite
    name = db.Column(db.String(100)) # texto corto
    image = db.Column(db.String(255)) # url o ubicacion de la imagen