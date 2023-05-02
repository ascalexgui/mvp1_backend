from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base


class Despesa(Base):
    __tablename__ = 'despesa'

    idDespesa       = Column(Integer, primary_key=True)
    nome            = Column(String(140))
    valor           = Column(Float)
    quantidade      = Column(Integer)
    data_insercao   = Column(DateTime, default=datetime.now())

    def __init__(self, nome:str, valor:float,quantidade: Integer,
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria uma despesa

        Arguments:
            nome: nome da despesa
            valor: valor pago pelo despesa
            quantidade:
            data_insercao: data do cadastro da despesa no banco
        """
        self.nome = nome
        self.valor = valor
        self.quantidade = quantidade

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao