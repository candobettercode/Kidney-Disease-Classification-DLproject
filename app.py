from src import logging
from src.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline  
from src.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from src.pipeline.stage_03_model_training import ModelTrainingPipeline


STAGE_NAME = "Data Ingestion stage"

try:
    logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logging.exception(e)
    raise e



STAGE_NAME = "Prepare base model"
try: 
    logging.info(f"*******************")
    logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logging.exception(e)
    raise e



STAGE_NAME = "Training"
try: 
   logging.info(f"*******************")
   logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_trainer = ModelTrainingPipeline()
   model_trainer.main()
   logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logging.exception(e)
        raise e
