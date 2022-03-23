from .cart import Cart


def basket(request):
    return {'cart': Cart(request)}
