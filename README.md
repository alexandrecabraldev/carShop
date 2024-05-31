```markdown
# Car Shop Backend

Este é o backend de uma loja de carros, desenvolvido utilizando Python, Flask e Postgres. O projeto fornece APIs para autenticação, gerenciamento de carros e outras funcionalidades necessárias para a loja.

## Requisitos

- Python (versão 3.12.2 ou superior)
- pip (versão 24.0 ou superior)
- Postgres
- Docker

## Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/alexandrecabraldev/carShop.git
    ```

2. Criar um ambiente virtual (opcional, mas recomendado):
    Primeiro, crie e ative um ambiente virtual para isolar as dependências do seu projeto:

    ```bash
    python -m venv nome_seu_ambiente_virtual
    nome_seu_ambiente_virtual\Scripts\activate
    ```
3. Construa e inicie os serviços compose.yaml do docker:

    ```bash
    docker-compose up --build
    ```
4. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

## Executando o Projeto

1. Inicie o servidor:

    ```bash
    python src/app.py
    ```

2. O servidor estará rodando em [http://localhost:5000](http://localhost:5000).

## Estrutura do Projeto

```
carShop/
├── src/
│   ├── controllers/
│   │   ├── userController.py
│   │   ├── carController.py
│   │   └── ...
│   ├── models/
│   │   ├── User.py
│   │   ├── Car.py
│   │   └── ...
│   ├── schemas/
│   │   ├── car_schema.py
│   │   ├── user_schema.py
│   │   └── ...
│   ├── utils/
│   │   ├── decorators.py
│   │   └── ...
│   ├── app.py
│   └── config.py
├── .gitignore
├── README.md
└── compose.yaml
├── requirements.txt
└── ...
```

## Endpoints Principais

### Autenticação

- `POST /login`: Autentica um usuário.
- `POST /user`: Cadastra um novo usuário.

### Gerenciamento de Carros

- `GET /car`: Retorna uma lista de todos os carros.
- `POST /car`: Adiciona um novo carro.
- `PUT /car/:id`: Atualiza os detalhes de um carro específico.
- `DELETE /car/:id`: Remove um carro.


### Dinâmica

- Cada carro deve tem as informações name, brand, model, price, image_url.
- Só é possivel cadastrar um carro com a autenticação de administrador, assim como atualizar e deletar.
- A rota GET /car é aberta, ou seja, pode ser acessada independente de autenticação.

```