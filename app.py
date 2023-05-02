from flask_openapi3 import OpenAPI, Info, Tag
from sqlalchemy.exc import IntegrityError
from sqlalchemy import func
from urllib.parse import unquote

from flask_cors import CORS
from flask import redirect

from model import Session, Despesa
from logger import logger
from schemas import *

info = Info(title="API Fecha a Conta", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)


# definindo tags
home_tag = Tag(name="Documentação", description="Documentação: Swagger")
despesa_tag = Tag(name="Despesa", description="Adição, visualização e remoção das despesas à base")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para o SWAGGER com a documentação.
    """
    return redirect('/openapi/swagger')

"""
------------------------------------------
Adiciona uma nova despesa a base de dados 
& 
Retorna uma representação das despesas. 
POST
------------------------------------------
"""

@app.post('/inclui_despesa', tags=[despesa_tag],
          responses={"200": DespesaViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def inclui_despesa(form: DespesaSchema):
    """Adiciona uma nova despesa informando o nome, quantidade e valor"""

    despesa = Despesa(
        nome=form.nome.lower(),
        quantidade=form.quantidade,
        valor=form.valor)

    try:
        # criando conexão com a base
        session = Session()
        # adicionando despesa
        session.add(despesa)
        # efetivando o camando de adição da nova despesa na tabela
        session.commit()
        return apresenta_despesa(despesa), 200

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar nova despesa :/"
        return {"message": error_msg}, 400

"""
------------------------------------------
Faz a busca por todas as Despesas cadastradas 
& 
Retorna uma representação da listagem das despesas e total das despesas ( soma quantidade * valor de cada despesa)
GET
------------------------------------------
"""

@app.get('/lista_despesas', tags=[despesa_tag],
         responses={"200": ListagemDespesasSchema, "404": ErrorSchema})
def get_lista_despesas():
    """Retorna a lista com as despesas já cadastradas"""

    # criando conexão com a base
    session = Session()
    # fazendo a busca
    # despesas = session.query(Despesa).all()

    despesas = session.query(Despesa).order_by(Despesa.nome.asc()).all()

    if not despesas:
        # se não há despesas cadastradas
        return {"despesas":[], "total_gasto":0}, 200
    else:
        # retorna a representação das despesas
        return apresenta_despesas(despesas), 200

"""
------------------------------------------------
Busca por uma Despesa a partir do nome da despesa
&
Retorna uma representação das despesas.
GET
------------------------------------------------
"""

@app.get('/despesa_por_nome', tags=[despesa_tag],
         responses={"200": DespesaViewSchema, "404": ErrorSchema})
def get_despesa_por_nome(query: DespesaBuscaNomeSchema):
    """Busca por uma despesa já cadastrada através do seu nome"""

    nome = query.nome.lower()
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    despesa = session.query(Despesa).filter(func.lower(Despesa.nome) == nome).first()

    if not despesa:
        # se o despesa não foi encontrada
        error_msg = "Despesa não encontrada na base :/"
        logger.warning(f"Erro ao buscar produto ' {nome}, {error_msg}")
        return {"message": error_msg}, 404
    else:
        # retorna a representação da despesa
        return apresenta_despesa(despesa), 200


"""
------------------------------------------------
Deleta uma Despesa a partir do seu nome
&
Retorna uma mensagem de confirmação da remoção.
DELETE
------------------------------------------------
"""

@app.delete('/deleta_por_nome', tags=[despesa_tag],
            responses={"200": DespesaDelSchema, "404": ErrorSchema})
def del_deleta_por_nome(query: DespesaBuscaNomeSchema):
    """Deleta uma despesa a partir do seu nome"""

    nome = unquote(query.nome).lower()

    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    despesa = session.query(Despesa).filter(Despesa.nome == nome).first()

    if despesa:
        session.query(Despesa).filter(Despesa.nome == nome).delete()
        session.commit()
        # retorna a representação da mensagem de confirmação        
        return {"message": "Despesa removida", "nome": nome}
    else:
        # se o despesa não foi encontrada
        error_msg = "Despesa não encontrado na base :/"
        return {"message": error_msg}, 404