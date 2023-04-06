import elasticsearch
from src.index.connection import connect_to_es
from src.database.connection import connect_to_db
from src.config.cfg_parser import get_config


def try_create_index(es, index_name):

    mapping = {
        "mappings": {
            "properties": {
                "id": {
                    "type": "integer"
                },
                "text": {
                    "type": "text"
                }
            }
        }
    }
    try:
        es.indices.create(name=index_name, body=mapping)
    except elasticsearch.exceptions.RequestError as ex:
        if ex.error == 'resource_already_exists_exception':
            return False
        else:
            raise ex
    return True


def index_database():
    config = get_config('config.ini')
    index_cfg = config['index']

    es = connect_to_es()

    alias = index_cfg['alias']
    new_index = index_cfg['name-1']
    if try_create_index(es, new_index):
        old_index = index_cfg['name-2']
    else:
        new_index = index_cfg['name-2']
        old_index = index_cfg['name-1']
        try_create_index(es, new_index)#TODO :: check for creation error

    # code

    es.indices.update_aliases({
        "actions": [
            {"add":    {"index": new_index, "alias": alias}},
            {"remove": {"index": old_index, "alias": alias}}
        ]
    })
    es.options(ignore_status=[400,404]).indices.delete(index=old_index)
