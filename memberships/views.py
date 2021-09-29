from django.shortcuts import render, get_object_or_404
from .models import Membership


def all_memberships(request):
    """ A view to show all the memberships, including search queries"""

    memberships = Membership.objects.all()

    context = {
        'memberships': memberships,
    }

    return render(request, 'memberships/memberships.html', context)


def membership_detail(request, membership_id):
    """ A view to show an individual memberships """

    membership = get_object_or_404(Membership, pk=membership_id)

    context = {
        'membership': membership,
    }

    return render(request, 'memberships/membership_detail.html', context)
    