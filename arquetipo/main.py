from flask import Flask
from envs.dev.dev_env import config, get_database_config
from database.db import init_app
from users.routes.user_route import users_routes
from flask_cors import CORS

app = Flask(__name__)

# cors config
app.config['JSON_AS_ASCII'] = False
CORS(app)

#db config
user = get_database_config().get('MYSQL_USER')
host = get_database_config().get('MYSQL_HOST')
password = get_database_config().get('MYSQL_PASSWORD')
database = get_database_config().get('DATABASE_NAME')
sql_track_modifications = get_database_config().get('SQLALCHEMY_TRACK_MODIFICATIONS')

app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://'+user+'@'+host+'/'+database
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = sql_track_modifications

init_app(app)

#blueprints
app.register_blueprint(users_routes)

print("TESTING")
#MAIN
if __name__ == "__main__":
    app.config.from_object(config['dev'])
    app.run()
