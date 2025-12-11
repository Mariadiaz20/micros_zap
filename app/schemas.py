from typing import Optional, List
from pydantic import BaseModel
from datetime import datetime

# ---------------------------
# Usuarios
# ---------------------------
class UsuarioBase(BaseModel):
    nombre: str
    email: str
    telefono: Optional[str] = None
    activo: Optional[bool] = True

class UsuarioCreate(UsuarioBase):
    password: str

class UsuarioUpdate(BaseModel):
    nombre: Optional[str]
    email: Optional[str]
    telefono: Optional[str]
    password: Optional[str]
    activo: Optional[bool]

class UsuarioOut(UsuarioBase):
    id: int
    creado: Optional[datetime]

    # reemplazar Config.orm_mode por model_config para Pydantic v2
    model_config = {"from_attributes": True}

# ---------------------------
# Direcciones
# ---------------------------
class DireccionBase(BaseModel):
    direccion: str
    ciudad: str
    departamento: str
    codigo_postal: Optional[str] = None
    telefono: Optional[str] = None
    usuario_id: int

class DireccionCreate(DireccionBase):
    pass

class DireccionUpdate(BaseModel):
    direccion: Optional[str]
    ciudad: Optional[str]
    departamento: Optional[str]
    codigo_postal: Optional[str]
    telefono: Optional[str]
    usuario_id: Optional[int]

class DireccionOut(DireccionBase):
    id: int

    model_config = {"from_attributes": True}

# ---------------------------
# Categorias
# ---------------------------
class CategoriaBase(BaseModel):
    nombre: str
    descripcion: Optional[str] = None

class CategoriaCreate(CategoriaBase):
    pass

class CategoriaUpdate(BaseModel):
    nombre: Optional[str]
    descripcion: Optional[str]

class CategoriaOut(CategoriaBase):
    id: int

    model_config = {"from_attributes": True}

# ---------------------------
# Productos
# ---------------------------
class ProductoBase(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    precio: float
    stock: int
    imagen_url: Optional[str] = None
    categoria_id: Optional[int] = None

class ProductoCreate(ProductoBase):
    pass

class ProductoUpdate(BaseModel):
    nombre: Optional[str]
    descripcion: Optional[str]
    precio: Optional[float]
    stock: Optional[int]
    imagen_url: Optional[str]
    categoria_id: Optional[int]

class ProductoOut(ProductoBase):
    id: int

    model_config = {"from_attributes": True}

# ---------------------------
# Ordenes (Pedido)
# ---------------------------
class OrderBase(BaseModel):
    usuario_id: int
    total: float
    estado: Optional[str] = "pendiente"

class OrderCreate(OrderBase):
    pass

class OrderUpdate(BaseModel):
    usuario_id: Optional[int]
    total: Optional[float]
    estado: Optional[str]

class OrderOut(OrderBase):
    id: int

    model_config = {"from_attributes": True}

# ---------------------------
# Order items (PedidoProducto)
# ---------------------------
class OrderItemBase(BaseModel):
    pedido_id: int
    producto_id: int
    quantity: int

class OrderItemCreate(OrderItemBase):
    pass

class OrderItemUpdate(BaseModel):
    quantity: Optional[int]

class OrderItemOut(OrderItemBase):
    model_config = {"from_attributes": True}