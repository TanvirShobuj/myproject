from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product, Cart

def index(request):
    """ Display the product list and cart items on the index page """
    products = Product.objects.all()
    cart_items = Cart.objects.filter(user=request.user) if request.user.is_authenticated else []
    return render(request, "index.html", {"products": products, "cart_items": cart_items})

@login_required
def cart_page(request):
    """ Display the cart page with cart items """
    cart_items = Cart.objects.filter(user=request.user)
    return render(request, "cart.html", {"cart_items": cart_items})

@login_required
def add_to_cart(request, product_id):
    """ Add a product to the cart """
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('index')  # Redirect back to index page

@login_required
def cart_page(request):
    """ Display items in the cart """
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)

    return render(request, "cart_page.html", {"cart_items": cart_items, "total_price": total_price})

@login_required
def checkout(request):
    """ Proceed to payment page """
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)

    if request.method == "POST":
        # Simulate payment processing (Integrate with Stripe, PayPal, etc.)
        Cart.objects.filter(user=request.user).delete()  # Clear cart after payment
        return redirect('payment_success')

    return render(request, "checkout.html", {"cart_items": cart_items, "total_price": total_price})


def payment_success(request):
    """ Show payment success message """
    return render(request, "payment_success.html")
