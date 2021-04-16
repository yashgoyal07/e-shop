from configs.mysql_config import MysqlConfig
import mysql.connector
from helpers.utils import get_environment
import logging


class MysqlModel(object):
    def __init__(self):
        self.environment = get_environment()
        self.db_config = MysqlConfig.INSTANCE_CONFIG.get(self.environment, {})

    def get_connection(self):
        connection = mysql.connector.connect(host=self.db_config.get('host'),
                                             port=self.db_config.get('port'),
                                             username=self.db_config.get('username'),
                                             password=self.db_config.get('password'))
        return connection

    def dml_query(self, query, query_params):
        conn = None
        try:
            conn = self.get_connection()
            cur = conn.cursor(dictionary=True)
            cur.execute(query, query_params)
            conn.commit()
        except mysql.connector.Error as err:
            logging.error(f'mysql connector error coming from dml_query due to {err}')
            raise
        except Exception as err:
            logging.error(f'error coming from dml_query due to {err}')
            raise
        finally:
            if conn:
                conn.close()

    def dql_query(self, query, query_params):
        conn = None
        try:
            conn = self.get_connection()
            cur = conn.cursor(dictionary=True)
            cur.execute(query, query_params)
            result = cur.fetchall()
            return result
        except mysql.connector.Error as err:
            logging.error(f'mysql connector error coming from dql_query due to {err}')
            raise
        except Exception as err:
            logging.error(f'error coming from dql_query due to {err}')
            raise
        finally:
            if conn:
                conn.close()

    def dqlw_query(self, query):
        conn = None
        try:
            conn = self.get_connection()
            cur = conn.cursor(dictionary=True)
            cur.execute(query)
            result = cur.fetchall()
            return result
        except mysql.connector.Error as err:
            logging.error(f'mysql connector error coming from dql_query due to {err}')
            raise
        except Exception as err:
            logging.error(f'error coming from dql_query due to {err}')
            raise
        finally:
            if conn:
                conn.close()
