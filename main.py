from src.loader import load_data
from src.transformer import transform_data
from src.analyser import analyze_data
from src.config_loader import load_config
from src.utils import setup_logging
import logging

if  __name__=='__main__':
    config = load_config("config/config.yaml")
    setup_logging(config['log_path'])
    
    try:
        sales_df, product_df, store_df = load_data(config['data_paths'])
        transformed_df = transform_data(sales_df, product_df, store_df)
        analyze_data(transformed_df, config['data_paths']['output'])
        logging.info(f'data pipeline comleted successfuly')
    except Exception as e:
        logging.exception(f'pipeline failed: {e}')