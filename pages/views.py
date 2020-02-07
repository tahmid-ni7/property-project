from django.shortcuts import render
from listings.models import Listing,AboutText
from realtors.models import Realtor
from listings.choices import bedroom_choices, price_choices, city_choices


# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings': listings,
        'bedroom_choices': bedroom_choices,
        'city_choices': city_choices,
        'price_choices': price_choices
    }
    return render(request, 'pages/index.html', context)


def about(request):
    realtors = Realtor.objects.order_by('-hire_date')[:3]
    mvp_realtors = Realtor.objects.filter(is_mvp=True)
    about_area = AboutText.objects.all().filter(is_published=True)

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors,
        'about_area': about_area
    }
    return render(request, 'pages/about.html', context)
