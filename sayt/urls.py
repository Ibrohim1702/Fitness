from django.urls import path

from sayt.views import *

urlpatterns = [
    path("", index, name="home"),
    path("contact/", contact, name="contact"),
    path("service/", service, name="service"),
    path("about/", about, name="about")
]