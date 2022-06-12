
from flask import Flask,jsonify
from flask import request


app = Flask(__name__)

@app.route("/")
def hello_world():
    return '{"mensaje":"Lista de Mercado"}'

#Funcion de productos de mercado (Ruta)
productos=[]
#Lista de productos en formato json
@app.route("/productos",methods=['GET'])
def api():
    return jsonify(productos) 

@app.route("/add/<nombre>", methods=['GET'])
def add(nombre):
    producto=nombre.split(":") #separar por : para el nombre del producto y el tipo 
    producto_a_insertar={"nombre":producto[0],"tipo":producto[1]} #(Se puede agregar mas elementos)
    productos.append(producto_a_insertar) #Insertar nuevo elemento a la lista
    return jsonify({"Mensaje":"Se ingreso correctamente el producto"}) 

@app.route("/editar/<nombre>", methods=['PUT']) # edita los productos mediante un json 
def editar(nombre):
    try:
        cambioProducto = [productos for productos in productos if productos['nombre'] == nombre]
        if (len(cambioProducto) > 0):
            cambioProducto[0]['nombre'] = request.json['nombre']
           # cambioProducto[0]['cantidad'] = request.json['cantidad']
           # cambioProducto[0]['precio'] = request.json['precio'] 
            return jsonify({
                "mensaje" : "Exito editando el producto",
                "producto" : cambioProducto[0]
            })
        return 'producto NO encontrado'
    except:
        return 'Verifica la informacion ha ocurrido un error'


@app.route("/eliminar/<nombre>", methods=['DELETE']) # selecciona el nombre del producto 
def eliminar(nombre):                                       # que desea eliminar indicando el nombre
    try:
        eliProducto = [producto for producto in productos if producto['nombre'] == nombre]
        if len(eliProducto) > 0:
            productos.remove(eliProducto[0])
            return jsonify({
                "mensaje": "Producto Eliminado",
                "productos": productos
            })
        return "Producto NO encontrado"
    except:
        return 'Verifica la informacion ha ocurrido un error'
   
            
