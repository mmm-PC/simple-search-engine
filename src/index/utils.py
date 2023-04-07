import elasticsearch
from src.index.connection import connect_to_es
from src.database.connection import connect_to_db
from src.config.cfg_parser import get_config


def try_create_index(es, index_name):
    config = get_config('config.ini')
    es_cfg = config['elasticsearch']

    mapping = {
        # "mappings": {
            "properties": {
                "id": {
                    "type": "integer"
                },
                "text": {
                    "type": "text"
                }
            }
        # }
    }

    # index_exists = es.indices.exists(index=index_name)
    # if not index_exists:
    try:
        es.indices.create(index=index_name, mappings=mapping)
    except elasticsearch.exceptions.RequestError as ex:
    # else:
        # return False
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

    db = connect_to_db()
    cursor = db.cursor()

    cursor.execute('SELECT id FROM posts')
    posts_ids = cursor.fetchall()
    for id in posts_ids:
        cursor.execute('SELECT id, text FROM posts WHERE id = {}'.format(id[0]))
        data = cursor.fetchone()
        data = {
            "id": "{}".format(int(data[0])),
            "text": "{}".format(data[1])
        }
        es.index(index = new_index, body = data)

    cursor.close()
    db.close()

    es.indices.update_aliases({
        "actions": [
            {"add":    {"index": new_index, "alias": alias}},
            {"remove": {"index": old_index, "alias": alias}}
        ]
    })
    es.options(ignore_status=[400,404]).indices.delete(index=old_index)
