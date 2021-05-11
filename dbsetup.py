import sys, datetime

from sqlalchemy import Column, ForeignKey, Integer, String, Date, Boolean, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.sql.sqltypes import Text



Base = declarative_base()

def _get_date():
    return datetime.datetime.now()


class Category(Base):
    __tablename__ = 'categorias'
    idCat = Column(Integer, primary_key = True)
    categoria = Column(String(80), nullable = False)
    fecha = Column(Date, default=_get_date)


class Product(Base):
    __tablename__ = 'productos'
    id = Column(Integer, primary_key = True)
    id_categoria = Column(Integer, ForeignKey('categorias.idCat'))
    codigo = Column(String(250))
    descripcion = Column(String(80), nullable = False)
    imagen = Column(String(250))
    stock = Column(Integer)
    cantidad = Column(Integer)
    precio_compra = Column(Integer)
    precio_venta = Column(Integer)
    ventas = Column(Integer)
    fecha = Column(Date, default=_get_date)
    categoria = relationship(Category)


class Client(Base):
    __tablename__ = 'clientes'
    id = Column(Integer, primary_key = True)
    nombre = Column(String(80), nullable = False)
    documento = Column(Integer, nullable = False)
    email = Column(String(50))
    telefono = Column(String(15))
    direccion = Column(String(250))
    fecha_nacimiento = Column(Date, default=_get_date)
    compras = Column(Integer)
    ultima_compra = Column(Date, default=_get_date)
    fecha = Column(Date, default=_get_date)


class Outcome(Base):
    __tablename__ = 'ventas'
    id_e = Column(Integer, primary_key = True)
    codigo = Column(Integer)
    id_cliente = Column(Integer, ForeignKey('clientes.documento'))
    id_vendedor = Column(Integer)
    productos = Column(Text())
    checkIn = Column(Boolean)
    neto = Column(Integer)
    total = Column(Integer)
    metodo_pago = Column(Integer)
    fecha_e = Column(Date, default=_get_date)
    cliente = relationship(Client)


class Income(Base):
    __tablename__ = 'entradas'
    id_e = Column(Integer, primary_key = True)
    codigo = Column(Integer, ForeignKey('ventas.codigo'))
    id_cliente = Column(Integer, ForeignKey('clientes.documento'))
    productos = Column(String(1000))
    neto = Column(Integer)
    total = Column(Integer)
    fecha_e = Column(Date, default=_get_date)
    cliente = relationship(Client)
    salida = relationship(Outcome)


engine = create_engine('mysql+pymysql://connection-strings')
Base.metadata.create_all(engine)