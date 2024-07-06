import pandas as pd 
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
