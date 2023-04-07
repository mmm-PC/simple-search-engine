from src.config.cfg_parser import get_config
from src.database.utils import parse_to_db
from src.api.main import app
from src.index.utils import index_database

import json
from src.database.connection import connect_to_db


def main():
    config = get_config('config.ini')
    # parse_to_db("database\\data\\posts.csv")

    # db = connect_to_db()
    # cursor = db.cursor()

    # cursor.execute('SELECT id FROM posts')
    # posts_ids = cursor.fetchall()
    # print(json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]'))
    # for id in posts_ids:
    #     cursor.execute('SELECT id, text FROM posts WHERE id = {}'.format(id[0]))
    #     data = cursor.fetchall()
    #     print(data)

    index_database()
    app.run(port = config['server']['port'])


if __name__ == "__main__":
    main()