from django.urls import path
from .views import index, cart_page, add_to_cart,checkout,payment_success # ✅ Ensure these functions exist in views.py

urlpatterns = [
    path('', index, name='index'),
    path('cart/', cart_page, name='cart_page'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
     path('checkout/', checkout, name='checkout'),  # ✅ Route for checkout
]

urlpatterns += [
    path('payment-success/', payment_success, name='payment_success'),
]
