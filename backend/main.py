from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from .database import SessionLocal, engine
from . import models, schemas, crud

# cria tabelas
models.Base.metadata.create_all(bind=engine)

# instancia única da aplicação
app = FastAPI(title="Helpdesk Interno")


# dependência do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# rota raiz (health check)
@app.get("/")
def home():
    return {"status": "API rodando corretamente"}


# criar chamado
@app.post("/chamados", response_model=schemas.ChamadoResponse)
def criar_chamado(
    chamado: schemas.ChamadoCreate,
    db: Session = Depends(get_db)
):
    return crud.criar_chamado(db, chamado)


# listar chamados
@app.get("/chamados", response_model=list[schemas.ChamadoResponse])
def listar_chamados(
    db: Session = Depends(get_db)
):
    return crud.listar_chamados(db)
