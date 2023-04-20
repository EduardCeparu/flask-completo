from repo.user_repo import *
from dao_schema.user_schema import *
from flask import request, jsonify

user_schema = UserSchema()
users_schema = UserSchema(many=True)


# lista de usuarios
def users():
    data = find_all_repo()
    return users_schema.dump(data)


# buscar por id de usuario
def find_user(id):
    return user_schema.jsonify(find_one_repo(id));


# buscar por id de username
def find_by_username(username):
    return users_schema.jsonify(find_by_username_repo(username))

#guardar usuario
def user_registry():
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']

    user_by_request = User(None, username, email, password)
    data = save_repo(user_by_request)
    return user_schema.jsonify(data)

# modificar
def update_user(id):
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']

    user_by_request = User(None, username, email, password)
    update_repo(id, user_by_request)
    data = find_one_repo(id)
    return user_schema.jsonify(data)

#eliminar

def delete_user(id):
    delete_repo(id)
    return jsonify({"message" : "Eliminado correctamente"})