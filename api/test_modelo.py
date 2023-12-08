from model.avaliador import Avaliador
from model.carregador import Carregador
from model.modelo import Model

# Instanciação das Classes
carregador = Carregador()
avaliador = Avaliador()

# Parâmetros    
url_dados = "../golden_dataset.csv"
colunas = ['species', 'island', 'bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g', 'sex']

# Carga dos dados
dataset = carregador.carregar_dados(url_dados, colunas)

# Separando em dados de entrada e saída
X = dataset.iloc[:, 0:-1]
Y = dataset.iloc[:, -1]

# Importando scaler utilizado
scaler_path = 'ml_model/scaler.pkl'
scaler = Model.carrega_scaler(scaler_path)

# Método para testar o modelo a partir do arquivo correspondente
# O nome do método a ser testado necessita começar com "test_"
def test_modelo_cart():  
    # Importando o modelo
    lr_path = 'ml_model/model.pkl'
    modelo_lr = Model.carrega_modelo(lr_path)

    # Obtendo as métricas
    acuracia_lr, recall_lr, precisao_lr, f1_lr = avaliador.avaliar(modelo_lr, scaler, X, Y)
    
    # Testando as métricas
    assert acuracia_lr >= 0.75 
    assert recall_lr >= 0.5 
    assert precisao_lr >= 0.5 
    assert f1_lr >= 0.5 
 