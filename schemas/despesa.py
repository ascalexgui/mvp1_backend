from pydantic import BaseModel
from typing import Optional, List
from model.despesa import Despesa

class DespesaSchema(BaseModel):
    """ Define como uma nova despesa a ser inserida deve ser representado
    """
    nome: str = "Aluguel casa"
    valor: float = 5000.00
    quantidade: Optional[int] = 1


class DespesaBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no ID da despesa.
    """
    id: int = 1
    nome: Optional[str] = "Casa"

class DespesaBuscaNomeSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome da despesa.
    """
    nome: str = "Aluguel casa"


class ListagemDespesasSchema(BaseModel):
    """ Define como uma listagem das despesas será retornada.
    """
    despesas: List[DespesaSchema]
    total_gasto: float


def apresenta_despesas(despesas: List[Despesa]):
    """ Retorna uma representação da lista de despesas seguindo o schema definido em
        DespesaViewSchema.
    """
    result = []
    total_gasto = .0
    for despesa in despesas:
        result.append({
            "id"        : despesa.id,
            "nome"      : despesa.nome,
            "quantidade": despesa.quantidade,
            "valor"     : despesa.valor
        })
        total_gasto = total_gasto + (despesa.quantidade * despesa.valor)


    return {"despesas": result, "total_gasto": total_gasto}
  

class DespesaViewSchema(BaseModel):
    """ Define como uma despesa será retornada: despesa
    """
    id: int = 1
    nome: str = "Aluguel casa"
    quantidade: Optional[int] = 1
    valor: float = 5000.00

class DespesaDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    message: str
    nome: str

def apresenta_despesa(despesa: Despesa):
    """ Retorna uma representação da despesa seguindo o schema definido em
        DespesaViewSchema.
    """
    return {
        "id": despesa.id,
        "nome": despesa.nome,
        "quantidade": despesa.quantidade,
        "valor": despesa.valor    
    }
