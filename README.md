# Minha API FECHA_A_CONTA

## Aluno : Andréia Souza Carvalho

Este pequeno projeto faz parte do primeiro MVP da Sprint I do curso "Desenvolvimento Full Stack Básico" 

O objetivo aqui é apresentar o conhecimento adquirido ao longo do módulo 01 que englobou os seguinte módulos:

1) Programação Orientada a Objetos
2) Banco de dados
3) Desenvolvimento Full Stack Básico

O banco é carregado na "__init__.py"

Usei o Visual Studio CODE.

Uso de um recurso ORM facilita o mapeamento entre aquilo que está no banco e as classes de negócio.

## Como executar 

É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).
O ambiente virtual é criado na pasta do projeto no subdiretório ENV ( esse diretório não deve ser enviado para o GIT (repositório))
O objetivo do ambiente virtual é criar uma área onde instalamos as bibliotecas necessárias para o projeto, bem como a versão do Python que iremos utilizar. 

Uma vez criado o ambiente virtual não precisamos instalar tudo novamente quando desativamos esse ambiente. A pasta do ambiente virtual é o ENV.

Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

	• Criando o ambiente virtual do projeto:
	cd your-project
	py -m venv env
	 
	Será criada uma pasta ENV no seu projeto com o ambiente virtual
	 
	• Ativando o ambiente virtual
	 
	.\env\Scripts\activate( ambiente Windows)
	 
	Source env\bin\activate (ambiente Linux)
  
  • Carregando as libs python 
  
  (env)$ pip install -r requirements.txt


  • Executando a API 

  (env)$ flask run --host 0.0.0.0 --port 5000


Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.
