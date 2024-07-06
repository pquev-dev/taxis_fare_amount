from prefect import task,flow 
from utils.utils import *
from process_data import DataProcesing
from config import *

@task(
    retries=3,
    retry_delay_seconds = 2,
    name="Procesamiento,limpieza datos",tags=['limpieza','procesamiento']
)
def processing_data():
    #cargar los datos
    data = load_data(TRAIN_PATH_DATA)

    data_processing = DataProcesing(data)
    data_processing.run()
    

@task(
    retries=3,
    retry_delay_seconds = 2,
    name="Entremiento/Ejecucion modelo",tags=['modelo','entrenamiento']
)
def process_train():
    pass


@flow(name="main_runner",log_prints=True)
def main_flow():
    processing_data()
    # process_train()
#ejecturar todo el flujo
if __name__ == "__main__":
    main_flow()
    




