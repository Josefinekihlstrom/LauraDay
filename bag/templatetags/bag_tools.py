from django import template


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """ Calculates the subtotal of a product added with a qty > 1 """

    return price * quantity
