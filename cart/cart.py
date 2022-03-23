from urllib import request
from store.models import Product
from decimal import Decimal


class Cart():
    """
    A base Basket class, providing some default behaviors that
    can be inherited or overrided, as necessary.
    """

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('skey')
        if 'skey' not in request.session:
            cart = self.session['skey'] = {}
        self.cart = cart

    def add(self, product, qty):

        product_id = product.id

        if product_id not in self.cart:
            self.cart[product_id] = {'price' : str(product.sale_price), 'qty': int(qty)}

        self.session.modified = True

    def __len__(self):
        """
        Get the basket data and count the qy of items
        """

        return sum(item['qty'] for item in self.cart.values())