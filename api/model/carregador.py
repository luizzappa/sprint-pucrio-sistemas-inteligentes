import pandas as pd

class Carregador:

    def carregar_dados(self, url: str, atributos: list):
        """ Carrega e retorna um DataFrame.
        """
        
        df = pd.read_csv(url, names=atributos,
                           skiprows=1, delimiter=';') 

        return df[[
            'island',
            'bill_length_mm',
            'bill_depth_mm',
            'flipper_length_mm',
            'body_mass_g',
            'sex',
            'species'
        ]]