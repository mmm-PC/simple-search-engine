from src.config.cfg_parser import get_config
from elasticsearch import Elasticsearch

def connect_to_es():
    config = get_config('config.ini')
    es_settigs = config['elasticsearch']
    es = Elasticsearch([{'host': es_settigs['host'], 'port': int(es_settigs['port']), 'scheme': es_settigs['scheme']}],timeout=int(es_settigs['timeout']), max_retries=int(es_settigs['max_retries']), retry_on_timeout=bool(es_settigs['retry_on_timeout']))

    return es