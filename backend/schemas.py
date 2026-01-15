from pydantic import BaseModel
from datetime import datetime


class ChamadoBase(BaseModel):
    titulo: str
    descricao: str
    prioridade: str


class ChamadoCreate(ChamadoBase):
    pass


class ChamadoResponse(ChamadoBase):
    id: int
    status: str
    criado_em: datetime

    class Config:
        from_attributes = True
