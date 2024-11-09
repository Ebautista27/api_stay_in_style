from marshmallow import fields
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()

# Tablas y modelos

class Rol(db.Model):
    __tablename__ = 'rol'
    ID_rol = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(5))

class Usuario(db.Model):
    __tablename__ = 'usuario'
    ID_usuario = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(50))
    Num_cel = db.Column(db.String(11))
    email = db.Column(db.String(50))
    direccion = db.Column(db.String(45))
    password = db.Column(db.String(40))
    ID_rol = db.Column(db.Integer, db.ForeignKey('rol.ID_rol'))

class Carrito(db.Model):
    __tablename__ = 'carrito'
    ID_carrito = db.Column(db.Integer, primary_key=True)
    total = db.Column(db.String(5))

class Carrito_Producto(db.Model):
    __tablename__ = 'carrito_producto'
    ID_carrito = db.Column(db.Integer, primary_key=True)
    ID_producto = db.Column(db.Integer)

class Factura(db.Model):
    __tablename__ = 'factura'
    ID_factura = db.Column(db.Integer, primary_key=True)
    ID_usuario = db.Column(db.Integer, db.ForeignKey('usuario.ID_usuario'))

class Metodo_pago(db.Model):
    __tablename__ = 'metodo_pago'
    ID_metodo = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(10))

class Detalle_factura(db.Model):
    __tablename__ = 'detalle_factura'
    ID_factura = db.Column(db.Integer, primary_key=True)
    ID_producto = db.Column(db.Integer)
    Cantidad = db.Column(db.Integer)

class Producto(db.Model):
    __tablename__ = 'producto'
    ID_producto = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(15))
    Talla = db.Column(db.String(20))
    Categoria = db.Column(db.String(18))
    Estado = db.Column(db.String(10))
    Precio = db.Column(db.Numeric(10, 2))

class Reseña(db.Model):
    __tablename__ = 'reseña'
    ID_reseña = db.Column(db.Integer, primary_key=True)
    Comentario = db.Column(db.String(150))
    Calificacion = db.Column(db.Integer)
    ID_producto = db.Column(db.Integer, db.ForeignKey('producto.ID_producto'))

# Esquemas para la serialización

class RolSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Rol
        include_relationships = True
        load_instance = True

class UsuarioSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Usuario
        include_relationships = True
        load_instance = True

class CarritoSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Carrito
        include_relationships = True
        load_instance = True

class Carrito_ProductoSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Carrito_Producto
        include_relationships = True
        load_instance = True

class FacturaSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Factura
        include_relationships = True
        load_instance = True

class Metodo_pagoSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Metodo_pago
        include_relationships = True
        load_instance = True

class Detalle_facturaSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Detalle_factura
        include_relationships = True
        load_instance = True

class ProductoSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Producto
        include_relationships = True
        load_instance = True

class ReseñaSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Reseña
        include_relationships = True
        load_instance = True
