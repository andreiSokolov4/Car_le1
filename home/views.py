from uuid import uuid4

from django.contrib import admin
from django.shortcuts import render, get_object_or_404
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
    return render(request, 'pages/dealer_warranty.html')

def contact_us(request):
    return render(request, 'pages/contact_us.html')


def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)
    photos = car.photos.all()
    return render(request, 'pages/car_detail.html', {'car': car, 'photos': photos})

def listings(request):
    cars = Car.objects.all()

    # Get filter criteria from request
    mark = request.GET.get('mark')
    model = request.GET.get('model')
    year = request.GET.get('year')

    # Apply filters if they exist
    if mark:
        cars = cars.filter(mark__icontains=mark)
    if model:
        cars = cars.filter(model__icontains=model)
    if year:
        cars = cars.filter(year=year)

    return render(request, 'pages/listings.html', {'cars': cars})


def submit_info(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        car_link = request.POST.get('car_link')
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Phone: {phone}")
        print(f"message: {message}")
        print(f"car link: {car_link}")
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

        # Printing out the information
        print(f"First Name: {first_name}")
        print(f"Link: {car_link}")
        print(f"Middle Name: {middle_name}")
        print(f"Last Name: {last_name}")
        print(f"Address 1: {address_1}")
        print(f"Address 2: {address_2}")
        print(f"City: {city}")
        print(f"State: {state}")
        print(f"Zip Code: {zip_code}")
        print(f"Social Security: {social_security}")
        print(f"Date of Birth: {date_of_birth}")
        print(f"Drivers License Number: {drivers_license_number}")
        print(f"Drivers License State: {drivers_license_state}")
        print(f"Drivers License Exp: {drivers_license_exp}")
        print(f"Mobile Phone: {mobile_phone}")
        print(f"Home Phone: {home_phone}")
        print(f"Email: {email}")
        print(f"Years: {years}")
        print(f"Months: {months}")
        print(f"Residence Type: {residence_type}")
        print(f"Rent/Mortgage: {rent_mortgage}")
        print(f"Employer: {employer}")
        print(f"Employer Type: {employer_type}")
        print(f"Monthly Income: {monthly_income}")
        print(f"Occupation: {occupation}")
        print(f"Employer Address 1: {employer_address_1}")
        print(f"Employer Address 2: {employer_address_2}")
        print(f"Employer City: {employer_city}")
        print(f"Employer State: {employer_state}")
        print(f"Employer Zip: {employer_zip}")
        print(f"Work Phone: {work_phone}")
        print(f"Employer Years: {employer_years}")
        print(f"Employer Months: {employer_months}")

        return HttpResponse("Form submitted!")
    return render(request, 'pages/index.html')