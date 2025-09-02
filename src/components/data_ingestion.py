import os
import zipfile
import gdown
import certifi
import time

from src import logging
from src.utils.common import get_size
from src.entity.config_entity import (DataIngestionConfig)


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    
    def download_file(self, retries: int = 3, wait: int = 5)-> str:
        '''
        Downloads the dataset from Google Drive link using gdown with retries.
        Returns the path of the downloaded file.
        '''

        try: 
            dataset_url = self.config.source_URL
            zip_download_dir = self.config.local_data_file
            os.makedirs("artifacts/data_ingestion", exist_ok=True)
            logging.info(f"Downloading data from {dataset_url} into file {zip_download_dir}")

            file_id = dataset_url.split("/")[-2]
            prefix = 'https://drive.google.com/uc?/export=download&id='
            url = prefix + file_id
            logging.info(f"Preparing to download data from {dataset_url}")


            gdown.download(prefix+file_id,zip_download_dir,quiet=False, verify=certifi.where())

            attempt = 0
            while attempt < retries:
                try:
                    logging.info(f"Attempt {attempt+1}: Downloading to {zip_download_dir}")
                    gdown.download(url, zip_download_dir, quiet=False, verify=certifi.where())

                    if os.path.exists(zip_download_dir) and os.path.getsize(zip_download_dir) > 0:
                        logging.info(
                            f"✅ Download successful! "
                            f"File saved at {zip_download_dir} "
                            f"({get_size(Path(zip_download_dir))})"
                        )
                        return zip_download_dir
                    else:
                        raise Exception("Downloaded file is empty!")

                except Exception as e:
                    logging.error(f"Download attempt {attempt+1} failed: {e}")
                    attempt += 1
                    if attempt < retries:
                        logging.info(f"Retrying in {wait} seconds...")
                        time.sleep(wait)
                    else:
                        logging.critical("❌ Max retries reached. Download failed.")
                        raise e

        except Exception as e:
            logging.error(f"Error in downloading file: {e}")
            raise e
            

    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        try:
            unzip_path = self.config.unzip_dir
            os.makedirs(unzip_path, exist_ok=True)

            logging.info(f"Extracting {self.config.local_data_file} to {unzip_path}")
            with zipfile.ZipFile(self.config.local_data_file, "r") as zip_ref:
                zip_ref.extractall(unzip_path)

            logging.info(f"Extraction complete! Data available at {unzip_path}")
            return unzip_path

        except zipfile.BadZipFile:
            logging.error("The downloaded file is not a valid zip file.")
            raise
        except Exception as e:
            logging.error(f"Error in extracting file: {e}")
            raise