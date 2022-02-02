from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
path('', views.home, name="Home"),
path('home/', views.index, name="ShopHome"),
path("about/", views.about, name="AboutUs"),
path("contact/", views.contact, name="ContactUs"),
path("tracker/", views.tracker, name="TrackingStatus"),
path("search/", views.search, name="Search"),
path("products<int:myid>", views.productView, name="ProductView"),
path("checkout/", views.checkout, name="Checkout"),
]
urlpatterns += staticfiles_urlpatterns()