from src.config.cfg_parser import get_config
from src.index.index import Index
from src.database.database import Database
from src.api.api import API

import logging
FORMAT = '%(asctime)-15s %(message)s'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger('')


def main():
    config = get_config('config.ini')

    api = API(Database(), Index())

    # api.database.parse_to_db("database\\data\\posts.csv")

    # logger.warning("Initial indexing started...")
    # if not api.index.index_database(api.database):
    #     logger.error("Initial indexing failed")
    # else:
    #     logger.warning("Initial indexing completed")

    api.app.run(port=config['server']['port'])


if __name__ == "__main__":
    main()