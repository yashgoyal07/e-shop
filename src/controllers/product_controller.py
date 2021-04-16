from helpers.mysql_queries import INSERT_PRODUCT_QUERY, GET_PRODUCT_QUERY, GET_PRODUCT_ID_QUERY, GET_PRODUCT_ALL_QUERY
from models.mysql_model import MysqlModel
import logging


class ProductController(object):
    def __init__(self):
        self.mysql_model_obj = MysqlModel()

    def add_product(self, product):
        try:
            product_list = [product['name'], product['description'], product['price'], product['category'],
                            product['ratings'], product['units'], product['reviews'], product['img_path']]
            product_tuple = tuple(product_list)
            self.mysql_model_obj.dml_query(query=INSERT_PRODUCT_QUERY, query_params=product_tuple)
        except Exception as err:
            logging.error(f'Error coming from add_product due to {err}')
            raise

    def get_product_category(self, category):
        try:
            result = self.mysql_model_obj.dql_query(query=GET_PRODUCT_QUERY, query_params=(category,))
            print(result)
            return result
        except Exception as err:
            logging.error(f'Error coming from get_product due to {err}')
            raise

    def get_product_id(self, id):
        try:
            result = self.mysql_model_obj.dql_query(query=GET_PRODUCT_ID_QUERY, query_params=(id,))
            print(result)
            return result
        except Exception as err:
            logging.error(f'Error coming from get_product due to {err}')
            raise

    def get_product(self):
        try:
            result = self.mysql_model_obj.dqlw_query(query=GET_PRODUCT_ALL_QUERY)
            print(result)
            return result
        except Exception as err:
            logging.error(f'Error coming from get_product due to {err}')
            raise
