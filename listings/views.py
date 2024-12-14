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


#Fonction de recherche dans le formulaire
def search(request):
    query_list = Listing.objects.order_by('-list_date')

    #Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            query_list = query_list.filter(description__icontains=keywords)

    #city
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            query_list = query_list.filter(city__iexact=city)

    #state
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            query_list = query_list.filter(state__iexact=state)

    #Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            query_list = query_list.filter(bedrooms__lte=bedrooms)

    #Bedrooms
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            query_list = query_list.filter(price__lte=price)

    context = {
        'listings': query_list,
        'state_choices': state_choices,
        'price_choices':  price_choices,
        'bedroom_choices': bedroom_choices,
        'values' : request.GET
    }
    return render(request, 'listings/search.html', context)