from src.config.cfg_parser import get_config
import psycopg2

def connect_to_db():
    config = get_config('config.ini')
    db_settigs = config[config['database']['main']]
    connection = psycopg2.connect(host=db_settigs['host'],
                                  database=db_settigs['database'],
                                  user=db_settigs['user'],
                                  password=db_settigs['password'])

    return connection