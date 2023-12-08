from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score
import pandas as pd

class Avaliador:

    def avaliar(self, modelo, scaler, X_test, Y_test):
        """ Faz uma predição e avalia o modelo. Poderia parametrizar o tipo de
        avaliação, entre outros.
        """
        data = {
            'island': X_test['island'],
            'bill_length_mm': X_test['bill_length_mm'], 
            'bill_depth_mm': X_test['bill_depth_mm'], 
            'flipper_length_mm': X_test['flipper_length_mm'], 
            'body_mass_g': X_test['body_mass_g'], 
            'sex': X_test['sex']
        }
        atributos = ['island', 'bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g', 'sex']
        entrada = pd.DataFrame(data, columns=atributos)
        array_entrada = entrada.values
        X_entrada = array_entrada[:,0:6].astype(float)
        rescaled_entrada = scaler.transform(X_entrada)
        predicoes = modelo.predict(rescaled_entrada)
        
        # Caso o seu problema tenha mais do que duas classes, altere o parâmetro average
        return (accuracy_score(Y_test, predicoes),
                recall_score(Y_test, predicoes, average='micro'),
                precision_score(Y_test, predicoes, average='micro'),
                f1_score(Y_test, predicoes, average='micro'))