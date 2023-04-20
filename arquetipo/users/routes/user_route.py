from flask import Blueprint
from users.controller.user_controller import *

users_routes = Blueprint('users_routes', __name__, url_prefix="/api")


@users_routes.get("/users")
def users_list():
    return users()


@users_routes.get("/user/<int:id>")
def user_by_id(id):
    return find_user(id)


# buscar usuario por username
@users_routes.get("/by-username/<string:username>")
def users_by_username(username):
    return find_by_username_repo(username)


# guardar usuario
@users_routes.post("/save")
def save():
    return user_registry()


# modificar usuario
@users_routes.put("/update/<int:id>")
def update(id):
    return update_user(id)

# Eliminar usuario
@users_routes.delete("/delete/<int:id>")
def delete(id):
    delete_user(id)
    return jsonify({"message": "Eliminado correctamente"})