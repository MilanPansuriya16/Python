import mysql.connector
from src.main.encrypt_decrypt.Lec25_AES_encryption import decrypt
from loguru import logger

class MySqlConnection:
    def __init__(self,config):
        self.config = config
        self.connection = None
    
    def connect(self):
        try:
            self.connection = mysql.connector.connect(host = self.config["mysql_database"]["host"],
                                                user = self.config["mysql_database"]["user"],
                                                password = self.config["mysql_database"]["password"],
                                                database = self.config["mysql_database"]["databases"])
            logger.info(f"MySql Connection succesful")
        except Exception as e:
            logger.error(f"Error Occured: {e}")
            raise e
        

    def close(self):
        if self.connection.is_connected():
            self.connection.close()
            logger.info(f"MySql Connection Close")


class MySqlCURDOperation:
    def __init__(self,mysql_connection):
        self.connection = mysql_connection

    def read_from_mysql(self,query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            result =  cursor.fetchall()
            return result
        except Exception as e:
            logger.info(f"Error in MySql Query Run {e}")
            raise e
        finally:
            if cursor:
                cursor.close()
                logger.info("cursor closed")


        
        
