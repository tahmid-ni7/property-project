from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'listings/listings.html')


def listing(request):
    return render(request, 'listings/single_listing.html')


def search(request):
    return render(request, 'listings/search.html')
