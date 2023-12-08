from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from model import Model
from schemas import *
from flask_cors import CORS


# Instanciando o objeto OpenAPI
info = Info(title="Backend pinguins", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Definindo tags para agrupamento das rotas
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
pinguim_tag = Tag(name="Pinguim", description="Predição da espécie de um pinguim")


# Rota home
@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


# Rota de predição da espécie do pinguim
@app.post('/pinguim', tags=[pinguim_tag],
          responses={"200": Pinguim, "400": ErrorSchema, "409": ErrorSchema})
def predict(form: Pinguim):
    """Realiza a predição de uma espécie de pinguim com base em suas características.

    Args:
        island (int): 0 (Dream), 1 (Biscoe), 2 (Torgersen)
        bill_length_mm (int): comprimento do bico (milímetros)
        bill_depth_mm (int): profundidade do bico (milímetros)
        flipper_length_mm (int): comprimento da nadadeira (milímetros)
        body_mass_g (int): massa corporal (gramas)
        sex (int): sexo do pinguim, 0 (Fêmea) e 1 (Macho)
        
    Returns:
        specie (int): 0 (Adelie), 1 (Chinstrap), 2 (Gentoo)
    """
    
    # Carregando modelo
    ml_path = 'ml_model/model.pkl'
    modelo = Model.carrega_modelo(ml_path)
    scaler_path = 'ml_model/scaler.pkl'
    scaler = Model.carrega_scaler(scaler_path)
    
    pinguim = Pinguim(
        island=form.island,
        bill_length_mm=form.bill_length_mm,
        bill_depth_mm=form.bill_depth_mm,
        flipper_length_mm=form.flipper_length_mm,
        body_mass_g=form.body_mass_g,
        sex=form.sex
    )

    especie = Model.preditor(modelo, scaler, pinguim)
    
    return f"{int(especie)}", 200
