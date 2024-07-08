'''configuracion del arranque'''

VERSION = 1 

#obtener data
N_ROWS = 10_000_000
TRAIN_PATH_DATA = "./data/collect_data/train.csv"
TEST_PATH_DATA = "./data/collect_data/test.csv"
SAVE_MODEL_PATH = "./model"

#model 
FEATURES = ['passenger_count','hour','day','dayofweek','dayofyear','month','quarter']
TARGET = "fare_amount"
MODELS = ['xgboost','rf','lrg']
TEST_SIZE = 0.25
RANDOM_STATE = 42

PARAMS = {
    'xgboost' : {
        #....
    },
    'rf' : {
        #....
    },
    'lrg' :{}
}

#desarrollador
DEVELOPER = "Patricio Quevedo"
