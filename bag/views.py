from django.shortcuts import (
    render, redirect, reverse,
    HttpResponse, get_object_or_404
    )
from django.contrib import messages
from products.models import Product


def view_bag(request):
    """ Renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add quantity of a product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    # if product is already in bag, qty is updated
    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(
            request, f'Updated {product.name} quantity to {bag[item_id]}')
    # else it adds the product
    else:
        bag[item_id] = quantity
        messages.success(
            request, f'{product.name} was added to your shopping bag.')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ Adjust quantity of a product in the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(
            request, f'Updated {product.name} quantity to {bag[item_id]}')
    # if product is manually set to 0 the product will be deleted
    # when update button is clicked
    else:
        bag.pop(item_id)
        messages.success(
            request, f'{product.name} was removed from your shopping bag.')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ Remove product from the shopping bag """

    try:
        product = get_object_or_404(Product, pk=item_id)
        bag = request.session.get('bag', {})

        bag.pop(item_id)
        messages.success(
            request, f'{product.name} was removed from your shopping bag.')

        request.session['bag'] = bag
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error while removing following product: {e}')
        return HttpResponse(status=500)
