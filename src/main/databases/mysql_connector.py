import mysql.connector
from src.main.encrypt_decrypt.Lec25_AES_encryption import decrypt
from loguru import logger


def read_from_mysql(config,query):

    connection = None
    cursor = None
    try:
        connection = mysql.connector.connect(host = config["mysql_database"]["host"],
                                            user = config["mysql_database"]["user"],
                                            password = config["mysql_database"]["password"],
                                            database = config["mysql_database"]["databases"])

        # logger.info(f"{connection}")      # To check the connection is established or not


        # read the data from databases
        # query = 'select * from labours_table'
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        # logger.info(f"{result}")
        # logger.info('Query done in the database')
        return result
    
    except Exception as e:
        logger.info(f"Error occured in mysql as {e}")
        raise e

    finally:
        # cursor.close()
        # connection.close()
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()