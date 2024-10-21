from uuid import uuid4
import requests
import json
from django.contrib import admin
from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.http import HttpResponse
from .models import Car


def index(request):
    # Get query parameters from the GET request
    car_model = request.GET.get('car-model')
    max_price = request.GET.get('max-price')
    min_year = request.GET.get('min-year')

    # Initialize the queryset
    cars = Car.objects.all()

    # Filter based on user input
    if car_model:
        cars = cars.filter(model__icontains=car_model)

    if max_price:
        try:
            cars = cars.filter(price__lte=float(max_price))
        except ValueError:
            pass  # Handle the case where conversion fails

    if min_year:
        try:
            cars = cars.filter(year__gte=int(min_year))
        except ValueError:
            pass  # Handle the case where conversion fails

    return render(request, 'pages/index.html', {'cars': cars})

def about_us(request):
    return render(request, 'pages/About_us.html')

def financing(request):
    return render(request, 'pages/Financing.html')

def shipping(request):
    return render(request, 'pages/shipping.html')

def dealer_warranty(request):
    return render(request, 'pages/Dealer_warranty.html')

def contact_us(request):
    return render(request, 'pages/contact_us.html')


def car_detail(request, caryear, carmark, carmodel):
    # Get the car based on the year, mark, and model
    car = get_object_or_404(Car, year=caryear, mark=carmark, model=carmodel)
    photos = car.photos.all()
    return render(request, 'pages/car_detail.html', {'car': car, 'photos': photos})


def listings(request):
    cars = Car.objects.all()  # Start with all cars

    # Collect filter parameters from GET request
    mark = request.GET.get('mark')
    miles = request.GET.get('miles')
    body = request.GET.get('body')
    sort_by = request.GET.get('sort_by')

    # Apply filters based on the selected values
    if mark:
        cars = cars.filter(mark=mark)

    if miles:
        # Filter based on mileage ranges
        if miles == "10-30k":
            cars = cars.filter(miles__gte=10000, miles__lt=30000)
        elif miles == "30-50k":
            cars = cars.filter(miles__gte=30000, miles__lt=50000)
        elif miles == "50k+":
            cars = cars.filter(miles__gte=50000)

    if body:
        cars = cars.filter(body=body)

    # Sorting the results
    if sort_by:
        if sort_by == 'price':
            cars = cars.order_by('price')  # Adjust according to your price field type
        elif sort_by == 'year':
            cars = cars.order_by('-year')
        elif sort_by == 'miles':
            cars = cars.order_by('miles')

    return render(request, 'pages/listings.html', {'cars': cars})


def get_geolocation(ip):
    try:
        response = requests.get(f'http://ipinfo.io/{ip}/json')
        if response.status_code == 200:
            data = response.json()
            city = data.get('city', 'N/A')
            region = data.get('region', 'N/A')
            country = data.get('country', 'N/A')
            print(f"{city}, {region}, {country}")
            return f"{city}, {region}, {country}"
        return "Location not found"
    except Exception as e:
        return "Error retrieving location"

def get_client_ip(request):
    # Check X-Forwarded-For for proxies or use request.META for the IP
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
        print(ip)
    else:
        ip = request.META.get('REMOTE_ADDR')
        print(ip)
    return ip


def submit_info(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        car_link = request.POST.get('car_link')
        client_ip = get_client_ip(request)
        geolocation = get_geolocation(client_ip)

        # Send email
        email_subject = 'New Inquiry Submitted'
        email_body = f"""
        Name: {name}
        Email: {email}
        Phone: {phone}
        Message: {message}
        Car Link: {car_link}
        Geolocation: {geolocation}
        IP Address: {client_ip}
        """
        send_mail(
            email_subject,                # subject
            email_body,                   # message body
            'sales@fishercarmart.com',    # from email
            ['sales@fishercarmart.com'],  # recipient email
            fail_silently=False,
        )

        return HttpResponse("Form submitted!")
    return render(request, 'submit_form.html')


def submit_fin_form(request):
    if request.method == 'POST':
        # Personal Information
        car_link = request.POST.get('car_link1')
        first_name = request.POST.get('first-name')
        middle_name = request.POST.get('middle-name')
        last_name = request.POST.get('last-name')
        address_1 = request.POST.get('address-1')
        address_2 = request.POST.get('address-2')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip')
        social_security = request.POST.get('social-security')
        date_of_birth = request.POST.get('date-of-birth')
        drivers_license_number = request.POST.get('drivers-license-number')
        drivers_license_state = request.POST.get('drivers-license-state')
        drivers_license_exp = request.POST.get('drivers-license-exp')
        mobile_phone = request.POST.get('mobile-phone')
        home_phone = request.POST.get('home-phone')
        email = request.POST.get('email')

        # Residence Information
        years = request.POST.get('years')
        months = request.POST.get('months')
        residence_type = request.POST.get('residence-type')
        rent_mortgage = request.POST.get('rent-mortgage')

        # Employment Information
        employer = request.POST.get('employer')
        employer_type = request.POST.get('employer-type')
        monthly_income = request.POST.get('monthly-income')
        occupation = request.POST.get('occupation')
        employer_address_1 = request.POST.get('employer-address-1')
        employer_address_2 = request.POST.get('employer-address-2')
        employer_city = request.POST.get('employer-city')
        employer_state = request.POST.get('employer-state')
        employer_zip = request.POST.get('employer-zip')
        work_phone = request.POST.get('work-phone')
        employer_years = request.POST.get('employer-years')
        employer_months = request.POST.get('employer-months')

        # Get the user's IP and geolocation
        client_ip = get_client_ip(request)
        geolocation = get_geolocation(client_ip)

        # Email content
        email_subject = 'New Financial Application Submitted'
        email_body = f"""
        Car Link: {car_link}

        Personal Information:
        First Name: {first_name}
        Middle Name: {middle_name}
        Last Name: {last_name}
        Address 1: {address_1}
        Address 2: {address_2}
        City: {city}
        State: {state}
        Zip Code: {zip_code}
        Social Security: {social_security}
        Date of Birth: {date_of_birth}
        Drivers License Number: {drivers_license_number}
        Drivers License State: {drivers_license_state}
        Drivers License Exp: {drivers_license_exp}
        Mobile Phone: {mobile_phone}
        Home Phone: {home_phone}
        Email: {email}

        Residence Information:
        Years: {years}
        Months: {months}
        Residence Type: {residence_type}
        Rent/Mortgage: {rent_mortgage}

        Employment Information:
        Employer: {employer}
        Employer Type: {employer_type}
        Monthly Income: {monthly_income}
        Occupation: {occupation}
        Employer Address 1: {employer_address_1}
        Employer Address 2: {employer_address_2}
        Employer City: {employer_city}
        Employer State: {employer_state}
        Employer Zip: {employer_zip}
        Work Phone: {work_phone}
        Employer Years: {employer_years}
        Employer Months: {employer_months}

        Geolocation (based on IP): {geolocation}
        IP Address: {client_ip}
        """

        # Send email
        send_mail(
            email_subject,
            email_body,
            'sales@fishercarmart.com',  # From email
            ['sales@fishercarmart.com'],  # To email
            fail_silently=False,
        )

        return HttpResponse("Form submitted!")
    return render(request, 'pages/index.html')