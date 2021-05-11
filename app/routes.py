import json
from app import app, api
from flask import (
    render_template,
    url_for,
    redirect,
    request,
    json,
    Response,
    flash,
    session,
    jsonify
)
from flask_restx import Resource
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dbsetup import (
    Base,
    Client,
    Product,
    Category,
    Outcome,
    Income,
    engine )

Base.metadata.bind = engine

DBSession = sessionmaker(bind = engine)
session = DBSession()
################################################################################
# Rutas de la API

@api.route('/api/cat/', '/api/cat')
class GetAndPostCategory(Resource):

    #GET
    def get(self):
        '''Devuelve todas las categorias a través del método GET'''
        categorias = session.query(Category).all()
        cat_dict = {}
        cat_list = []
        for c in categorias:
            cat_dict['idCat'] = c.idCat
            cat_dict['categoria'] = c.categoria
            cat_dict['fecha'] = c.fecha
            cat_list.append(cat_dict)
            cat_dict = {}

        return jsonify(cat_list)

@api.route('/api/product/', '/api/product')
class GetAndPostProduct(Resource):

    #GET
    def get(self):
        '''Devuelve todos los productos a través del método GET'''
        productos = session.query(Product).all()
        cat_dict = {}
        cat_list = []
        for p in productos:
            cat_dict['id'] = p.id
            cat_dict['id_categoria'] = p.id_categoria
            cat_dict['codigo'] = p.codigo
            cat_dict['descripcion'] = p.descripcion
            cat_dict['imagen'] = p.imagen
            cat_dict['stock'] = p.stock
            cat_dict['cantidad'] = p.cantidad
            cat_dict['precio_compra'] = p.precio_compra
            cat_dict['precio_venta'] = p.precio_venta
            cat_dict['ventas'] = p.ventas
            cat_dict['fecha'] = p.fecha
            cat_list.append(cat_dict)
            cat_dict = {}

        return jsonify(cat_list)


@api.route('/api/client/', '/api/client')
class GetAndPostClient(Resource):

    #GET
    def get(self):
        '''Devuelve todos los clientes a través del método GET'''
        clientes = session.query(Client).all()
        cat_dict = {}
        cat_list = []
        for c in clientes:
            cat_dict['id'] = c.id
            cat_dict['nombre'] = c.nombre
            cat_dict['documento'] = c.documento
            cat_dict['informacion'] = {
                'email' : c.email,
                'telefono' : c.telefono,
                'direccion' : c.direccion,
                'ultima_compra' : c.ultima_compra
                }
            cat_dict['fecha_nacimiento'] = c.fecha_nacimiento
            cat_dict['compras'] = c.compras
            cat_dict['fecha'] = c.fecha
            cat_list.append(cat_dict)
            cat_dict = {}

        return jsonify(cat_list)


@api.route('/api/outcome/', '/api/outcome')
class GetAndPostOutcome(Resource):

    #GET
    def get(self):
        '''Devuelve todas las salidas a través del método GET'''
        salidas = session.query(Outcome).all()
        cat_dict = {}
        cat_list = []
        for s in salidas:
            cat_dict['id'] = s.id_e
            cat_dict['id_cliente'] = s.id_cliente
            cat_dict['codigo'] = s.codigo
            cat_dict['productos'] = json.loads(s.productos)
            cat_dict['neto'] = s.neto
            cat_dict['total'] = s.total
            cat_dict['check-in'] = s.checkIn
            cat_dict['metodo_pago'] = s.metodo_pago
            cat_dict['fecha'] = s.fecha_e
            cat_list.append(cat_dict)
            cat_dict = {}

        return jsonify(cat_list)


@api.route('/api/income/', '/api/income')
class GetAndPostIncome(Resource):

    #GET
    def get(self):
        '''Devuelve todas las entradas a través del método GET'''
        entradas = session.query(Income).all()
        cat_dict = {}
        cat_list = []
        for e in entradas:
            cat_dict['id'] = e.id_e
            cat_dict['id_cliente'] = e.id_cliente
            cat_dict['codigo'] = e.codigo
            cat_dict['productos'] = json.loads(e.productos)
            cat_dict['neto'] = e.neto
            cat_dict['total'] = e.total
            cat_dict['fecha'] = e.fecha_e
            cat_list.append(cat_dict)
            cat_dict = {}

        return jsonify(cat_list)
################################################################################



