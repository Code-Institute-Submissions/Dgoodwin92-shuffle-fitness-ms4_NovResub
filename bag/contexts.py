from django.conf import settings
from django.shortcuts import get_object_or_404
from memberships.models import Membership

def bag_contents(request):

    bag_items = []
    total = 0
    membership_count = 0
    bag = request.session.get('bag', {})

    for membership_id, quantity in bag.items():
        membership = get_object_or_404(Membership, pk=membership_id)
        total += quantity * membership.price
        membership_count += quantity
        bag_items.append({
            'membership_id': membership_id,
            'quantity': quantity,
            'membership': membership,
        })

    grand_total = total

    context = {
        'bag_items': bag_items,
        'total': total,
        'membership_count': membership_count,
        'grand_total': grand_total,
    }

    return context
    