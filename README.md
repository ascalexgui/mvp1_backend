# Minha API

Este pequeno projeto faz parte do primeiro MVP da Sprint I do curso "Desenvolvimento Full Stack Básico" 

O objetivo aqui é apresentar o conhecimento adquirido ao longo do módulo 01 que englobou os seguinte módulos:

1) Programação Orientada a Objetos
2) Banco de dados
3) Desenvolvimento Full Stack Básico

O banco é carregado na __init__.py

Uso de um recurso ORM facilita o mapeamento entre aquilo que está no banco e as classes de negócio.

A BASE 

---
## Como executar 


Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

```
(env)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

Para executar a API  basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.
