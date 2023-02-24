from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)

#with app.app_context():

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Guide(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=False)
    content = db.Column(db.String(144), unique=False)

    def __init__(self, title, content):
        self.title = title
        self.content = content


class GuideSchema(ma.Schema):
    class Meta:
        fields = ('title', 'content')


guide_schema = GuideSchema()
guides_schema = GuideSchema(many=True)

# endpoint para crear una nueva guia
@app.route('/guide', methods=['POST'])
def add_guide():
    title=request.json['title'] #añadimos al ppio || las librerias request y jsonfy
    content=request.json['content']
    new_guide=Guide(title,content) #class Guide
    
    db.session.add(new_guide) #nos comunicamos con la BD, para añadir la guia
    db.session.commit() #método SQLAlchemy: guarda los nuevos datos
    #buena práctica: que nos devuelva la guia creada, para comprobar que está ok
    guide=Guide.query.get(new_guide.id)
    return guide_schema.jsonify(guide)

#endpoint para consultar todas las guias
@app.route('/guides', methods=['GET'])
def get_guides():
    all_guides=Guide.query.all() #consulta
    result=guides_schema.dump(all_guides)
    return jsonify(result)

#endpoint para consultar una sola guia
@app.route('/guide/<id>', methods=['GET'])
def get_guide(id):
    guide=Guide.query.get(id)
    return guide_schema.jsonify(guide)

#endpoint para actualizar una guia
@app.route('/guide/<id>', methods=['PUT'])
def get_query(id):
    guide=Guide.query.get(id)
    title=request.json['title']
    content=request.json['content']

    guide.title=title  #sobreescribimos los valores del titulo y contenido
    guide.content=content

    db.session.commit()
    return guide_schema.jsonify(guide)

#endpoint para borrar una guia
@app.route('/guide/<id>', methods=['DELETE'])
def guide_delete(id):
    guide=Guide.query.get(id)
    db.session.delete(guide)
    db.session.commit()
    #return guide_delete.jsonify(guide)
    return 'Guide was succesuly deleted'


if __name__ == '__main__':
    app.run(debug=True)

