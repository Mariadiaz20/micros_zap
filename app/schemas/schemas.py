# ...existing code...
from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from datetime import datetime

# Base model que activa from_attributes (equivalente a orm_mode en v1)
class CustomBaseModel(BaseModel):
    model_config = {"from_attributes": True}


# ============================================================
# USUARIO
# ============================================================

class DireccionBase(CustomBaseModel):
    direccion: str
    ciudad: str
    departamento: str
    codigo_postal: Optional[str] = None
    telefono: Optional[str] = None


class DireccionCreate(DireccionBase):
    pass


class Direccion(DireccionBase):
    id: int


class UsuarioBase(CustomBaseModel):
    nombre: str
    email: EmailStr
    telefono: Optional[str] = None


class UsuarioCreate(UsuarioBase):
    password: str


class UsuarioUpdate(CustomBaseModel):
    nombre: Optional[str] = None
    telefono: Optional[str] = None


class Usuario(UsuarioBase):
    id: int
    activo: bool
    creado: datetime
    direcciones: List[Direccion] = Field(default_factory=list)


# ============================================================
# ADMIN
# ============================================================

class AdminBase(CustomBaseModel):
    usuario: str


class AdminCreate(AdminBase):
    password: str


class Admin(AdminBase):
    id: int
    rol: str
    creado: datetime


# ============================================================
# CATEGORÍA
# ============================================================

class CategoriaBase(CustomBaseModel):
    nombre: str
    descripcion: Optional[str] = None


class CategoriaCreate(CategoriaBase):
    pass


class CategoriaUpdate(CustomBaseModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None


class Categoria(CategoriaBase):
    id: int


# ============================================================
# PRODUCTOS
# ============================================================

class ProductoBase(CustomBaseModel):
    nombre: str
    descripcion: Optional[str] = None
    precio: float
    stock: int
    imagen_url: Optional[str] = None


class ProductoCreate(ProductoBase):
    categoria_id: int


class ProductoUpdate(CustomBaseModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    precio: Optional[float] = None
    stock: Optional[int] = None
    imagen_url: Optional[str] = None
    categoria_id: Optional[int] = None


class Producto(ProductoBase):
    id: int
    categoria_id: int


# ============================================================
# PEDIDOS
# ============================================================

class PedidoProducto(CustomBaseModel):
    product_id: int
    quantity: int


class PedidoBase(CustomBaseModel):
    estado: Optional[str] = "pendiente"


class PedidoCreate(PedidoBase):
    usuario_id: int
    productos: List[PedidoProducto]


class PedidoUpdate(CustomBaseModel):
    estado: Optional[str] = None


class Pedido(CustomBaseModel):
    id: int
    usuario_id: int
    total: float
    estado: str
    creado: datetime
    productos: List[Producto] = Field(default_factory=list)
# ...existing code...