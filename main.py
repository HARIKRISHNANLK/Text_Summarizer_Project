from src.textSummarizer.pipeline.stage_01_ingestion import DataIngestionTrainingPipeline
# C:\Users\Harikrishnan\Desktop\Machine_Learning\Text_Summarizer_Project\src\textSummarizer\pipeline\stage_01_ingestion.py
# C:\Users\Harikrishnan\Desktop\Machine_Learning\Text_Summarizer_Project\src\textSummarizer\conponents\data_ingestion.py
from src.textSummarizer.logging import logger

STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e