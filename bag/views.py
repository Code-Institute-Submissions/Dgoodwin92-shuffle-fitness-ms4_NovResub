from django.shortcuts import render, redirect, reverse, HttpResponse


def view_bag(request):
    """ A view to return the bag contents page """
    
    return render(request, 'bag/bag.html')


def add_to_bag(request, membership_id):
    """ Add a membership to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if membership_id in list(bag.keys()):
        bag[membership_id] += quantity
    else:
        bag[membership_id] = quantity

    request.session['bag'] = bag
    
    return redirect(redirect_url)
    

def remove_from_bag(request, membership_id):
    """ Remove memberships from the bag """
    try:
        bag = request.session.get('bag', {})
        
        if quantity > 0:
            bag.pop(membership_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
    