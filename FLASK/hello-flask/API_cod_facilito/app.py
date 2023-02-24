from flask import Flask
from flask import jsonify

def create_app(environment):
    app=Flask(__name__)
    return app

app=create_app()

#definimos los endpoints
@app.route('/users', methods=['GET'])
def get_users():
    response={'message':'success'}
    return jsonify (response)

@app.route('/users/<id>', methods=['GET'])
def get_user():
    response={'message':'success'}
    return jsonify (response)

@app.route('/users', methods=['POST'])
def create_user():
    response={'message':'success'}
    return jsonify (response)

@app.route('/users/<id>', methods=['PUT'])
def update_user():
    response={'message':'success'}
    return jsonify (response)

@app.route('/users/<id>', methods=['DELETE'])
def delete_user():
    response={'message':'success'}
    return jsonify (response)

if __name__=='__main__':
    app.run(debug=True)