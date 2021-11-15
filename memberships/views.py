from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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


@login_required
def add_membership(request):
    """ Add a Membership to the site """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site admin can access that area.')
        return redirect(reverse('home'))

    if request.method == "POST":
        form = MembershipForm(request.POST, request.FILES)
        if form.is_valid():
            membership = form.save()
            messages.success(request, 'Successfully added a membership!')
            return redirect(reverse('membership_detail', args=[membership.id]))
        else:
            messages.error(request, 'Failed to add a membership. Please check form is valid.')
    else:
        form = MembershipForm()
        
    template = 'memberships/add_membership.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_membership(request, membership_id):
    """ Edit a membership on the site """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site admin can access that area.')
        return redirect(reverse('home'))

    membership = get_object_or_404(Membership, pk=membership_id)
    if request.method == 'POST':
        form = MembershipForm(request.POST, request.FILES, instance=membership)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated membership!')
            return redirect(reverse('membership_detail', args=[membership.id]))
        else:
            messages.error(request, f'You are editing {membership.name}')
    else:
        form = MembershipForm(instance=membership)
        messages.warning(request, f'You are editing {membership.name}')
    
    template = 'memberships/edit_membership.html'
    context = {
        'form': form,
        'membership': membership
    }

    return render(request, template, context)


@login_required
def delete_membership(request, membership_id):
    """ Delete a membership from the site """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site admin can access that area.')
        return redirect(reverse('home'))
        
    membership = get_object_or_404(Membership, pk=membership_id)
    membership.delete()
    messages.success(request, 'Membership deleted!')
    return redirect(reverse('memberships'))
