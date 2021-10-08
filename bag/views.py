from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from memberships.models import Membership


def view_bag(request):
    """ A view to return the bag contents page """
    
    return render(request, 'bag/bag.html')


def add_to_bag(request, membership_id):
    """ Add a membership to the shopping bag """

    membership = Membership.objects.get(pk=membership_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if membership_id in list(bag.keys()):
        bag[membership_id] += quantity
    else:
        bag[membership_id] = quantity
        messages.success(request, f'Added {membership.name} to your bag')

    request.session['bag'] = bag
    
    return redirect(redirect_url)
    

def remove_from_bag(request, membership_id):
    """ Remove memberships from the bag """
    try:
        membership = get_object_or_404(Membership, pk=membership_id)
        bag = request.session.get('bag', {})
        
        bag.pop(membership_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
       