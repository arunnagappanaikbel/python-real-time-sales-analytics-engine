import logging
from functools import wraps

def setup_logging(path):
    logging.basicConfig(filename=path, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    

def log_exceptions(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.exception(f"Exception in {func.__name__}: {e}")
            raise
    return wrapper