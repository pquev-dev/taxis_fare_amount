import pandas as pd 
import numpy as np
from utils.utils import add_features_date,select_features_target,calculate_distance
from config import FEATURES,TARGET

class DataProcesing():

    def __init__(self,data : pd.DataFrame):
        self.data = data
        

    def clear_zero_values(self,data : pd.DataFrame)->pd.DataFrame:
        """
        Eliminar valores en 0
        """
        data = data[data['passenger_count']>0]
        data = data[data['fare_amount']>0]
        return data

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
            data_to_process = add_features_date(data=data_to_process,date_column='key')
            #agregar columna de distancia
            data_to_process['distance'] = data_to_process.apply(
                calculate_distance(data_to_process.pickup_latitude,
                                   data_to_process.pickup_longitude,
                                   data_to_process.dropoff_latitude,
                                   data_to_process.dropoff_longitude)
            )
            data_to_process.to_pickle('./data/process_final_data.pkl')            
        
        except Exception as err:
            print(f"error en la ejecucion de limpieza : {err}")




