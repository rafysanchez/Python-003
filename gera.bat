@echo off
echo Criando estrutura de arquivos e pastas para projeto Flask com SQLite3...

:: Criar diretório principal
mkdir product_service
cd product_service

:: Criar arquivos raiz
echo # Configuração do projeto > config.py
echo from app import create_app > run.py
echo # Lista de dependências do projeto > requirements.txt
echo # Documentação do Projeto Flask com Clean Architecture > README.md
echo # Variáveis de ambiente > .env
echo __pycache__/ > .gitignore
echo *.pyc >> .gitignore
echo .env >> .gitignore
echo .venv >> .gitignore
echo *.db >> .gitignore

:: Criar estrutura de diretórios da aplicação
mkdir app
cd app
echo # Inicialização da aplicação > __init__.py
echo def create_app(config_name='development'): > __init__.py
echo     app = Flask(__name__) >> __init__.py
echo     return app >> __init__.py
echo # Configuração das extensões do Flask > extensions.py

:: API
mkdir api
cd api
echo # Inicialização da API > __init__.py
mkdir resources
cd resources
echo # Inicialização dos recursos > __init__.py
echo # Endpoint de Produtos > product_resource.py
cd ../..

:: Domain
mkdir domain
cd domain
echo # Inicialização do domínio > __init__.py
mkdir models
cd models
echo # Inicialização dos modelos > __init__.py
echo # Modelo de Produto > product.py
cd ..
mkdir schemas
cd schemas
echo # Inicialização dos schemas > __init__.py
echo # Schema de Produto > product_schema.py
cd ../..

:: Services
mkdir services
cd services
echo # Inicialização dos serviços > __init__.py
echo # Serviço de Produto > product_service.py
cd ..

:: Repository
mkdir repository
cd repository
echo # Inicialização dos repositórios > __init__.py
echo # Repositório base > base_repository.py
echo # Repositório de produtos > product_repository.py
cd ..

:: Database
mkdir database
cd database
echo # Inicialização da database > __init__.py
echo # Configuração do banco de dados > db.py
mkdir migrations
cd ..

cd ..

:: Testes
mkdir tests
cd tests
echo # Inicialização dos testes > __init__.py
echo # Configuração dos testes > conftest.py
echo # Testes da API de produtos > test_product_api.py
echo # Testes do serviço de produtos > test_product_service.py
echo # Testes do repositório de produtos > test_product_repository.py
cd ..

echo.
echo Estrutura de arquivos e pastas criada com sucesso!
echo Instalando dependências do projeto...

:: Instalação opcional de dependências
pip install flask flask-restful flask-sqlalchemy marshmallow pytest python-dotenv

echo.
echo Processo finalizado! A estrutura do projeto Flask foi criada com sucesso.