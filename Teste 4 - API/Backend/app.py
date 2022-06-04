from flask import Flask, jsonify, request as requestflask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from requests import request

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/teste_4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Relacao(db.Model):
    __tablename__ = 'relacao_ans'
    registro_ans = db.Column(db.Integer, primary_key = True )
    cnpj = db.Column(db.String, nullable=False)
    razao_social = db.Column(db.String, nullable=False)
    nome_fantasia = db.Column(db.String, nullable=False)
    modalidade = db.Column(db.String, nullable=False)
    logradouro = db.Column(db.String, nullable=False)
    numero = db.Column(db.String, nullable=False)
    complemento = db.Column(db.String, nullable=False)
    bairro = db.Column(db.String, nullable=False)
    cidade = db.Column(db.String, nullable=False)
    uf = db.Column(db.String, nullable=False)
    cep = db.Column(db.String, nullable=False)
    ddd = db.Column(db.String, nullable=False)
    telefone =db.Column(db.String, nullable=False)
    fax = db.Column(db.String, nullable=False)
    endereco_eletronico = db.Column(db.String, nullable=False)
    representante = db.Column(db.String, nullable=False)
    representante_cargo = db.Column(db.String, nullable=False)
    data_registroans = db.Column(db.Date, nullable=False)

class RelacaoSchema(ma.Schema):
    class Meta:
        fields = ('registro_ans', 'cnpj','razao_social', 'nome_fantasia', 'modalidade', 'logradouro', 'numero', 'complemento', 'bairro', 'cidade', 'uf', 'cep',
        'ddd', 'telefone', 'fax', 'endereco_eletronico','representante', 'representante_cargo', 'data_registroans')

relacao_schema = RelacaoSchema()
relacao_schema = RelacaoSchema(many = True)


    


@app.route('/get', methods= ['GET'])
def get_db():
    all_db = Relacao.query.all()
    results = relacao_schema.dump(all_db)
    return jsonify(results)



@app.route('/postconsulta', methods= ['GET', 'POST'])
def get_consulta():
    reqs = requestflask.get_json()
    print(reqs)
    if len(reqs) != 0:
        if reqs['consulta'] != '':
            textoconsulta = reqs['consulta'] 
            print(textoconsulta)
            consulta = Relacao.query.filter((Relacao.registro_ans == textoconsulta) | (Relacao.cnpj == textoconsulta) |
            (Relacao.razao_social == textoconsulta) | (Relacao.nome_fantasia == textoconsulta) | (Relacao.modalidade == textoconsulta) |
            (Relacao.logradouro == textoconsulta) | (Relacao.numero == textoconsulta) |(Relacao.complemento == textoconsulta) |
            (Relacao.bairro == textoconsulta) | (Relacao.cidade == textoconsulta) | (Relacao.uf == textoconsulta) | (Relacao.cep == textoconsulta) |(Relacao.ddd == textoconsulta)|
            (Relacao.telefone == textoconsulta) |(Relacao.fax == textoconsulta) | (Relacao.endereco_eletronico == textoconsulta) | (Relacao.representante == textoconsulta) |(Relacao.representante_cargo == textoconsulta) |(Relacao.data_registroans == textoconsulta) ).all()
            results = relacao_schema.dump(consulta)
            return jsonify(results)
        return 'None'


if __name__ == "__main__":
    app.run(debug=True)