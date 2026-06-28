from src.main.databases.mysql_connector import *

import configparser
config = configparser.ConfigParser()
config.read(r"src\resources\config_file.ini")

def main():
    my_sql_db_connection_obj = MySqlConnection(config)
    my_sql_db_connection_obj.connect()

    query = 'select * from labours_table'
    crud_operation_obj = MySqlCURDOperation(my_sql_db_connection_obj.connection)
    final_result = crud_operation_obj.read_from_mysql(query)
    logger.info(f"{final_result}")
    my_sql_db_connection_obj.close()
    

if __name__ == "__main__":
    main()