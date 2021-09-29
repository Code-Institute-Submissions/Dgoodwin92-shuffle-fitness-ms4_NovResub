from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Membership


def all_memberships(request):
    """ A view to show all the memberships, including search queries"""

    memberships = Membership.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You did not enter any search criteria!")
                return redirect(reverse('memberships'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            memberships = memberships.filter(queries)

    context = {
        'memberships': memberships,
        'search_term': query,
    }

    return render(request, 'memberships/memberships.html', context)


def membership_detail(request, membership_id):
    """ A view to show an individual memberships """

    membership = get_object_or_404(Membership, pk=membership_id)

    context = {
        'membership': membership,
    }

    return render(request, 'memberships/membership_detail.html', context)
    