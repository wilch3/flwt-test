"""Inserting orders to the database."""
from database.db_utils import db_connect, create_order
from order.order import Order

con = db_connect()
# at least 5 orders in the database
ord_1 = Order("Dell XPS 15", 12, 1)
ord_2 = Order("Acer Swift 5", 8, 2)
ord_3 = Order("ASUS ZenBook 14", 3, 2)
ord_4 = Order("Apple MacBook Air 2018", 15, 4)
ord_5 = Order("Lenovo ThinkPad L590", 11, 3)

try:
    for i in range(1, 6):
        order = globals()["ord_" + str(i)]
        create_order(con, order.name, order.amount, order.client_id)
        con.commit()
except:
    con.rollback()
    raise RuntimeError("Could not commit.")
