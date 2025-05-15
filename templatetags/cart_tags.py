from django import template

register = template.Library()

@register.inclusion_tag('carts/partials/cart_item_variations.html')
def display_cart_item_variations(variations):
    return {'variations': variations}