from django.shortcuts import render, redirect
from requests import request
from cart.models import CartItem
from store.models import Product
from .forms import OrderForm
from .models import Order, OrderProduct, Payment
import datetime
from backend.settings import PAYSTACK_PUBLIC_KEY, PAYSTACK_SECRET_KEY
from pypaystack import Transaction, Customer, Plan
from django.http import JsonResponse
from django.template.loader import render_to_string
from backend.settings import EMAIL_HOST_USER
from django.core.mail import send_mail

def payment(request):
    if request.POST.get('action') == 'post':
        user = request.user
        payment_id = int(request.POST.get('transID'))
        amount_paid = int(request.POST.get('amount_val'))
        status = request.POST.get('status')
        orderID = int(request.POST.get('orderID'))
        transID = int(request.POST.get('transID'))
        order = Order.objects.get(user=user, is_ordered=False, order_number=orderID)
        transaction = Transaction(authorization_key=PAYSTACK_SECRET_KEY)
        
        #strore all the transaction details in the payment models
        all_transaction = transaction.getone(transID)[3]
        print(all_transaction)
        payment = Payment(
            user = request.user,
            payment_id = payment_id,
            amount_paid = amount_paid,
            status = status
        )
        payment.save()
        if status == "success":
            order.is_ordered = True
            order.payment = payment
            order.status = 'Completed'
            order.save()
    #move the cart items to Order Product Model
        cart_items = CartItem.objects.filter(user=request.user)
        for item in cart_items:
            orderproduct = OrderProduct()
            orderproduct.order_id = order.id
            orderproduct.payment = payment
            orderproduct.user_id = request.user.id
            orderproduct.product_id = item.product_id
            orderproduct.quantity = item.quantity
            orderproduct.product_price = item.product.discounted_price
            orderproduct.ordered = True
            orderproduct.save()

            cart_item = CartItem.objects.get(id=item.id)
            product_variation =cart_item.variation.all()
            orderproduct = OrderProduct.objects.get(id=orderproduct.id)
            orderproduct.variations.set(product_variation)
            orderproduct.save()

        #reduce the quantity of product if sold
            product = Product.objects.get(id=item.product_id)
            product.stock -= item.quantity
            product.save()
    
    #clear cart if order is succcess
    CartItem.objects.filter(user=request.user).delete()

    #Send Email after order
    # setup Email
    subject = 'Order Recieved'
    message = render_to_string('store/order/order_received_email.html', {
        'user': user,
        'order':order,
    })
    to_email = user.email
    send_mail(subject, message, EMAIL_HOST_USER, [to_email])
    response = JsonResponse({'Order_number': order.order_number, 'transID':transID})
    return response

def place_orders(request, total=0, quantity=0):
    current_user = request.user
    cart_items = CartItem.objects.filter(user=current_user)
    cart_count = cart_items.count()
    if cart_count <= 0:
        return redirect('store:shop')

    for cart_item in cart_items:
        total += (cart_item.product.discounted_price * cart_item.quantity)
        quantity += cart_item.quantity


    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            # Store all the billing information inside Order table
            data = Order()
            data.user = current_user
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.phone = form.cleaned_data['phone']
            data.email = form.cleaned_data['email']
            data.address_line_1 = form.cleaned_data['address_line_1']
            data.address_line_2 = form.cleaned_data['address_line_2']
            data.country = form.cleaned_data['country']
            data.state = form.cleaned_data['state']
            data.city = form.cleaned_data['city']
            data.order_note = form.cleaned_data['order_note']
            data.order_total = total
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            # Generate order number
            yr = int(datetime.date.today().strftime('%Y'))
            dt = int(datetime.date.today().strftime('%d'))
            mt = int(datetime.date.today().strftime('%m'))
            d = datetime.date(yr,mt,dt)
            current_date = d.strftime("%Y%m%d") #20210305
            order_number = current_date + str(data.id)
            data.order_number = order_number
            data.save()

            order = Order.objects.get(user=current_user, is_ordered=False, order_number=order_number)
            paystack_public_key = PAYSTACK_PUBLIC_KEY
            context = {
                'order': order,
                'total': total,
                'cart_items':cart_items,
                'paystack_public_key': paystack_public_key,
            }
            return render(request, 'store/order/payment.html', context)   
        else:
            return redirect('cart:checkout')  


def order_complete(request):
    order_number = request.GET.get('order_number')
    payment_id = request.GET.get('payment_id')

    try:
        order = Order.objects.get(order_number=order_number, is_ordered= True)
        ordered_product = OrderProduct.objects.filter(order_id=order.id)
        payment= Payment.objects.get(payment_id=payment_id)

        subtotal = 0
        for i in ordered_product:
            subtotal = i.product_price * i.quantity

        context = {
            'order':order,
            'ordered_product':ordered_product,
            'order_number': order.order_number,
            'payment_id': payment.payment_id,
            'payment':payment,
            'subtotal':subtotal

        }
        return render(request, 'store/order/order_complete.html', context)
    except (Payment.DoesNotExist, Order.DoesNotExist):
        return redirect("store:home")