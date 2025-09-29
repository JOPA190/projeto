from flask import Flask, jsonify, request  # classe para criar a aplicação web
from datetime import datetime  # para trabalhar com as datas e horários
import uuid  # gera os identificadores únicos aos usuários

app = Flask(__name__)  # cria uma instância da aplicação Flask

usuarios = []  # local onde será armazenado os usuários, funciona como um "banco de dados"


@app.route('/usuarios', methods=['GET'])  # define uma rota até '/usuarios' que aceita somente o GET
def listar_usuarios():
    return jsonify(usuarios)  # converte a lista para JSON


# define uma rota para '/usuarios/<id>' onde <id> é um parâmetro variável na URL
@app.route('/usuarios/<string:id>', methods=['GET'])
def buscar_usuario(id):
    # passa por cada usuário na lista
    for usuario in usuarios:
        # verifica se o ID do usuário é igual ao recebido pela URL
        if usuario['id'] == id:
            return jsonify(usuario)  # se encontrar retorna o usuário em JSON
    return jsonify({"erro": "Usuário não encontrado"}), 404  # se não achar retorna um erro 404


# define uma rota para '/usuarios' que aceita somente POST (usado para criar novos recursos)
@app.route('/usuarios', methods=['POST'])
def criar_usuario():
    # verifica se existe um JSON no corpo da requisição e se tem os campos 'nome' e 'email'
    if not request.json or 'nome' not in request.json or 'email' not in request.json:
        return jsonify({"erro": "Dados incompletos"}), 400  # validação básica dos campos
    
    # verifica se tem o '@' no email
    if '@' not in request.json['email']:
        return jsonify({"erro": "Email inválido"}), 400
    
    # cria novo usuário
    novo_usuario = {
        "id": str(uuid.uuid4()),  # gera ID único
        "nome": request.json['nome'],
        "email": request.json['email'],
        "data_criacao": datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # pega a data/hora atual e formata como string
    }
    
    # adiciona o novo usuário criado a lista
    usuarios.append(novo_usuario)
    return jsonify(novo_usuario), 201


# rota inicial para testar se API está rodando
@app.route('/')
def home():
    return jsonify({"mensagem": "API de Usuários rodando!"})


if __name__ == '__main__':
    app.run(debug=True)  # inicia o servidor web do Flask