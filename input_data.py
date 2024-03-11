import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def read_csv(file_path):
    try:
        return pd.read_csv(file_path, encoding='utf-8')
    except Exception as e:
        logging.error(f"Failed to read CSV file {file_path}: {e}")
        raise

def read_json(file_path):
    try:
        return pd.read_json(file_path, lines=True, encoding='utf-8')
    except ValueError:
        logging.info(f"Reading JSON file as a whole: {file_path}")
        try:
            return pd.read_json(file_path, lines=False, encoding='utf-8')
        except Exception as e:
            logging.error(f"Failed to read JSON file {file_path}: {e}")
            raise

def read_xlsx(file_path):
    try:
        return pd.read_excel(file_path)
    except Exception as e:
        logging.error(f"Failed to read XLSX file {file_path}: {e}")
        raise

def read_xml(file_path):
    try:
        return pd.read_xml(file_path)
    except Exception as e:
        logging.error(f"Failed to read XML file {file_path}: {e}")
        raise

def read_parquet(file_path):
    try:
        return pd.read_parquet(file_path)
    except Exception as e:
        logging.error(f"Failed to read Parquet file {file_path}: {e}")
        raise

def read_dataset(file_path):
    try:
        if file_path.endswith('.csv'):
            return read_csv(file_path)
        elif file_path.endswith('.json'):
            return read_json(file_path)
        elif file_path.endswith('.xlsx'):
            return read_xlsx(file_path)
        elif file_path.endswith('.xml'):
            return read_xml(file_path)
        elif file_path.endswith('.parquet'):
            return read_parquet(file_path)
        else:
            logging.error(f"Unsupported file format for file {file_path}")
            raise ValueError("Unsupported file format.")
    except ValueError as ve:
        logging.error(ve)
        raise