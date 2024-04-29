from django.shortcuts import render

from .models import Country, Location


def country(request):
    return render(request,"index.html")

def addcountry(request):
    if request.method=='POST':
        country_id = request.POST['country_id']
        country_name = request.POST['country_name']
        region_id = request.POST['region_id']
        Country.objects.create(country_id=country_id,country_name=country_name,region_id=region_id)
        usersdata = Country.objects.all()
        return render(request, "displaycountry.html", {"countries":usersdata})

def displaycountry(request):
    usersdata = Country.objects.all()
    return render (request,"displaycountry.html", {"countries":usersdata})


def addLocation(request):
    # Query the database to retrieve the list of country IDs
    countries = Country.objects.all()
    country_ids = [country.country_id for country in countries]

    return render(request, 'addLocation.html', {'country_ids': country_ids})

def add_location(request):
    if request.method=='POST':
        location_id = request.POST['location_id']
        street_address = request.POST['street_address']
        postal_code = request.POST['postal_code']
        city = request.POST['city']
        state_province = request.POST['state_province']
        country_id = request.POST['country_id']
        Location.objects.create(location_id=location_id,street_address=street_address,postal_code=postal_code,city=city,state_province=state_province,country_id=country_id)
        locations = Location.objects.all()
        return render(request, "displayLocation.html", {'locations': locations})

def addloc(request):
    return render(request, "addLocation.html")

def display_locations(request):
    # Query the database to retrieve all location objects
    locations = Location.objects.all()

    return render(request, 'displayLocation.html', {'locations': locations})


def canada_addresses(request):
    # Query to find the addresses of Canada using join
    canada_locations = Location.objects.filter(country__country_id='CA')
    canada_addresses = []
    for location in canada_locations:
        canada_addresses.append({
            'location_id': location.location_id,
            'street_address': location.street_address,
            'postal_code': location.postal_code,
            'city': location.city,
            'state_province': location.state_province,
            'country_name': location.country.country_name
        })

    return render(request, 'displaycanada.html', {'locations': canada_addresses})


# views.py
from django.shortcuts import render
from .models import Location, Country


def canada_address(request):
    canada_locations = Location.objects.filter(country__country_id='CA')
    canada_country = Country.objects.get(country_id='CA')
    canada_addresses = []
    for location in canada_locations:
        canada_addresses.append({
            'location_id': location.location_id,
            'street_address': location.street_address,
            'postal_code': location.postal_code,
            'city': location.city,
            'state_province': location.state_province,
            'country_name': canada_country.country_name
        })

    return render(request, 'withoutsql.html', {'locations': canada_addresses})

