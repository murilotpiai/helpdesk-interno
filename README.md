# 🛠️ Helpdesk Interno – API REST

API REST para gerenciamento de chamados internos, desenvolvida em Python com FastAPI e integrada ao SQL Server.

Este projeto simula um sistema real de helpdesk utilizado em ambientes corporativos para abertura e acompanhamento de chamados técnicos.

---

## 🚀 Tecnologias Utilizadas

- Python 3
- FastAPI
- SQLAlchemy
- Pydantic
- SQL Server
- PyODBC
- Swagger (OpenAPI)

---

## 📌 Funcionalidades

- Criar chamados técnicos
- Listar chamados cadastrados
- Definir prioridade do chamado
- Status automático (`aberto`)
- Documentação automática da API via Swagger

---

## 🗂️ Estrutura do Projeto

helpdesk-interno/
│
├── backend/
│ ├── main.py # Rotas da API
│ ├── database.py # Conexão com SQL Server
│ ├── models.py # Models SQLAlchemy
│ ├── schemas.py # Schemas Pydantic
│ ├── crud.py # Regras de negócio
│
├── test_db.py # Teste de conexão com o banco
├── requirements.txt
├── README.md
└── .gitignore


