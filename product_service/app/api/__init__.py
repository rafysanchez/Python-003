# Inicialização da API 

from flask import Blueprint

bp = Blueprint('api', __name__)

from app.api.resources import product_resource 
