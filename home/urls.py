from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
import home
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls, name='admin'),
    path('car/<int:caryear>_<str:carmark>_<str:carmodel>/', views.car_detail, name='car_detail'),
    path('submit/', views.submit_info, name='submit_info'),
path('submit_fin_form/', views.submit_fin_form, name='submit_fin_form'),
path('listings/', views.listings, name='listings'),

path('about_us/', views.about_us, name='about_us'),

path('financing/', views.financing, name='financing'),

path('shipping/', views.shipping, name='shipping'),

path('dealer_warranty/', views.dealer_warranty, name='dealer_warranty'),

path('contact_us/', views.contact_us, name='contact_us'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
