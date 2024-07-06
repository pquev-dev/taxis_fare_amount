import pandas as pd 
import numpy as np

class DataProcesing():

    def __init__(self,data : pd.DataFrame):
        self.data = data
        

    def clear_zero_values(self,data : pd.DataFrame)->pd.DataFrame:
        """
        Eliminar valores en 0
        """
        return data[data['fare_amount']>0]

    def clear_nan_values(self,data : pd.DataFrame)->pd.DataFrame:
        """
        Eliminar valores nulos
        """
        return data.dropna()
    
    def fill_values(self,data : pd.DataFrame,column : str,value: float)->pd.DataFrame:
        '''
        Rellenar los valores nulos con algun valor 
        '''
        data[column] = data[column].fillna(value)
        return data
    
    def delete_outliers(self, data : pd.DataFrame,columns  : list) -> pd.DataFrame:
        if len(columns) == 0:
            breakpoint

        for i in columns:
            serie = data[i]
            q3 = np.quantile(serie,0.75)
            q1 = np.quantile(serie,0.25)
            iqr = q3 - q1 
            up_limit = q3 + 1.5 * iqr 
            down_limit = q3 - 1.5 * iqr 

            data[f"outlier_{i}"] = 0
            data.loc[(data[i]<down_limit) or (data[i]>up_limit),f"outlier_{i}"] = 1



    def run(self,):
        """
        funcion principal de proceso de datos
        """
        try:
            data_to_process = self.data

            data_to_process = self.clear_nan_values(data_to_process)
            data_to_process = self.clear_zero_values(data_to_process)
            print(data_to_process)

        except Exception as err:
            print(f"error en la ejecucion de limpieza : {err}")




