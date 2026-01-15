from sqlalchemy.orm import Session
from .models import Chamado
from .schemas import ChamadoCreate



def criar_chamado(db: Session, chamado: ChamadoCreate):
    novo_chamado = Chamado(
        titulo=chamado.titulo,
        descricao=chamado.descricao,
        prioridade=chamado.prioridade
    )
    db.add(novo_chamado)
    db.commit()
    db.refresh(novo_chamado)
    return novo_chamado


def listar_chamados(db: Session):
    return db.query(Chamado).all()
