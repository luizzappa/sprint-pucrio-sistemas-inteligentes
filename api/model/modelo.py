# 3rd's
import numpy as np
import pickle
import pandas as pd
# locals
from schemas import Pinguim

class Model:
    
    def carrega_modelo(path):
        """
        Carrega o modelo de IA salvo em pkl
        """
        
        if path.endswith('.pkl'):
            model = pickle.load(open(path, 'rb'))
        else:
            raise Exception('Formato de arquivo não suportado')
        return model

    def carrega_scaler(path):
        """
        Carrega o scaler utilizado
        """
        
        if path.endswith('.pkl'):
            scaler = pickle.load(open(path, 'rb'))
        else:
            raise Exception('Formato de arquivo não suportado')
        return scaler 
    
    def preditor(model, scaler, pinguim: Pinguim):
        """
        Realiza a predição da espécie de pinguim com base no modelo treinado
        """
        data = {
            'island': [pinguim.island],
            'bill_length_mm': [pinguim.bill_length_mm], 
            'bill_depth_mm': [pinguim.bill_depth_mm], 
            'flipper_length_mm': [pinguim.flipper_length_mm], 
            'body_mass_g': [pinguim.body_mass_g], 
            'sex': [pinguim.sex]
        }
        atributos = ['island', 'bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g', 'sex']
        entrada = pd.DataFrame(data, columns=atributos)
        array_entrada = entrada.values
        X_entrada = array_entrada[:,0:6].astype(float)
        rescaled_entrada = scaler.transform(X_entrada)
        saida = model.predict(rescaled_entrada)

        return saida[0]