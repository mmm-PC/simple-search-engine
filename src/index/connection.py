from src.config.cfg_parser import get_config
from elasticsearch import Elasticsearch

def connect_to_es():
    config = get_config('config.ini')
    es_settigs = config['elasticsearch']
    es = Elasticsearch([{'host': es_settigs['host'], 'port': es_settigs['port']}])

    return es