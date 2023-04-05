from src.config.cfg_parser import get_config
from src.database.utils import parse_to_db
from src.api.main import app

def main():
    config = get_config('config.ini')
    # parse_to_db("database\\data\\posts.csv")

    app.run(port = config['server']['port'])


if __name__ == "__main__":
    main()