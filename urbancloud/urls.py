
from django.contrib import admin
from django.urls import path
from urbancloud import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', views.index,name="index"),
    # path('/index', views.index,name="index"),
    path('aboutus', views.aboutus,name="aboutus"),
    path('service', views.service,name="service"),
    path('contactus', views.contact_us,name="contactus"),
]
urlpatterns += staticfiles_urlpatterns()

