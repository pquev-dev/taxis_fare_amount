import pandas as pd 
import numpy as np
import os
import pickle
from config import *
from sklearn.model_selection import train_test_split


def load_data(filepath : str)->pd.DataFrame:
    """
    Funcion para apertura de documentos csv
    """
    data = pd.read_csv(filepath,nrows=N_ROWS)
    return data

def split_data(X : pd.DataFrame, y : pd.Series)->dict:
    """
    Funcion que permite separar la data en entrenamiento y test
    """
    X_train,X_test,y_train,y_test = train_test_split(X,
                                                    y,
                                                    test_size=TEST_SIZE,
                                                    random_state=RANDOM_STATE)
    split_slit = {
        'x_train' : X_train,
        'x_test' : X_test,
        'y_train' : y_train,
        'y_test' : y_test
    }
    
    return split_data

def calculate_distance(x1,y1,x2,y2):
        distance = np.sqrt((x2 - x1 )**2 + (y2 - y1)**2)
        return distance

def add_features_date(data : pd.DataFrame,date_column : str)->pd.DataFrame:
    '''Agergar nuevas columnas a partir de la fecha'''
    data[date_column] = pd.to_datetime(data[date_column])

    #new columns 
    data['hour'] = data[date_column].dt.hour
    data['day'] = data[date_column].dt.day
    data['dayofweek'] = data[date_column].dt.dayofweek
    data['dayofyear'] = data[date_column].dt.dayofyear
    data['month'] = data[date_column].dt.month
    data['quarter'] = data[date_column].dt.quarter

    return data

def select_features_target(data,features,target)->dict:
    dict_data = {'features' : data[features],'target' : data[target] }
    return dict_data

def save_pickle(data,filename : str)->None:
    """
    Esta funcion guarda el modelo en formato pkl.
    """

    filepath = os.path.join(SAVE_MODEL_PATH,f"{filename}.pkl")
    with open(filepath, "wb") as file:
        pickle.dump(data,file)
        
def load_pickle(filename):
    """
    Apertura de documento pkl (modelo)
    """
    filepath = os.path.join(SAVE_MODEL_PATH,f"{filename}.pkl")
    with open(filepath,"rb") as file:
        data = pickle.load(file)
    return data
