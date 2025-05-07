from django.shortcuts import get_object_or_404, render

from category.models import Category
from store.models import Product

# Create your views here.

def store(request, category_slug=None):
    """View function to display products in the store.""" 
    categories = None
    products = None
    
    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        product_count = products.count()
        
    else:   
        products = Product.objects.all().filter(is_available=True)
        product_count = products.count()
    
    if product_count == 0:
        message = "No products available at the moment."
    else:
        message = f"{product_count} products available."
        
        
    context = {
        'products': products,
        'product_count': product_count,
        'message': message,
    }
    return render(request, 'store/store.html', context)


def product_detail(request, category_slug, product_slug):
    """View function to display product details."""
    try:
        single_product = get_object_or_404(Product, 
                                         category__slug=category_slug, 
                                         slug=product_slug)
    except Exception as e:
        raise e
    
    context = {
        'single_product': single_product,
    }   
    
    return render(request, 'store/product_detail.html', context)