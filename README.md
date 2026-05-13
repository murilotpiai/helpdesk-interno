# Helpdesk Interno

API REST para gerenciamento de chamados internos de TI, desenvolvida com Python, FastAPI e SQLAlchemy. O projeto simula um fluxo inicial de suporte tecnico dentro de uma organizacao, com abertura e listagem de chamados.

Este repositorio foi organizado como projeto de portfolio para demonstrar backend, estruturacao de API, modelagem simples de dados e documentacao tecnica.

## Objetivo do projeto

Criar uma base de sistema de helpdesk interno para registrar solicitacoes de suporte, centralizar chamados e facilitar o acompanhamento por uma equipe de TI.

## Tecnologias utilizadas

- Python 3
- FastAPI
- SQLAlchemy
- SQLite como banco local padrao
- SQL Server via `DATABASE_URL`, quando configurado
- Uvicorn
- Pydantic

## Funcionalidades

- Health check da API na rota `/`
- Cadastro de chamados
- Listagem de chamados cadastrados
- Persistencia em banco de dados
- Documentacao automatica via Swagger em `/docs`
- Separacao basica entre rotas, modelos, schemas, banco de dados e operacoes CRUD

## Estrutura do projeto

```text
helpdesk-interno/
|-- backend/
|   |-- main.py        # Ponto de entrada da API
|   |-- database.py    # Configuracao de conexao com o banco
|   |-- models.py      # Modelos SQLAlchemy
|   |-- schemas.py     # Schemas Pydantic
|   |-- crud.py        # Operacoes de acesso a dados
|   `-- __init__.py
|-- docs/
|   `-- requisitos/
|       |-- requisitos-funcionais.md
|       |-- requisitos-nao-funcionais.md
|       `-- regras-de-negocio.md
|-- test_db.py
|-- requirements.txt
|-- .env.example
|-- .gitignore
`-- README.md
```

## Como executar

1. Clone o repositorio:

```bash
git clone https://github.com/murilotpiai/helpdesk-interno.git
cd helpdesk-interno
```

2. Crie e ative um ambiente virtual:

```bash
python -m venv venv
```

No Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

3. Instale as dependencias:

```bash
pip install -r requirements.txt
```

4. Configure o ambiente, se quiser usar outro banco:

```bash
copy .env.example .env
```

Sem `.env`, a aplicacao usa SQLite local em `helpdesk.db`.

5. Execute a API:

```bash
python -m uvicorn backend.main:app --reload
```

6. Acesse a documentacao:

```text
http://127.0.0.1:8000/docs
```

## Exemplo de chamado

```json
{
  "titulo": "Computador nao liga",
  "descricao": "Usuario informou que a estacao nao inicializa apos queda de energia.",
  "prioridade": "alta"
}
```

## Aprendizados

- Organizacao de uma API backend em camadas simples
- Criacao de rotas REST com FastAPI
- Uso de schemas para validar entrada e saida de dados
- Persistencia com SQLAlchemy
- Importancia de documentar requisitos e regras de negocio
- Configuracao de ambiente para facilitar execucao em outras maquinas

## Melhorias futuras

- Autenticacao de usuarios
- Controle de perfis, como solicitante, tecnico e administrador
- Filtros por status, prioridade e data
- Atualizacao de status do chamado
- Testes automatizados
- Dashboard para acompanhamento dos atendimentos
- Container Docker para padronizar a execucao

## Autor

Desenvolvido por Murilo Turcato Piai, estudante de Sistemas de Informacao na UNIFAFIBE, com foco em desenvolvimento web, backend, dados e sistemas corporativos.

- LinkedIn: https://www.linkedin.com/in/mtpiai
- GitHub: https://github.com/murilotpiai
