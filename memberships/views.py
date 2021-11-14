from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Membership, Category
from .forms import MembershipForm


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


def add_membership(request):
    """ Add a Membership to the site """
    if request.method == "POST":
        form = MembershipForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added a membership!')
            return redirect(reverse('add_membership'))
        else:
            messages.error(request, 'Failed to add a membership. Please check form is valid.')
    else:
        form = MembershipForm()
        
    template = 'memberships/add_membership.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
