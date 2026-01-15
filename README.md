# Helpdesk Interno

## 📌 Visão Geral

O **Helpdesk Interno** é uma API backend desenvolvida para gerenciar chamados de suporte técnico dentro de uma organização. O sistema permite a abertura, listagem e gerenciamento inicial de chamados, simulando um ambiente real de atendimento de TI.

Este projeto foi criado com foco em **boas práticas**, **organização de código** e **estrutura profissional**, sendo ideal para fins acadêmicos, portfólio e preparação para vagas de estágio/júnior.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* **FastAPI**
* **SQLAlchemy**
* **SQLite / SQL Server** (configurável)
* **Uvicorn**
* **Git & GitHub**

---

## 📂 Estrutura do Projeto

```
helpdesk-interno/
│
├── backend/
│   ├── main.py        # Ponto de entrada da API
│   ├── database.py    # Conexão com banco de dados
│   ├── models.py      # Modelos ORM
│   ├── schemas.py     # Schemas Pydantic
│   ├── crud.py        # Regras de acesso a dados
│   └── __init__.py
│
├── docs/
│   └── requisitos/
│       ├── requisitos-funcionais.md
│       ├── requisitos-nao-funcionais.md
│       └── regras-de-negocio.md
│
├── test_db.py         # Teste de conexão com o banco
├── README.md
├── .gitignore
└── venv/              # Ambiente virtual (ignorado no Git)
```

---

## 🚀 Como Executar o Projeto

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/SEU_USUARIO/helpdesk-interno.git
cd helpdesk-interno
```

### 2️⃣ Criar e ativar o ambiente virtual

```bash
python -m venv venv
```

**Windows:**

```powershell
venv\Scripts\Activate.ps1
```

### 3️⃣ Instalar dependências

```bash
pip install -r requirements.txt
```

### 4️⃣ Executar a API

```bash
python -m uvicorn backend.main:app --reload
```

### 5️⃣ Acessar a documentação automática

Abra no navegador:

```
http://127.0.0.1:8000/docs
```

---

## 📌 Funcionalidades Atuais

* Criar chamados de suporte
* Listar chamados cadastrados
* Persistência em banco de dados
* Documentação automática via Swagger

---

## 🧩 Próximas Funcionalidades (Roadmap)

* Autenticação de usuários
* Status do chamado (aberto, em atendimento, fechado)
* Prioridade do chamado
* Filtro por usuário e status
* Dashboard administrativo

---

## 👨‍💻 Autor

Projeto desenvolvido por **Murilo Piai**, com foco em aprendizado prático de backend, APIs REST e organização de projetos profissionais.

---

## 📄 Licença

Este projeto é de uso educacional e livre para estudos.

