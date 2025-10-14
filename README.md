# Mini API de Cadastro de Usuários

Uma API REST desenvolvida em **Python** com **Flask**, que permite realizar operações básicas de cadastro de usuários.

## Funcionalidades

* Criar novo usuário
* Listar todos os usuários
* Buscar usuário por ID
* Validação de e-mail
* Tratamento de erros

## Tecnologias Utilizadas

* **Python** – Linguagem de programação
* **Flask** – Framework web
* **UUID** – Geração de identificadores únicos
* **JSON** – Estrutura de dados
* Banco de dados em memória (dados não persistentes)

## Como Executar

### Pré-requisitos

* Python 3.6 ou superior
* Pip (gerenciador de pacotes do Python)

### Instalação e Execução

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/mini-api-usuarios.git
   cd mini-api-usuarios
   ```

2. Instale as dependências (se aplicável):

   ```bash
   pip install -r requirements.txt
   ```

3. Execute a API:

   ```bash
   python API_de_cadastro.py
   ```

4. A API estará disponível em:

   ```
   http://localhost:5000
   ```

## Endpoints da API

### `GET /`

Retorna mensagem de status da API.

**Resposta:**

```json
{
  "mensagem": "API de Usuários rodando!"
}
```

### `GET /usuarios`

Lista todos os usuários cadastrados.

**Resposta:**

```json
[
  {
    "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    "nome": "João Silva",
    "email": "joao@email.com",
    "data_criacao": "2024-01-15 14:30:00"
  }
]
```

### `POST /usuarios`

Cria um novo usuário.

**Corpo da requisição:**

```json
{
  "nome": "Maria Santos",
  "email": "maria@email.com"
}
```

**Resposta (sucesso):**

```json
{
  "id": "b2c3d4e5-f6g7-8901-bcde-f23456789012",
  "nome": "Maria Santos",
  "email": "maria@email.com",
  "data_criacao": "2024-01-15 14:35:00"
}
```

### `GET /usuarios/<id>`

Busca um usuário pelo ID.

**Exemplo de requisição:**

```
GET /usuarios/a1b2c3d4-e5f6-7890-abcd-ef1234567890
```

**Resposta (sucesso):**

```json
{
  "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "nome": "João Silva",
  "email": "joao@email.com",
  "data_criacao": "2024-01-15 14:30:00"
}
```

**Resposta (erro):**

```json
{
  "erro": "Usuário não encontrado"
}
```

## Desenvolvimento



Principais pontos implementados:

* CRUD básico de usuários
* Validação de e-mail
* Tratamento de erros
* Respostas no formato JSON
* Banco de dados em memória
