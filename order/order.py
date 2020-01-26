class Order:
    """Order class

    :param name: Name of the product
    :param amount: The mount of the product in order
    :param client_id: ID of the client the order needs to be sent to
    """

    def __init__(self, name, amount, client_id):
        self.name = name
        self.amount = amount
        self.client_id = client_id

    def __repr__(self):
        return f"Order: {self.name}, amount: {self.amount}, client id: {self.client_id}"
