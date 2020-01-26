"""Database operations are stored here."""
import sqlite3

# default path to connect to and create a database
DEFAULT_PATH = 'order.db'


def db_connect(db_path=DEFAULT_PATH):
    """Creates connection with a database (passed in DEFAULT_PATH)

    :param db_path: Path to the database
    :return: Connection
    """
    con = sqlite3.connect(db_path)
    return con


def create_table(con):
    """Creates orders table

    :param con: Existing connection
    """
    sql = """CREATE TABLE orders (
                      name text,
                      amount integer,
                      client_id integer
                      )"""
    cursor = con.cursor()
    cursor.execute(sql)


def get_all_orders(con):
    """
    Gets all instances of orders table

    :param con: Existing connection
    :return: Tuple of instances (orders)
    """
    sql = "SELECT * FROM orders"
    cursor = con.cursor()
    cursor.execute(sql)

    return cursor.fetchall()


def create_order(con, name, amount, client_id):
    """Creates order, saves it to the database

    :param con: Existing connection
    :param name: Name of the product in order
    :param amount: The amount of product
    :param client_id: ID of the client
    """
    sql = "INSERT INTO orders VALUES(:name, :amount, :client_id)"
    cursor = con.cursor()
    cursor.execute(sql, {'name': name, 'amount': amount, 'client_id': client_id})
