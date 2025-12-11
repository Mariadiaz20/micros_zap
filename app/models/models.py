from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base
from datetime import datetime


# ============================================================
# USUARIO
# ============================================================

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    telefono = Column(String, nullable=True)
    password = Column(String)
    activo = Column(Boolean, default=True)
    creado = Column(DateTime, default=datetime.utcnow)

    direcciones = relationship("Direccion", back_populates="usuario")


class Direccion(Base):
    __tablename__ = "direcciones"

    id = Column(Integer, primary_key=True, index=True)
    direccion = Column(String)
    ciudad = Column(String)
    departamento = Column(String)
    codigo_postal = Column(String, nullable=True)
    telefono = Column(String, nullable=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))

    usuario = relationship("Usuario", back_populates="direcciones")


# ============================================================
# ADMIN
# ============================================================

class Admin(Base):
    __tablename__ = "admins"

    id = Column(Integer, primary_key=True, index=True)
    usuario = Column(String, index=True)
    password = Column(String)
    rol = Column(String)
    creado = Column(DateTime, default=datetime.utcnow)


# ============================================================
# CATEGORÍA
# ============================================================

class Categoria(Base):
    __tablename__ = "categorias"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    descripcion = Column(String, nullable=True)


# ============================================================
# PRODUCTOS
# ============================================================

class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    descripcion = Column(String, nullable=True)
    precio = Column(Float)
    stock = Column(Integer)
    imagen_url = Column(String, nullable=True)
    categoria_id = Column(Integer, ForeignKey("categorias.id"))


# ============================================================
# PEDIDOS
# ============================================================

class Pedido(Base):
    __tablename__ = "pedidos"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    total = Column(Float)
    estado = Column(String, default="pendiente")
    creado = Column(DateTime, default=datetime.utcnow)

    productos = relationship("Producto", secondary="pedido_productos")


class PedidoProducto(Base):
    __tablename__ = "pedido_productos"

    pedido_id = Column(Integer, ForeignKey("pedidos.id"), primary_key=True)
    producto_id = Column(Integer, ForeignKey("productos.id"), primary_key=True)
    quantity = Column(Integer)