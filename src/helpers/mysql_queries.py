INSERT_PRODUCT_QUERY = """INSERT INTO `eshop`.`products` (name, description, price, category, ratings, units, reviews,
                                                          img_path) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
GET_PRODUCT_QUERY = """SELECT * FROM `eshop`.`products` WHERE category = %s"""
GET_PRODUCT_ID_QUERY = """SELECT * FROM `eshop`.`products` WHERE id = %s"""
CREATE_TABLE_QUERY = """CREATE TABLE `eshop`.`products` (`id` INT NOT NULL,
                                                          `name` VARCHAR(500) NULL,
                                                          `description` TEXT NULL,
                                                          `price` FLOAT NULL,
                                                          `category` VARCHAR(500) NULL,
                                                          `ratings` INT NULL,
                                                          `units` BIGINT NULL,
                                                          `reviews` BIGINT NULL,
                                                          `img_path` VARCHAR(500) NULL,
                                                          PRIMARY KEY (`id`));"""

GET_PRODUCT_ALL_QUERY = """SELECT * FROM `eshop`.`products`"""