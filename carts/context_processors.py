from django.db.models import Sum
from .views import _cart_id
from .models import Cart, CartItem

def counter(request):
    if 'admin' in request.path:
        return {}
    
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_count = CartItem.objects.filter(
            cart=cart, 
            is_active=True
        ).aggregate(total=Sum('quantity'))['total'] or 0
    except Cart.DoesNotExist:
        cart_count = 0
    
    return {'cart_count': cart_count}