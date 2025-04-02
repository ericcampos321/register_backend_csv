# Desafio Técnico - Busca de Operadoras

## Descrição

Este projeto consiste em uma API desenvolvida em **FastAPI** que realiza uma busca textual na lista de operadoras cadastradas em um arquivo **CSV**, retornando os registros mais relevantes. O frontend foi implementado utilizando **Vue.js** para interação com o usuário.

---

## Estrutura do Projeto

```
register_backend_csv/
├── src/
│   ├── config/
│   │   └── env_config.py
│   ├── controller/
│   ├── repository/
│   ├── routes/
│   ├── services/
│   ├── utils/
│   └── main.py
├── .env.local
├── .env.production
├── requirements.txt
└── README.md
```

## Configuração

### Variáveis de ambiente

O projeto utiliza dois arquivos de ambiente:

- `.env.local`
- `.env.production`

Exemplo de `.env.local`:

```
NODE_ENV=local
HOST=localhost
PORT=5000
CSV_FILE_PATH=operadoras.csv
```

Exemplo de `.env.production`:

```
NODE_ENV=production
HOST=0.0.0.0
PORT=8000
CSV_FILE_PATH=operadoras.csv
```


### Criação do ambiente virtual

```bash
python -m venv venv
```

### Ativar o ambiente virtual

#### Windows (PowerShell)
```bash
.env\Scripts\Activate
```

#### Linux ou WSL
```bash
source venv/bin/activate
```

### Instalar as dependências

```bash
pip install -r requirements.txt
```

## Execução

### Ambiente Local

#### Windows PowerShell
```bash
$Env:NODE_ENV="local"; python src/main.py
```

#### Linux ou WSL
```bash
NODE_ENV=local python src/main.py
```

### Ambiente Produção

#### Windows PowerShell
```bash
$Env:NODE_ENV="production"; python src/main.py
```

#### Linux ou WSL
```bash
NODE_ENV=production python src/main.py
```

---
**Observação:** No Windows CMD use:
```cmd
set NODE_ENV=local && python src/main.py
```
## Endpoints Disponíveis

| Método | Rota                   | Descrição                         |
|:-----:|:-----------------------:|:---------------------------------:|
| GET   | /operators/search      | Consulta operadoras por termo     |

Exemplo:
```
GET http://localhost:5000/operators/search?search=claro
```

---

## 🚀 Ambiente de Execução

Este projeto utiliza variáveis de ambiente configuradas nos arquivos `.env.local` e `.env.production` para facilitar a configuração.

Exemplo de variáveis:
```
NODE_ENV=local
HOST=localhost
PORT=5000
CSV_FILE_PATH=operadoras.csv
```

---

## Comandos Rápidos

| Ação                         | Comando (Windows)                                                      | Comando (Linux/Mac)                                                    |
|------------------------------|-----------------------------------------------------------------------|-----------------------------------------------------------------------|
| Criar ambiente virtual       | `python -m venv venv`                                                 | `python3 -m venv venv`                                                |
| Ativar ambiente              | `.env\Scriptsctivate`                                             | `source venv/bin/activate`                                            |
| Instalar dependências        | `pip install -r requirements.txt`                                     | `pip install -r requirements.txt`                                     |
| Rodar ambiente local         | `$Env:NODE_ENV="local"; uvicorn src.main:app --reload`                 | `NODE_ENV=local uvicorn src.main:app --reload`                        |
| Rodar ambiente produção      | `$Env:NODE_ENV="production"; uvicorn src.main:app`                     | `NODE_ENV=production uvicorn src.main:app`                            |

---

## Requisitos do Teste

Esse projeto foi estruturado com foco em:

- Organização do código seguindo padrão MVC
- Utilização de variáveis de ambiente para configuração
- Leitura eficiente do CSV
- Resposta padronizada com mensagens e status
- Scripts claros para ambiente local e produção

---

## Autor

Desenvolvido por **Eric Campos** – Projeto de Nivelamento Técnico
