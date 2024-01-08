from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from datetime import datetime
import bcrypt


app = Flask(__name__)
app.config['SECRET_KEY'] = 'chave_secreta_super_segura'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
ma = Marshmallow(app)
jwt = JWTManager(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)


def verify_password(plain_password, hashed_password):
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password)


with app.app_context():
    db.create_all() 
    danilo_exists = User.query.filter_by(username="danilo").first()
    
    if not danilo_exists:
        hashed_password = bcrypt.hashpw("123456".encode('utf-8'), bcrypt.gensalt())
        danilo = User(username="danilo", password=hashed_password)
        db.session.add(danilo)
        db.session.commit()

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    card_number = db.Column(db.String(16), unique=True, nullable=False)

class CardSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Card

user_schema = UserSchema()
card_schema = CardSchema()



@app.route('/api/auth', methods=['POST'])
def auth():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()

    if user and verify_password(password, user.password):
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token)

    return jsonify({'message': 'Authentication failed'}), 401



@app.route('/api/insert', methods=['POST'])
@jwt_required()
def insert_card():
    data = request.get_json()
    card_number = data.get('card_number')

    existing_card = Card.query.filter_by(card_number=card_number).first()

    if existing_card:
        return jsonify({'message': 'O cartão já existe'}), 400

    new_card = Card(card_number=card_number)
    db.session.add(new_card)
    db.session.commit()

    return jsonify({'message': 'Cartão inserido com sucesso'})



@app.route('/api/processar-arquivo', methods=['POST'])
@jwt_required()
def processar_arquivo_txt():
    try:
        if 'file' not in request.files:
            return jsonify({'message': 'Nenhum arquivo encontrado'}), 400

        file = request.files['file']

        if file.filename == '':
            return jsonify({'message': 'Nenhum arquivo selecionado'}), 400

        processar_arquivo(file)

        return jsonify({'message': 'Arquivo processado com sucesso'}), 200

    except Exception as e:
        return jsonify({'message': 'Erro ao processar arquivo', 'error': str(e)}), 500

def processar_arquivo(file):
    nome_cliente = None
    data_insercao = None
    lote = None
    qtd_cartoes = None

    for i, linha in enumerate(file):
        linha = linha.decode('utf-8').strip()

        if i == 0:
            nome_cliente = linha[0:28].strip()
            data_insercao = linha[29:36].strip()
            lote = linha[37:44].strip()
            qtd_cartoes = linha[45:50].strip()
        elif 1 <= i <= int(qtd_cartoes):
            identificador = linha[0].strip()
            numeracao_lote = linha[1:6].strip()
            numero_cartao = linha[7:25].strip()

            if numero_cartao:
                try:
                    novo_cartao = Card(card_number=numero_cartao)
                    db.session.add(novo_cartao)
                except Exception as e:
                    print(f"Erro: Falha ao inserir cartão na linha {i + 1}. Detalhes: {str(e)}")

    db.session.commit()
    print("Processamento do arquivo concluído com sucesso.")



@app.route('/api/query/<card_number>', methods=['GET'])
@jwt_required()
def query_card(card_number):
    card = Card.query.filter_by(card_number=card_number).first()

    if card:
        return jsonify({'message': 'O cartão já existe', 'card_id': card.id})

    return jsonify({'message': 'Cartão não existe'}), 404



if __name__ == '__main__':
    app.run(debug=True)
