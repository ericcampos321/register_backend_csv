# Desafio Técnico - Busca de Operadoras

## Descrição

Este projeto consiste em uma API desenvolvida em **FastAPI** que realiza uma busca textual na lista de operadoras cadastradas em um arquivo **CSV**, retornando os registros mais relevantes. O frontend foi implementado utilizando **Vue.js** para interação com o usuário.

---

## Tecnologias Utilizadas

- Python 3.13
- FastAPI
- Uvicorn
- Pandas
- Vue.js
- Postman

---

## Estrutura do Projeto

├── src │ ├── controller │ ├── models │ ├── repository │ ├── routes │ ├── services │ ├── utils │ └── main.py ├── operadoras.csv └── README.md

## Como Executar

### 1. Clonar o projeto

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git](https://github.com/ericcampos321/register_backend_csv.git
cd seu-repositorio


### 2. Criar ambiente virtual e instalar dependências
python -m venv venv
source venv/bin/activate  # Linux
venv\Scripts\activate     # Windows

pip install -r requirements.txt
