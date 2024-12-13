from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from . models import Listing
from .choices import state_choices, price_choices, bedroom_choices

# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 3) #6 articles par page

    #obtenir le numéro de la page dépuis les paramètre GET
    page = request.GET.get('page')
    paged_listing = paginator.get_page(page) #obtenir la page demandée

    context = {
        'listings' : paged_listing,
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    #recupérer l'objet avec l'ID correspondant
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html', context)


def search(request):

    context = {
        'state_choices': state_choices,
        'price_choices':  price_choices,
        'bedroom_choices': bedroom_choices
    }
    return render(request, 'listings/search.html', context)