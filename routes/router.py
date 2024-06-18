from flask import Blueprint, request, redirect, render_template, url_for, jsonify
from controls.usuarioController import UsuarioController
from controls.comandoController import ComandoController
from controls.tda.linked.linkedList import LinkedList

router = Blueprint("router", __name__)
control = UsuarioController()
comandoControl = ComandoController()


@router.route("/", methods=["GET"])
def index():
    lista = control._lista()
    data = [usuario.serializable for usuario in lista]
    return render_template("index.html", lista=data)


@router.route("/guardar", methods=["POST", "GET"])
def guardar():
    if request.method == "POST":
        data = request.form
        control._usuario._nombre = data["nombre"]
        control._usuario._apellido = data["apellido"]
        control._usuario._telefono = data["telefono"]
        control.save
        control._usuario = None
        return redirect(url_for("router.index"))
    return render_template("guardar.html")


@router.route("/guardarComandos/<int:id>", methods=["POST", "GET"])
def guardarComandos(id):
    lista = LinkedList()
    for comando in comandoControl._lista():
        if comando._id_usuario == id:
            lista.add(comando.serializable, lista._length)
    print(lista)
    if request.method == "POST":
        data = request.form
        comandoControl._comando._id_usuario = id
        comandoControl._comando._fecha = data["fecha"]
        comandoControl._comando._contenido = data["contenido"]
        print(comandoControl._comando._fecha)
        print(comandoControl._comando._contenido)
        comandoControl.save
        comandoControl._comando = None
        return redirect(url_for("router.guardarComandos", id=id))
    return render_template("comandos.html", lista=lista, id=id)

@router.route("/redireccionar", methods=["GET"])
def redireccionar():
    return redirect(url_for("router.guardar"))

@router.route("/ordenarUsuarios", methods=["POST"])
def ordenarUsuarios():
    sortOrder = request.json.get('sortOrder')
    sortField = request.json.get('sortField')
    sortMethod = request.json.get('sortMethod')
    asc = (sortOrder == "asc")
    lista = control._lista()
    if sortMethod == "quickSort":
        lista.quick("_" +  sortField, asc = asc)
    elif sortMethod == "mergeSort":
        lista.merge("_" + sortField, asc = asc)
    elif sortMethod == "shellSort":
        lista.shell("_" + sortField, asc = asc)
    data = [usuario.serializable for usuario in lista]
    print(data)
    return jsonify(data)

@router.route("/buscarUsuarios", methods=["POST"])
def buscarUsuarios():
    searchField = request.json.get('searchField')
    searchAttr = request.json.get('searchAttr')
    lista = control._lista()
    if searchAttr == "telefono":
        X = lista.busquedaBinaria("_" + searchAttr, searchField)
        lista2 = LinkedList()
        lista2.add(X, 0)
        data = [usuario.serializable for usuario in lista2]
        return jsonify(data)
    else:
        lista = lista.linealBinaria("_" + searchAttr, searchField)
        print(lista)
        data = [usuario.serializable for usuario in lista]
        return jsonify(data)




