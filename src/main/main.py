from src.main.databases.mysql_connector import *

import configparser
config = configparser.ConfigParser()
config.read(r"src\resources\config_file.ini")

def main():
    query = 'select * from labours_table'
    print(config.sections())
    final_result = read_from_mysql(config, query)
    logger.info(f"{final_result}")


if __name__ == "__main__":
    main()