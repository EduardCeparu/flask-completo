from flask import Flask,jsonify

app = Flask(__name__)

@app.get('/home')

def home():
    return jsonify({"message" : "mi texto"})

@app.post('/save')
def save():
    return jsonify({'message': 'Guardando...'})

@app.put('/put')
def modify():
    return jsonify({'message': 'Modificando...'})

@app.delete('/delete')
def delete():
    return jsonify({'message': 'Eliminando...'})


if __name__ == '__main__':
    app.run(debug=True)

